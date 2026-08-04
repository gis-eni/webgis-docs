=====================
Portal Configuration
=====================

File ``_config/portal.config``
===============================

The installation of the portal is optional. If WebGIS is used only as an API for HTML/JavaScript clients, it can be omitted.
In that case, map applications can still be created, but without additional tools.
Without the portal installation, there is also no **MapBuilder** available.

This file is created with ``default values`` when the API starts for the first time if it does not already exist.
This section explains how to adapt the file to your own requirements for productive use.

The file is, like ``api.config``, an XML file that contains various ``key-value pairs``.

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <configuration>
     <appSettings>
       <!-- Shared Crypto Keys -->
       <add key="shared-crypto-keys-path" value="C:\apps\webgis/test/webgis-repository/security/keys" />

       <!-- General -->
       <add key="company" value="my-company" />
       <add key="portal-name" value="webGIS Portal" />
       <add key="portal-name-url" value="http://www.e-steiermark.com" />

       <!-- Security -->
       <!-- windows, token, clientid, forms, anonym (url) -->
       <add key="security" value="anonym" />
       <!-- allowed methods separated by commas, no spaces !! -->
       <add key="security_allowed_methods" value="anonym" />

       <!-- For generating selection lists (when Windows Auth is used) -->
       <add key="portal-windows-authentication-ldap-directory" value="LDAP://my-domain" />
       <add key="portal-windows-authentication-ldap-format" value="my-domain\{0}" />

       <add key="use-local-url-scheme" value="true" />
       <add key="allow-subscriber-user-access-page-settings" value="true" />

       <!-- Advanced Security -->
       <!-- default: true; if false, login is no longer possible (security: no configuration in internet) -->
       <add key="allow-subscriber-login" value="true" />

       <!-- URL to the portal as seen by the user -->
       <add key="api" value="http://localhost:5001" />
       <!-- URL to the portal as seen from the server -->
       <add key="api-internal-url" value="http://localhost:5001" />
       <add key="portal-url" value="http://localhost:5002" />

       <add key="portal-custom-content-rootpath"
         value="C:\apps\webgis/test/webgis-repository/portal-page-content" />
       <!-- EPSG code primarily used and used for distance calculations -->
       <add key="map-calc-crs" value="3857" />
       <!-- Progressive Web App true/false, currently not used -->
       <add key="register-serviceworker" value="false" />

       <!-- Cache -->
       <add key="cache-provider" value="fs" />
       <!-- Same connection string as in api.config -->
       <add key="cache-connectionstring" value="C:\apps\webgis/test/webgis-repository/db/cache" />

       <!-- Cache Aside -->
       <!-- optional: empty, redis, inapp -->
       <add key="cache-aside-provider" value="inapp" />
       <!-- 3600 seconds caching -->
       <add key="cache-aside-connectionstring" value="3600" />

       <!-- Subscriber Database -->
       <!-- same connection string as in api.config -->
       <add key="subscriber-db-connectionstring"
         value="fs:C:\apps\webgis/test/webgis-repository/db/subscriber" />

       <!-- Allow custom layouts -->
       <add key="query-custom-map-layout" value="true" />
     </appSettings>
   </configuration>

Section ``General``
===================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``company``
     - Unique identifier for the portal operator's company (for example ``e``, ``kagis``, ``sagis``). It is used for styling. Style sheet files that are not overwritten during updates can be stored in a subdirectory with this prefix.
   * - ``portal-name``
     - Text shown in the title bar of all portal pages (default: *WebGIS Portal*).
   * - ``portal-name-url``
     - URL of the portal operator's website. Opened when the user clicks the title bar text.

