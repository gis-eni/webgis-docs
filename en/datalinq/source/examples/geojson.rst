Integrating GeoJSON
===================

This example explains how to integrate a GeoJSON service and display it in a table.
A selection list is offered via a filter. This is also filled by a GeoJSON service.

The corresponding service is a *gView MapServer* service with addresses. The values are retrieved
via a query. For the selection list, a query from the service is likewise used, with an additional DISTINCT.

.. note::
    The example can also be implemented 1:1 for an ArcGIS Server MapServer service. Here,
    only the path in the *connection string* of the *endpoint* changes.

Endpoint
--------

First, an *endpoint* named ``geojson-gview`` must be created.
The type for the *endpoint* is ``GeoJson``. As the connection string, specify
the URL to the gView Server GeoServices REST interface:

.. code-block::

   https://localhost/gview/geoservices/rest/services

Queries
--------

We want to query the addresses from a service (e.g. ``test/basis``). To do this, create a *query* ``adressen``
under the *endpoint*.

As the query, specify the URL path, relative to the URL given in the *endpoint's* connection string.
For gView (or AGS), the easiest way to determine this URL path is via the MapServer's REST interface.
There, you can usually create and run a query for the service via a user interface.
The URL path can then be copied from the browser's address bar.

.. code-block::

   /test/postgis/MapServer/0/query?where=plz%3D{{plz}}&
                                  geometry=&geometryType=&inSR=&relationParam=&objectIds=&time=0&distance=0&
                                  units=&outFields=*&returnGeometry=true&maxAllowableOffset=0&
                                  geometryPrecision=0&outSR=&returnIdsOnly=false&returnCountOnly=false&
                                  returnExtentOnly=false&orderByFields=&outStatistics=&groupByFieldsForStatistics=&
                                  returnZ=false&returnM=false&returnDistinctValues=false&
                                  returnTrueCurves=false&resultOffset=0&resultRecordCount=0&
                                  datumTransformation=&rangeValues=&quantizationParameters=&parameterValues=&
                                  historicMoment=0&
                                  layerId=0&f=geojson

.. note::
    A gView or AGS query requires many parameters. It is therefore recommended to create the link via the
    MapServer's UI.

In the example, a placeholder for a query was also defined: ``where=plz%3D{{plz}}``

.. note::
    The ``=`` must be URL-encoded as ``%3D``.

.. note::
    ``geojson`` must be specified as the output format of the query. The standard JSON format of gView or AGS
    is not GeoJSON! ``&f=geojson``

If you call the query (https://localhost/datalinq/select/geojson-gview@adressen?plz=3100&_pjson=true),
you get, for example, the following result:

.. code-block::

    [
        {
            "oid": null,
            "_location": {
                "Latitude": 48.1877734994291,
                "Longitude": 15.627903754497671,
                "BBox": null,
                "BBoxValid": false
            },
            "gid": 8285,
            "ortsname": "St. Pölten",
            "strassenname": "...",
            "adrcd": 6192061,
            "subcd": 1,
            "adresse": "... 1, 3100 St.Pölten",
            "hnr": "1",
            "plz": 3100,
            "pgnr": 30201,
            "pgname": "St. Pölten",
            "okznr": 3158,
            "kgnr": 19544,
            "kgname": "St. Pölten"
        },...
    ]

In the next step, we build a query via the MapServer interface that performs a DISTINCT on
the postal codes (plz), and enter the URL path into a new DataLinq query
``adressen-distinct-plz``:

.. code-block::

   /test/postgis/MapServer/0/query?where=1%3D1&
                                  geometry=&geometryType=&
                                  inSR=&relationParam=&objectIds=&time=0&distance=0&
                                  units=&outFields=plz&returnGeometry=false&
                                  maxAllowableOffset=0&geometryPrecision=0&outSR=&
                                  returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&
                                  orderByFields=&outStatistics=&groupByFieldsForStatistics=&
                                  returnZ=false&returnM=false&returnDistinctValues=true&returnTrueCurves=false&
                                  resultOffset=0&resultRecordCount=0&datumTransformation=&rangeValues=&
                                  quantizationParameters=&parameterValues=&historicMoment=0&
                                  layerId=0&f=geojson

This query requires no parameters and, when called (https://localhost/datalinq/select/geojson-gview@adressen-distinct-plz?_pjson=true),
returns the following:

.. code-block::

    [
        {
            "oid": null,
            "plz": 1300
        },
        {
            "oid": null,
            "plz": 2723
        },
        {
            "oid": null,
            "plz": 3925
        },...
    ]

View
----

Under the ``adressen`` query, we now build a view ``table``:

.. code-block::

    @DLH.Table(Model.Records, max: 100)

When called, this should show the first 100 addresses.

.. note::
    In the query, we specified a filter with the placeholder ``{{plz}}``.
    Therefore, the table may be *empty*. The parameter must now also be passed to the *view*.
    For testing, this can also be done via the *view's* settings:

    Under ``Test Url Parameters``, ``plz=3100`` can be entered.

In the next step, we further extend the *view* with a filter to filter by postal code.
The filter should offer a selection list of postal codes, filled via the DataLinq query ``adresse-distinct-plz``:

.. code-block::

    @DLH.FilterView(label: "Filter123",
                filterParameters: new Dictionary<string, object>{
                    {"plz", new { displayname="Postleitzahl",
                                  source="geojson-gview@adressen-distinct-plz",
                                  valueField="plz",
                                  nameField="plz" }
                    }
                })

    @DLH.Table(Model.Records, max: 100)

If you run the *view*, the table should now be filterable by postal code.
