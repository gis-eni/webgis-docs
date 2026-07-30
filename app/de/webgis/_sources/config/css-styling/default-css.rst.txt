.. _css-default:

``default.css`` – Farben und Größen
=====================================

Über die Datei ``default.css`` werden CSS-Variablen überschrieben, die das gesamte
Erscheinungsbild von *WebGIS Portal* und *WebGIS API* steuern – insbesondere Farben und Größen.

Ablageort
---------

Die Datei wird im ``content/styles/<company>``-Unterverzeichnis der jeweiligen Anwendung abgelegt.
Soll sich die Datei auf eine bestimmte Portal-Seite beziehen, wird sie im Unterverzeichnis ``content/portals/<portal-page-id>`` abgelegt
und heißt dort ``map-default.css``.

.. code-block:: none

    // Für die Company
    api/
    └── wwwroot/
        └── content/
            └── styles/
                └── <company>/
                    └── default.css

    // Für eine bestimmte Portal Seite
    portal/
    └── wwwroot/
        └── content/
            └── portals/
                └── <portal-page-id>/
                    └── map-default.css

``<company>`` entspricht dem Wert des ``company``-Schlüssels aus der ``portal.config``.
``<portal-page-id>`` entspricht dem Wert der ``id`` aus der jeweiligen Portal-Seite (Url-Name).

.. note::

    Das Verzeichnis ``/<company>/`` und ``/<portal-page-id>`` wird bei einem Update **nicht** überschrieben.
    Alle Anpassungen darin bleiben erhalten.

