.. _css-default:

``default.css`` - Colors and sizes
===================================

The ``default.css`` file overrides CSS variables that control the overall appearance of *WebGIS Portal* and *WebGIS API*, especially colors and sizes.

Location
--------

The file is stored in the ``content/styles/<company>`` subdirectory of the respective application.
If the file is intended for a specific portal page, it is stored in ``content/portals/<portal-page-id>`` and named ``map-default.css`` there.

.. code-block:: none

    // For the company
    api/
    └── wwwroot/
        └── content/
            └── styles/
                └── <company>/
                    └── default.css

    // For a specific portal page
    portal/
    └── wwwroot/
        └── content/
            └── portals/
                └── <portal-page-id>/
                    └── map-default.css

``<company>`` corresponds to the value of the ``company`` key in ``portal.config``.
``<portal-page-id>`` corresponds to the ``id`` value of the respective portal page URL name.

.. note::

    The ``/<company>/`` and ``/<portal-page-id>/`` directories are **not** overwritten during an update.
    All changes inside them are preserved.

If the following key is set in ``portal.config``, a portal author can enter the content of ``default.css`` directly in the portal without having to store the file physically in the repository:

.. code-block:: xml

     <add key="portal-custom-content-rootpath" value="..../webgis-repository/portal-page-content" />

Brand variables (recommended adjustment)
----------------------------------------

Usually it is enough to adjust only the **brand variables** to make the application appear in your corporate colors.
All other colors are derived from them.

.. code-block:: css

    .webgis-container, body {
        /* Primary color - the most important customization value */
        --webgis-brand-primary: #82C828;

        /* Optional: light variant (otherwise calculated automatically) */
        /* --webgis-brand-primary-light: #d9f0d0; */

        /* Optional: dark variant (otherwise calculated automatically) */
        /* Not used in default.css, but can be used for custom adjustments */
        /* --webgis-brand-primary-dark: #3a7a20; */
    }

.. tip::

    In most cases, it is enough to set only ``--webgis-brand-primary``.
    The light and dark variants are calculated automatically from the primary color unless they are explicitly overridden.

Examples
--------

Concrete implementation examples can be found under :doc:`examples-default-css`.

All available CSS variables
----------------------------

All variables are defined within the selector ``.webgis-container, body { ... }``.

Brand
^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-brand-primary``
     - ``#82C828``
     - Primary application color.
   * - ``--webgis-brand-primary-light``
     - *(calculated)*
     - Light variant of the primary color for backgrounds.
   * - ``--webgis-brand-primary-dark``
     - *(calculated)*
     - Dark variant of the primary color for text and accents.

Buttons
^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-brand-button-bg``
     - ``var(--webgis-brand-primary-light)``
     - Background color of normal buttons.
   * - ``--webgis-brand-button-col``
     - ``var(--webgis-ui-text-selected)``
     - Text color of normal buttons.
   * - ``--webgis-brand-button-border``
     - ``var(--webgis-brand-primary)``
     - Border color of normal buttons.
   * - ``--webgis-brand-button-hover-bg``
     - ``#fff``
     - Background color on hover.
   * - ``--webgis-brand-button-hover-col``
     - ``#333``
     - Text color on hover.
   * - ``--webgis-brand-button-hover-border``
     - ``var(--webgis-brand-primary)``
     - Border color on hover.
   * - ``--webgis-brand-button-cancel-bg``
     - ``var(--webgis-ui-surface-sunken)``
     - Background for cancel buttons.
   * - ``--webgis-brand-button-cancel-col``
     - ``var(--webgis-ui-text-disabled)``
     - Text color for cancel buttons.
   * - ``--webgis-brand-button-cancel-border``
     - ``var(--webgis-brand-primary)``
     - Border color for cancel buttons.
   * - ``--webgis-brand-button-danger-bg``
     - ``#faa``
     - Background for danger buttons, for example delete.
   * - ``--webgis-brand-button-danger-col``
     - ``#333``
     - Text color for danger buttons.
   * - ``--webgis-brand-button-danger-border``
     - ``#f00``
     - Border color for danger buttons.

Surfaces
^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-surface``
     - ``#fff``
     - Default background of panels and dialogs.
   * - ``--webgis-ui-surface-hover``
     - ``#efefef``
     - Background in the hover state.
   * - ``--webgis-ui-surface-sunken``
     - ``#f6f6f6``
     - Sunken background, for example for input fields.
   * - ``--webgis-ui-surface-splitter``
     - ``#e0e0e0``
     - Color of divider lines.
   * - ``--webgis-ui-surface-header``
     - ``var(--webgis-ui-surface-sunken)``
     - Background of section headers.
   * - ``--webgis-ui-surface-disabled``
     - ``#aaa``
     - Background for disabled elements.
   * - ``--webgis-ui-surface-readonly``
     - ``#eee``
     - Background for read-only fields.
   * - ``--webgis-ui-surface-inverse``
     - ``#444``
     - Inverted background (dark mode).
   * - ``--webgis-ui-surface-inverse-strong``
     - ``#000``
     - Strongly inverted background.

