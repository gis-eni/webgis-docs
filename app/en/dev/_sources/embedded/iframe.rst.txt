Embedding Maps via iFrame
=============================

This section presents an application in which an existing WebGIS map is embedded on a
third-party page via an ``iframe``. In addition, a ``callback`` function is used to try to react on the
third-party page to changes in the map view. It is also possible to fetch an image of the current map content from the *parent*
page, in order to download the current map image (or display it in an ``img`` element on the third-party page)

IFrame with WebGIS Application
------------------------------

To embed a WebGIS application on the third-party page, a corresponding ``iframe`` element must be defined within
the ``body`` element:

.. code-block:: html

    <iframe src="http://localhost/map0.htm"
			style="z-index:0;width:500px;height:500px">
    </iframe>

``src`` here points to the WebGIS application. This can be a static page that includes the WebGIS API,
or a WebGIS map made available via a WebGIS portal (see example below).

Callback Functions
-------------------

.. note::
   A prerequisite for a callback to work is that this is allowed by the embedded map. For this,
   the following API entry must be set via JavaScript on the embedded map (if it is a map of a
   WebGIS portal, this entry should be made in ``custom.js``):

   ``webgis.security.allowEmbeddingMessages = true;``

A ``callback`` function can be used within the third-party page to react to changes in the map view.
For this, a script must first be loaded on the third-party page, which enables communication with the IFrame:

.. code-block:: html

   <script src="https://api.webgiscloud.com/scripts/api/embedding/webgis-embedding.js"></script>

.. note::
   Ideally, the script should be fetched from the same API instance that is also embedded via the IFrame.
   In this example, that is the API in the WebGIS Cloud. This can generally always be used, however
   version differences with the embedded API can occur.

The script makes a ``webgis_embedding`` object available on the third-party page. This can be instantiated for the IFrame:

.. code-block::

    var embedding = new webgis_embedding('webgis-frame', {
        // Options: Events
        onChangeExtent: function(event) {},
        onReceiveCurrentMapImage: function(event) {}
    });

The constructor must be passed the id of the IFrame and an *options* object. The *options* can be used to define the *event handlers*
that are called when, for example, the map view changes in the embedded map.

The following *event handlers* are possible:

* ``onChangeExtent(event)``
  Called when the map view changes. The event provides the following properties:

.. code-block:: javascript

   {
        event: 'map-refresh',
        mapId: 'map',
        bounds: [10.283203125000423, 45.68315803253279, 15.776367187500407, 49.3895244515819],
        center: [13.029785156250398, 47.56911375866688],
        scale: 4622334
   }

Every *event* has the properties ``event`` (describes the type of event) and ``mapId``. The *mapId* can be used to identify
a map on the embedded page. The *mapId* is required for some methods (e.g. to fetch the current map presentation
as an image, see below).

* ``onReceiveCurrentMapImage(event)``
  Called when an image of the current map presentation is delivered. This event is only called after a call to
  the ``requestCurrentMapImage()`` function. The ``event`` object looks like this:

.. code-block:: javascript

   {
        event: 'current-map-image',
        mapId: 'map',
        href: 'https://......',   // Url to the map image (only if result_format is not additionally specified). A map image can generally only be fetched once and is then automatically deleted from the server!
        base64: '...........'     // Base64 string of the map image (only if result_format = 'base64')
   }

The following example shows a possible implementation of these two events:

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

Since the *mapId* is needed later to fetch the current map image, it is saved in a global variable.
Otherwise, in the example only the current ``event`` is output to the *console*. If a map image is delivered, in the example it
is set as the source for an ``img`` tag.

The ``webgis_embedding`` object exports the following methods:

``requestCurrentMapImage(mapId, [format: "png"/"jpg"], [result_format: "href","base64"])``

The function requests the current map presentation as an image. For this, the id of the map must be specified.
Optionally, an image format ("png" = default, "jpg") and a format for the result ("href" = default, corresponds to a link,
"base64", image is returned base64 encoded) can be specified

The following is a complete example of a third-party page that embeds a map as an IFrame and offers buttons for fetching the
current map in different formats:

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
