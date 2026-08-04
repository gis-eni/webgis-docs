=========================
Benutzerdefinierte Marker
=========================

Im WebGIS Viewer werden Ergebnisse standardmäßig mit einem **blauen Marker** markiert. In manchen Fällen soll jedoch ein anderes Symbol verwendet werden.

Allgemeine Vorgehensweise
=========================

Die Darstellung von **Markern** wird über das Objekt ``webgis.markerIcons`` in der **WebGIS API** gesteuert. Dieses Array enthält vordefinierte Marker, die über **Schlüssel** (Keys) angesprochen werden.

**Beispiel:** 

Ein vordefinierter Marker für die aktuelle Position:

.. code-block:: JavaScript

    this.markerIcons["currentpos_red"] = {
        url: function () { 
            return webgis.css.imgResource('position_red.png', 'markers') 
        },
        size: [38, 38], 
        anchor: [19, 19], 
        popupAnchor: [0, -20]
    }; 

Eigenschaften eines Marker-Objekts
----------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Eigenschaft**
     - **Beschreibung**
   * - ``url``
     - Eine **Funktion**, die die **URL des Marker-Bildes** zurückgibt. Wird ``webgis.css.imgResource()`` verwendet, muss das Bild im **api5/content/api/img**-Verzeichnis liegen. Der erste Parameter ist der **Dateiname**, der zweite der **Unterordner**. Falls das Marker-Bild nicht in diesem Verzeichnis liegt, kann eine **absolute URL** angegeben werden:  

       .. code-block::

          "http://myserver.com/markers/mein_marker.png"

   * - ``size``
     - Die **Größe des Markers** in **Pixel**.
   * - ``anchor``
     - Die **Koordinaten des Einfügepunkts** im Bild (**von links, oben**) in **Pixel**.
   * - ``popupAnchor``
     - Die **Koordinaten der Infoblase** relativ zum **Einfügepunkt des Markers** in **Pixel**.

.. note::

   **Marker-Attribute** wie **Größe** oder **Einfügepunkt** können auch als **Funktionen** definiert werden, wenn dynamische Anpassungen erforderlich sind.

Marker für Abfrageergebnisse
============================

Die Marker für **Abfrageergebnisse** werden folgendermaßen definiert:

.. code-block:: Javascript

    this.markerIcons["query_result"]["default"] = {
        url: function (index, feature) { 
            return webgis.css.imgResource('marker_blue.png', 'markers'); 
        },
        size: function (index, feature) { return [25, 41]; },
        anchor: function (index, feature) { return [12, 42]; },
        popupAnchor: function (index, feature) { return [0, -42]; }
    };

Hierbei gilt:

- ``query_result``: Definiert Marker für Abfrageergebnisse.
- ``default``: Wird verwendet, wenn keine spezielle Definition für eine bestimmte Abfrage vorliegt.
- Größe und Einfügepunkt als Funktionen: Im Gegensatz zu statischen Werten werden diese **dynamisch berechnet**.

**Funktionsparameter:**  

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Parameter**
     - **Beschreibung**
   * - ``index``
     - Fortlaufende **Nummer des Suchergebnisses**, für das der Marker geladen wird.
   * - ``feature``
     - Das **Feature-Objekt** im **GeoJSON-Format**, für das der Marker angezeigt wird.

Diese Parameter werden im Beispiel zwar übergeben, aber nicht genutzt.  
Standardmäßig wird immer **derselbe Marker** für alle Ergebnisse gesetzt.

Überschreiben von Markern
=========================

Falls eine Seite auf die WebGIS API zugreift, können **Marker-Eigenschaften** nach dem Laden der Datei **api.min.js** überschrieben werden. Die Syntax entspricht der Standarddefinition, jedoch kann ``this`` nicht verwendet werden. Stattdessen erfolgt der Zugriff direkt über ``webgis``.

**Beispiel:** Ein benutzerdefinierter Marker mit eigenem Symbol:

.. code-block:: Javascript

    webgis.markerIcons["currentpos_red"] = {
        url: function () { 
            return "http://myserver.com/markers/mein_super_marker_symbol.png" 
        },
        size: [20, 20], 
        anchor: [9, 9], 
        popupAnchor: [0, -10]
    };

.. warning::  

   Das ``markerIcons``-Array kann nicht mit ``this`` angesprochen werden und der Zugriff muss direkt über ``webgis.markerIcons`` erfolgen.


Marker in der custom.js
-----------------------

