======================
App Menu Items
======================

In addition to custom tools (see :doc:`customtools`), ``custom.js`` can also be used to add custom entries to the **app menu** (the burger menu in the top right of the viewer). This is useful, for example, for links to a SAML login/logout, to an external application, or to further information.

.. code-block:: javascript

    webgis.custom.appMenuItems.add({
        name: 'Login',
        command: 'https://login.example.com/samllogin?target=/webgis/map/demo/basemap',
        tooltip: 'Anmelden',
        command_target: 'self',
        image: 'https://cdn.example.com/icons/box-arrow-in-right.svg'
    });

    webgis.custom.appMenuItems.add({
        name: 'Logout',
        command: 'https://login.example.com/profile/SAML2/POST/SLO',
        tooltip: 'Abmelden',
        command_target: 'self',
        image: 'https://cdn.example.com/icons/box-arrow-right.svg'
    });

As with custom tools: if ``webgis.custom.appMenuItems.add(...)`` is called in ``custom.js``, the entry is added to all maps of this portal page. If the entry should only appear in certain maps, this can be restricted via the ``mapUrlName`` variable as usual (see :doc:`allgemeines`).

Properties of an App Menu Item
======================================

The parameter passed is an object that must contain at least the properties ``name`` and ``command``.

.. list-table:: Properties of an App Menu Item
   :widths: 20 80
   :header-rows: 1

   * - **Property**
     - **Description**
   * - ``name``
     - Label of the menu item.
   * - ``command``
     - URL that is called when the menu item is clicked.
   * - ``tooltip``
     - Text shown as a tooltip when hovering the mouse over the menu item.
   * - ``command_target``
     - Controls how the link is called:

       - ``'self'``: link opens in the current tab.
       - ``'_blank'``: link opens in a new tab.
       - ``'dialog'``: link opens in a dialog in the viewer (may not work for third-party sites).

   * - ``image``
     - Icon for the menu item. Can be an absolute URL (e.g. to an SVG icon) or a file name, if the icon is located in ``content/api/img/tools``.

.. tip::

    A typical use case is login/logout via SAML, as shown in the example above: the **Login** entry calls the SAML login endpoint and redirects back to the map after successful login (``target`` parameter). The **Logout** entry calls the single logout endpoint (SLO).
