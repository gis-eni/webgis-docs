WebGIS 5.0 API: map
===================

Members
-------

======================================  ===============================================================================================
Name	                                Beschreibung	                                                                               
======================================  ===============================================================================================
:ref:`addDynamicContentAnchor`          Zum Hinzufügen von dynamischem Inhalt in eine Karte.	                                       
:ref:`addMarkerAnchor`	                Fügt einen Marker der Karte hinzu.	                                                           
:ref:`currentBasemapServiceIdAnchor`    Frage die Id des aktuellen Hintergrunddienstes ab.	                                           
:ref:`getServiceAnchor`                 Gibt das entsprechende Service Objekt zurück.	                                               
:ref:`printAnchor`                      Erzeugt aus der aktuell dargestellten Karte einen Ausdruck bzw. ein Bild.                               
:ref:`removeMarkerAnchor`	            Entfernt einen Marker aus der Karte.	                                                       
:ref:`removeMarkerGroupAnchor`          Entfernt alle Marker, die mit der Methode toMarkerGroup() einer bestimmten Gruppe zugeor...	   
:ref:`serviceIdsAnchor`	                Gibt ein Array mit den Ids aller Services (Kartendiensten) zurück, die in der Karte eingebun..	
:ref:`setBasemapAnchor`	                Schaltet eine entsprechende Hintergrundkarte sichtbar                                           
:ref:`setScaleAnchor`	                Zoomt die Karte auf einen Punkt und Maßstab.                                                   
:ref:`toMarkerGroupAnchor`              Mit dieser Methode kann ein Marker einer Gruppe zugeordnet werden.                             
:ref:`zoomToAnchorMap`	                Zoomt die Karte auf einen übergebenen Ausschnitt.                                              
======================================  ===============================================================================================


Properties
----------

=================================   ===============================================================================================
Name	                            Beschreibung	                                                                               
=================================   ===============================================================================================
:ref:`graphicsPropertyAnchor`       Das graphics Element für diese Karte.                                       
:ref:`sketchPropertyAnchor`	        Über diess Eigenschaft erfolgt der Zugriff auf den Sketch in der Karte.	                                                                                                       
=================================   ===============================================================================================


Member Details
--------------

.. _addDynamicContentAnchor :

addDynamicContent (contentItems, loadFirst)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Zum Hinzufügen von dynamischem Inhalt in eine Karte.

Dynamischer Inhalt kann dabei sein:

* Ein GeoRSS Dienst
* Ein GeoJson Dienst
* Eine von der API veröffentlichte Abfrage

*Beispiel*


.. code-block:: javascript

    map.addDynamicContent([
            {   // Einbinden einer vordefinierten API Suche
                id: 'dynamic_content_id1',
                name: "Dynamische Inhalt 1",
                url: '/rest/services/serviceid@cms/queries/queryid',
                type: 'api-query'
            },
            {   // Einbinden einer vordefinierten API Suche mit suchbegriff(en)
                id: 'dynamic_content_id2',
                name: "Dynamische Inhalt 2",
                url: '/rest/services/serviceid@cms/queries/queryid/query?suchbegriff=wert&..',
                type: 'api-query' 
            },              
            {
                id: 'dynamic_content_id3',
                name: "Geo RSS Dienst",
                url: 'http://....../info.rss',
                type: 'georss'
                },
                {
                id: 'dynamic_content_id3',
                name: "GeoJson Dienst",
                url: 'http://....../info.json',
                type: 'geojson'
                },
         ], true);


.. _addMarkerAnchor :

addMarker (options)
^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Fügt einen Marker der Karte hinzu. Als Parameter wird ein Objekt übergeben, dass mindestens die geographischen Koordinaten des Markers enthalten muss. Zusätzlich kann noch beispielsweise ein Text übergeben werden, der dann in einem Popup für den Marker dargestellt wird.

*Beispiel*

.. code-block:: javascript

    marker = map.addMarker({
        lat: lngLat[1],
        lng: lngLat[0],
        icon:'blue',
        text: "Ich bin hier: (" + x + ", " + y + ")",
        openPopup: true,
        buttons: [{
            label: 'Marker entfernen',
            onclick: function(map, marker) {
                map.removeMarker(marker);
            }
        }]
    });


Hier wird noch ein Text für das Popup Fenster übergeben. Außerdem soll das Popup Fenster gleich geöffnet werden. Mit der Eigenschaft ``buttons`` kann noch ein Array von Objekten übergeben werden, die dann im Popup als Buttons dargestellt werden. Das Klickevent kann hier über die Eigentschaft onclick für jeden Button angeführt werden und erhält als Parameter das Map Objekt.

