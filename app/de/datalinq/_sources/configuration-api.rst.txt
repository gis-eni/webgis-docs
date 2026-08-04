Konfiguration DataLinq.API und DataLinq.CodeApi
===============================================

Die Konfiguration von **DataLinq.API** und **DataLinq.CodeAPI** erfolgt über zwei Dateien:

1. **datalinq.api.json** - Verwaltung von Clients und Dateispeicherpfad, etc
2. **datalinq.config** - Definiert globale Konstanten und Code-Instanzen

Die Konfigurationsdateien ermöglichen eine flexible Anpassung der Anwendung an 
verschiedene Einsatzszenarien.

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
      "StoragePath": "{path_to_storage}",
      "Razor": {
        "Engine": "default"  // default or legacy (old engine)
      },
      "Crypto": {
        "SecureStringEncryptionLevel": "",  // optional
        "DefaultPasswort": "{a-secure-password}",  // optional
        "SaltBytes": "{8byte-base64-encoded}"  //optional
      },
      "ImageRequestWhiteList": [
        "https://upload.wikimedia.org/",
        "https://raw.githubusercontent.com/"
      ],
      "SelectEngines": {
        "TextFileEngine": {
          "AllowedExtensions": [
            ".txt",
            ".csv"
          ],
          "AllowedPaths": [
            "C:\\DataLinq\\Data\\" // or /etc/datalinq/data on linux
          ]
        }
      }
    },
    "DataLinq.CodeApi": {
      "InitializeSandboxOnStartup": true,
      "ClientEndpoints": [   
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
    },
    "AiService": {
      "UseAzure": false,
      "AzureOpenAi": {
        "DeploymentName": "",
        "Endpoint": "",
        "ApiKey": ""
      },
      "OpenAi": {
        "ModelId": "",
        "ApiKey": "",
        "ServiceUrl": ""
      }
    },
    "Agent": {
      "DataLinqQueryAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqQueryPrompt.txt",
      "DataLinqCodeAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqCodePrompt.txt",
      "DataLinqEndpointAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqEndpointPrompt.txt",
      "DataLinqGeneralAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqGeneralPrompt.txt",
      "UserHistorySummarizerAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/UserHistorySummarizerPrompt.txt"
    },
    "TokenCache": {
      "StorageType": "file",
      "RedisConnectionString": "localhost:6379",
      "FilePath": "C:\\temp\\datalinq\\Tokens\\",
      "DefaultTTL": "00:05:00",
      "DefaultMaxUsage": null,
      "EnableBackgroundCleanup": false,
      "CleanupIntervalMinutes": "24:00:00"
    },
    "VersionControl": {
      "UseVersionControl": false,
      "LocalRepositoryPath": "C:\\temp\\datalinq\\repo",
      "RemoteUrl": "http://localhost:3000/admin/datalinq-repo.git",
      "DefaultBranch": "main",
      "CredentialType": "Token",
      "Username": "",
      "Password": "",
      "PersonalAccessToken": "",
      "DefaultAuthorName": "DataLinq Bot",
      "DefaultAuthorEmail": "bot@datalinq.com",
      "AutoCreateRepository": true
    }
  }

Erläuterung der Konfiguration:

DataLinq.Api
++++++++++++

- **StoragePath**  
  Definiert das Wurzelverzeichnis im Dateisystem für Endpoints, Queries und Views.

- **Razor**  
  - **Engine** - Legt die Razor-Rendering-Engine fest (`default`, `legacy`).

- **Crypto**  
  - **SecureStringEncryptionLevel** - Stellt die Verschlüsselungsebene für gespeicherte Verbindungsdaten und Abfrage ein.
    
    - **None**: - Sensible Daten werden im Storage Unverschlüsselt abgelegt  
  
    - **DefaultStaticEncryption**: - (Default) Daten werden im Storage mit einem fixen Password verschlüsselt
    
    - **RandomSaltedPasswordEncryption**: - Daten werden mit einem hier definieren Password und Salz verschlüsselt.
      Wird diese Wert gewählt müssen die beiden Werte **DefaultPasswort** und **SaltBytes** angeführt werden.   
  
  - **DefaultPasswort** - Standardpasswort für die Verschlüsselung (bei RandomSaltedPasswordEncryption).  
  - **SaltBytes** - Base64-kodierte Salt-Werte für zusätzliche Sicherheit (bei RandomSaltedPasswordEncryption).

- **ImageRequestWhiteList** *(optional)*  
  Liste erlaubter URL-Präfixe, von denen externe Bilder geladen werden dürfen. 
  Wird der Abschnitt nicht angeführt, sind keine externen Bildquellen freigegeben.

