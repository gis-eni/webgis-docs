Examples of *UI Master Templates*
==================================

Creating *UI master templates* requires basic knowledge of JSON (*JavaScript Object Notation*).
The examples shown here are mainly intended to help you understand the form and possibilities of *UI master templates*.
Further below, it is shown how these templates can be created in an automated way via the MapBuilder.

The following example adds a general quick-search topic to every map:

.. code::

   {
        "ui": {
            "options": [
                {
                    "element": "topbar",
                    "options": {
                        "quick_search_service": "elastic_allgemein@default",
                        "quick_search": true,
                        "detail_search": false,
                        "app_menu": false
                    }
                }
            ]
        }
    }

Here, in the *UI element* ``topbar`` (usually the search), the switch ``quick_search`` is set to ``true``.
This shows the quick search in every map. Under ``quick_search_service``, the search services
that should be included in all services are listed (separated by commas).

For completeness, the switches ``detail_search`` (detailed search) and ``app_menu`` are also listed here.
However, since these are set to ``false``, they have no effect on maps.

If you also want the app menu to be shown in every map, the corresponding switch can be set to ``true``.

The following example shows a JSON for the *UI element* ``Tabs``. Here, the tools
*Share Map*, *Print*, and *Download Map Image* are added to every map. In addition, a general print layout is made available in all
maps:

.. code::

    {
        "ui": {
            "options": [
                {
                    "element": "tabs",
                    "options": {
                    "add_presentations": false,
                    "add_settings": false,
                    "add_tools": true,
                    "add_queryResults": false,
                    "options_presentations": {
                        "gdi_button": false
                    },
                    "options_settings": {
                        "gdi_button": false,
                        "themes": true
                    },
                    "options_tools": {
                        "containers": [
                        {
                            "name": "Karte",
                            "tools": [
                                "webgis.tools.serialization.sharemap",
                                "webgis.tools.print",
                                "webgis.tools.downloadmapimage"
                            ]
                        },
                        {
                            "name": "webgis.tools.io.print",
                            "options": [
                                "l9ljwxcvu-e2dedi_cq2guq@ccgis_default"
                            ]
                        }]
                    }
                }
            }]
        }
    }
