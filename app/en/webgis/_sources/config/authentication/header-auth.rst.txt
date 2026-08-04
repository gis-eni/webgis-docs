Header-based Authentication
===========================

In this method, the authenticated user name and roles are read from **HTTP header variables** in the request.

This is especially useful when the *WebGIS Portal* is operated behind a *reverse proxy*.
In that case, the *reverse proxy* handles the **authentication** and **authorization** of requests.
When forwarding requests, it adds specific HTTP headers that contain information about the authenticated user.
The *WebGIS Portal* reads these header variables and uses them for **access control** for maps and map services.

.. danger::

   When this method is used, the *WebGIS Portal* must be reachable **only** through the *reverse proxy*.
   If the portal is directly accessible, attackers could abuse this method.
   The *WebGIS Portal* does not verify whether the header variables were actually set by the *reverse proxy*.

Header-based authentication is enabled through the ``header-authentication`` section in ``portal.config``:

.. code-block:: xml

   <section name="header-authentication">
      <add key="use" value="true" />  <!-- default false -->
      <add key="username-variable" value="X-username" />
      <add key="roles-variable" value="X-roles" />

      <add key="extract-role-parameters" value="none" /> <!-- none, insideBrackets -->

      <add key="role-separator" value=";" />  <!-- default: , -->
      <add key="role-parameters-separator" value="," />  <!-- default: , -->

      <add key="user-prefix" value="header-user" />
      <add key="role-prefix" value="header-role" />

      <!-- Optional: -->
      <add key="extended-role-parameters-from-headers-prefix" value="X-AUTH-" />
      <add key="extended-role-parameters-from-headers" value="roleparam1,roleparam2" />
   </section>

Configuration values
====================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - ``use`` (default: ``false``)
     - Enables header-based authentication.
   * - ``username-variable``
     - Defines the **header name** that contains the user name.
   * - ``roles-variable``
     - Defines the **header name** that carries the user roles.
   * - ``extract-role-parameters`` (default: ``none``)
     - Role parameters allow an **additional restriction** of roles.
       For example, if a user group is assigned the role ``GEMEINDE``, a *role parameter* can specify the municipality the permission applies to.
       *Reverse proxy* systems can pass these parameters through ``roles-variable``.
       - ``none`` -> No role parameters are extracted.
       - ``insideBrackets`` -> Role parameters are expected inside brackets after the role.

       Example for ``insideBrackets``:
       ``role1(param1=1,param2=2);gemeinde(gemnr=123456)``
       -> **Roles:** ``role1``, ``gemeinde``
       -> **Role parameters:** ``param1=1``, ``param2=2``, ``gemnr=123456``
   * - ``role-separator`` (default: ``,``)
     - Separator between multiple roles in the ``roles-variable`` header.
   * - ``role-parameters-separator`` (default: ``,``)
     - Separator for individual role parameters during *parsing*.
       Example: ``(param1=1,param2=2,...)``
   * - ``user-prefix``, ``role-prefix``
     - Defines namespaces for users and roles to avoid ambiguity when multiple authentication methods are used.
       The prefix is separated from the user name by ``::``.

       Example:
       ``user-prefix = header-user``, user name = ``maxmustermann``
       -> ``header-user::maxmustermann``

       In CMS permission management, the full name including the prefix is used
       (``header-user::maxmustermann``).

   * - ``extended-role-parameters-from-headers-prefix``, ``extended-role-parameters-from-headers``
     - These two parameters allow the definition of **additional role parameters** that are extracted from HTTP headers.
       The prefix is added before the parameter name to make it unique.

       -> The headers ``X-AUTH-roleparam1`` and ``X-AUTH-roleparam2`` in the example above are extracted as role parameters:
       additional role parameters could then be ``roleparam1=value1`` and ``roleparam2=value2``.