- **SelectEngines**
  DataLinq bietet unterschiedliche **Engines** an, um auf Daten zuzugreifen:
   
   - Datenbanken
   - Andere DataLinq.API Instanzen
   - Pain Text: Hier werden die Daten direkt als Text in der **DataLinq.Code** Anwendung eingegeben
   - Text Datein: Dateien, die am **DataLinq.API** Server liegen oder von dort erreichbar sind
   - Innerhalb von Anwendung, die die **DataLinq.API** implementieren, zB *WebGIS.API* können
     noch weiter **Engines** angeboten werden, zB GeoJSON, ...

  Einige **Engines** brauchen spezielle Einstellungen, die hier angeführt werden können. 
  Die oben angeführten Einstellungen sind die Standardwerte und gelten auch wenn unter Dateisystem
  Abschnitt nichts angeführt wird.

  - **TextFileEngine** - Hier muss angeben werden, auf welche Verzeichnisse und Dateiendungen
    mit der **TextFileEngine** zugegriffen werden darf. 

DataLinq.CodeApi
++++++++++++++++

Wird dieser Abschnitt nicht angeführt, wird in dieser Instanz die **DataLinq.CodeApi** nicht 
angeboten. 

.. note:: 
  
   Das macht beispielsweise für **DataLinq** Instanzen Sinn, die über das 
   Internet angeboten werden. Über diese Instanzen können nur **DataLinq** Berichte publiziert
   aber nicht verändert werden.  
   
   Die Bearbeitung des **Storage** über die **DataLinq.CodeApi** sollte immer nur über 
   Verbindungen erfolgen, die nicht über das Internet laufen (zB nur Intranet!)

- **InitializeSandboxOnStartup** *(optional)*  
  Legt fest, ob die Code-Sandbox bereits beim Start der Instanz initialisiert wird 
  (Standard: ``true``). Bei ``false`` wird die Sandbox erst bei der ersten Verwendung 
  initialisiert, was die Startzeit verkürzt.

- **ClientEndpoints**  
  Definiert erlaubte Client-Verbindungen zur *DataLinq.Code API*.
  Hier wird die Url der *DataLinq.Code* Anwendung angegeben.

.. note::

  Wird hier nichts angeben, kann jeder Client (**DataLinq.Code** Instanz) die 
  Daten im **Storage** bearbeiten. Es ist also wichtig hier Werte einzutragen und 
  Clients mit sicheren Passwörtern anzuführen!  

- **Clients**  
  Definiert Benutzer mit Anmeldeinformationen und Berechtigungen.
  
  - **Id** - Eindeutige Kennung des Clients.
  - **Name** - Anzeigename bzw. Benutzername des Clients.
  - **Password** - Passwort für die Anmeldung des Clients.
  - **EndPointParameters** - Einschränkung der zugänglichen Endpoint-Parameter (z.B. ``*,_*``).

AiService *(optional)*
++++++++++++++++++++++

Konfiguriert die KI-Unterstützung (z.B. für Abfrage-, Code- und Endpoint-Assistenten).
Der Abschnitt ist optional. Die KI-Dienste werden nur aktiviert, wenn entweder ein 
Azure-OpenAI-Endpoint (**AzureOpenAi:Endpoint**) oder eine OpenAI-Service-URL 
(**OpenAi:ServiceUrl**) angegeben ist. Ohne diese Werte bleiben die KI-Funktionen deaktiviert.

- **UseAzure** - Legt fest, ob Azure OpenAI (``true``) oder OpenAI (``false``) verwendet wird.

- **AzureOpenAi** - Einstellungen für Azure OpenAI.
  
  - **DeploymentName** - Name des bereitgestellten Modells (Deployment).
  - **Endpoint** - URL des Azure-OpenAI-Endpoints.
  - **ApiKey** - Zugriffsschlüssel für den Azure-OpenAI-Dienst.

- **OpenAi** - Einstellungen für OpenAI (oder kompatible Dienste).
  
  - **ModelId** - Kennung des zu verwendenden Modells.
  - **ApiKey** - Zugriffsschlüssel für den OpenAI-Dienst.
  - **ServiceUrl** - URL des OpenAI-kompatiblen Dienstes.

.. note::

   **ApiKey**-Werte sollten nicht im Klartext in der Konfigurationsdatei abgelegt,
   sondern über *User Secrets* oder Umgebungsvariablen bereitgestellt werden.

Agent *(optional)*
++++++++++++++++++

