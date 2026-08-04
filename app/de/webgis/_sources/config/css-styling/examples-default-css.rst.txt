``default.css`` – Beispiele
============================

Diese Seite zeigt konkrete ``default.css``-Beispiele in aufsteigender Einfachheit.
Zu jedem Beispiel sind zwei Screenshots (TOC und Tools) sowie ein CSS-Snippet angeführt.

Modern: Primärfarbe plus Header-Akzent
-----------------------------------------

Nur die Primärfarbe wird gesetzt, die helle Variante wird automatisch berechnet.

.. list-table::
   :widths: 50 50

   * - .. image:: img/modern_simple-toc.jpg
          :alt: Beispiel modern_simple - TOC
          :width: 100%
     - .. image:: img/modern_simple-tools.jpg
          :alt: Beispiel modern_simple - Tools
          :width: 100%

.. literalinclude:: img/modern_simple.css
   :language: css

Modern: nur Primär und Lightfarbe
--------------------------------------

(STMK)

Hier wird die Helle Farbe nicht automatisch berechnet, sondern explizit gesetzt.

.. list-table::
   :widths: 50 50

   * - .. image:: img/modern_with_custom_light-toc.jpg
          :alt: Beispiel modern_with_custom_light - TOC
          :width: 100%
     - .. image:: img/modern_with_custom_light-tools.jpg
          :alt: Beispiel modern_with_custom_light - Tools
          :width: 100%

.. literalinclude:: img/modern_with_custom_light.css
   :language: css

Flat: Kein Underline bei selektieren Items
----------------------------------------------

(BGL)

Primär- und Light-Farbe werden gleich gesetzt. Dadurch entsteht ein reduzierter, flacher Look.

.. list-table::
   :widths: 50 50

   * - .. image:: img/flat-toc.jpg
          :alt: Beispiel flat - TOC
          :width: 100%
     - .. image:: img/flat-tools.jpg
          :alt: Beispiel flat - Tools
          :width: 100%

.. literalinclude:: img/flat.css
   :language: css

Zwei Primärfarben
----------------------------------------------

(NÖ)

Die helle Variante wird explizit gesetzt und nicht automatisch berechnet. Das gibt mehr Kontrolle
über Lesbarkeit und Kontrast.

.. list-table::
   :widths: 50 50

   * - .. image:: img/modern_two_primary_colors-toc.jpg
          :alt: Beispiel modern_two_primary_colors - TOC
          :width: 100%
     - .. image:: img/modern_two_primary_colors-tools.jpg
          :alt: Beispiel modern_two_primary_colors - Tools
          :width: 100%

.. literalinclude:: img/modern_two_primary_colors.css
   :language: css

Textfarbe von selektierten Items anpassen
--------------------------------------------------

(OÖ)

Neben Brand-Farben wird hier auch ``--webgis-ui-text-selected`` angepasst, um die Lesbarkeit
auf hellen Flächen zu verbessern.

.. list-table::
   :widths: 50 50

   * - .. image:: img/modern_with_custom_light2-toc.jpg
          :alt: Beispiel modern_with_custom_light2 - TOC
          :width: 100%
     - .. image:: img/modern_with_custom_light2-tools.jpg
          :alt: Beispiel modern_with_custom_light2 - Tools
          :width: 100%

.. literalinclude:: img/modern_with_custom_light2.css
   :language: css

Dialog Header anpassen
------------------------------

(VBG)

Zusätzlich zur Brand-Farbe werden Dialog-/Panel-Header gezielt über
``--webgis-ui-surface-header`` und ``--webgis-ui-text-header`` gestaltet.

.. list-table::
   :widths: 50 50

   * - .. image:: img/modern_with-custom-headers-toc.jpg
          :alt: Beispiel modern_with-custom-headers - TOC
          :width: 100%
     - .. image:: img/modern_with-custom-headers-tools.jpg
          :alt: Beispiel modern_with-custom-headers - Tools
          :width: 100%

.. literalinclude:: img/modern_with-custom-headers.css
   :language: css

Presentation-Container hervorheben
-----------------------------------------------------

(KTN)

Dieses Beispiel ergänzt die Standard-Variablen um ein gezieltes Styling für
nicht selektierte Presentation-Container (``.webgis-presentation_toc-title``).

.. image:: img/modern_with_presention_containers-toc.jpg
   :alt: Beispiel modern_with_presention_containers - TOC
   :width: 100%

.. note::

   Für dieses Beispiel liegt derzeit kein ``*_tools.jpg`` vor. Das ist optional.

.. literalinclude:: img/modern_with_presention_containers.css
   :language: css
