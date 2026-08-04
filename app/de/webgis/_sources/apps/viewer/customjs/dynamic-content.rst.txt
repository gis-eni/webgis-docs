==================
Dynamische Inhalte
==================

Wurden in eine Karte *dynamische Inhalte* eingefügt (siehe Abschnitt ``MapBuilder``), können die Marker und Ergebnisse ebenfalls über die ``custom.js`` angepasst werden.

Marker
======

Das Anpassen der Marker für *dynamische Inhalte* funktioniert analog zu Abfragemarkern über die Auflistung ``webgis.markerIcons[]``. Allerdings lauten die Listenwerte hier ``dynamic_content`` und ``dynamic_content_extenddependent``:

* ``webgis.markerIcons["dynamic_content"]["default"]``: Definition von *Marker-Icons* für allgemeine *dynamische Inhalte*. Standardmäßig werden hier Marker mit Nummern angezeigt.
* ``webgis.markerIcons["dynamic_content_extenddependent"]["default"]``: Für *dynamische Inhalte*, die bei jeder Änderung des Kartenausschnitts neu geladen werden. Dazu muss beim Erstellen des Inhalts ``Ausschnittsabhängig`` angegeben werden (siehe ``MapBuilder``). Standardmäßig werden hier Marker ohne fortlaufende Nummern angezeigt. Fortlaufende Nummern wie bei *statischen dynamischen Inhalten* würden den Anwender hier verwirren, da sich die Nummern bei jeder Verschiebung der Karte ändern könnten.

Schränkt man die ``webgis.markerIcons["dynamic_content"]`` bzw. ``webgis.markerIcons["dynamic_content_extenddependent"]`` mit ``["default"]`` ein, gilt die Definition für alle *dynamischen Inhalte*. Anstelle von ``["default"]`` kann auch der Anzeigename des *dynamischen Inhalts* angegeben werden, z. B. ``webgis.markerIcons["dynamic_content_extenddependent"]["Aktuelle Baustellen"]``.

.. note:: Da eine grundlegende Beschreibung für Marker bereits im vorherigen Kapitel für Abfrageergebnisse erläutert wurde und die Vorgehensweise analog ist, werden hier nur praxisnahe Beispiele aufgeführt.

**Beispiel:**  
Ein *dynamischer Inhalt* stellt Kunden als Punkt auf der jeweiligen Adresse dar. Die Grundlage ist eine ``API-Abfrage``. Da auf einer Adresse mehrere Kunden wohnen können (z. B. Mehrfamilienhaus), wurde bei der Abfrage ``Union`` eingestellt (siehe Tutorial CMS - Abfragen). Dadurch werden Kunden, die sich am selben Adresspunkt befinden, zu einem *Objekt/Marker* zusammengefasst. Die ``Properties`` des Features entsprechen dadurch einem Array (statt einem allgemeinen Objekt oder ``Record``). Jeder Eintrag in diesem Objekt entspricht einem ``Record`` für einen Kunden.

In der Karte sollen Marker in unterschiedlichen Farben dargestellt werden, wenn sich unter einer Adresse mehrere Kunden befinden. Dazu wird geprüft, ob ``properties`` ein Array ist. Außerdem soll die Anzahl der Kunden im Marker als Zahl angezeigt werden.

.. code-block:: javascript

   webgis.markerIcons["dynamic_content_extenddependent"]["Kunden"] = {
        url: function (i, f) {
            if (Array.isArray(f.properties) && f.properties.length > 1) {  // Wenn Array mit mehreren Einträgen => roter Marker 
                return webgis.baseUrl + '/rest/numbermarker/' + f.properties.length + '?c=f00';
            }
            return webgis.baseUrl + '/rest/numbermarker/1?c=00f';  // Sonst blauer Marker
        },
        size: function (i, f) { return [33, 41]; },
        anchor: function (i, f) { return [16, 42]; },
        popupAnchor: function (i, f) { return [0, -42]; }
    };

Ergebnis:

.. image:: img/dynamic-content1.png

Hooks
=====

Über ``hooks`` kann nach dem Laden eines *dynamischen Inhalts* auf die Features zugegriffen werden. Dabei können die Features auch geändert werden. Ein Anwendungsbeispiel für ``hooks`` ist das Umbenennen oder Einschränken der Attribute, die für den *dynamischen Inhalt* angezeigt werden sollen.

Folgende Auflistungen stehen zur Verfügung:

* ``webgis.hooks["dynamic_content_loaded"]["default"]``: Hier kann eine Funktion angegeben werden, die das Ergebnis eines dynamischen Inhalts (GeoJSON) bearbeitet.
* ``webgis.hooks["dynamic_content_feature_loaded"]["default"]``: Hier kann eine Funktion definiert werden, die einzelne Features eines dynamischen Inhalts nach dem Laden bearbeitet.

**Beispiel:**  
In der Karte sollen maximal 100 Ergebnisse angezeigt werden, auch wenn der *dynamische Dienst* mehr liefert. Die Regel soll nur für den *dynamischen Inhalt* mit dem Namen ``Solr`` angewendet werden:

.. code-block:: javascript

    webgis.hooks["dynamic_content_loaded"]["Solr"] = function (response) {
        response.features = response.features.slice(0,100);
    };

Der gleiche Inhalt liefert sehr viele Attribute mit nicht anwenderfreundlichen Namen zurück. Daher sollen im nächsten Schritt nur wenige Attribute übernommen und sinnvoll benannt werden. Dies erfolgt für jedes *Feature* einzeln:

.. code-block:: javascript
    
    webgis.hooks["dynamic_content_feature_loaded"]["Solr"] = function (feature) {
        if (feature.properties) {
            var properties = feature.properties;

            feature.properties = {
                Kategorie: properties.map_category || '',
                "Objekt Art": properties.subtext || '',
                Text: properties.textexact || '',
            };
        }
    };

Ergebnis:

.. image:: img/dynamic-content2.png

Im letzten Schritt sollen für diesen Dienst auch noch die Marker angepasst werden. Die Einfärbung erfolgt je nach ``Kategorie``. Außerdem soll im Marker die ``Objekt Art`` als Text angezeigt werden. Falls es sich um die Kategorie ``Haltestelle`` handelt, wird das zweite Wort von ``Text`` als Label genutzt, da dies in diesem Beispiel immer dem Namen der Haltestelle entspricht (das erste Wort wäre Ort/Gemeinde):

.. code-block:: javascript

    webgis.markerIcons["dynamic_content_extenddependent"]["Kagis Solr"] = {
        url: function (i, f) {
            var label = f.properties["Objekt Art"].substr(0, 2);
            switch (f.properties.Kategorie) {
                case 'Öffentliche Ordnung und Sicherheit':
                    return webgis.baseUrl + '/rest/textmarker/' + label + '?c=f00';
                case 'Gesundheit':
                    return webgis.baseUrl + '/rest/textmarker/' + label + '?c=0f0';
                case 'Soziale Einrichtung':
                    return webgis.baseUrl + '/rest/textmarker/' + label + '?c=00f';
                case 'Haltestelle':
                    var words = f.properties.Text.split(' ');
                    return webgis.baseUrl + '/rest/textmarker/' + words[Math.min(words.length, 1)].substr(0, 3) + '?c=0a0,0a0';
            }
            return webgis.baseUrl + '/rest/textmarker/' + label + '?c=f0f';
        },
        size: function (i, f) { return [33, 41]; },
        anchor: function (i, f) { return [16, 42]; },
        popupAnchor: function (i, f) { return [0, -42]; }
    };

Ergebnis:

.. image:: img/dynamic-content3.png
