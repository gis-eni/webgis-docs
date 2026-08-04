Scope and layers
================

The different CSS files can be adjusted on multiple layers, where a higher layer overrides the values from the layer below it.

``default.css``:
^^^^^^^^^^^^^^^^^

Used by: Portal, API

Scope: Viewer, portal pages, API pages

1. Delivered default values defined in ``default.css``.
   This file should not be overwritten.

2. Company layer:
   For a **company** defined in ``portal.config``, the deployment tool copies a dedicated ``default.css`` file to
   ``api/wwwroot/content/styles/<company>/default.css``.

3. Portal page layer:
   A portal page can have its own ``default.css`` file in
   ``portal/wwwroot/portals/<portal-id>/map-default.css``.
   Alternatively, the file can be edited in the admin UI for the corresponding portal page (for example when the application runs in a **container**).

``portal.css``:
^^^^^^^^^^^^^^^

Used by: Portal

Scope: Portal pages only, not the viewer

1. Delivered default values defined in ``portal.css``.
   This file should not be overwritten.

2. Company layer:
   For a **company** defined in ``portal.config``, the deployment tool copies a dedicated ``portal.css`` file to
   ``portal/wwwroot/content/companies/<company>/portal.css``.

3. Portal page layer:
   A portal page can have its own ``portal.css`` file in
   ``portal/wwwroot/portals/<portal-id>/portal.css``.
   Alternatively, the file can be edited in the admin UI for the corresponding portal page (for example when the application runs in a **container**).

``site.css``:
^^^^^^^^^^^^^

Used by: Portal, API, CMS

Scope: Portal pages, login pages, admin pages, not the viewer

1. Delivered default values defined in ``site.css``.
   This file should not be overwritten.

2. Company layer:
   For a **company** defined in ``portal.config``, the deployment tool creates a dedicated ``site.overrides.css`` file.
   This file should also not be overwritten, because it is replaced during every deployment.
   Changes to this file should be made only through the deployment tool (modify-css).

   Alternatively, the corresponding values can be set via environment variables when the application is not installed with the deployment tool but through **container images**.

``cms.css``:
^^^^^^^^^^^^

Used by: CMS

Scope: CMS user interface

Overrides the values for the CMS interface for all CMS trees.
If a file named ``cms.<cms-id>.css`` is created, the values are overridden only for the corresponding CMS tree.

The file is always copied into the same directory in which the CMS tree is located
(same level, **not** inside the tree directory itself).

This is only necessary if special CMS trees need colors other than the default values.
Otherwise, adjusting ``site.css`` is sufficient because the CMS interface inherits its values from ``site.css``.