Als Icon können über die entsprechende ``icon``-Eigenschaft gesetzt werden. Mögliche Werte sind hier

* blue
* currentpos_red
* currentpos_green
* sektch_vertex

übergeben werden. Übergibt man dieser Eigenschaft ein Objekt, können auch komplett benutzerdefinierte Marker erstellt werden:

.. code-block:: javascript

    icon: {
        iconUrl: 'http://...', // Url zu einem Icon Bild
        iconSize: [30, 20], // Größe des Bildes
        iconAnchor: [15, 10], // Einfügepunkt des Markers in Bildkoordinaten
        popupAnchor: [15, 0] // Einfügepunkt des Popups in Bildkoordinaten
    }





.. _currentBasemapServiceIdAnchor :

currentBasemapServiceId ()
^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Frage die Id des aktuellen Hintergrunddienstes ab. Hintergrunddienste sind immer Tiling Dienste (Kacheln).

*Beispiel*


.. code-block:: javascript

    var basemapId = map.currentBasemapServiceId();




.. _getServiceAnchor :

getService (id)
^^^^^^^^^^^^^^^

*Beschreibung*

Gibt das entsprechende Service Objekt zurück.

*Beispiel*


.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');






.. _printAnchor :

print (options, callback)
^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Erzeugt aus der aktuell dargestellten Karte einen Ausdruck bzw. ein Bild. In diesem Bild sind alle Dienste, Kacheln und dargestellen Graphiken (gilt nicht für den aktuellen Werkzeugsketch oder Marker von Abfrageergebnissen) zusamengefasst.

Der erste Parameter gibt Optionen an, die das zurückgebene Bild beschreiben. Hier sind alle Eigenschaften optional (siehe Beispiel). Wichtig sind vor allem die Eigenschaften ``imageWidth`` und ``imageHeight``, die die Größe des ausgegeben Bildes beschreiben. Die Defaultwerte sind hier [1024, 760]. Weiters kann der Maßstab über die Eigenschaft ``scale`` übergeben werden. Hier ist der Defaultwert der aktuelle Maßstab in der Karte im Browser. Beim Erzeugen des Kartenbildes bleibt der übergebene Maßstab immer erhalben. Wenn sich die Bildgröße von der Größe der Karte im Browser unterscheidet, kann sich somit auch der aktuelle Auschnitt ändern. Die aufrufende API Applikation ist hier dafür verantwortlich, dass die Größe richtig übergeben wird. Wenn sich die Kartenbildgröße von der Karte im Browser unterscheidet und trotzdem der gesammte dargestellt Ausschnitt gezeichnet werden soll, muss der Maßstab (Eigenschaft scale) entsprechend angepasst werden. Der Mittelpunkt der Karte im Browser ist auch immer der Mittelpunkt im erzeugten Kartenbild.

Theoretisch können auch Parameter übergeben werden, um als Rückgabe ein PDF Dokument zu bekommen. Das wird hier allerdings nicht beschrieben, da die Möglichkeiten hier vom jeweiligen Betreiber/Adrministrator der WebGIS-API abhängig ist.

Die Funktion ist asynkron, der zweite Parameter ist eine Funktion, die aufgerufen wird, wenn das Kartenbild fertig ist. Dieser Funktion wird ein Objekt übergeben mit einer Eigenschaft ``url``, die einen Link zum erstellen Bild entspricht.

*Beispiel*


.. code-block:: javascript

    map.print({}, function(result) {
    // result.url....
    });


.. code-block:: javascript

    map.pring({
        imageWidth: 1920,    // default: 1024
        imageHeight: 1024,   // default: 760
        scale: 1000               // defaullt: aktueller Maßstab in der Karte
    },
    function(result) {
        webgis.$('<img />').attr('src', result.url).appendTo('body');
    });



.. _removeMarkerAnchor :

removeMarker (marker)
^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Entfernt einen Marker aus der Karte. Einziges Argument ist hier der Marker der von der Methode :ref:`addMarkerAnchor` zurück gegeben wird.

*Beispiel*


.. code-block:: javascript

    var marker=map.addMarker({...});
    ...
    map.removeMarker(marker);





.. _removeMarkerGroupAnchor :

removeMarkerGroup (groupName)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Entfernt alle Marker, die mit der Methode :ref:`toMarkerGroupAnchor` einer bestimmten Gruppe zugeordnet wurden. Als Parameter wird der Gruppenname (Zeichenkette) übergeben.

*Beispiel*


