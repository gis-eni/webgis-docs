=========================
Windows-Authentifizierung
=========================

Damit die **Windows-Authentifizierung** verwendet wird, muss in der ``portal.config`` 
der Schlüssel ``security`` bzw. ``security_allowed_methods`` das **Schlüsselwort** 
``windows`` enthalten.

.. code-block:: xml

    <!-- Security -->
    <add key="security" value="windows"/>                  <!-- windows, token, clientid, forms, anonym (url) -->
    <add key="security_allowed_methods" value="windows" /> <!-- erlaubte Methoden mit Beistrich getrennt, keine Leerzeichen !! -->

Im IIS für die *WebGIS Portal* Anwendung ausschließlich als Authentifizierungsmethode 
**Windows Authentication** eingestellt werden.