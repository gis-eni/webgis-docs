Konfiguration
=============

Die Konfiguration von **WebGIS DataLinq** erfolgt über zwei Dateien:

1. **appsettings.json** – Verwaltung von Verschlüsselung, Clients und Dateispeicherpfad  
2. **datalinq.config** – Definiert globale Konstanten wie das Environment  

Beide Konfigurationsdateien ermöglichen eine flexible Anpassung der Anwendung an verschiedene Einsatzszenarien.

===============

`appsettings.json`
------------------

Diese Datei befindet sich im Verzeichnis:  
**project/datalinq/appsettings.json**  

Sie enthält zentrale Einstellungen für Sicherheit, Pfade und Clients.

Beispiel:

.. code-block:: json

    {
      "Crypto": {
        "defaultPasswort": "passwort",
        "saltBytes": "saltBytes"
      },
      "rootPath": "path",
      "secureStringEncryptionLevel": "",
      // None, DefaultStaticEncryption, RandomSaltedPasswordEncryption
      "Clients": [
        {
          "id": "1",
          "name": "client1",
          "password": "passwort1"
        },
        {
          "id": "2",
          "name": "client2",
          "password": "passwort2",
          "EndPointParameters": "*,_*"
        },
        {
          "id": "3",
          "name": "client3",
          "password": "passwort3",
          "EndPointParameters": "*"
        }
      ]
    }

Erläuterung der Konfiguration:

- **Crypto**  
  - **defaultPasswort** – Standardpasswort für Verschlüsselung  
  - **saltBytes** – Salzwerte für die Verschlüsselung der Daten  

- **rootPath**  
  - Definiert das Wurzelverzeichnis im Dateisystem, in dem die Endpoints, Queries und Views gespeichert werden.  

- **secureStringEncryptionLevel**  
  - Legt das Level der Verschlüsselung fest:  
    - `None` – Keine Verschlüsselung  
    - `DefaultStaticEncryption` – Standardmäßige statische Verschlüsselung  
    - `RandomSaltedPasswordEncryption` – Verschlüsselung mit zufälligem Salt  

- **Clients**  
  - Hier können Benutzer (`Clients`) definiert werden, die sich mit Benutzernamen und Passwort anmelden.  
  - **EndPointParameters** bestimmt die Berechtigungen für Datenendpunkte.

===============

`datalinq.config`
-----------------

Diese Datei befindet sich unter:  
**project/datalinq/_config/datalinq.config**  

Sie dient zur Definition von Konstanten, die im DataLinq-Code verwendet werden können, z. B. zur Unterscheidung von Entwicklungsumgebungen.

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

Diese Werte können im Code ausgelesen werden, um die Anwendung entsprechend der Umgebung zu konfigurieren.

===============

Mit diesen Konfigurationsdateien kann **WebGIS DataLinq** flexibel an unterschiedliche Anforderungen angepasst werden.
