.. _css-styling:

================================
Styling und CSS-Anpassungen
================================

Das Erscheinungsbild von *WebGIS Portal*, *WebGIS API* und *WebGIS CMS* kann über eigene
CSS-Dateien individuell angepasst werden, ohne dass Änderungen bei einem Update verloren gehen.

Je nach Anwendung stehen unterschiedliche Dateien zur Verfügung:

.. list-table::
   :widths: 20 25 55
   :header-rows: 1

   * - Anwendung
     - CSS-Datei(en)
     - Zweck
   * - WebGIS Portal
     - ``default.css``, ``portal.css``, ``site.css``
     - Farben/Größen sowie Logo und Navbar-Styling
   * - WebGIS API
     - ``default.css``, ``site.css``
     - Farben und Größen im Viewer
   * - WebGIS CMS
     - ``cms.css``, ``site.css``
     - Primärfarbe der CMS-Oberfläche


.. note::
    
    Die wichtigste Datei ist die ``default.css``, da sie das Erscheinungsbild des **Viewers** und der **Portalseiten** bestimmt.


.. toctree::
   :maxdepth: 1
   :caption: Inhaltsverzeichnis:

   scope
   default-css
   portal-css
   cms-css
   site-css
   examples-default-css

