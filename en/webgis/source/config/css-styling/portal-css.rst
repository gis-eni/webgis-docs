.. _css-portal:

``portal.css`` - Logo and navbar for the portal
===============================================

The ``portal.css`` file is relevant only for the *WebGIS Portal* and complements :doc:`default-css`.
It is mainly used to add a **company logo to the navigation bar**.

.. note::

    Since the portal navbar and logos can now also be adjusted through ``site.css`` for all WebGIS applications,
    see :doc:`site-css`, the use of ``portal.css`` is now mostly obsolete and remains mainly for backward compatibility.
    The one remaining use case is customizing the logo in the navigation bar for a specific portal page (i.e. when
    several portal pages exist that each need a different logo).
    In that case ``portal.css`` applies at the portal level and overrides ``site.css`` at the global level.

Location
--------

.. code-block:: none

    portal/
    └── wwwroot/
        └── content/
            └── companies/
                └── <company>/
                    ├── portal.css
                    └── img/
                        └── logo.png    <- logo image (optional)

``<company>`` corresponds to the value of the ``company`` key in ``portal.config``.

.. note::

    The ``/<company>/`` directory is **not** overwritten during an update.
    All changes inside it are preserved.

If the following key is set in ``portal.config``, a portal author can enter the content of ``default.css`` directly in the portal without storing the file physically in the repository:

.. code-block:: xml

     <add key="portal-custom-content-rootpath" value="..../webgis-repository/portal-page-content" />

Embed a logo in the navbar
--------------------------

The portal navbar logo can be replaced via the CSS selector ``.webgis-portal-navbar-logo``:

.. code-block:: css

    .navbar-brand {
        background-image: url('../img/logo.png');
        background-size: 28px;
    }

The logo image is best stored in the same company directory, for example under ``wwwroot/custom/<company>/img/logo.png``.
The relative path ``../img/logo.png`` refers to the storage location of ``portal.css``.
