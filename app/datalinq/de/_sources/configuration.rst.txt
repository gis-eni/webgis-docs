Konfiguration
=============

Die Konfiguration von **WebGIS DataLinq** erfolgt über zwei Dateien:

1. **datalinq.api.json** – Verwaltung von Verschlüsselung, Clients und Dateispeicherpfad
2. **datalinqcode.json** – Definiert globale Konstanten und Code-Instanzen

Beide Konfigurationsdateien ermöglichen eine flexible Anpassung der Anwendung an verschiedene Einsatzszenarien.

===============

`datalinq.api.json`
-------------------

Diese Datei befindet sich im Verzeichnis:  
**DataLinq.Api/_config/datalinq.api.json**  

Sie enthält zentrale Einstellungen für Sicherheit, Pfade und Clients.

Beispiel:

.. code-block:: json

  {
    "DataLinq.Api": {
      "RootPath_": "",
      "Razor": {
        "Engine": "default"
      },
      "Crypto": {
        "SecureStringEncryptionLevel": "",
        "DefaultPasswort_": "",
        "SaltBytes_": ""
      }
    },
    "DataLinq.CodeApi": {
      "ClientEndpoints_": [
        "http://localhost"
      ],
      "Clients": [
        {
          "Id": "1",
          "Name": "datalinq",
          "Password": "datalinq",
          "EndPointParameters": "*,_*"
        }
      ]
    }
  }

Erläuterung der Konfiguration:

- **RootPath_**  
  Definiert das Wurzelverzeichnis im Dateisystem für Endpoints, Queries und Views.

- **Razor**  
  - **Engine** – Legt die Razor-Rendering-Engine fest (`default`, `legacy`, `core`).

- **Crypto**  
  - **SecureStringEncryptionLevel** – Stellt die Verschlüsselungsebene für gespeicherte Verbindungsdaten ein.  
  - **DefaultPasswort_** – Standardpasswort für die Verschlüsselung.  
  - **SaltBytes_** – Base64-kodierte Salt-Werte für zusätzliche Sicherheit.

- **ClientEndpoints_**  
  Definiert erlaubte Client-Verbindungen zur *DataLinq.Code API*.

- **Clients**  
  Definiert Benutzer mit Anmeldeinformationen und Berechtigungen.

===============

`datalinqcode.json`
-------------------

Diese Datei befindet sich unter:  
**datalinq.code/_config/datalinqcode.json**  

Sie dient zur Definition von Konstanten, die im DataLinq-Code verwendet werden, sowie zur Konfiguration von Code-Instanzen.

Beispiel:

.. code-block:: json

  {
    "DataLinq.Code": {
      "Crypto": {
        "DefaultPasswort_": "",
        "SaltBytes_": ""
      },
      "Instances_": [
        {
          "Name": "Local",
          "Description": "A local datalinq instance for testing and development",
          "LoginUrl": "~/DataLinqAuth?redirect={0}",
          "LogoutUrl": "~/DataLinqAuth/Logout?redirect={0}",
          "CodeApiClientUrl": "~"
        }
      ]
    }
  }

Erläuterung:

- **Crypto**  
  - **DefaultPasswort_** – Standardpasswort für die Verschlüsselung.  
  - **SaltBytes_** – Base64-kodierte Salt-Werte für zusätzliche Sicherheit.

- **Instances_**  
  Definiert DataLinq-Code-Instanzen.  
  - **Name** – Name der Instanz.  
  - **Description** – Beschreibung der Instanz.  
  - **LoginUrl** – URL für die Anmeldung.  
  - **LogoutUrl** – URL für die Abmeldung.  
  - **CodeApiClientUrl** – Basis-URL für die Code-API.