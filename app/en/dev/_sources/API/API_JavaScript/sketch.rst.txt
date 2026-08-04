WebGIS 5.0 API: sketch
======================

Members
-------

=========================  ==================================================================
Name                       Description
=========================  ==================================================================
:ref:`fromJsonAnchor`      Takes over the sketch from a geometry object of a GeoJson feature.
:ref:`toJsonAnchor`        Returns the sketch as a GeoJSON geometry object.
:ref:`zoomToAnchorSketch`  Zooms to the sketch.
=========================  ==================================================================


Member Details
--------------

.. _fromJsonAnchor :

fromJson (json, append, readOnly)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Takes over the sketch from a geometry object of a GeoJson feature.

*Example*

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

Coordinates are expected in WGS84. If the coordinates are in a different system, this must be specified via the SRID property.

**Note:** if this coordinate system does not match the map's coordinate system, it must be registered with ``webgis.registerCRS(id)``.




.. _toJsonAnchor :

toJson (crsId)
^^^^^^^^^^^^^^

*Description*

Returns the sketch as a GeoJSON geometry object. A coordinate system can be passed as a parameter here. Otherwise, the object is returned in WGS84.

**Note:** if this coordinate system does not match the map's coordinate system, it must be registered with ``webgis.registerCRS(id)``.

*Example*

.. code-block:: javascript

    var jsonGeometry = sender.toJson(31259);

returns, for example:

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

*Description*

Zooms to the sketch.

*Example*

.. code-block:: javascript

    map.sketch.zoomTo();
