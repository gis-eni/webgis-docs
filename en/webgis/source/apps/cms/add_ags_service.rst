Integrating an ArcGIS Server Service
======================================

For this, switch to ``Services/ArcGIS Server/MapServer Service`` in the CMS tree:

.. image:: img/image120.png

Click ``Integrate new service``:

.. image:: img/image121.png

Then click ``Update Services``, assign a name, and click ``Apply``.

.. note::
   If the name is maintained in the MXD in the case of AGS, it is also already adopted automatically. If
   it is not maintained, the name in the service is "Layer" or "Layers" => it is not adopted into the CMS => it becomes "General".

Applying can take a few seconds. Afterwards, you can click on the service in the view and edit further properties of the service:

.. image:: img/image123.png

Once the service appears in the list, further properties of the service can be edited:

.. image:: img/image124.png

* **Export Map Format:**
  Normally, the AGS returns the result of a map request in JSON format. This contains the URL
  to the actual image in the output directory. In our case, the image is stored in the output directory behind our
  firewall and is NOT reachable via the internet. The map image would therefore be created, but
  is not reachable for the browser. The value "Image" remedies this problem. In this case, the
  result from the AGS is returned not as JSON, but as an image (bytes). WebGIS receives this directly and stores it in the
  "Cloud" output directory, which is available via the internet. In the cloud, this method also has the advantage
  that it cannot be traced via the internet where the map service comes from.
  Client (Browser) <-> WebGIS <-> ArcGIS Server

.. note::
   For a WebGIS instance installed at a customer's site, this value should generally be left empty or set to JSON,
   because a client usually has access to the output directory. This generally results in less traffic:

   1. Client (Browser) <-> WebGIS <-> ArcGIS Server (ImageRequest/JSON)
   2. Client (Browser)            <->           Output directory

Dynamic Services
------------------

The following settings offer a simplification when it comes to parameterization:

.. image:: img/add_ags_service1.png

Normally, both presentation variants and queries must be parameterized separately in the CMS for a service.
This gives the administrator flexibility to determine which topics can be toggled visible or
queried, and in what way. However, a grouping of the topics is often already defined in the service. To avoid
parameterizing the same thing in multiple places, this setting can be used. This creates the presentation variants
*dynamically* from the service.

.. note::
   Below the service there are the sections ``Queries`` and ``Layer Toggles``, where these properties can be
   parameterized individually. If you set a value other than ``None`` in the options shown here, these sections
   disappear. It is only possible to make the content available either *dynamically* or *individually parameterized*.

Dynamic Presentation Variants
++++++++++++++++++++++++++++++++

* **None:** The presentation variants must be parameterized individually. To do this, the individual toggles must first be defined in the ``Layer Toggles`` section of the service. These can then be added to a presentation container in the ``Map Viewer`` CMS node. This process is described in the following sections.

* **Auto:** The topic tree is taken from the service. For each topic, a *checkbox* button is offered in the corresponding group. In the map viewer, a separate container for this service is created in the presentation-variants TOC.

* **AutoMaxLevel(1,2,3):** The topics are likewise taken from the service here. However, not all hierarchy levels are adopted. The maximum number of levels corresponds to the value specified here. Topics that are located at a deeper level are combined into a single topic (group) that can be toggled via a *checkbox*.

  Example: a service has the following topics:

    * Base data/Cadastre/Parcels
    * Base data/Cadastre/Usage symbols
    * Base data/Cadastre/Labeling

  With ``Auto``, the tree is displayed as follows:

  .. code::

        [[  Service Container ]]
        -----------------------
        + Base data
          + Cadastre
            [x] Parcels
            [x] Usage symbols
            [x] Usage symbols

  ``AutoMaxLevel2`` would limit the tree to two levels. The bottom group would appear as a *checkbox* and toggle all topics beneath it:

  .. code::

        [[  Service Container ]]
        -----------------------
        + Base data
          [x] Cadastre

  ``AutoMaxLevel1`` finally allows only one level within the presentation-variants container:

  .. code::

        [[  Service Container ]]
        -----------------------
        [x] Base data

.. note::
   With dynamic presentation variants, the individual layers are always toggled via *checkboxes*. If you want to
   use additional options (buttons, option boxes, markers), the complete tree must be parameterized in the CMS via
   layer toggles/presentation variants.

Dynamic Queries
+++++++++++++++++

* **None:** The queries must be parameterized for the service in the ``Queries`` section. This process is described in the next section.

* **Auto:** A query topic is created at runtime for each queryable topic in the service. All fields are shown in the results table.

.. note::
   All queryable topics are offered as a query with all fields. If certain topics should be
   available as a query, or if search fields should be searchable within topics, all queries
   must be parameterized in the CMS.

.. _cms-ags-user-renderer-labeling:

User-defined Rendering and Labeling
-----------------------------------

.. versionadded:: 9.26.4104

The following service properties allow users to define the presentation or the labeling of individual layers
themselves in the table of contents of the map viewer (menu items **Presentation** and **Labeling** in the context menu, see the
`manual <https://docs.webgiscloud.com/en/webgis-manual/mapviewer/presentation/index.html#toc-context-menu>`_):

* **Allow user-defined rendering (Rendering from TOC):** the user can define a custom presentation for individual layers
  (single symbol, unique values, classes).
* **Allow user-defined labeling (Labeling from TOC):** the user can define a custom labeling for individual layers
  or switch the labeling off.

Both properties are switched off by default and, like other authorizable properties, can be restricted to certain roles.
Prerequisites:

* The ArcGIS Server service must support **DynamicLayers** (``supportsDynamicLayers``). The function is only available for feature layers
  (point, line, polygon).
* The respective function must be enabled in the ``toc-contextmenu`` section of ``api.config``
  (``allow-toc-userrenderer`` or ``allow-toc-userlabeling``, see :ref:`api-config-toc-contextmenu`).
* Only the fields that are also offered in the **QueryBuilder** are available to the user.

The presentation or labeling defined by the user is passed to ArcGIS Server via DynamicLayers with every map request.
Invalid definitions (e.g. fields that are not allowed) are ignored; the layer is then drawn with its default presentation.

.. _cms-ags-query-statistics:

Statistics for a Query Result
-----------------------------

.. versionadded:: 9.26.4104

The **Statistics** tool is available in the result table of the map viewer (count, minimum, maximum, average, sum
and count per value of a field, see the
`manual <https://docs.webgiscloud.com/en/webgis-manual/mapviewer/search_identify/operations/results_desktop/results_desktop.html#results-query-statistics>`_).
The statistics are calculated by ArcGIS Server over the whole query (``outStatistics`` or ``groupByFieldsForStatistics``), even if
the query returns more hits than are shown in the table. No separate configuration is necessary. The following
prerequisites and restrictions apply:

* Statistics are only available for layers of **ArcGIS Server** services that support statistics queries (``supportsStatistics``).
  For other services (e.g. WMS, WFS), the tool is not shown.
* The **QueryBuilder** must be allowed for the service. Only the fields enabled in the CMS for the service under **QueryBuilder** are offered
  (as with the *Restrict* tool).
* For date fields, only key figures (count, minimum, maximum) are calculated; grouping or restricting by values is not possible.
* The number of values for *Count per value* is limited by the maximum record count of the service (``maxRecordCount``).
  If not all values are returned, this is shown to the user.
* Restricting to a rank (all values with the same count) is limited to 1000 values and not possible if empty values or
  values with a comma are included.
