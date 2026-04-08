Geo Codes
=========

GeoCodes sind alphanumerische Codes, die geografische Standorte repräsentieren. 
Sie bieten eine kompakte und standardisierte Möglichkeit, Orte auf der Erde zu identifizieren. 
GeoCodes werden in verschiedenen Anwendungen verwendet, von Navigation und Kartierung bis hin zu 
Geocaching und Standortdiensten.

Im WebGIS können GeoCodes sowohl in über das XYZ (Koordinaten) Werkzeug angefragt werden, also auch 
in der Schnellsuche gefunden werden. Es werden folgende GeoCodes unterstützt:

.. list-table:: Uebersicht Geo Codes
   :header-rows: 1

   * - Name
     - Displayname
     - Link
     - Beispiel
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

Der **Name** gilt als eindeutige Bezeichnung des GeoCode-Formats und wird in der Konfiguration
angegeben um einen GeoCoder im WebGIS zu aktivieren.

.. note::

    **LatLon** sind kein klassischer GeoCode im engeren Sinne, sondern die gebräuchlichste Form 
    der geografischen Koordinaten. Die wie GeoCodes zu behandeln macht für die Schnellsuche Sinn,
    da Anwender oft Koordinaten eingeben, um einen Ort zu finden. Die Koordinaten können über diese 
    *GeoCoder* in der Schnellsuche erkannt und direkt auf der Karte angezeigt werden.

.. note::

    Welche GeoCode in der Schnellsuche funktionieren wird in der ``api.config``.
    Die GeoCode, die auch über das XYZ Werkzeug abgefragt werden können, in der Datei ``webgis-repository\configuration\etc\coordinates\proj\xy\defalt.xml``
    festgelegt.
