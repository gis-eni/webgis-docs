Embedded Maps
===================

Embedded maps refers to WebGIS API applications (maps) that are embedded on a third-party page.
The web page on which the WebGIS map is embedded is subsequently referred to as the third-party page.

There are basically two methods for this:

* On the third-party page, the API JavaScript files are loaded as shown in the API guide, and a map is built with them.
  The map is then shown in a DOM element of the third-party page. When the map is created, a *map* object is created,
  which can subsequently be accessed using the methods described in the API guide.



* An existing WebGIS application (map) is embedded on a third-party page via an ``iframe``. In this case, the third-party page
  generally has no access to the *map* object created on the embedded page. However, it is possible to react to
  changes in the map view via ``callback`` functions.

  .. toctree::
    :maxdepth: 2

    iframe
