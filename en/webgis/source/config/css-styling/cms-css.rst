.. _css-cms:

``cms.css`` - Styling the CMS interface
=======================================

The ``cms.css`` file can be used to change the primary color of the *WebGIS CMS* user interface.

Location
--------

In contrast to ``default.css`` and ``portal.css``, ``cms.css`` is not stored in the application's ``wwwroot`` directory,
but in the **file system** where the CMS trees are managed.

The ``path`` value of a ``cms-item`` entry in ``cms.config`` points to the folder of the respective CMS tree.
The ``cms.css`` file must be placed **one level above** that folder, meaning in the parent directory.

Example: the following entry is configured in ``cms.config``:

.. code-block:: json

    {
      "id": "webgis-release-default",
      "path": "C:\\apps\\webgis-repositoy\\cms\\param\\webgis-release-default",
      "scheme": "webgis"
    }

Then ``cms.css`` is stored here:

.. code-block:: none

    C:\apps\webgis-repositoy\cms\param\
    ├── cms.css                        <- applies to all CMS trees in this directory
    └── webgis-release-default\       <- CMS tree folder (path in cms.config)

.. important::

    The file is located **next to** the tree folder, **not inside it**.

Multiple CMS trees with different styling
-----------------------------------------

If several CMS trees are stored in one directory and each should have a different appearance,
the file must be named according to the pattern ``cms.<tree-folder-name>.css``:

.. code-block:: none

    C:\apps\webgis-repositoy\cms\param\
    ├── cms.webgis-release-default.css <- styling only for this tree
    ├── cms.webgis-custom.css          <- styling only for this tree
    ├── webgis-release-default\
    └── webgis-custom\

An unnamed ``cms.css`` file without a tree name acts as the **fallback** for all trees in the same directory that do not have their own named CSS file.

Available CSS variables
-----------------------

For the CMS, only the **brand variables** are available. They are defined in the ``:root { ... }`` selector:

.. code-block:: css

    :root {
        /* Primary color of the CMS interface */
        --webgis-brand-primary: #ff5a9a;

        /* Optional: light variant (otherwise calculated automatically) */
        --webgis-brand-primary-light: #ffd5ff;
    }

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Default value
     - Description
   * - ``--webgis-brand-primary``
     - ``#59c134``
     - Primary color of the CMS interface.
   * - ``--webgis-brand-primary-light``
     - *(calculated)*
     - Light variant of the primary color. It is calculated automatically from ``--webgis-brand-primary`` if it is not explicitly set.
