.. webgis documentation master file, created by
   sphinx-quickstart on Tue Oct  1 12:52:32 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

WebGIS 5.0 API JavaScript
=========================

This documentation describes the basic objects needed to create map applications with the WebGIS API. To be able to use the API, the following entries are required in the corresponding HTML:

.. code-block:: html

    <link href="https://api.webgiscloud.com/content/styles/default.css" rel="stylesheet" />
    <script src="https://api.webgiscloud.com/scripts/api/api.min.js" id="webgis-api-script"></script>

It is important here that the ``<script>`` tag gets ``id="webgis-api-script"``!

Optionally, UI elements (TOC, tools, search) can be used in the map, if the following content is additionally added to a page.

.. code-block:: html

    <link href="http://api.webgiscloud.com/content/api/ui.css" rel="stylesheet" />
    <script src="http://api.webgiscloud.com/scripts/api/api-ui.min.js"></script>

In the scripting part of the page, the webgis object can now be initialized and a map created.

.. code-block:: javascript

    webgis.init(function() {
        // maps can be created from here on
        var map = webgis.createMap('map', {
            extent: 'web_mercator_at@webgiscloud',
            services: 'geoland_bm@webgiscloud,geoland_bm_of@webgiscloud,geoland_bm_ov@webgiscloud'
        });
    });

The map extent and the services depend on the respective API operator

The links given here always point to the current version of the WebGIS API. To access a specific version, the following calls are possible:

.. code-block:: html

    <link href="https://api.webgiscloud.com/content/styles/v/3.0.0/default.css" rel="stylesheet" />
    <script src="https://api.webgiscloud.com/scripts/api/v/3.0.0/api.min.js" id="webgis-api-script"></script>

    <link href="http://api.webgiscloud.com/content/api/v/3.0.0/ui.css" rel="stylesheet" />
    <script src="http://api.webgiscloud.com/scripts/api/v/3.0.0/api-ui.min.js"></script>


The following list describes the elements for creating map applications.


.. toctree::
   :maxdepth: 1

   graphics<graphics.rst>
   map<map.rst>
   service<service.rst>
   sketch<sketch.rst>
   ui<ui.rst>
   webgis<webgis.rst>
