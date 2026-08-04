WebGIS 5.0 API: map
===================

Members
-------

====================================  ===========================================================================================
Name                                  Description
====================================  ===========================================================================================
:ref:`addDynamicContentAnchor`        For adding dynamic content to a map.
:ref:`addMarkerAnchor`                Adds a marker to the map.
:ref:`currentBasemapServiceIdAnchor`  Queries the id of the current background service.
:ref:`getServiceAnchor`               Returns the corresponding service object.
:ref:`printAnchor`                    Creates a printout or image from the currently displayed map.
:ref:`removeMarkerAnchor`             Removes a marker from the map.
:ref:`removeMarkerGroupAnchor`        Removes all markers that were assigned to a specific group with the toMarkerGroup() method.
:ref:`serviceIdsAnchor`               Returns an array with the ids of all services (map services) included in the map.
:ref:`setBasemapAnchor`               Makes the corresponding background map visible
:ref:`setScaleAnchor`                 Zooms the map to a point and scale.
:ref:`toMarkerGroupAnchor`            With this method, a marker can be assigned to a group.
:ref:`zoomToAnchorMap`                Zooms the map to a given extent.
====================================  ===========================================================================================


Properties
----------

=============================  =======================================================
Name                           Description
=============================  =======================================================
:ref:`graphicsPropertyAnchor`  The graphics element for this map.
:ref:`sketchPropertyAnchor`    This property provides access to the sketch in the map.
=============================  =======================================================


Member Details
--------------

.. _addDynamicContentAnchor :

addDynamicContent (contentItems, loadFirst)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

For adding dynamic content to a map.

Dynamic content can be:

* A GeoRSS service
* A GeoJson service
* A query published by the API

*Example*


.. code-block:: javascript

    map.addDynamicContent([
            {   // Including a predefined API search
                id: 'dynamic_content_id1',
                name: "Dynamic Content 1",
                url: '/rest/services/serviceid@cms/queries/queryid',
                type: 'api-query'
            },
            {   // Including a predefined API search with search term(s)
                id: 'dynamic_content_id2',
                name: "Dynamic Content 2",
                url: '/rest/services/serviceid@cms/queries/queryid/query?searchterm=value&..',
                type: 'api-query'
            },
            {
                id: 'dynamic_content_id3',
                name: "Geo RSS Service",
                url: 'http://....../info.rss',
                type: 'georss'
                },
                {
                id: 'dynamic_content_id3',
                name: "GeoJson Service",
                url: 'http://....../info.json',
                type: 'geojson'
                },
         ], true);


.. _addMarkerAnchor :

addMarker (options)
^^^^^^^^^^^^^^^^^^^

*Description*

Adds a marker to the map. The parameter is an object that must contain at least the geographic coordinates of the marker. In addition, for example, a text can be passed, which is then shown in a popup for the marker.

*Example*

.. code-block:: javascript

    marker = map.addMarker({
        lat: lngLat[1],
        lng: lngLat[0],
        icon:'blue',
        text: "I am here: (" + x + ", " + y + ")",
        openPopup: true,
        buttons: [{
            label: 'Remove marker',
            onclick: function(map, marker) {
                map.removeMarker(marker);
            }
        }]
    });


Here, a text for the popup window is also passed. In addition, the popup window should be opened immediately. With the ``buttons`` property, an array of objects can also be passed, which are then shown as buttons in the popup. The click event can be specified here via the onclick property for each button, and receives the map object as a parameter.

The icon can be set via the corresponding ``icon`` property. Possible values here are

* blue
* currentpos_red
* currentpos_green
* sektch_vertex

If you pass an object to this property, completely custom markers can also be created:

.. code-block:: javascript

    icon: {
        iconUrl: 'http://...', // Url to an icon image
        iconSize: [30, 20], // Size of the image
        iconAnchor: [15, 10], // Insertion point of the marker in image coordinates
        popupAnchor: [15, 0] // Insertion point of the popup in image coordinates
    }





.. _currentBasemapServiceIdAnchor :

currentBasemapServiceId ()
^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Queries the id of the current background service. Background services are always tiling services (tiles).

*Example*


.. code-block:: javascript

    var basemapId = map.currentBasemapServiceId();




.. _getServiceAnchor :

getService (id)
^^^^^^^^^^^^^^^

*Description*

Returns the corresponding service object.

*Example*


.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');






.. _printAnchor :

print (options, callback)
^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Creates a printout or image from the currently displayed map. In this image, all services, tiles, and displayed graphics (does not apply to the current tool sketch or markers from query results) are combined.

The first parameter specifies options that describe the returned image. All properties here are optional (see example). The properties ``imageWidth`` and ``imageHeight``, which describe the size of the output image, are particularly important. The default values here are [1024, 760]. Furthermore, the scale can be passed via the ``scale`` property. The default value here is the current scale in the map in the browser. When creating the map image, the passed scale is always retained. If the image size differs from the size of the map in the browser, the current view may thus change. The calling API application is responsible for ensuring that the size is passed correctly. If the map image size differs from the map in the browser and the entire displayed view should still be drawn, the scale (``scale`` property) must be adjusted accordingly. The center of the map in the browser is also always the center of the generated map image.

