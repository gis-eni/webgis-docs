Beispiele für *UI Master Vorlagen*
==================================

Das Erstellen von *UI Master Vorlagen* setzt rudimentäre Kenntnisse in JSON (*Javascript Object Notation*) voraus.
Die hier gezeigten Beispiele dienen vor allem dem Verständnis der Form und der Möglichkeiten von *UI Master Vorlagen*.
Weiter unter wird gezeigt, wie diese Vorlagen automatisiert über den MapBuilder erstellt werden können.

Folgendes Beispiel fügt jeder Karte ein allgemeines Schnellsuche-Thema hinzu:

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

Hier wird im *UI Element* ``topbar`` (in der Regel die Suche) der Schalter ``quick_search`` auf ``true`` gesetzt.
Damit wird in jeder Karte die Schnellsuche angezeigt. Unter ``quick_search_service`` werden die Suchdienste 
aufgelistet (mit Beistrich getrennt), die in allen Diensten vorkommen sollen.

Der Vollständigkeit halber werden hier auch noch die Schalter ``detail_search`` (Detailsuche) und ``app_menu`` aufgeführt.
Da diese allerdings auf ``false`` gesetzt sind, haben sie für Karten keine Auswirkung.

Möchte man, dass in jeder Karte auch das App-Menü angezeigt wird, kann der entsprechende Schalter auf ``true`` gesetzt werden.

Das folgende Beispiel zeigt ein JSON für das *UI Element* ``Tabs``. Hier werden jeder Karte die Werkzeuge,
*Karte teilen*, *Drucken* und *Kartenbild herunterladen* hinzugefügt. Außerdem wird ein allgemeines Drucklayout in allen 
Karten bereitgestellt:

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