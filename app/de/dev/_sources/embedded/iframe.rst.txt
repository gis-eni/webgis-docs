Karten über iFrame einbettten
=============================

In diesem Abschnitt wird eine Anwendung vorgestellt, bei der eine bestehende WebGIS Karte über ein ``iframe`` auf einer
Drittseite eingebunden wird. Zusätzlich wird über eine ``callback`` Funktion versucht, auf der Drittseite auf
Änderungen des Kartenausschnittes zu reagieren. Außerdem kann ein Bild des aktuellen Karteninhalts von der *Parent* Seite abgeholt werden,
um das aktuelle Kartenbild herunterzuladen (bzw. in einem ``img`` Element auf der Drittseite darzustellen)

IFrame mit WebGIS Anwendung
---------------------------

Um eine WebGIS Anwendung auf der Drittseite einzubetten, ist ein entsprechendes ``iframe`` Element innerhalb
des ``body`` Elements zu definieren:

.. code-block:: html

    <iframe src="http://localhost/map0.htm"
			style="z-index:0;width:500px;height:500px">
    </iframe>

``src`` Verweist dabei auf die WebGIS Anwendung. Dies kann eine statische Seite, die die WebGIS API
einbindet, oder auch eine WebGIS Karte sein, die über ein WebGIS Portal bereitgestellt wird (siehe Beispiel unten) sein.

Callback Funktionen
-------------------

.. note::
   Voraussetzung, damit ein Callback funktioniert, ist, dass dies von der eingebetten Karte erlaubt wird. Dafür muss
   auf der eingebetten Karte folgender API Eintrag per javascript gesetzt werden (Falls es sich um eine Karte eines 
   WebGIS Portals handeln ist dieser Eintrag in der ``custom.js`` erfolgen):

   ``webgis.security.allowEmbeddingMessages = true;``

Über eine ``callback`` Funktion kann innerhalb der Drittseite auf Änderngen des Kartenausschnittes reagiert werden.
Dazu muss zuerst ein Script auf der Drittseite geladen werden, dass die Kommunikation mit dem IFrame ermöglicht:

.. code-block:: html

   <script src="https://api.webgiscloud.com/scripts/api/embedding/webgis-embedding.js"></script>

.. note::
   Das Script sollte idealerweise von der API Instanz geholt werden, die auch über das IFrame eingebunden wird.
   Hier im Beispiel ist das die API in der WebGIS Cloud. Diese kann grundsätzlich immer verwendet werden, allerdings
   kann es dabei zur eingebettet API zu Versionsunterschieden kommen.

Über das Script kommt ein Objekte ``webgis_embedding`` auf die Drittseite. Dieses kann für das IFrame instanziert werden:

.. code-block::

    var embedding = new webgis_embedding('webgis-frame', {
        // Options: Events	
        onChangeExtent: function(event) {},
        onReceiveCurrentMapImage: function(event) {}
    }); 

Dem Konstruktor muss die Id des IFrames und ein *Options* Objekt übergeben werden. Über die *Options* können die *EventHandler*
definiert werden, die aufgerufen werden, wenn sich in der eingebettete Karte beispielsweise der Kartenausschnitt ändert.

Folgende *EventHandler* sind möglich:

* ``onChangeExtent(event)``
  Wird aufgerufen, wenn sich der Kartenausschnitt ändert. Das Event liefert folgende Eigenschaften:

.. code-block:: javascript  

   {
        event: 'map-refresh',
        mapId: 'map',
        bounds: [10.283203125000423, 45.68315803253279, 15.776367187500407, 49.3895244515819],
        center: [13.029785156250398, 47.56911375866688],
        scale: 4622334
   }

Jedes *Event* hat die Eigenschaften ``event`` (beschreibt die Art des Events) und ``mapId``. Über *mapId* kann eine Karte
auf der eingebetteten Seite identifiziert werden. Für einige Methoden ist die *mapId* notwendig (z.B. um das aktuelle Kartendarstellung
als Bild abzuholen, siehe unten). 