.. code-block:: javascript

    map.toMarkerGroup('my-markers', map.addMarker({...});
    map.toMarkerGroup('my-markers', map.addMarker({...});
    ...
    map.removeMarkerGroup('my-markers');




.. _serviceIdsAnchor :

serviceIds ()
^^^^^^^^^^^^^

*Beschreibung*

Gibt ein Array mit den Ids aller Services (Kartendiensten) zurück, die in der Karte eingebunden sind. Diese Methode kann verwendet werden um alle vorhanden Dienste in der Karte aufzulisten oder zu verarbeiten.

*Beispiel*

Hier wirde ein Schleife über alle Dienste ausgeführt und danach mit der Methode :ref:`getServiceAnchor` das eigentliche service-Object abgefragt. Danach kann auf die Methode und Eigenschaften des Dienstes zugegriffen werden.

.. code-block:: javascript

    var serviceIds = map.getServiceIds();
    for(var i = 0;i < serviceIds.length; i++) {
        var service = map.getService(serviceIds[i]);

        // do something
        console.log(service.name);

        service.setOpacity(0.5);

        // ...
    }






.. _setBasemapAnchor :

setBasemap (serviceId) 
^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Schaltet eine entsprechende Hintergrundkarte sichtbar. Als Hintergrundkarte ist hier immer Tiling-Dinst zu verstehen. Da immer nur ein Hintergrunddienst gleichzeit sichtbar ist, wird mit dieser Methode der aktuelle Hintergrunddienst automatisch ausgeblendet.

Als Parameter wird die Id des Hintergrunddienstes übergeben.

*Beispiel*


.. code-block:: javascript

    map.setBasemap('ortsplan@ccgis-default');



.. _setScaleAnchor :

setScale (s, center)
^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Zoomt die Karte auf einen Punkt und Maßstab. Der erste Parameter ist der Maßstab (zb 1000 für 1:1000). Der zweite Paremeter ist das neue Kartenzentrum als Array von geographischen Koordinaten [Lng, Lat].

*Beispiel*


.. code-block:: javascript

    map.zoomTo(1000, [15, 46]);   // Maßstab 1:1000



.. _toMarkerGroupAnchor :

toMarkerGroup (groupName, marker)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Mit dieser Methode kann ein Marker einer Gruppe zugeordnet werden. Das Gruppe ist hier eine beliebige Zeichenkette zu verstehen, die als Klammer für gleichartige Marker dient. Durch das Zuordnen von Markern in eine Gruppe wird später das entfernen dieser Marker einfacher, siehe Methode :ref:`removeMarkerGroupAnchor`.

Der erster Parameter für die Methode ist der Name der Gruppe, der zweite Parameter entspricht dem Marker, wie er von der Methode :ref:`addMarkerAnchor` zurückgegeben wird.


*Beispiel*


.. code-block:: javascript

    map.toMarkerGroup('my-markers', map.addMarker({...}));



.. _zoomToAnchorMap :

zoomTo (bounds, project)
^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Zoomt die Karte auf einen übergebenen Ausschnitt. Der erste Paremeter ist ein Array mit den Werten der BoundingBox: [min-Lng, min-Lat, max-Lng, max-Lat].

Lng steht hier für Longitude, also die geographische Länge (Längengrad)

Lat steht hier für Latitude, also die geographische Breite (Breitengrad)

 

Der zweite Parameter ist optional und ein Bool-Werte.

 

Die Methode erwartet als BoundingBox geographische Koordinaten (Länge [-180...+180], Breite [-90...+90]). Wird für den zweiten Parameter der Wert true übergeben, können hier auch projezierte Koordinaten in System der Karte übergeben werden.

*Beispiel*


.. code-block:: javascript

    map.zoomTo([15, 47, 16, 28]);

    map.zoomTo([-68000, 215000, -69000, 216000], true); // zB bei Kartenprojetion 31256 - GK-M34



Property Details
----------------


.. _graphicsPropertyAnchor :

graphics
^^^^^^^^

*Beschreibung*

Das graphics Element für diese Karte. Damit hat man Zugriff auf auf graphische Overlays (Linien, Symbole, Flächen) bzw. kann solche der Karte hinzufügen. 

*Beispiel*


.. code-block:: javascript

    map.graphics.fromGeoJson(geoJson);


.. _sketchPropertyAnchor :

sketch
^^^^^^

*Beschreibung*

Über diess Eigenschaft erfolgt der Zugriff auf den Sketch in der Karte. Mit dem Sketch hat der Anwender die Möglichkeit, Objekte zu zeichnen. Dies wird beispielsweise beim Messen oder Bearbeiten verwendet.

*Beispiel*


.. code-block:: javascript

    map.sketch.zoomTo();