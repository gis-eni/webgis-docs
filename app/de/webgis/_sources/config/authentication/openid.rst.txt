=================================
OpenID Connect Authentifizierung
=================================

Mit sich Anwender im *WebGIS Portal* über *Open ID Connect* anmelden können, muss in der 
``portal.config`` folgendes definiert werden:

.. code-block:: xml

    <!-- Security -->
    <add key="security" value="oidc"/>                  <!-- windows, token, clientid, forms, anonym (url) -->
    <add key="security_allowed_methods" value="oidc" /> <!-- erlaubte Methoden mit Beistrich getrennt, keine Leerzeichen !! -->

Weiters muss die Datei ``_config/application-security.json`` angepasst werden.
Hier werden die Eigenschaften (Authority, ClientId, etc) für die **OpenID Connect** Anmeldung angeführt:

.. code-block:: json

    {
      "identityType": "oidc",
      "oidc" : {    // example for Keycloak 
          "authority": "http://localhost:8080/realms/webgisrealm",
          "clientId":"webgis-portal",
          "clientSecret": "",
          "scopes": ["openid", "roles" ],
        
          // claims
          "claimsFromUserInfoEndpoint": true,
          "nameClaimType": "preferred_username",
          // optional (roles)
          "roleClaimType": "roles",  // optional, nur wenn Rollen im Token vorhanden sind
          "roleClaimValueSeparator": ","  // optional, nur wenn mehrere Rollen im Token vorhanden sind, die durch ein Trennzeichen getrennt sind
        }
    }

Windows Azure ID
----------------

Eine Anmeldung über Windows Azure wird ebenfalls angeboten. Dabei handelt sich ebenfalls um 
eine **OpenID Connect** Anmeldung. Die Konfiguration in der ``_config/application-security.json``
ist allerdings zu modifizieren:

.. code-block:: json

    {
      "identityType": "azure-ad",
      "azure-ad": {
          "Instance": "https://login.microsoftonline.com/",
          "Domain": "{my-domain}.onmicrosoft.com",
          "TenantId": "{my-tenant-id}",
          "ClientId": "{my-client-id}",

          // optional (roles)
          "extended-roles-from": "windows",  // optional, nur wenn Rollen aus lokalem AD kommen sollten
          // or
          "roleClaimType": "roles",  // optional, nur wenn Rollen im Token vorhanden sind
          "roleClaimValueSeparator": ","  // optional, nur wenn mehrere Rollen im Token vorhanden sind, die durch ein Trennzeichen getrennt sind
       }
    }

Der Parameter ``etendet-roles-from = windows`` ist optional. Hier wird nur der Username aus 
der Azure Anmeldung übernommen, die Gruppen für diesen User werden hier allerdings aus dem
Windows AD (LDAP) ausgelesen.

Wenn die Rollen/Gruppen direkt im Azure Token vorhanden sind, können diese mit den Parametern
``roleClaimType`` und ``roleClaimValueSeparator`` ausgelesen werden.
Es können dabei mehrere Claims mit dem ``roleClaimType`` im Token vorhanden sein, oder
mehrere Rollen in einzelnen Claim, die durch ein Trennzeichen
(z.B. Komma ``roleClaimValueSeparator``) getrennt sind.

Anmeldekachel OpenId Connect
----------------------------

Damit sich Anwender über **OpenID Connect** auf einer *WebGIS Portal Seite* anmelden können,
muss noch die *Security* für die Seite angepasst werden (bei der WebGIS API als Subscriber anmelden
→ Pages → entsprechende Seite auswählen)

.. image::  img/openid1.png

Mit diese Einstellung erscheint dann auf der *WebGIS Portal* Startseite die Option 
``Mit OpenId Connect anmelden``:

.. image:: img/openid2.png