WebGIS 5.0 API: graphics
========================

Members
-------

=========================    =============================================================================
Name                         Beschreibung                                                                
=========================    =============================================================================
:ref:`clearAnchor`           Entfernt die Graphik aus der Karte.                                         
:ref:`fromGeoJsonAnchor`     Übernimmt ein GeoJSON Objekt und überblendend dieses in der Karte als Grafik.
=========================    =============================================================================


Member Details
--------------


.. _clearAnchor :

clear()
^^^^^^^

*Beschreibung*

Entfernt die Graphik aus der Karte.

*Beispiel*

.. code-block:: javascript

    map.graphics.clear();


.. _fromGeoJsonAnchor :

fromGeoJson (gr)
^^^^^^^^^^^^^^^^

*Beschreibung*

Übernimmt ein GeoJSON Objekt und überblendend dieses in der Karte als Grafik.


*Beispiel*

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

Die Koordinaten werden in WGS84 erwartet. Liegen die Koordinaten in einem anderem System, muss das über die Eigenschaft SRID angeführt werden.

Über die Properties der einzelnen Features kann auch die Farbe und der Stil für die dargestellten Objekte angeben werden:


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


**Achtung:** entspricht dieses Koordinatensystem nicht dem Kartenkoordinatensystem, muss diese mit ``webgis.registerCRS(id)`` registriert werden

