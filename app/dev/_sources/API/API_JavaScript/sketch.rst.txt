WebGIS 5.0 API: sketch
======================

Members
-------

=========================   =============================================================================
Name                        Beschreibung                                                                
=========================   =============================================================================
:ref:`fromJsonAnchor`       Übernimmt den Sketch aus einem Geometrie Objekt einen GeoJson Features.                                     
:ref:`toJsonAnchor`         Gibt den Sketch als GeoJSON Geometry Objekt zurück.
:ref:`zoomToAnchorSketch`   Zoom auf den Sketch.
=========================   =============================================================================


Member Details
--------------

.. _fromJsonAnchor :

fromJson (json, append, readOnly)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Übernimmt den Sketch aus einem Geometrie Objekt einen GeoJson Features.

*Beispiel*

.. code-block:: javascript

    map.sketch.fromJson(
    {
        "type": "LineString",
        "SRID": 31259,
        "coordinates": [
            [687883.796875, 189434.5859375],
            [687883.3828125, 189439.5546875],
            [687880.8359375, 189470.359375],
            [687877.625, 189500.25],
            [687869.25, 189564.15625],
            [687868.3046875, 189570.625],
            [687863.4765625, 189603.4921875]
        ]
    }
    );

Die Koordinaten werden in WGS84 erwartet. Liegen die Koorinaten in einem anderm System, muss das über die Eigenschaft SRID angeführt werden.

**Achtung:** entspricht dieses Koordinatensystem nicht dem Kartenkoordinatensystem, muss diese mit ``webgis.registerCRS(id)`` registriert werden.




.. _toJsonAnchor :

toJson (crsId) 
^^^^^^^^^^^^^^

*Beschreibung*

Gibt den Sketch als GeoJSON Geometry Objekt zurück. Als Parameter kann hier ein Koordinatensystem übergeben werden. Ansonsten wird das Objekt in WGS84 zurück gegeben.

**Achtung:** entspricht dieses Koordinatensystem nicht dem Kartenkoordinatensystem, muss diese mit ``webgis.registerCRS(id)`` registriert werden.

*Beispiel*

.. code-block:: javascript

    var jsonGeometry = sender.toJson(31259);

liefert beispielsweise:

.. code-block:: javascript

    {
        "type": "LineString",
        "SRID": 31259,
        "coordinates": [
            [687883.796875, 189434.5859375],
            [687883.3828125, 189439.5546875],
            [687880.8359375, 189470.359375],
            [687877.625, 189500.25],
            [687869.25, 189564.15625],
            [687868.3046875, 189570.625],
            [687863.4765625, 189603.4921875]
        ]
    }




.. _zoomToAnchorSketch :

zoomTo () 
^^^^^^^^^

*Beschreibung*

Zoom auf den Sketch.

*Beispiel*

.. code-block:: javascript

    map.sketch.zoomTo();

