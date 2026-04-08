===================================
Werkzeug ``XZ (Koordinaten/Höhen)``
===================================

.. note::

  In früheren **WebGIS 4.0**-Installationen befand sich im **API-App-Verzeichnis** der 
  Ordner ``system/proj``, in dem Projektionen definiert wurden. Diese Konfiguration wurde 
  nun in das Verzeichnis ``etc/coordinates/proj`` verschoben.

h.xml
=====

Zusätzlich zu diesem ``proj``-Ordner kann im Verzeichnis ``etc/coordinates`` nun optional 
eine Datei ``h.xml`` erstellt werden. In dieser Datei wird festgelegt, welche **Höhenwerte** 
zusätzlich zu den Koordinaten ermittelt werden.  

Die Struktur von ``h.xml`` entspricht der Konfigurationsdatei des Höhenabfragetools 
(``etc/heightabovedatum``).

default.xml
============

In der Datei ``proj/xy/default.xml`` kann definiert werden, welche Koordinatensysteme mit dem 
XYZ Werkzeug abgefragt werden können. Es können sowohl **Koordinaten** als auch **Höhenwerte** zurückgegeben werden,
wenn die entsprechenden Einstellungen in ``h.xml`` vorgenommen wurden.

.. code:: XML

  <?xml version="1.0" encoding="utf-8" ?>
  <projections>
    
    <projection id="31254" displayname="GK M28" minx="-200000" maxx="200000"/>
    <projection id="31255" displayname="GK M31" minx="-200000" maxx="200000"/>
    <projection id="31256" displayname="GK M34" minx="-200000" maxx="200000"/>
    <projection id="31287" displayname="Lambert (neu)" />
    
    <projection id="31257" displayname="BMN M28" maxx="300000"/>
    <projection id="31258" displayname="BMN M31" minx="300000" maxx="600000"/>
    <projection id="31259" displayname="BMN M34" minx="600000"/>
    <projection id="4326" displayname="WGS84" digits="6" />
    <projection id="4326" displayname="WGS84(GM)" displaystyle="dm" digits="2"/>
    <projection id="4326" displayname="WGS84(GMS)" displaystyle="dms" digits="1"/>
    <projection id="32632" displayname="UTM 32N" minx="-150000" maxx="850000" />
    <projection id="32633" displayname="UTM 33N" minx="-150000" maxx="850000" />

    <projection id="3857" displayname="web"  />
    
    <projection id="4326" displayname="UTMRef" displaystyle="mrgs" digits="5"/>
    
  </projections>

* **id**: EPSG-Code des Koordinatensystems
* **displayname**: Anzeigename im XYZ Werkzeug
* **minx/maxx**: Optional können hier die minimalen und maximalen X-Koordinaten angegeben werden, 
   um die Anzeige der Projektion im XYZ Werkzeug einzuschränken.
* **digits**: Anzahl der Nachkommastellen, die im XYZ Werkzeug angezeigt werden sollen
* **displaystyle**: Optional kann hier die Darstellungsweise der Koordinaten im XYZ Werkzeug 
   festgelegt werden. Mögliche Werte sind:
   * **dm**: Grad und Dezimalminuten (z. B. 47°04,69')
   * **dms**: Grad, Minuten und Sekunden (z. B. 47°04'41,4'')
   * **<geo-code-name>**: Name eines GeoCoders (https://docs.webgiscloud.com/de/webgis/annex/geocodes.html)

.. note::

   Mit dem XYZ Tool können auch **GeoCodes** abgefragt werden (siehe Anhang).
   Diese Beziehen sich in der Regel auf die **geographischen Koordinaten (EPSG:4326)**, 
   welche GeoCoder verwendet wird, kann über den Displaystyle festgelegt werden.

   Geographische Koordinaten (EPSG:4326) können auch mit einem benutzerdefinierten 
   Displaystyle angezeigt werden, z. B. als Grad und Dezimalminuten (47°04,69') ``dm`` oder 
   Grad, Minuten und Sekunden (47°04'41,4'') ``dms``.

tip.txt
=======

In der Benutzeroberfläche des XYZ Werkzeugs werden **Eingabe Tipps** angezeigt, 
die angeben, wie Koordinaten eingegeben werden können. Der Inhalt dieses Tooltips kann 
in der Datei ``tip.txt`` angepasst werden.

.. note::

  Die Dateien ``default.xml`` und ``tip.txt`` müssen nicht zwingend vorhanden sein.
  Wenn sie nicht vorhanden sind, greift WebGIS auf die Standardkonfiguration zurück,
  diese liegen in den Dateien ``default_.xml`` und ``tip_.txt``.