Styling and CSS Customization
=============================

The appearance of *WebGIS Portal*, *WebGIS API*, and *WebGIS CMS* can be customized with your own CSS files without losing changes during an update.

Depending on the application, different files are available:

.. list-table::
   :widths: 20 25 55
   :header-rows: 1

   * - Application
     - CSS file(s)
     - Purpose
   * - WebGIS Portal
     - ``default.css``, ``portal.css``, ``site.css``
     - Colors, sizes, logo, and navbar styling
   * - WebGIS API
     - ``default.css``, ``site.css``
     - Colors and sizes in the viewer
   * - WebGIS CMS
     - ``cms.css``, ``site.css``
     - Primary color of the CMS user interface

.. note::

    The most important file is ``default.css``, because it determines the appearance of the **viewer** and the **portal pages**.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   scope
   default-css
   portal-css
   cms-css
   site-css
   examples-default-css