Ist in der ```portal.config`` folgender Key gesetzt, kann eine Karten Author den Inhalt der ``default.css``
auf dem Portal direkt eingeben, ohne dass die Datei physisch im Repository abgelegt werden muss:

.. code-block:: xml

     <add key="portal-custom-content-rootpath" value="..../webgis-repository/portal-page-content" />


Brand-Variablen (empfohlene Anpassung)
---------------------------------------

In der Regel genügt es, nur die **Brand-Variablen** anzupassen, um die Anwendung in den
eigenen Unternehmensfarben erscheinen zu lassen. Alle anderen Farben leiten sich davon ab.

.. code-block:: css

    .webgis-container, body {
        /* Primärfarbe – der wichtigste Anpassungswert */
        --webgis-brand-primary: #59c134;

        /* Optional: helle Variante (wird sonst automatisch berechnet) */
        /* --webgis-brand-primary-light: #d9f0d0; */

        /* Optional: dunkle Variante (wird sonst automatisch berechnet) */
        /* Wird nicht in default.css verwendet, kann aber für eigene Anpassungen genutzt werden */
        /* --webgis-brand-primary-dark: #3a7a20; */
    }

.. tip::

    In den meisten Fällen reicht es aus, nur ``--webgis-brand-primary`` zu setzen.
    Die helle und dunkle Variante werden automatisch aus der Primärfarbe berechnet,
    sofern sie nicht explizit überschrieben werden.


Beispiele
---------

Konkrete Umsetzungsbeispiele finden Sie unter :doc:`examples-default-css`.

Alle verfügbaren CSS-Variablen
-------------------------------

Alle Variablen werden innerhalb des Selektors ``.webgis-container, body { ... }`` definiert.

Brand
^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-brand-primary``
     - ``#59c134``
     - Primärfarbe der Anwendung (Hauptakzentfarbe).
   * - ``--webgis-brand-primary-light``
     - *(berechnet)*
     - Helle Variante der Primärfarbe für Hintergründe.
   * - ``--webgis-brand-primary-dark``
     - *(berechnet)*
     - Dunkle Variante der Primärfarbe für Texte und Akzente.

Buttons
^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-brand-button-bg``
     - ``var(--webgis-brand-primary-light)``
     - Hintergrundfarbe normaler Buttons.
   * - ``--webgis-brand-button-col``
     - ``var(--webgis-ui-text-selected)``
     - Textfarbe normaler Buttons.
   * - ``--webgis-brand-button-border``
     - ``var(--webgis-brand-primary)``
     - Rahmenfarbe normaler Buttons.
   * - ``--webgis-brand-button-hover-bg``
     - ``#fff``
     - Hintergrundfarbe bei Hover.
   * - ``--webgis-brand-button-hover-col``
     - ``#333``
     - Textfarbe bei Hover.
   * - ``--webgis-brand-button-hover-border``
     - ``var(--webgis-brand-primary)``
     - Rahmenfarbe bei Hover.
   * - ``--webgis-brand-button-cancel-bg``
     - ``var(--webgis-ui-surface-sunken)``
     - Hintergrund für Abbrechen-Buttons.
   * - ``--webgis-brand-button-cancel-col``
     - ``var(--webgis-ui-text-disabled)``
     - Textfarbe für Abbrechen-Buttons.
   * - ``--webgis-brand-button-cancel-border``
     - ``var(--webgis-brand-primary)``
     - Rahmenfarbe für Abbrechen-Buttons.
   * - ``--webgis-brand-button-danger-bg``
     - ``#faa``
     - Hintergrund für Gefahren-Buttons (z. B. Löschen).
   * - ``--webgis-brand-button-danger-col``
     - ``#333``
     - Textfarbe für Gefahren-Buttons.
   * - ``--webgis-brand-button-danger-border``
     - ``#f00``
     - Rahmenfarbe für Gefahren-Buttons.

Oberflächen (Surfaces)
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-surface``
     - ``#fff``
     - Standardhintergrund von Panels und Dialogen.
   * - ``--webgis-ui-surface-hover``
     - ``#efefef``
     - Hintergrund bei Hover-Zustand.
   * - ``--webgis-ui-surface-sunken``
     - ``#f6f6f6``
     - Abgesenkter Hintergrund (z. B. für Eingabefelder).
   * - ``--webgis-ui-surface-splitter``
     - ``#e0e0e0``
     - Farbe von Trennlinien.
   * - ``--webgis-ui-surface-header``
     - ``var(--webgis-ui-surface-sunken)``
     - Hintergrund von Abschnitts-Kopfzeilen.
   * - ``--webgis-ui-surface-disabled``
     - ``#aaa``
     - Hintergrund für deaktivierte Elemente.
   * - ``--webgis-ui-surface-readonly``
     - ``#eee``
     - Hintergrund für schreibgeschützte Felder.
   * - ``--webgis-ui-surface-inverse``
     - ``#444``
     - Invertierter Hintergrund (dunkler Modus).
   * - ``--webgis-ui-surface-inverse-strong``
     - ``#000``
     - Stark invertierter Hintergrund.

Text
^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-text``
     - ``#000``
     - Standardtextfarbe.
   * - ``--webgis-ui-text-selected``
     - ``var(--webgis-brand-primary-dark)``
     - Textfarbe für selektierte Elemente.
   * - ``--webgis-ui-text-label``
     - ``#333``
     - Farbe für Beschriftungen.
   * - ``--webgis-ui-text-header``
     - ``var(--webgis-brand-primary)``
     - Farbe für Überschriften in Panels.
   * - ``--webgis-ui-text-disabled``
     - ``#777``
     - Textfarbe für deaktivierte Elemente.
   * - ``--webgis-ui-text-dark-bg``
     - ``#fff``
     - Textfarbe auf dunklem Hintergrund.
   * - ``--webgis-ui-text-highlighted-bg``
     - ``#000``
     - Textfarbe auf hervorgehobenem Hintergrund.

Schriftgrößen
^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-font-size-tool-label``
     - ``8.5px``
     - Schriftgröße der Beschriftungen unter Werkzeug-Icons.

Rahmen (Borders)
^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-border``
     - ``#ccc``
     - Standard-Rahmenfarbe.
   * - ``--webgis-ui-border-subtle``
     - ``#e0e0e0``
     - Dezente Rahmenfarbe.
   * - ``--webgis-ui-border-info``
     - ``#fbed80``
     - Rahmenfarbe für Info-Hinweise.
   * - ``--webgis-ui-border-danger``
     - ``#ff0000``
     - Rahmenfarbe für Fehlerzustände.
   * - ``--webgis-ui-border-value-changed``
     - ``#59c1fb``
     - Rahmenfarbe für geänderte Werte.
   * - ``--webgis-ui-border-width-item-selected``
     - ``2px``
     - Rahmenbreite bei selektierten Listen-Einträgen.
   * - ``--webgis-ui-border-width-button``
     - ``2px``
     - Rahmenbreite von Buttons.
   * - ``--webgis-ui-border-radius-button``
     - ``10px``
     - Eckenradius von Buttons.

Overlays
^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-overlay-scrim``
     - ``rgba(0,0,0,0.8)``
     - Dunkler Hintergrund-Overlay (z. B. für modale Dialoge).
   * - ``--webgis-ui-overlay-scrim-light``
     - ``rgba(0,0,0,0.6)``
     - Hellere Variante des Overlay.
   * - ``--webgis-ui-overlay-light``
     - ``rgba(255,255,255,0.25)``
     - Heller semi-transparenter Overlay.
   * - ``--webgis-ui-overlay-muted``
     - ``#cccccc1f``
     - Gedämpfter Overlay für subtile Hervorhebungen.

Status-Farben
^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-status-error-bg``
     - ``#ffcccc``
     - Hintergrund für Fehlermeldungen.
   * - ``--webgis-ui-status-error-bg-strong``
     - ``#ff8888``
     - Kräftiger Fehlerhintergrund.
   * - ``--webgis-ui-status-warning-bg``
     - ``#ffffaa``
     - Hintergrund für Warnmeldungen.
   * - ``--webgis-ui-status-highlighted-bg``
     - ``#ffffaa``
     - Hintergrund für hervorgehobene Inhalte.
   * - ``--webgis-ui-status-info-bg``
     - ``#ffffaa``
     - Hintergrund für Informationshinweise.
   * - ``--webgis-ui-status-success-bg``
     - ``#e0ffe0``
     - Hintergrund für Erfolgsmeldungen.

Bubble / Kontextmenü
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-bubble-park``
     - ``#aaa``
     - Farbe für gepinnte Infoboxen.
   * - ``--webgis-ui-bubble-parked-bg``
     - ``#fa7c03``
     - Hintergrundfarbe für angeheftete Infoboxen.
   * - ``--webgis-ui-bubble-contextmenu-bg``
     - ``#026894``
     - Hintergrundfarbe des Karten-Kontextmenüs.

Abstände und Größen
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-tool-item-img-size``
     - ``26px``
     - Größe der Werkzeug-Icons in der Toolbar.
   * - ``--webgis-ui-tool-item-padding``
     - ``12px``
     - Innenabstand eines Werkzeug-Eintrags.
   * - ``--webgis-ui-tool-item-margin``
     - ``3px``
     - Außenabstand zwischen Werkzeug-Einträgen.
   * - ``--webgis-ui-presentation-toc-title-padding``
     - ``5px 20px 5px 5px``
     - Innenabstand des TOC-Titels (eingeklappt).
   * - ``--webgis-ui-presentation-toc-title-margin``
     - ``-5px 8px -5px 20px``
     - Außenabstand des TOC-Titels (eingeklappt).
   * - ``--webgis-ui-presentation-toc-title-expanded-padding``
     - ``5px 20px 5px 30px``
     - Innenabstand des TOC-Titels (ausgeklappt).
   * - ``--webgis-ui-presentation-toc-title-expanded-margin``
     - ``-5px -5px -5px -5px``
     - Außenabstand des TOC-Titels (ausgeklappt).
   * - ``--webgis-ui-presentation-toc-item-padding``
     - ``8px``
     - Innenabstand eines TOC-Eintrags.
   * - ``--webgis-ui-presentation-toc-item-marign``
     - ``3px``
     - Außenabstand eines TOC-Eintrags.
   * - ``--webgis-ui-presentation-toc-item-font-size``
     - ``14px``
     - Schriftgröße der TOC-Einträge.
   * - ``--webgis-ui-presentation-toc-item-legend-size``
     - ``30px``
     - Größe der Legendensymbole im TOC.
   * - ``--webgis-ui-button-padding``
     - ``10px 14px``
     - Innenabstand von Buttons.
   * - ``--webgis-ui-button-font-size``
     - ``14px``
     - Schriftgröße von Buttons.
   * - ``--webgis-ui-input-padding``
     - ``8px 5px``
     - Innenabstand von Eingabefeldern.
   * - ``--webgis-ui-input-font-size``
     - ``14px``
     - Schriftgröße von Eingabefeldern.


