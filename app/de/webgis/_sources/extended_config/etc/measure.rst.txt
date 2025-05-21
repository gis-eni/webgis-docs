===========================
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