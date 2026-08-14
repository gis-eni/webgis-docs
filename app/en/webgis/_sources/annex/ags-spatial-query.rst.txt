ArcGIS Server Spatial-Query Workaround
=======================================

.. note::

   Only affects map services of type **ArcGIS Server (REST)** that work against a
   **SQL Server** as their data source.

The Problem
-----------

For a **spatial query** (e.g. Identify by area, polygon selection, buffer search), the
**ArcGIS Server** evaluates the request against the **SQL Server** in two steps:

1. First, it filters purely by the **bounding box** (the rectangular envelope) of the query
   geometry. At this stage, the ArcGIS Server already applies a **row limit**.
2. Only afterwards are the resulting candidates clipped against the **actual query geometry**
   (e.g. the exact polygon) to determine the final results.

The problem: the row limit from step 1 is applied **before** the actual spatial clip. For
geometries whose bounding box is significantly larger than the geometry itself (e.g. narrow,
elongated or diagonally oriented polygons, large rings with a small core area, etc.), many of
the rows found via the bounding box can lie outside the actual query geometry. These
"unnecessary" hits consume the row limit from step 1, even though they would be discarded in
step 2 anyway.

In practice this means a query can return **fewer results than actually exist within the query
shape** — in extreme cases even **zero results**, despite matching objects being present. The
effect is more likely the denser the data is and the less favorable the ratio between the
bounding box and the actual geometry is.

The Workaround
---------------

To work around this behavior, a spatial query is no longer issued to the ArcGIS Server as a
single request, but resolved in several steps:

1. **Query object ids only** (``returnIdsOnly``)

   First, a query is issued that returns **only the object ids** for the query geometry, not
   the actual feature data (geometry and attributes). This variant of the query is **not
   affected** by the bounding-box problem described above, since the ArcGIS Server correctly and
   completely performs the spatial clip here.

2. **Fetching object ids in chunks**

   Even for a ``returnIdsOnly`` query, it must be prevented that, in the worst case, millions of
   ids are returned at once (e.g. if the query geometry covers a very large number of objects).
   The ArcGIS Server REST parameter for this is called ``resultRecordCount`` and exists, in
   principle, in **all** ArcGIS Server versions.

   The actual problem: for ``returnIdsOnly`` queries, ``resultRecordCount`` is only actually
   honored starting with **ArcGIS Server 11.5**. On older versions (**AGS < 11.5**), the
   parameter is simply **ignored** for this type of query — the ArcGIS Server then returns at
   most **1000 ids** regardless of what was requested, and does so **without any indication**
   that more results would actually exist (no ``exceededTransferLimit`` flag or similar, as
   known from regular feature queries). Whether the 1000 ids returned are already all the
   results, or whether more actually exist, therefore **cannot be determined** from the response
   itself. This is exactly what makes the workaround necessary and fairly elaborate: it has to
   actively keep paging and check whether new ids keep showing up, rather than being able to
   rely on a completion flag from the server.

   For this fallback case (AGS < 11.5, ``resultRecordCount`` ineffective for
   ``returnIdsOnly``), the assumed chunk size is controlled via the configurable **fallback
   value** (see ``ags-spatial-query-default-max-record-count-fallback`` below), which defaults
   to **1000 ids** per request.

   To obtain **all** ids despite this limit, the ids are fetched page by page:

   - The first request returns up to **[chunk size]** ids, sorted by ``ORDER BY OBJECTID``.
   - The **highest object id returned** is determined from the result.
   - The next request extends the original query geometry with the additional condition
     ``AND OBJECTID > [highest id found so far]``, returning the **next chunk** of ids.
   - This is repeated until either

     - a request returns **no further ids** (i.e. all results have been found), or
     - the total number of collected ids reaches the configured
       ``ags-spatial-query-max-result-cap`` limit. In this case, collection is aborted and the
       result is flagged as **incomplete** (``FeatureCollection.HasMore``), since further
       results may exist that were not fetched.

   Since each chunk in this approach is a separate ``returnIdsOnly`` query with the additional
   ``OBJECTID >`` filter sent to the ArcGIS Server, this step is also **not affected** by the
   bounding-box problem described above: each of these sub-queries is correctly evaluated by the
   ArcGIS Server against the actual geometry, just spread across several smaller portions
   instead of a single one.

3. **Loading features for the collected ids**

   Only once the complete (or cap-limited) list of object ids has been determined are the actual
   feature data (geometry and attributes) fetched via ``query by objectIds``. This step, too, is
   performed **in chunks**, whose size — if known from the service — follows the ArcGIS Server
   service's ``maxRecordCount``, or otherwise the configured fallback value
   (``ags-spatial-query-default-max-record-count-fallback``). To reduce the overall query
   duration, several of these chunks can be requested **in parallel** (see
   ``ags-spatial-query-max-parallel-batch-requests``).

Configuration
-------------

The behavior of the workaround can be adjusted via the ``tool-identify`` *section* in
``api.config``:

.. code-block:: xml

    <section name="tool-identify">
      <!-- ArcGIS Server spatial-query bounding-box workaround -->
      <add key="ags-spatial-query-max-result-cap" value="2000" />
      <add key="ags-spatial-query-default-max-record-count-fallback" value="1000" />
      <add key="ags-spatial-query-max-parallel-batch-requests" value="4" />
    </section>

The meaning of the individual attributes is described in the
:doc:`../config/api/index` chapter, under the **Identify** tool.
