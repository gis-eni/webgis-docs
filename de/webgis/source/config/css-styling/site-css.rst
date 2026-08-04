.. _css-site:

``site.css`` – Logo und Navbar
================================

Die Datei ``site.css`` ist für alle *WebGIS Anwendungen* relevant und gibt den Stil von 
Allgemeinen Seiten (Login Seiten, Admin Seiten etc.) vor. Sie wird hauptsächlich verwendet, 
um:

* Grundfarben für die Anwendung zu definieren
* Unternehmenslogo in der Navigationsleiste einzubinden
* Farbe der Navigationsleiste zu definieren

Die Datei ist nicht von ``Company`` und ``Portal Seite`` abhängig. Es gibt keine Speicherort
um diese Datei zu überschreiben. Und die möglichen Werte zu ändern kann ``cms-modify``
über das ``deployment tool`` verwendet werden. Wird nicht mit dem ``deployment tool`` installiert,
sondern über **Container Images**, können die entsprechenden Werte über Umgebungsvariablen
gesetzt werden.

Folgende Variablen können überschrieben werden:

.. code-block:: css

    :root {
        /* Brand */
        --webgis-brand-primary: #82C828;
        --webgis-brand-primary-light: color-mix(in oklch, var(--webgis-brand-primary) 25%, white);
        --webgis-brand-primary-light-text-color: #333;
        --webgis-brand-logo: url();

        /* Navbar (optional) */
        --webgis-ui-surface-navbar: var(--webgis-brand-primary);
        --webgis-ui-text-navbar: #fff;
    }

Brand
^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-brand-primary``
     - ``#82C828``
     - Primärfarbe der Anwendung (Hauptakzentfarbe).
   * - ``--webgis-brand-primary-light``
     - *(berechnet)*
     - Helle Variante der Primärfarbe für Hintergründe.
   * - ``--webgis-brand-primary-light-text-color``
     - ``#333``
     - Textfarbe, die auf der hellen Variante der Primärfarbe gut lesbar ist.
   * - ``--webgis-brand-logo``
     - ``url()``
     - URL des Logos, das in der Navigationsleiste angezeigt werden soll.

Navbar
^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-ui-surface-navbar``
     - ``var(--webgis-brand-primary)``
     - Hintergrundfarbe der Navigationsleiste.
   * - ``--webgis-ui-text-navbar``
     - ``#fff``
     - Textfarbe in der Navigationsleiste.

Setzen über Ümgebungsvariablen
-------------------------------

Die Variablen können auch über Umgebungsvariablen gesetzt werden. Die Umgebungsvariablen
haben den Präfix ``CSS_WEBGIS_`` und die Variablen werden in Großbuchstaben geschrieben. 

Brand
^^^^^^

* ``CSS_WEBGIS_BRAND_PRIMARY``
* ``CSS_WEBGIS_BRAND_PRIMARY_LIGHT``
* ``CSS_WEBGIS_BRAND_PRIMARY_LIGHT_TEXT_COLOR``
* ``CSS_WEBGIS_BRAND_LOGO``

Navbar
^^^^^^

* ``CSS_WEBGIS_UI_SURFACE_NAVBAR``
* ``CSS_WEBGIS_UI_TEXT_NAVBAR``