Text
^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-text``
     - ``#000``
     - Default text color.
   * - ``--webgis-ui-text-selected``
     - ``var(--webgis-brand-primary-dark)``
     - Text color for selected elements.
   * - ``--webgis-ui-text-label``
     - ``#333``
     - Color for labels.
   * - ``--webgis-ui-text-header``
     - ``var(--webgis-brand-primary)``
     - Color for headings in panels.
   * - ``--webgis-ui-text-disabled``
     - ``#777``
     - Text color for disabled elements.
   * - ``--webgis-ui-text-dark-bg``
     - ``#fff``
     - Text color on a dark background.
   * - ``--webgis-ui-text-highlighted-bg``
     - ``#000``
     - Text color on a highlighted background.

Font sizes
^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-font-size-tool-label``
     - ``8.5px``
     - Font size of the labels under tool icons.

Borders
^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-border``
     - ``#ccc``
     - Default border color.
   * - ``--webgis-ui-border-subtle``
     - ``#e0e0e0``
     - Subtle border color.
   * - ``--webgis-ui-border-info``
     - ``#fbed80``
     - Border color for info notes.
   * - ``--webgis-ui-border-danger``
     - ``#ff0000``
     - Border color for error states.
   * - ``--webgis-ui-border-value-changed``
     - ``#59c1fb``
     - Border color for changed values.
   * - ``--webgis-ui-border-width-item-selected``
     - ``2px``
     - Border width for selected list entries.
   * - ``--webgis-ui-border-width-button``
     - ``2px``
     - Border width of buttons.
   * - ``--webgis-ui-border-radius-button``
     - ``10px``
     - Corner radius of buttons.

Overlays
^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-overlay-scrim``
     - ``rgba(0,0,0,0.8)``
     - Dark background overlay, for example for modal dialogs.
   * - ``--webgis-ui-overlay-scrim-light``
     - ``rgba(0,0,0,0.6)``
     - Lighter variant of the overlay.
   * - ``--webgis-ui-overlay-light``
     - ``rgba(255,255,255,0.25)``
     - Light, semi-transparent overlay.
   * - ``--webgis-ui-overlay-muted``
     - ``#cccccc1f``
     - Muted overlay for subtle highlighting.

Status colors
^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-status-error-bg``
     - ``#ffcccc``
     - Background for error messages.
   * - ``--webgis-ui-status-error-bg-strong``
     - ``#ff8888``
     - Strong error background.
   * - ``--webgis-ui-status-warning-bg``
     - ``#ffffaa``
     - Background for warning messages.
   * - ``--webgis-ui-status-highlighted-bg``
     - ``#ffffaa``
     - Background for highlighted content.
   * - ``--webgis-ui-status-info-bg``
     - ``#ffffaa``
     - Background for informational notes.
   * - ``--webgis-ui-status-success-bg``
     - ``#e0ffe0``
     - Background for success messages.

Bubble / context menu
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-bubble-park``
     - ``#aaa``
     - Color for pinned info boxes.
   * - ``--webgis-ui-bubble-parked-bg``
     - ``#fa7c03``
     - Background color for pinned info boxes.
   * - ``--webgis-ui-bubble-contextmenu-bg``
     - ``#026894``
     - Background color of the map context menu.

Spacing and sizes
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-tool-item-img-size``
     - ``26px``
     - Size of the tool icons in the toolbar.
   * - ``--webgis-ui-tool-item-padding``
     - ``12px``
     - Padding of a tool entry.
   * - ``--webgis-ui-tool-item-margin``
     - ``3px``
     - Margin between tool entries.
   * - ``--webgis-ui-presentation-toc-title-padding``
     - ``5px 20px 5px 5px``
     - Padding of the TOC title (collapsed).
   * - ``--webgis-ui-presentation-toc-title-margin``
     - ``-5px 8px -5px 20px``
     - Margin of the TOC title (collapsed).
   * - ``--webgis-ui-presentation-toc-title-expanded-padding``
     - ``5px 20px 5px 30px``
     - Padding of the TOC title (expanded).
   * - ``--webgis-ui-presentation-toc-title-expanded-margin``
     - ``-5px -5px -5px -5px``
     - Margin of the TOC title (expanded).
   * - ``--webgis-ui-presentation-toc-item-padding``
     - ``8px``
     - Padding of a TOC entry.
   * - ``--webgis-ui-presentation-toc-item-marign``
     - ``3px``
     - Margin of a TOC entry.
   * - ``--webgis-ui-presentation-toc-item-font-size``
     - ``14px``
     - Font size of TOC entries.
   * - ``--webgis-ui-presentation-toc-item-legend-size``
     - ``30px``
     - Size of the legend symbols in the TOC.
   * - ``--webgis-ui-button-padding``
     - ``10px 14px``
     - Padding of buttons.
   * - ``--webgis-ui-button-font-size``
     - ``14px``
     - Font size of buttons.
   * - ``--webgis-ui-input-padding``
     - ``8px 5px``
     - Padding of input fields.
   * - ``--webgis-ui-input-font-size``
     - ``14px``
     - Font size of input fields.