Definiert die Pfade zu den Prompt-Dateien der einzelnen KI-Agenten. Der Abschnitt ist 
nur in Verbindung mit einem konfigurierten **AiService** relevant.

- **DataLinqQueryAgent** - Prompt-Datei für den Abfrage-Assistenten.
- **DataLinqCodeAgent** - Prompt-Datei für den Code-Assistenten.
- **DataLinqEndpointAgent** - Prompt-Datei für den Endpoint-Assistenten.
- **DataLinqGeneralAgent** - Prompt-Datei für den allgemeinen Assistenten.
- **UserHistorySummarizerAgent** - Prompt-Datei zur Zusammenfassung des Verlaufs.

TokenCache *(optional)*
+++++++++++++++++++++++

Konfiguriert die Zwischenspeicherung (Cache) von Tokens. Wird der Abschnitt nicht angeführt,
gelten die Standardwerte.

- **StorageType** - Art des Token-Speichers: ``file`` (Dateisystem) oder ``redis``.
- **RedisConnectionString** - Verbindungszeichenfolge zum Redis-Server (nur bei ``redis``).
- **FilePath** - Verzeichnis für die Token-Ablage (nur bei ``file``).
- **DefaultTTL** - Standard-Lebensdauer eines Tokens im Format ``hh:mm:ss``.
- **DefaultMaxUsage** - Maximale Anzahl an Verwendungen pro Token (``null`` = unbegrenzt).
- **EnableBackgroundCleanup** - Aktiviert die periodische Bereinigung abgelaufener Tokens.
- **CleanupIntervalMinutes** - Intervall der Bereinigung im Format ``hh:mm:ss`` 
  (nur wirksam bei aktiviertem **EnableBackgroundCleanup**).

VersionControl *(optional)*
+++++++++++++++++++++++++++

Konfiguriert die Anbindung des **Storage** an ein Git-Repository, um Änderungen an 
Endpoints, Queries und Views zu versionieren. Wird der Abschnitt nicht angeführt oder 
**UseVersionControl** auf ``false`` gesetzt, ist die Versionierung deaktiviert.

- **UseVersionControl** - Aktiviert (``true``) bzw. deaktiviert (``false``) die Git-Versionierung.
- **LocalRepositoryPath** - Lokaler Pfad des Git-Repositorys. 
  Dieser Pfad wird auch als **RepoPath** des **Storage** verwendet.
- **RemoteUrl** - URL des Remote-Repositorys (z.B. auf Gitea, GitHub oder GitLab).
- **DefaultBranch** *(optional)* - Standard-Branch für Commits (Standard: ``main``).

- **CredentialType** - Art der Authentifizierung gegenüber dem Remote-Repository:
  
  - **None** - Keine Authentifizierung (z.B. bei rein lokalen Repositorys).
  - **Token** - (Default) Authentifizierung über einen *Personal Access Token*.
  - **UsernamePassword** - Authentifizierung über Benutzername und Passwort.

- **Username** - Benutzername (nur bei **UsernamePassword**).
- **Password** - Passwort (nur bei **UsernamePassword**).
- **PersonalAccessToken** - Zugriffstoken (nur bei **Token**).

- **DefaultAuthorName** *(optional)* - Name des Autors für automatische Commits 
  (Standard: ``DataLinq Bot``).
- **DefaultAuthorEmail** *(optional)* - E-Mail des Autors für automatische Commits 
  (Standard: ``bot@datalinq.com``).
- **AutoCreateRepository** *(optional)* - Legt fest, ob ein nicht vorhandenes Repository 
  automatisch erstellt wird (Standard: ``true``).

===============

`datalinq.config`
-----------------

Diese Datei ist optional befindet sich unter:  
**datalinq.api/_config/datalinq.config**  

Sie dient zur Definition von Konstanten, die im DataLinq Views (Razor Code) verwendet werden:

.. code-block:: text

  @{  var env = Const.Environment;   }

  @if(env == "Production") {
     // ...
  }

Beispiel:

.. code-block:: xml

  <?xml version="1.0" encoding="utf-8" ?>
    <configuration>
      <const>
        <add name="Environment" value="Test" />
        <!-- production, staging, test, development, ... -->
      </const>
  </configuration>

Erläuterung:

- **<const>** - Hier können Konstanten definiert werden, die später im Code genutzt werden.

Diese Werte können im Code ausgelesen werden, um die Anwendung entsprechend 
der Umgebung zu konfigurieren.

Mit diesen Konfigurationsdateien kann **DataLinq** flexibel an unterschiedliche 
Anforderungen angepasst werden.