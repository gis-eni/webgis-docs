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

Inhaltsverzeichnis
==================

Um das Verhalten des Inhaltsverzeichnis anzupassen gibt es folgende Settings:

* ``makePresentationTocGroupCheckboxes`` (**``true``** / ``false``)): 
  ist diese Option auf ``true`` gesetzt, werden bei aufklappbaren Gruppen-Layern im
  Inhaltsverzeichnis automatisch Checkboxes angeboten, wenn alle darunter liegenden 
  Layer/Darstellungsvarianten ebenfalls eine Checkbox aufweisen.
  Mit dieser Checkbox können dann alle darunter liegenden Layer mit einem Klick sichtbar
  oder unsichtbar geschalten werden.

* ``orderPresentationTocContainsByServiceOrder`` (``true``/ **``false``**):
  Damit wird festgelegt, das im Inhaltsverzeichnis die Container nach der Zeichenreihenfolge
  der Dienste sortiert werden. Ansonsten gilt die Sortierung aus dem CMS, wie sie 
  unter ``Viewer/Darstellungsvarianten`` definiert ist.
  Verwendet man keine Darstellungsvarianten sondern dynamische Inhaltsverzeichnisse,
  würde die Container ohne diese Option alphabetisch sortiert.

.. code:: javascript

   webgis.usability.makePresentationTocGroupCheckboxes = true;

   webgis.usability.orderPresentationTocContainsByServiceOrder = true;  // default: false

Toolbox
=======

Mit diesen Einstellungen können die Werkzeuge in der *Toolbox* konfiguriert werden.
Die Einstellungen erfolgen pro Werkzeug, die Syntax ist wie folgt:

.. code:: javascript

   webgis.usability.toolProperties['{tool-id}'] = { 
        container: 'a custom container for this tool', // optional
        name: 'a custom name for this tool', // optional
        tooltip: 'a custom tooltip for this tool', // optional
        priority: 100 // optional, default: 0
   };

Die ``{tool-id}`` ist die ID des Werkzeugs. Man bekommt die **Ids** der einzelnen Werkzeuge
über die WebGIS API ``/rest/tools``

Ein Anwendungsbeispiel ist beispielsweise, wenn Werkzeuge in einem anderen Container (Reiter),
verschoben werden sollten, zB:

.. code:: javascript

  webgis.usability.toolProperties['webgis.tools.fullextent'] =  { 
        container: 'Start' 
  };
  webgis.usability.toolProperties['webgis.tools.identify'] = { 
    container: ['Start','Abfragen'], priority: 10
  };
  webgis.usability.toolProperties['webgis.tools.boxzoomin'] = { priority: 12 };

Hier wird das Werkzeug *Vollausdehnung* in den Reiter *Start* verschoben und das Werkzeug
*Abfragen* in den Reiter *Start* und *Abfragen*. Sollte ein Werkzeug also in mehreren Reitern
sichtbar sein, muss der Container als Array angegeben werden.
Das Werkzeug *Box-Zoom* erhält eine höhere Priorität und landet damit im Reiter (Container) 
weiter vorne (Mit ``priority`` kann die Reihenfolge der Werkzeuge innerhalb eines Containers beeinflusst werden).   

Des weiteren kann die Reihenfolger der Container bestimmt werden:

.. code:: javascript

    webgis.usability.toolContainerOrder = [
        'Start',
        'Abfragen',
        'Messwerkzeuge',
        'Zeichnen',
        'Navigation'
    ];

Wird hier nichts angegeben, entspricht die Reihenfolge der Container jener Reihenfolge, mit der die 
Werkzeuge in die Karte eingefügt wurden. 

.. note::

    Ändert man die ``toolProperties`` der Werkzeuge, sollte immer auch die Container Reihenfolge
    definiert werden, da sonst die Reihenfolge der Container eher zufällig vergeben wird.

.. note::

    Es müssen bei der Reihenfolge nicht alle Container angegeben werden. Gibt es einen Container,
    der nicht in der Liste ist, wird dieser immer am Ende angezeigt.

Tastatur-Shortcuts
==================

Die WebGIS API bietet die Möglichkeit, Tastatur-Shortcuts für verschiedene Aktionen zu verwenden. 
Diese Shortcuts können in der ``custom.js`` aktiviert werden, um die Benutzerfreundlichkeit 
zu verbessern.

.. code:: javascript

   webgis.usability.useAdvancedKeyShortcutHandling = true;

Der Standardwert ist ``false``, was bedeutet, dass die erweiterten Tastatur-Shortcuts für WebGIS API Anwendungen
nicht aktiviert sind. Verwendet man den WebGIS Viewer, wird standardmäßig auch die ``custom-recommendations.js`` geladen,
die diesen Wert auf ``true`` setzt. Im Viewer sind die Shortcuts also standardmäßig aktiviert.

Sind die erweiterten Tastatur-Shortcuts aktiviert, können folgende Aktionen durchgeführt werden:

**Bearbeiten-Selektionswerkzeug**

- **Leertaste**: Nur ein Objekt selektieren. Es wird das Objekt ausgewählt, dass dem geklickten Punkt am nächsten ist.
- **E**: Wie oben, nur dass sofort die Bearbeiten Maske geöffnet wird. 
- **D**: Wie oben, nur dass sofort die Löschen Maske geöffnet wird.

.. note::

   **Voraussetzung**: das Selektionswerkzeug muss aktiv sein (Punkt Selektion) und ein Thema aus der Liste muss ausgewählt sein.

.. _customjs-domain-pro-behaviour:

Auswahllisten Pro Verhalten
===========================

Parametriert man im CMS Editmasken Felder als Auswahlliste (Typ ``Domain``), kann in der 
CMS Dialog unter ``optional: Domain Behaviour (experimental)`` das Verhalten der Auswahlliste 
auf ``Pro`` gesetzt werden. Damit wird die Auswahlliste als *select2* dargestellt, 
was eine bessere Benutzererfahrung bietet.

Voraussetzung ist, dass die *select2* Bibliothek für diesen Zweck verwendet soll.
Standardmäßig, ändert sich das ``Pro`` Verhalten der Auswahllisten erst dann, wenn die 
``webgis.usability.select_pro_behaviour`` Konstante in der ``custom.js`` gesetzt wird.

.. code:: javascript

   webgis.usability.select_pro_behaviour = "select2";

.. note::

    Derzeit ist der einzig mögliche Werte für diese Konstante ``select2``.
    Alle anderen Werte werden ignoriert und das Verhalten der Auswahllisten bleibt unverändert.

.. note::

    Ein Beschreibung des ``Pro`` Verhaltens der Auswahllisten findet sich in der
    :ref:`CMS Domain Verhalten ändern <cms-fields-domain-behaviour>`.