Der erste Wert, der in der ``custom.js``-Datei überschrieben wird, ist der **Standard-Marker für Abfrageergebnisse**.  

**Beispiel:** Hier wird für jedes Abfrageergebnis anstelle des einfachen blauen Markers ein **blauer Marker mit einer Zahl** angezeigt.

.. code-block:: Javascript

    webgis.markerIcons["query_result"]["default"] = {
        url: function (i, f) {
            return webgis.css.imgResource('marker_blue_' + (i + 1) + '.png', 'markers'); 
        },
        size: function (i, f) { return [25, 41]; },
        anchor: function (i, f) { return [12, 42]; },
        popupAnchor: function (i, f) { return [0, -42]; }
    };

.  
Die Zahl entspricht dem **Index des Suchergebnisses**.

**Funktionsweise:**

- Der Marker wird aus der Datei ``marker_blue_i.png`` im Ordner **markers** geladen wobei ``i``  steht für den Index des Abfrageergebnisses (beginnend bei 0).
- Damit die Nummerierung bei ``1`` startet, wird ``(i + 1)`` verwendet:
- Die verfügbaren Marker-Dateien befinden sich im Verzeichnis: ``portal5/content/api/img/markers``.
- Dort existieren Dateien mit den Namen **marker_blue_1.png, marker_blue_2.png, …, marker_blue_1000.png**.

.. code-block:: Javascript

    'marker_blue_' + (i + 1) + '.png', 'markers'

Das Ergebnis dieser Änderung sieht wie folgt aus:

.. image:: img/image1.png

Die Marker erhalten eine fortlaufende Nummer, was für den Anwender sehr praktisch ist, da so eine optische Zuordnung zwischen Liste und Karte möglich ist. Das nächste Beispiel bezieht sich ausschließlich auf die Abfrage ``gemeinden``:

.. code-block:: javascript

    webgis.markerIcons["query_result"]["gemeinden"] = {
        url: function (i, f) {
            if (f.properties.Gemeinde == "Graz")
                return webgis.css.imgResource('marker_circle_sketch_vertex_99.png', 'markers');
            return webgis.css.imgResource('marker_circle_sketch_vertex_' + (i + 1) + '.png', 'markers');
        },
        size: function (i, f) { return [21, 21]; },
        anchor: function (i, f) { return [11, 11]; },
        popupAnchor: function (i, f) { return [0, -11]; }
    };

Hier wird ebenfalls ein runder Marker mit fortlaufender Nummer verwendet. Allerdings wird hier direkt auf die Attribute des abgefragten Features zugegriffen. Im Beispiel wird einem Feature, bei dem das Attribut ``Gemeinde`` gleich ``Graz`` ist, ein fixer Marker mit der Nummer 99 zugewiesen.

.. tip:: Eishockey-Fans wissen, warum die Nummer 99 gewählt wurde.

Alle anderen Funktionen sind nicht vom Index oder vom Feature abhängig, da alle Marker gleich groß sind und den gleichen Einfügepunkt haben. Falls dies nicht der Fall ist, könnte man auch in diesen Funktionen das Feature abfragen und gegebenenfalls unterschiedliche Werte zurückgeben. Ein Beispiel für eine Zuordnung aufgrund von Feature-Eigenschaften könnte beispielsweise ein Thema ``medizinische Einrichtungen`` sein. So könnten unterschiedliche Marker für Ärzte, Krankenhäuser, Apotheken usw. verwendet werden.

Das Ergebnis aus diesem Beispiel würde etwa so aussehen:

.. image:: img/image2.png

Die folgenden Beispiele betreffen nicht mehr die Marker selbst, sondern die Darstellung der Ergebnisliste. In dieser Liste wird immer nur eine Vorschau mit wenigen Attributen angezeigt. Diese Attribute entsprechen den ersten drei Attributen, nach denen für dieses Thema gesucht werden kann. WebGIS nimmt an, dass diese Attribute aussagekräftig für eine Vorschau sind. Falls eine andere Darstellung gewünscht ist, kann dies mit den folgenden Beispielen umgesetzt werden:

.. code-block:: javascript

    webgis.hooks["query_result_feature"]["grundstuecke"] = function (map, $parent, feature, base) {
        base(map, $parent, feature);
        webgis.$("<a style='color:gray;font-size:.9em' href='http://bev.gv.at' target='_blank'>(c) 2017 BEV</a>").appendTo($parent);
    };

