.. webgis documentation master file, created by
   sphinx-quickstart on Tue Oct  1 12:52:32 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

WebGIS 5.0 API JavaScript
=========================

In dieser Dokumentation werden die grundlegenden Objekte beschrieben, die für das Erzeugen von Kartenanwendungen mit der WebGIS-API notwendig sind. Um die API nutzen können sind folgende Einträge in der entsprechenden HTML notwendig:

.. code-block:: html

    <link href="https://api.webgiscloud.com/content/styles/default.css" rel="stylesheet" />
    <script src="https://api.webgiscloud.com/scripts/api/api.min.js" id="webgis-api-script"></script>

Wichtig ist hier, dass der ``<script>`` Tag die ``id="webgis-api-script"`` erhält!

Optional können UI Elemente (TOC, Werkzeuge, Suche) in der Karte verwendet werden, wenn zusätzlich folgende Inhalte einer Seite hinzugefügt werden.

.. code-block:: html

    <link href="http://api.webgiscloud.com/content/api/ui.css" rel="stylesheet" />
    <script src="http://api.webgiscloud.com/scripts/api/api-ui.min.js"></script>

Im Scripting Teil der Seite kann nun das webgis-Objekt initialisert und eine Karte erstellt werden.

.. code-block:: javascript

    webgis.init(function() {
        // ab hier können Karten erzeugt werden
        var map = webgis.createMap('map', {
            extent: 'web_mercator_at@webgiscloud',
            services: 'geoland_bm@webgiscloud,geoland_bm_of@webgiscloud,geoland_bm_ov@webgiscloud'
        });
    });

Die Kartenausdehung und die Dienste sind vom jeweiligen API Betreiber anhängig

Mit den hier angeführten Links wird immer auf die aktuelle Version der WebGIS API verwiesen. Um auf ein spezielle Version zuzugriefen sind folgende Aufrufe möglich:

.. code-block:: html

    <link href="https://api.webgiscloud.com/content/styles/v/3.0.0/default.css" rel="stylesheet" />
    <script src="https://api.webgiscloud.com/scripts/api/v/3.0.0/api.min.js" id="webgis-api-script"></script>

    <link href="http://api.webgiscloud.com/content/api/v/3.0.0/ui.css" rel="stylesheet" />
    <script src="http://api.webgiscloud.com/scripts/api/v/3.0.0/api-ui.min.js"></script>


Im der folgenden Auflistung sind die Elemente zur Erstellung von Kartenanwendugen beschrieben.


.. toctree::
   :maxdepth: 1

   graphics<graphics.rst>
   map<map.rst>
   service<service.rst>
   sketch<sketch.rst>
   ui<ui.rst>
   webgis<webgis.rst>