Theoretically, parameters can also be passed to get a PDF document as a return value. This is not described here, however, since the options here depend on the respective operator/administrator of the WebGIS API.

The function is asynchronous; the second parameter is a function that is called when the map image is ready. This function is passed an object with a ``url`` property, which corresponds to a link to the created image.

*Example*


.. code-block:: javascript

    map.print({}, function(result) {
    // result.url....
    });


.. code-block:: javascript

    map.pring({
        imageWidth: 1920,    // default: 1024
        imageHeight: 1024,   // default: 760
        scale: 1000               // default: current scale in the map
    },
    function(result) {
        webgis.$('<img />').attr('src', result.url).appendTo('body');
    });



.. _removeMarkerAnchor :

removeMarker (marker)
^^^^^^^^^^^^^^^^^^^^^

*Description*

Removes a marker from the map. The only argument here is the marker returned by the :ref:`addMarkerAnchor` method.

*Example*


.. code-block:: javascript

    var marker=map.addMarker({...});
    ...
    map.removeMarker(marker);





.. _removeMarkerGroupAnchor :

removeMarkerGroup (groupName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Removes all markers that were assigned to a specific group with the :ref:`toMarkerGroupAnchor` method. The group name (string) is passed as a parameter.

*Example*


.. code-block:: javascript

    map.toMarkerGroup('my-markers', map.addMarker({...});
    map.toMarkerGroup('my-markers', map.addMarker({...});
    ...
    map.removeMarkerGroup('my-markers');




.. _serviceIdsAnchor :

serviceIds ()
^^^^^^^^^^^^^

*Description*

Returns an array with the ids of all services (map services) included in the map. This method can be used to list or process all services present in the map.

*Example*

Here, a loop is run over all services, and then the actual service object is queried with the :ref:`getServiceAnchor` method. Afterward, the service's methods and properties can be accessed.

.. code-block:: javascript

    var serviceIds = map.getServiceIds();
    for(var i = 0;i < serviceIds.length; i++) {
        var service = map.getService(serviceIds[i]);

        // do something
        console.log(service.name);

        service.setOpacity(0.5);

        // ...
    }






.. _setBasemapAnchor :

setBasemap (serviceId)
^^^^^^^^^^^^^^^^^^^^^^

*Description*

Makes the corresponding background map visible. A background map here always means a tiling service. Since only one background service can ever be visible at a time, this method automatically hides the current background service.

The id of the background service is passed as a parameter.

*Example*


.. code-block:: javascript

    map.setBasemap('ortsplan@ccgis-default');



.. _setScaleAnchor :

setScale (s, center)
^^^^^^^^^^^^^^^^^^^^

*Description*

Zooms the map to a point and scale. The first parameter is the scale (e.g. 1000 for 1:1000). The second parameter is the new map center as an array of geographic coordinates [Lng, Lat].

*Example*


.. code-block:: javascript

    map.zoomTo(1000, [15, 46]);   // scale 1:1000



.. _toMarkerGroupAnchor :

toMarkerGroup (groupName, marker)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

With this method, a marker can be assigned to a group. The group here is any string that serves as a bracket for markers of the same kind. Assigning markers to a group later makes it easier to remove those markers, see the :ref:`removeMarkerGroupAnchor` method.

The first parameter for the method is the name of the group; the second parameter corresponds to the marker as returned by the :ref:`addMarkerAnchor` method.


*Example*


.. code-block:: javascript

    map.toMarkerGroup('my-markers', map.addMarker({...}));



.. _zoomToAnchorMap :

zoomTo (bounds, project)
^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Zooms the map to a given extent. The first parameter is an array with the values of the bounding box: [min-Lng, min-Lat, max-Lng, max-Lat].

Lng here stands for Longitude, i.e. the geographic longitude.

Lat here stands for Latitude, i.e. the geographic latitude.



The second parameter is optional and a boolean value.



The method expects geographic coordinates as the bounding box (longitude [-180...+180], latitude [-90...+90]). If the value true is passed for the second parameter, projected coordinates in the map's coordinate system can also be passed here.

*Example*


.. code-block:: javascript

    map.zoomTo([15, 47, 16, 28]);

    map.zoomTo([-68000, 215000, -69000, 216000], true); // e.g. for map projection 31256 - GK-M34



Property Details
----------------


.. _graphicsPropertyAnchor :

graphics
^^^^^^^^

*Description*

The graphics element for this map. This gives access to graphical overlays (lines, symbols, areas), or allows such elements to be added to the map.

*Example*


.. code-block:: javascript

    map.graphics.fromGeoJson(geoJson);


.. _sketchPropertyAnchor :

sketch
^^^^^^

*Description*

This property provides access to the sketch in the map. With the sketch, the user has the ability to draw objects. This is used, for example, when measuring or editing.

*Example*


.. code-block:: javascript

    map.sketch.zoomTo();
