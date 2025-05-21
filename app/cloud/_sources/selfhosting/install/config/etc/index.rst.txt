Erweiterte Werkzeugkonfiguration (etc-Verzeichnis)
==================================================

Einige Werkzeug benötigen mehr Konfigurationsmöglichkeit, als es in einer 
*flachen* config-Datei möglich ist. Diese Konfigurationsdateien werden im ``etc``-Verzeichnis angelegt.

In der Regel gibt es für jedes konfigurierbare Werkzeug ein Unterverzeichnis. 
Im Installationspaket befindet sich in jedem dieser Sub-Verzeichnis ein example(s) Ordner, 
in dem eine mögliche Konfiguration abgelegt ist, die dann angepasst werden kann.

Einige Beispiele werden hier kurz beschreiben:

Werkzeug Strecke Messen
-----------------------

Damit das Strecke Messen Werkzeug auch in 3D möglich ist, 
kann ins ``etc/measure`` Verzeichnis eine Datei ``3d.xml`` abgelegt werden. 
Die Struktur des Files entspricht wieder dem für die Höhenabfrage. 
Die Einschränkung ist hier allerdings, dass nur eine Höhenabfrage definiert werden darf, 
und dass das Ergebnis ein Höhenwert (Zahl ohne Textzusatz wie müA…) ist:

.. code::
   
   <xml>

        <heightabovedatum 
            type="ims" 
            srs="31256"
            name="DTM"
            server="my.server.com:8010"          
            service="hoehenservice" 
            rastertheme="hoeheDTM "
                        expression="{0:0.00}"
                        />

    </xml>


Werkzeug XZ (Koordinaten/Höhen)
-------------------------------

In der alten WebGIS 4.0 Installationen lag im API app-Verzeichnis ein Ordner ``system/proj``,
in dem Projektionen definiert wurden. 
Diese Konfiguration befindet sich ab jetzt unter ``etc/coordinates/proj``.

Zusätzlich zum bisherigen proj-Ordner, kann in ``etc/coordinates`` jetzt auch noch (optional) 
ein ``h.xml`` angelegt werden. Hier wird angegeben, welche Höhen zusätzlich zu den Koordinaten 
ermittelt werden. 
Der Aufbau der Datei entspricht dem für das Höhenabfragetool (``etc/heightabovedatum``).