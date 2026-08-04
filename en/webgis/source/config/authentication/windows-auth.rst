Windows Authentication
======================

To use **Windows Authentication**, the ``portal.config`` file must contain the keyword ``windows`` in the ``security`` and ``security_allowed_methods`` keys.

.. code-block:: xml

    <!-- Security -->
    <add key="security" value="windows" />                  <!-- windows, token, clientid, forms, anonym (url) -->
    <add key="security_allowed_methods" value="windows" /> <!-- allowed methods separated by commas, no spaces !! -->

In IIS, the *WebGIS Portal* application must be configured to use **Windows Authentication** as the only authentication method.