Der ``Hook`` wird aufgerufen, wenn ein Ergebnis für die Vorschau gerendert wird. Dabei werden die Karte, das Parent-HTML-Element, das Feature und die Ursprungs- bzw. Default-Funktion übergeben. Im Beispiel wird zunächst die Ursprungsfunktion aufgerufen, um das Rendering wie gewohnt auszuführen:

.. code-block:: javascript

    base(map, $parent, feature);

Dieser Funktion werden die gleichen Parameter übergeben - mit Ausnahme von ``base`` selbst. Anschließend wird einfach ein Link zum BEV mit einer Copyright-Meldung hinzugefügt. Das Ergebnis entspricht dem obigen Screenshot mit den blauen Markern. In der Liste ist hinter jedem Ergebnis der Link in grauer Farbe erkennbar. Natürlich könnte er auch in einer neuen Zeile platziert werden.

.. tip:: Diese Methode ist besonders nützlich, wenn für eine Abfrage keine aussagekräftigen Attribute für eine Vorschau existieren.

Ein Beispiel hierfür ist ein Thema mit Baustellenfotos, die mit der Identify-Funktion in der Karte abgefragt werden können. Ein Feld ``Vorschau`` wird im CMS mit einer ``Imageexpression`` auf das Bild gesetzt. Um dieses Bild in der Vorschau anzuzeigen, kann folgender Code verwendet werden:

.. code-block:: javascript

    webgis.hooks["query_result_feature"]["enetze_fotos"] = function (map, $parent, feature, base) {
        $(feature.properties.Vorschau).appendTo($parent);
    };

Hier wird die ``base``-Funktion nicht mehr aufgerufen, sondern das Bild direkt eingefügt. Das Ergebnis sieht folgendermaßen aus:

.. image:: img/image3.png

Die Bilder erscheinen direkt in der Vorschau der Suchergebnisse. Klickt man auf ein Foto, wird in der Karte das entsprechende Marker-Popup sichtbar.

Dynamische Marker
-----------------

Die oben gezeigten Beispiele verwenden statische Marker-Icons. Zusätzlich besteht die Möglichkeit, Marker dynamisch zu erzeugen. Dabei können die Größe und die Farben übergeben werden. Um für die Abfrageergebnisse dynamische Marker zu verwenden, würde der Eintrag in der ``custom.js`` folgendermaßen aussehen:

.. code-block:: javascript

   webgis.markerIcons["query_result"]["default"] = {
       url: function (i, f) {
           return webgis.baseUrl + '/rest/numbermarker/' + (i + 1);
       },
       size: function (i, f) { return [33, 41]; },
       anchor: function (i, f) { return [16, 42]; },
       popupAnchor: function (i, f) { return [0, -42]; }
    };

Die URL für dynamische Marker lautet ``{webgis-api-url}/rest/numbermarker`` oder ``{webgis-api-url}/rest/textmarker``, also beispielsweise: ``https://api.webgiscloud.com/rest/numbermarker``. Der Unterschied zwischen ``numbermarker`` und ``textmarker`` besteht darin, dass beim ``numbermarker`` nur Zahlen übergeben werden dürfen. Beim ``textmarker`` können hingegen auch Texte übergeben werden. Falls der Text zu lang ist, wird er abgeschnitten.

Hier einige Beispiele für den Aufruf mit verschiedenen Eigenschaften:

**Marker mit Nummer:**

.. code-block:: text

    https://api.webgiscloud.com/rest/numbermarker/42

**Marker mit bestimmter Größe (Standard: 33x41 px):**

.. code-block:: text

    https://api.webgiscloud.com/rest/numbermarker/42?w=100&h=120

.. warning:: Der Wert für die Höhe muss immer größer sein als die Breite!

**Marker mit benutzerdefinierten Farben** (Füllfarbe, Umrandungsfarbe, Textfarbe als RGB-Hex-Code, 3- oder 6-stellig):

.. code-block:: text

    https://api.webgiscloud.com/rest/numbermarker/42?w=100&h=120&c=fff,f88,fcc

**Beispiele für Textmarker:**

.. code-block:: text

    https://api.webgiscloud.com/rest/textmarker/LoremIpsum?w=100&h=120&c=fff,f88,fcc&fs=22

Hier wurde zusätzlich der Parameter ``fs`` (FontSize) übergeben, der die Textgröße in Pixel angibt.

.. note:: Marker können auch für *dynamische Inhalte* angepasst werden. Die Vorgehensweise ist nahezu identisch mit den oben gezeigten Beispielen und wird im nächsten Kapitel erläutert. Die dort beschriebenen Techniken lassen sich ebenfalls auf die Marker von Abfragen anwenden.
