.. _css-site:

``site.css`` - Logo and navbar
==============================

The ``site.css`` file is relevant for all *WebGIS applications* and defines the style of general pages such as login and admin pages.
It is mainly used to:

* define the base colors of the application
* embed a company logo in the navigation bar
* define the navigation bar color

The file is not tied to a specific ``Company`` or portal page.
There is no dedicated storage location to override this file.
To change its values, ``cms-modify`` can be used through the ``deployment tool``.
If the application is not installed with the ``deployment tool`` but through **container images**, the corresponding values can be set via environment variables.

The following variables can be overridden:

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
     - Default value
     - Description
   * - ``--webgis-brand-primary``
     - ``#82C828``
     - Primary application color.
   * - ``--webgis-brand-primary-light``
     - *(calculated)*
     - Light variant of the primary color for backgrounds.
   * - ``--webgis-brand-primary-light-text-color``
     - ``#333``
     - Text color that remains readable on the light variant of the primary color.
   * - ``--webgis-brand-logo``
     - ``url()``
     - URL of the logo shown in the navigation bar.

Navbar
^^^^^^

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-ui-surface-navbar``
     - ``var(--webgis-brand-primary)``
     - Background color of the navigation bar.
   * - ``--webgis-ui-text-navbar``
     - ``#fff``
     - Text color in the navigation bar.

Set via environment variables
-----------------------------

The variables can also be set through environment variables.
The environment variables use the prefix ``CSS_WEBGIS_`` and the variable names are written in uppercase.

Brand
^^^^^

* ``CSS_WEBGIS_BRAND_PRIMARY``
* ``CSS_WEBGIS_BRAND_PRIMARY_LIGHT``
* ``CSS_WEBGIS_BRAND_PRIMARY_LIGHT_TEXT_COLOR``
* ``CSS_WEBGIS_BRAND_LOGO``

Navbar
^^^^^^

* ``CSS_WEBGIS_UI_SURFACE_NAVBAR``
* ``CSS_WEBGIS_UI_TEXT_NAVBAR``