Section ``Security``
====================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``security``
     - Defines the authentication method for portal sign-in. Possible values are ``windows`` and ``anonym``. In customer-specific installations, ``pvp``, ``pvp2``, and ``token`` are also available.
   * - ``security_allowed_methods``
     - Allows login with a different method than the one defined in ``security``. The desired login mode can be passed as a URL parameter (for example ``&security=anonym``). The methods listed here must be separated by commas. If only one method is allowed, it must match the value in ``security``.
   * - ``allow-subscriber-user-access-page-settings``
     - Determines whether authorized subscribers may edit content on portal pages. In closed systems, this can be set to ``false``.
   * - ``use-local-url-scheme``
     - ``true`` / ``false``

       In local or offline environments, this value can be set to ``true``. In that case, key exchange takes place over an unencrypted HTTP connection **without SSL**. For a public portal, this value should be ``false`` so that an encrypted **HTTPS** connection is ensured.

       .. danger::

          This value should only be set to ``true`` in local or offline environments, for example for test purposes. Even for intranet applications, encrypted SSL connections are recommended today.

In addition, optional credentials for secured endpoints can be defined here, for example for clearing the (user) cache.
These endpoints should be protected with a password to prevent unauthorized access.
The following keys enable the configuration of these credentials:

.. code-block:: xml

   <section name="security">
      <!-- optional: credentials for secured endpoints, e.g. cache/clear -->
      <add key="secure-endpoint-url-password" value="****************************" />
      <add key="secure-endpoint-basicauth-username" value="admin" />
      <add key="secure-endpoint-basicauth-password" value="**************************************" />
   </section>

Section ``Selection lists``
===========================

When Windows Authentication is used, configuration values for the **LDAP directory** can be defined here.
These values are used, for example, when assigning subscriber permissions to a portal page.
The possible options are then provided in **selection lists**.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attribute
     - Description
   * - ``portal-windows-authentication-ldap-directory``
     - Specifies the **LDAP directory** used for authentication.
       Example: ``LDAP://domain.at``
   * - ``portal-windows-authentication-ldap-format``
     - Defines the **login format** in the LDAP directory.
       Example: ``domain\{0}``

Section ``Cache database``
==========================

This database stores the **sessions**. It must contain the ``webgis_cache`` table (see above).
If the **Portal application** is used as well, both the **API** and the **Portal** must use the same session cache.

The values must match those in ``api.config``:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attribute
     - Description
   * - ``cache-provider``
     - Defines the cache location.

       Possible values:

       - ``db``: for a database
       - ``fs``: for the file system
   * - ``cache-connectionstring``
     - Connection string for the database or path in the file system.

Section ``Cache Aside`` (optional)
==================================

The values entered here must match those in ``api.config``.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``cache-aside-provider``
     - Determines the **cache mechanism** used for the **cache-aside** approach.

       Possible values: ``redis``, ``inapp``, or empty (no cache aside).
   * - ``cache-aside-connectionstring``
     - Defines the connection settings for the cache provider.

       Example: ``localhost:6379`` for Redis or a time value in seconds for in-app caching (for example ``3600``)

Section ``Subscriber database``
===============================

The values entered here must match those in ``api.config``.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``subscriber-db-connectionstring``
     - Connection string to the previously configured database or path to the corresponding directory in the file system.

Section ``Urls``
================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``api``
     - URL of the API as visible to the user.
   * - ``api-internal-url``
     - Internal URL used by the portal to communicate with the API, for example for accessing the storage. If both applications are installed on the same server, a local address can be used, for example ``http://localhost/webgis-api``. By default, this can be the same value as ``api``.
   * - ``portal-url``
     - URL of the portal, as visible to the user. This is used, for example, to generate links for sharing maps.

Section ``Advanced Security``
=============================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``allow-subscriber-login``
     - Controls whether subscribers can log in to this instance. A detailed description of this key is available in ``api.config`` under the ``Subscriber Registration`` section.
   * - ``query-custom-map-layout``
     - Allows the use of custom layouts in the map viewer depending on screen size. This key defines whether custom layouts are allowed (``true``) or prohibited (``false``).

Section ``Logging``
===================

.. code-block:: xml

   <!-- only for debugging, never in production -->
   <add key="trace" value="true" />
   <add key="tracePath" value="C:\apps\webgis\local\webgis-repository\logs" />

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``trace``
     - Enables logging for debugging purposes. When enabled, a ``trace.log`` file is created in the specified directory. The log can contain information about a user's login parameters, for example.

       .. danger::

          This function should only be used for debugging and never activated in a production environment.

   * - ``tracePath``
     - Defines the directory where the ``trace.log`` file is stored.