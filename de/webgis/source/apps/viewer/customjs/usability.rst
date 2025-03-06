=========
Usability
=========

Einige Funktionen der API lassen sich über sogenannte *Usability-Konstanten* steuern. Diese können in der ``custom.js`` für einzelne Karten oder gesamte Portalseiten gesetzt werden.

ClickBubble
===========

Die *ClickBubble* verbessert die Bedienbarkeit des Viewers auf Touch-Geräten. Werkzeuge, die einen Klick in die Karte voraussetzen (z. B. *Identify*), sind auf Touchscreens oft schwer zu bedienen, da ein Fingerklick ungenau sein kann.  
Wird die *ClickBubble* aktiviert, erscheint sie bei allen Werkzeugen, die eine Klick-Interaktion erfordern:

.. image:: img/image4.png

Anstatt direkt in die Karte zu klicken, zieht der Anwender die Bubble an die gewünschte Stelle. Die Spitze der Bubble markiert den genauen Punkt für die Aktion. Lässt man die Bubble los, kehrt sie automatisch in die obere rechte Ecke zurück und führt die gewünschte Aktion aus (z. B. *Identify*).

Klickt der Anwender auf die Bubble (ohne sie zu ziehen), öffnet sich eine Beschreibung zur Bedienung.

Kontextmenü-Bubble
==================

Einige Werkzeuge erfordern eine rechte Maustaste (z. B. das Kontextmenü für das Messen oder Editieren eines Sketches). Dafür kann eine zusätzliche *ContextMenu Bubble* aktiviert werden.  
Der Anwender kann diese anklicken, um das Kontextmenü zu öffnen, oder an eine bestimmte Position ziehen, um genau dort eine Aktion auszuführen (z. B. einen bestimmten *Vertex* verschieben oder löschen, rechtwinklig zur Kante konstruieren etc.).

.. image:: img/image5.png

Diese Funktion ermöglicht auch auf mobilen Geräten eine präzise Steuerung von Konstruktionen mit *Snapping*.

Aktivierung in ``custom.js``
============================

Diese Funktionen sind standardmäßig deaktiviert und müssen explizit in der ``custom.js`` aktiviert werden:

.. code-block:: javascript

    // ClickBubble aktivieren
    webgis.usability.clickBubble = true;
    // ContextMenu Bubble aktivieren
    webgis.usability.contextMenuBubble = true;

Da diese Funktionen nur auf Touch-Geräten sinnvoll sind, kann die Methode ``isTouchDevice()`` genutzt werden:

.. code-block:: javascript

    webgis.usability.clickBubble =
    webgis.usability.contextMenuBubble = webgis.isTouchDevice();

Sketch-Optimierungen
====================

Standardmäßig kann der Anwender bei einem *Sketch* auf einen *Vertex* klicken, um ein Popup-Menü zu öffnen:

.. image:: img/image6.png

Falls die rechte Maustaste oder die *ContextMenu Bubble* verfügbar ist, wird dieses Menü nicht mehr benötigt. Es kann jedoch weiterhin explizit aktiviert werden:

.. code-block:: javascript

    webgis.usability.sketchMarkerPopup = true;  // Empfehlung: false!!

Konstruktionswerkzeuge einschränken
===================================

In manchen Anwendungen sind nicht alle Konstruktionswerkzeuge erforderlich. Insbesondere die erweiterten Konstruktionsoptionen richten sich an versierte Anwender und können in bestimmten Karten deaktiviert werden:

.. code-block:: javascript

    webgis.usability.constructionTools = false;

Komplettes Kontextmenü deaktivieren
===================================

Falls das Kontextmenü beim Zeichnen nicht benötigt wird, kann es mit folgendem Code deaktiviert werden:

.. code-block:: javascript

    webgis.usability.sketchContextMenu = false;

Tastatur-Shortcuts für Sketch
=============================

Beim Konstruieren eines *Sketches* können verschiedene **Tastatur-Shortcuts** genutzt werden:

- **A**: Fügt einen *Vertex* auf einer Kante hinzu.
- **D**: Löscht einen *Vertex*.
- **Strg**: Ermöglicht das Aufziehen eines Fensters zur Mehrfachselektion von *Vertices*, die dann gemeinsam verschoben oder gelöscht werden können.

Diese Funktionalität kann über folgende Schalter gesteuert werden:

.. code-block:: javascript

   webgis.usability.allowSketchShortcuts = true;
   webgis.usability.allowSelectSketchVertices = true;
