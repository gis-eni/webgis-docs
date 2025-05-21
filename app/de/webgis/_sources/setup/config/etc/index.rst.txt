==================================================
Erweiterte Werkzeugkonfiguration (etc-Verzeichnis)
==================================================

Einige Werkzeuge erfordern erweiterte Konfigurationsmöglichkeiten, die über eine *flache* Konfigurationsdatei hinausgehen. Diese spezifischen Konfigurationsdateien werden im ``etc``-Verzeichnis abgelegt.

In der Regel existiert für jedes konfigurierbare Werkzeug ein eigenes Unterverzeichnis. Das Installationspaket enthält in diesen Unterverzeichnissen einen ``example(s)``-Ordner, der eine Beispielkonfiguration bereitstellt. Diese kann an individuelle Anforderungen angepasst werden.

Nachfolgend werden einige Beispiele beschrieben:

Werkzeug ``Strecke Messen``
===========================

Damit das **Strecke-Messen-Werkzeug** auch in **3D** genutzt werden kann, muss im Verzeichnis ``etc/measure`` eine Datei ``3d.xml`` angelegt werden. Die Struktur dieser Datei entspricht der Konfiguration für die Höhenabfrage. Es gibt jedoch einige Einschränkungen: 

- Es darf nur **eine** Höhenabfrage definiert werden.  
- Das Ergebnis muss ein **numerischer Höhenwert** sein (ohne Textzusätze wie „müA“).  

Beispielkonfiguration:

.. code-block:: xml

   <xml>
       <heightabovedatum 
           type="ims" 
           srs="31256"
           name="DTM"
           server="my.server.com:8010"          
           service="hoehenservice" 
           rastertheme="hoeheDTM"
           expression="{0:0.00}" />
   </xml>

Werkzeug ``XZ (Koordinaten/Höhen)``
====================================

In früheren **WebGIS 4.0**-Installationen befand sich im **API-App-Verzeichnis** der Ordner ``system/proj``, in dem Projektionen definiert wurden. Diese Konfiguration wurde nun in das Verzeichnis ``etc/coordinates/proj`` verschoben.

Zusätzlich zu diesem ``proj``-Ordner kann im Verzeichnis ``etc/coordinates`` nun optional eine Datei ``h.xml`` erstellt werden. In dieser Datei wird festgelegt, welche **Höhenwerte** zusätzlich zu den Koordinaten ermittelt werden.  

Die Struktur von ``h.xml`` entspricht der Konfigurationsdatei des Höhenabfragetools (``etc/heightabovedatum``).
