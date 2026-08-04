===========
General
===========

When publishing maps via portal pages in the WebGIS Portal, there is no direct access to the source code of the individual maps. To still make adjustments, a **custom.js** file can be used. This file should be located in the directory ``portal5/scripts/portals/{url-id-des-portals}``. During installation, such a file already exists under ``portal5/scripts/portals/eni``.

.. note::

   The viewer automatically loads this file every time a map is started. If it does not exist, this has no effect, but it can lead to log entries on the server. It is therefore advisable to at least keep an empty file with this name in place.

Since the file is included on every viewer call, it is suitable for **overriding API values**, e.g. for markers or custom tools.

.. tip::

    The methods shown here apply to **all maps of a portal page**. If a method should only be active for **specific maps**, this can be controlled via a **condition**.

    The variable ``mapUrlName`` contains the name of the currently loaded map and can be used to restrict behavior to specific maps.

    **Example:**

    Adding a custom **tool** only for the map **"Geoland"**:

    .. code-block:: JavaScript

        if (mapUrlName === "Geoland") {
            webgis.custom.tools.add({
                name: 'Super Tool',
                command: 'https://www.google.com/maps/@{y},{x},19z'
            });
        }