* ``onReceiveCurrentMapImage(event)``
  Wird aufgerufen, wenn ein Bild der aktuellen Kartendarstellung geliefert wird. Dieses Event wird erst nach einem Aufruf 
  der ``requestCurrentMapImage()`` Funktion aufgerufen. Das ``event`` Objekt hat folgendes aussehen:

.. code-block:: javascript

   {
        event: 'current-map-image',
        mapId: 'map',
        href: 'https://......',   // Url zum Kartenbild (nur wenn result_format nicht extra angeführt wird). Ein Kartenbild kann in er Regel nur einmal abgeholt werden und wird danach automatisch am Server gelöscht!
        base64: '...........'     // Base64 String des Kartenbildes (nur wenn result_format = 'base64')
   }

Folgendes Beispiel zeit eine mögliche Implementierung dieser beiden Events:

.. code-block:: javascript

    var mapId;
	var embedding = new webgis_embedding('webgis-frame', {
		onChangeExtent: function(event) {
			console.log('onChangeExtent', event);
			
			mapId = event.mapId;
		},
		onReceiveCurrentMapImage: function(event) {
			console.log('onReceiveCurrentMapImage', event);
			
			if(event.href) {
			    document.getElementById('webgis-map-image').src = event.href;
			} else if(event.base64) {
				document.getElementById('webgis-map-image').src = 'data:image/png;base64, ' + event.base64;
			}
		}
	}); 

Da die *mapId* später für das Abholen des aktuellen Kartenbildes benötigt wird, wird sie in einer globalen Variable gespeichert.
Ansonsten wird im Beispiel nur das aktuelle ``event`` in der *Console* ausgegeben. Wird ein Kartenbild geliefert wird es im Beispiel 
als Quelle für einen ``img`` Tag gesetzt.

Das ``webgis_embedding`` Objekte exportiert folgende Methoden:

``requestCurrentMapImage(mapId, [format: "png"/"jpg"], [result_format: "href","base64"])``

Die Funktion fordert die aktuelle Kartendarstellung als Bild an. Dazu muss die Id der Karte angeführt werden. 
Optional kann ein Bildformat ("png" = default, "jpg") und ein Format für das Ergebnis ("href" = default, entspricht Link,
"base64", Bild wird Base64 kodiert zurück gegeben)

In der Folge ein komplettes Beispiel einer Drittseite, die eine Karte als IFrame einbindet und Buttons zum Abholen der 
aktuellen Karte in unterschiedlichen Formaten anbietet:

.. code-block:: html

   <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no" />
        <meta name="apple-mobile-web-app-capable" content="yes" />

        <title></title>
        
        <script src="https://api.webgiscloud.com/scripts/api/embedding/webgis-embedding.js"></script>
        
    </head>
    <body>
        <h1>WebGIS IFrame</h1>
        
        <iframe id="webgis-frame"
                src="https://maps.webgiscloud.com/examples/map/Basemaps/Geoland%20Basemap.at"
                style="z-index:0;width:500px;height:500px">
            
        </iframe>
        
        <br/>
        <button onclick="download_map_image_href()">Download Map Image (href)</button>
        <button onclick="download_map_image_base64()">Download Map Image (Base64)</button>
        <br/>
        <img id="webgis-map-image" />
        
        <script type="text/javascript">
        
        var mapId;
        var embedding = new webgis_embedding('webgis-frame', {
            onChangeExtent: function(event) {
                console.log('onChangeExtent', event);
                
                mapId = event.mapId;
            },
            onReceiveCurrentMapImage: function(event) {
                console.log('onReceiveCurrentMapImage', event);
                
                if(event.href) {
                    document.getElementById('webgis-map-image').src = event.href;
                } else if(event.base64) {
                    document.getElementById('webgis-map-image').src = 'data:image/png;base64, ' + event.base64;
                }
            }
        }); 
        
        download_map_image_href = function(){
            embedding.requestCurrentMapImage(mapId);
        }
        
        download_map_image_base64 = function(){
            embedding.requestCurrentMapImage(mapId,'jpg','base64');
        }
        
        </script>
    </body>
    </html>


