WebGIS 5.0 API: graphics
========================

Members
-------

========================  ===============================================================
Name                      Description
========================  ===============================================================
:ref:`clearAnchor`        Removes the graphic from the map.
:ref:`fromGeoJsonAnchor`  Takes a GeoJSON object and overlays it on the map as a graphic.
========================  ===============================================================


Member Details
--------------


.. _clearAnchor :

clear()
^^^^^^^

*Description*

Removes the graphic from the map.

*Example*

.. code-block:: javascript

    map.graphics.clear();


.. _fromGeoJsonAnchor :

fromGeoJson (gr)
^^^^^^^^^^^^^^^^

*Description*

Takes a GeoJSON object and overlays it on the map as a graphic.


*Example*

.. code-block:: javascript

    map.graphics.fromGeoJson({
        geojson: {
            features: [{
                geometry: {
                    "type": "LineString",
                    "SRID": 31259,
                    "coordinates": [
                        [687883.796875, 189434.5859375],
                        [687883.3828125, 189439.5546875],
                        [687880.8359375, 189470.359375],
                        [687877.625, 189500.25],
                        [687869.25, 189564.15625],
                        [687868.3046875, 189570.625],
                        [687863.4765625, 189603.4921875],
                        [687855.375, 189647.125],
                        [687842.3125, 189708.890625]
                    ]
                }
            }]
        }
    });

Coordinates are expected in WGS84. If the coordinates are in a different system, this must be specified via the SRID property.

Color and style for the displayed objects can also be specified via the properties of the individual features:


.. code-block:: javascript

    map.graphics.fromGeoJson({
        geojson: {
        "features": [
        {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [
            [
                15.435174107551825,
                47.074882408392654
            ],
            [
                15.436670780182135,
                47.07599302849084
            ]
            ]
        },
        "properties": {
            "stroke": "#0000ff",
            "stroke-opacity": 0.8,
            "stroke-width": 9,
            "stroke-style": "15,15,3,15"
        }
        },
        {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
            15.435801744461317,
            47.074860488026204
            ]
        },
        "properties": {
            "symbol": "graphics/markers/hotspot0.gif"
        }
        },
        {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
            15.436622500419888,
            47.07542310791081
            ]
        },
        "properties": {
            "symbol": "graphics/markers/hotspot1.gif"
        }
        }
    ]
    }
    });


**Note:** if this coordinate system does not match the map's coordinate system, it must be registered with ``webgis.registerCRS(id)``
