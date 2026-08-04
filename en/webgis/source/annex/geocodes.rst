Geo Codes
=========

GeoCodes are alphanumeric codes that represent geographic locations.
They provide a compact and standardized way to identify places on Earth.
GeoCodes are used in various applications, from navigation and mapping to
geocaching and location-based services.

In WebGIS, GeoCodes can be queried both via the XYZ (coordinates) tool and
found via the quick search. The following GeoCodes are supported:

.. list-table:: Overview of Geo Codes
   :header-rows: 1

   * - Name
     - Display Name
     - Link
     - Example
   * - **mrgs**
     - MRGS/UTMRef Code
     - * https://en.wikipedia.org/wiki/Military_Grid_Reference_System
       * https://de.wikipedia.org/wiki/UTM-Referenzsystem
     - 33TWN3301713224
       33TWN3313
   * - **pluscode**
     - Google Plus Code
     - https://plus.codes/howitworks
     - 8FVQ3CCP+F2
   * - **geohash**
     - Geohash
     - https://en.wikipedia.org/wiki/Geohash
     - u26gz1p3x069
   * - **georef**
     - World Geographic Reference System
     - https://en.wikipedia.org/wiki/World_Geographic_Reference_System
     - PKAC26100427
   * - **latlon**
     - Geographic Coordinates (Latitude, Longitude)
     - * https://www.latlong.net/
       * https://en.wikipedia.org/wiki/Geographic_coordinate_system
     - 47.078167, 15.439833
       47.078167 15.439833
       47,078167 15,439833
       47,078167, 15,439833
       47°04,69' 15°26,39'
       47°04'41,4'' 15°26'23,4''
       47 04 41,4 15 26 23,4

The **Name** serves as the unique identifier of the GeoCode format and is specified in the
configuration to enable a GeoCoder in WebGIS.

.. note::

    **LatLon** is not a classic GeoCode in the strict sense, but the most common form
    of geographic coordinates. Treating it like a GeoCode makes sense for the quick search,
    since users often enter coordinates to find a location. The coordinates can be recognized
    via this *GeoCoder* in the quick search and shown directly on the map.

.. note::

    Which GeoCodes work in the quick search is defined in ``api.config``.
    The GeoCodes that can also be queried via the XYZ tool are defined in the file
    ``webgis-repository\configuration\etc\coordinates\proj\xy\defalt.xml``.
