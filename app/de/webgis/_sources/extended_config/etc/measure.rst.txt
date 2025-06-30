===========================
Werkzeug ``Strecke Messen``
===========================

Damit das **Strecke-Messen-Werkzeug** auch in **3D** genutzt werden kann, muss im Verzeichnis ``etc/measure`` eine Datei ``3d.xml`` angelegt werden. Die Struktur dieser Datei entspricht der Konfiguration für die Höhenabfrage. Es gibt jedoch einige Einschränkungen: 

- Es darf nur **eine** Höhenabfrage definiert werden.  
- Das Ergebnis muss ein **numerischer Höhenwert** sein (ohne Textzusätze wie „müA“).  

Beispielkonfiguration:

.. code-block:: xml

   <!-- Example for an ArcGIS Server Servie -->
   <xml>
        <heightabovedatum
            type="ags"
            srs="31256"
            name="DTM"
            server="my-server.com"
            service="https://my-server.com/../rest/.../servicename/MapServer"

            user="username" pwd="my-passw0rd" tokenExpiration="60"  
            
            rastertheme="DGM"  
            expression="{0:0.00}" />
   </xml>

.. code-block:: xml

   <!-- Example for an ArcGIS Server Mosaic services -->
   <xml>
        <heightabovedatum
            type="ags-mosaic"
            srs="31256"
            name="DTM"
            server="my-server.com"
            service="https://my-server.com/../rest/.../servicename/MapServer"            
            
            user="username" pwd="my-passw0rd" tokenExpiration="60"  
            
            rastertheme="DGM"  
            expression="{0:0.00}" />
   </xml>

.. code-block:: xml

   <!-- Example for a IMS Service -->
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

.. note::

   ``user`` und ``pwd`` sind nur erforderlich, wenn der Dienst geschützt ist.
   Bei geschützen AGS Diensten empfiehlt es sich auch den Parameter ``tokenExpiration`` zu setzen, 
   um die Gültigkeit des Tokens zu definieren. Der Wert ist in Minuten anzugeben.
   Wird hier ein zu hoher Wert angegeben, kann ein Token eventuell nicht abgeholt werden 
   (long living Tokens).