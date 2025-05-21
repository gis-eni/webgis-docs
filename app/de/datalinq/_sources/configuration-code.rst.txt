Konfiguration DataLinq.Code
===========================

Die Konfiguration von **DataLinq.Code** erfolgt über die Datei:

1. **datalinq.code.json** – Verwaltung von Verschlüsselung und **DataLinq.CodeApi** Instanzen.

Die Konfigurationsdatei ermöglichen eine flexible Anpassung der Anwendung 
an verschiedene Einsatzszenarien.

===============

`datalinq.code.json`
--------------------

Diese Datei befindet sich unter:  
**datalinq.code/_config/datalinq.code.json**  

Beispiel:

.. code-block:: json

  {
    "DataLinq.Code": {
      "Crypto": {
        "DefaultPasswort": "",
        "SaltBytes": ""
      },
      "Instances": [
        {
          "Name": "Local",
          "Description": "A local datalinq instance for testing and development",
          "LoginUrl": "{url-datalinq-code-api}",
          "LogoutUrl": "{url-datalinq-code-api}",  // optional
          "CodeApiClientUrl": "{url-datalinq-code-api}"
        }
      ]
    }
  }

Erläuterung:

- **Crypto**  
  Diese Werte werden in der Regel zufällig vergeben und sind optional. Laufen mehrere 
  Instanzen von **DataLinq.Code** hinter einem LoadBalancer, sollte hier für alle Instanzen
  fixe Werte vorgeben werden.

  - **DefaultPasswort** – Standardpasswort für die Verschlüsselung.  
  - **SaltBytes** – Base64-kodierte Salt-Werte für zusätzliche Sicherheit.

- **Instances**  
  Definiert **DataLinq.CodeApi** Instanzen. Mit einer **DataLinq.Code** Instanz,
  können mehrere **DataLinq.CodeApi** Instanzen verwaltet werden.

  - **Name** – Name der Instanz.  
  - **Description** – Beschreibung der Instanz.  
  - **LoginUrl** – URL für die Anmeldung. Der Anwender von *DataLinq.Code* muss sich über 
    den Browser anmelden. Hier muss die Url zur *DataLinq.CodeApi* angeben werden, die über 
    den Browser erreichbar ist.  
  - **LogoutUrl** – URL für die Abmeldung (optional, in der Regel gleich wie **LoginUrl**)
  - **CodeApiClientUrl** – Url zur *DataLinq.CodeApi*, wie sie von der *DataLinq.Code* angesprochen
    werden kann. In der Regel ist diese Url gleich wie die **LoginUrl**. Laufen die Anwendungen 
    in einer **Docker** oder **Kubernetes** Umgebung muss hier möglicherweise die Url angeben,
    über die die beiden Container miteinander kommunizieren können.