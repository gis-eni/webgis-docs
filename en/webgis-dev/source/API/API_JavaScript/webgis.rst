WebGIS 5.0 API: webgis
======================

Members
-------

========================  ===================================================================
Name                      Description
========================  ===================================================================
:ref:`createMapAnchor`    With this method, a new map is created in an HTML (div) element.
:ref:`initAnchor`         Entry point for every WebGIS API application.
:ref:`projectAnchor`      Projects coordinates from WGS84 into a projected coordinate system.
:ref:`registerCRSAnchor`  Registers a coordinate system for the projection.
:ref:`unprojectAnchor`    Projects coordinates from a projected coordinate system to WGS84.
========================  ===================================================================



Properties
----------

=============================  =============================================
Name                           Description
=============================  =============================================
:ref:`clientidPropertyAnchor`  The client id for the WebGIS API application.
=============================  =============================================


Member Details
--------------

.. _createMapAnchor :

createMap (elemId, options)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

With this method, a new map is created in an HTML (div) element. The parameters here are the id of the target HTML element and an object that describes the map. This object must specify at least the map extent (corresponding to the extent and coordinate system of the map) and the services to be loaded.

*Example*

.. code-block:: javascript

    var map = webgis.createMap('map', {
        extent: 'stmk_m34@ccgis_sdep',
        services: 'ortsplan@ccgis_sdep,estag_basis_ags@ccgis_sdep,estag_dkm_ags@ccgis_sdep'
    });

The names of the extents and services depend on the respective API operator and can be viewed via the REST interface.



.. _initAnchor :

init (oninit)
^^^^^^^^^^^^^

*Description*

Entry point for every WebGIS API application. This method initializes all necessary API elements. A function is passed as a parameter, which is called after initialization. Maps can only start being created after initialization.

*Example*

.. code-block:: javascript

    webgis.init(function() {
        // maps can be created from here on
        var map = webgis.createMap('map', {
            extent: 'stmk_m34@ccgis_sdep',
            services: 'ortsplan@ccgis_sdep,estag_basis_ags@ccgis_sdep,estag_dkm_ags@ccgis_sdep'
        });
    });




.. _projectAnchor :

project (id, lnglat)
^^^^^^^^^^^^^^^^^^^^

*Description*

Projects coordinates from WGS84 into a projected coordinate system. The parameters are the id of the coordinate system (EPSG code) and an array with the coordinates [geographic longitude, geographic latitude]. If the target coordinate system is not the map's coordinate system, it must first be registered with ``webgis.registerCRS``. Otherwise, an input value is returned. The result is again an array with the projected coordinates [X,Y]

*Example*

.. code-block:: javascript

    var xy=webgis.project(31259, [15, 47]);
    var X=xy[0];
    var Y=xy[1];




.. _registerCRSAnchor :

registerCRS (id)
^^^^^^^^^^^^^^^^

*Description*

Registers a coordinate system for the projection. Internally, the map calculates using geographic coordinates (EPSG:4326). The ``webgis.project`` and ``webgis.unproject`` methods are used to convert projected coordinates into this system. By loading a map with ``webgis.createMap``, a projection between the map system (extent) and the geographic coordinates is possible. If other coordinate systems also need to be projected, they must be registered with this method.

*Example*

.. code-block:: javascript

    webgis.registerCRS(31259);

Additionally registers BMN-M34 alongside the map coordinate system. Afterward, projections can be done with the ``webgis.project`` and ``webgis.unproject`` methods.



.. _unprojectAnchor :

unproject (id, xy)
^^^^^^^^^^^^^^^^^^

*Description*

Projects coordinates from a projected coordinate system to WGS84. The parameters are the id of the coordinate system (EPSG code) and an array with the coordinates [X,Y]. If the target coordinate system is not the map's coordinate system, it must first be registered with ``webgis.registerCRS``. Otherwise, an input value is returned. The result is again an array with the geographic coordinates [geographic longitude, geographic latitude]

*Example*

.. code-block:: javascript

    var ll=webgis.unproject(31259, [682467.9, 215093.3]);
    var lat=ll[0];
    var lng=ll[1];


Property Details
----------------


.. _clientidPropertyAnchor :

clientid
^^^^^^^^

*Description*

The client id for the WebGIS API application. If you develop an API client, you must first create it as an API subscriber. The client id generated in the process must be specified here, and it only applies to clients running under a specific domain (HTTP referer).

**Note:** the client id must be assigned before calling ``webgis.init()``!


*Example*

.. code-block:: javascript

    webgis.clientid='my client id';
