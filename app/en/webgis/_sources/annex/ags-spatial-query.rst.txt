ArcGIS Server Spatial-Query Workaround
=======================================

.. note::

   Only affects map services of type **ArcGIS Server (REST)** whose data resides in a
   **SQL Server** or **Oracle** database (see below).

The Problem
-----------

For a **spatial query** (e.g. Identify by area, polygon selection, buffer search), the
**ArcGIS Server** evaluates the request internally in two steps:

1. First, only the **bounding box** (the rectangular envelope) of the query geometry is sent to
   the database — including the **row limit** (``maxRecordCount``) that applies there.
2. Only afterwards is the resulting set clipped against the **actual query geometry** (e.g. the
   exact polygon) to determine the final results.

The problem: the row limit from step 1 is applied **before** the actual spatial clip. For large
or narrow geometries (e.g. elongated lines or polygons), this can mean that too few — or no —
real matches are among the first candidates found via the bounding box, even though
significantly more objects actually lie within the query geometry. As a result, a query can
return **fewer results than actually exist**, in extreme cases even **zero results**.

**ESRI confirms** this behavior, but classifies it as **"as designed"** — so no fix from the
ArcGIS Server side is to be expected.

Not affected by this problem are pure **counts** (``returnCountOnly``) and queries that return
**only object ids** (``returnIdsOnly``): for both of these query types, observation shows that
the actual query geometry is passed to the database, not just its bounding box. This is exactly
what the workaround described below relies on.

.. important::

   The problem only occurs when the ArcGIS Server service's data resides in a **SQL Server** or
   **Oracle** database. With **PostGIS** as the data source, no occurrence of this behavior has
   been observed so far.

Configurable per service: ``QueryStrategy`` (CMS)
----------------------------------------------------

Since different ArcGIS Server instances, or the databases behind them, behave differently (see
above — PostGIS, for instance, is not affected), the workaround is enabled **not globally, but
per service**. The **CMS** provides the **``QueryStrategy``** property on the respective
**ArcServerService** for this:

* **``Default``** — a normal query (feature query with geometry/where clause sent directly to
  the ArcGIS Server), without any additional requests. This is always the **fastest option** and
  is used wherever it reliably produces correct results.
* **``BoundingBoxProblem``** — enables the **ids-first workaround** described below, for
  services where the bounding-box problem actually occurs.

Behavior with ``BoundingBoxProblem`` (decision cascade)
-----------------------------------------------------------

Even when a service is configured for ``BoundingBoxProblem``, the more expensive workaround is
not applied blindly. Before it is used, several **pre-checks** fall back to ``Default`` whenever
the problem cannot actually occur for the specific query, or would be harmless:

1. **Geometry check**

   Pure **attribute queries** (without geometry), queries with an **envelope geometry** (the
   bounding box already equals the query geometry here, so there is no difference), or with a
   **point** (a point's bounding box is the point itself) cannot trigger the problem in
   principle → ``Default`` is used.

2. **Bbox candidate check**

   For all other geometry types (line, polygon, multipoint), a cheap count is performed first
   to determine how many objects lie within the **bounding box** of the query geometry
   (``returnCountOnly``, itself not affected by the problem). If this value is **below** the
   server-side row limit (``maxRecordCount``), nothing could have been cut off in the internal
   bbox step before the actual clip happens → ``Default`` is sufficient here too.

3. **Ids-first workaround**

   Only when neither pre-check applies does the actual workaround (internally
   ``BoundingBoxProblemAgsQueryStrategy``) come into play. It runs in three steps:

   **Step A — candidate count against the real geometry**

   First, a count is performed via ``returnCountOnly`` against the **actual** query geometry or
   where clause (not the bounding box). If this real result count is **below** the configurable
   threshold ``ags-spatial-query-ids-paging-threshold`` (default: ``50000``), a single,
   **unpaginated** ``returnIdsOnly`` query is sufficient: the ArcGIS Server reliably returns
   **all** ids without a row limit, as long as no ``resultRecordCount`` is passed.

   **Step B — paging for large result sets**

   If the real result count exceeds the threshold (potentially hundreds of thousands or millions
   of results), the ids are instead fetched **page by page using keyset pagination**: each
   request adds the condition ``{id field} > {highest id found so far}`` (sorted ascending), with
   a page size equal to the service's ``maxRecordCount``. This process is aborted as soon as one
   of the following conditions occurs:

   * A page returns **no further ids** → all results have been found.
   * The configured **time budget** (``ags-spatial-query-ids-timeout-seconds``, default:
     ``20`` seconds) is exceeded → abort, the result is flagged as **incomplete**.
   * There is **no more progress** (the highest id found stops increasing) → abort, as a
     safeguard against infinite loops or duplicates.
   * **More than 50 consecutive** pages are received that are marked as truncated by the server
     but come back nearly empty → abort.

   Regardless of the reason for stopping, the overall result is additionally capped client-side
   to ``ags-spatial-query-max-result-cap`` (default: ``2000``).

   **Step C — loading the actual features**

   Only once the object ids have been determined via one of the two approaches above are the
   actual feature data (geometry and attributes) loaded. This is done in **batches** (batch
   size: ``ags-spatial-query-default-max-record-count-fallback``), which can be requested in
   parallel (see ``ags-spatial-query-max-parallel-batch-requests``), via ``query by objectIds``
   — a query type that is also not affected by the bounding-box problem.

In short
--------

``Default`` is always the preferred, cheapest strategy. ``BoundingBoxProblem`` is only enabled
for services where the problem can actually occur (SQL Server/Oracle as the data source), and
even then it is checked repeatedly whether the more expensive ids-first detour is actually
needed at all (geometry type, number of bbox candidates, number of real candidates). Only in the
worst case — many real results combined with a problematic geometry — does the full paging
procedure (step B) come into play.

Configuration
-------------

The numeric values of the ids-first workaround (steps A through C) can be adjusted via the
``tool-identify`` *section* in ``api.config``:

.. code-block:: xml

    <section name="tool-identify">
      <!-- ArcGIS Server spatial-query bounding-box workaround -->
      <add key="ags-spatial-query-max-result-cap" value="2000" />
      <add key="ags-spatial-query-default-max-record-count-fallback" value="1000" />
      <add key="ags-spatial-query-max-parallel-batch-requests" value="4" />
      <add key="ags-spatial-query-ids-timeout-seconds" value="20" />
      <add key="ags-spatial-query-ids-paging-threshold" value="50000" />
    </section>

The meaning of the individual attributes is described in the
:doc:`../config/api/index` chapter, under the **Identify** tool.

The ``QueryStrategy`` itself (``Default`` / ``BoundingBoxProblem``) is **not** an
``api.config`` value — it is set per service on the **ArcServerService** in the **CMS**.
