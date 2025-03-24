Konfiguration DataLinq.API und DataLinq.CodeApi
===============================================

Die Konfiguration von **DataLinq.API** und **DataLinq.CodeAPI** erfolgt über zwei Dateien:

1. **datalinq.api.json** – Verwaltung von Clients und Dateispeicherpfad, etc
2. **datalinq.config** – Definiert globale Konstanten und Code-Instanzen

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
        "SecureStringEncryptionLevel": "",  // optinal
        "DefaultPasswort": "{a-secure-password}",  // optional
        "SaltBytes": "{8byte-base64-encoded}"  //optional
      },
      ,
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
    }
  }

Erläuterung der Konfiguration:

DataLinq.Api
++++++++++++

- **StoragePath**  
  Definiert das Wurzelverzeichnis im Dateisystem für Endpoints, Queries und Views.

- **Razor**  
  - **Engine** – Legt die Razor-Rendering-Engine fest (`default`, `legacy`).

- **Crypto**  
  - **SecureStringEncryptionLevel** – Stellt die Verschlüsselungsebene für gespeicherte Verbindungsdaten und Abfrage ein.
    
    - **None**: – Sensible Daten werden im Storage Unverschlüsselt abgelegt  
  
    - **DefaultStaticEncryption**: – (Default) Daten werden im Storage mit einem fixen Password verschlüsselt
    
    - **RandomSaltedPasswordEncryption**: – Daten werden mit einem hier definieren Password und Salz verschlüsselt.
      Wird diese Wert gewählt müssen die beiden Werte **DefaultPasswort** und **SaltBytes** angeführt werden.   
  
  - **DefaultPasswort** – Standardpasswort für die Verschlüsselung (bei RandomSaltedPasswordEncryption).  
  - **SaltBytes** – Base64-kodierte Salt-Werte für zusätzliche Sicherheit (bei RandomSaltedPasswordEncryption).

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

  - **TextFileEngine** – Hier muss angeben werden, auf welche Verzeichnisse und Dateiendungen
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

- **ClientEndpoints**  
  Definiert erlaubte Client-Verbindungen zur *DataLinq.Code API*.
  Hier wird die Url der *DataLinq.Code* Anwendung angegeben.

.. note::

  Wird hier nichts angeben, kann jeder Client (**DataLinq.Code** Instanz) die 
  Daten im **Storage** bearbeiten. Es ist also wichtig hier Werte einzutragen und 
  Clients mit sicheren Passwörtern anzuführen!  

- **Clients**  
  Definiert Benutzer mit Anmeldeinformationen und Berechtigungen.

===============

`datalinq.config`
-----------------

Diese Datei ist optional befindet sich unter:  
**datalinq.api/_config/datalinq.config**  

Sie dient zur Definition von Konstanten, die im DataLinq Views (Razor Code) verwendet werden:

.. code-block:: csharp

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

- **<const>** – Hier können Konstanten definiert werden, die später im Code genutzt werden.

Diese Werte können im Code ausgelesen werden, um die Anwendung entsprechend 
der Umgebung zu konfigurieren.

Mit diesen Konfigurationsdateien kann **DataLinq** flexibel an unterschiedliche 
Anforderungen angepasst werden.