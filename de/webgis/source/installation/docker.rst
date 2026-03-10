Installation in Docker
======================

Registry
--------

Images für die WebGIS Anwendungen sind auf Github verfügbar:

https://github.com/orgs/e-netze/packages?ecosystem=container

* webgis-cms
* webgis-api
* webgis-portal

Pull Images
-----------

.. note::

    Die Versionsnummer (hier 7.25.4002) muss ggf. an die gewünschte Version angepasst werden.

Images können mit dem folgenden Befehl heruntergeladen werden:

.. code:: bash

   docker pull ghcr.io/e-netze/webgis-cms:7.25.4002
   docker pull ghcr.io/e-netze/webgis-api:7.25.4002
   docker pull ghcr.io/e-netze/webgis-portal:7.25.4002


Lokal können die Images dann auf ``latest`` getaggt werden:

.. code:: bash  

   docker tag ghcr.io/e-netze/webgis-cms:7.25.4002 webgis-cms:latest
   docker tag ghcr.io/e-netze/webgis-api:7.25.4002 webgis-api:latest
   docker tag ghcr.io/e-netze/webgis-portal:7.25.4002 webgis-portal:latest

Starten der Container
---------------------

Zum Starten und Betreiben von WebGIS in Docker empfiehlt sich ``docker-compose``.
Eine Beispiel-Konfiguration ist im Verzeichnis 
``publish/linux-x64/docker`` im Repository https://github.com/e-netze/webgis/tree/main/publish/linux-x64/docker zu finden.

Die Konfiguration kann an die eigenen Bedürfnisse angepasst werden.
Die Konfiguration kann mit dem folgenden Befehl gestartet werden:

.. code:: bash

   docker-compose up -d

Die WebGIS Anwendungen sind dann unter den folgenden URLs erreichbar:

* CMS: http://localhost:5003
* API: http://localhost:5001
* Portal: http://localhost:5002

.. note:: 

    Voraussetzung ist, dass die Images lokal mit dem Tag ``latest`` verfügbar sind.

Stoppen der Container
----------------------

Die Container können mit dem folgenden Befehl gestoppt werden:

.. code:: bash

   docker-compose down

Konfiguration
--------------

Die jeweiligen ``_config`` Verzeichnisse für die Anwendungen wurde auf eigene Volumes gemappt.
Dort können die Konfigurationsdateien angepasst werden.
Die Konfigurationsdateien sind im Verzeichnis ``_config`` der jeweiligen Anwendung zu finden.

Das ``webgis-repository`` Verzeichnis wurde ebenfalls auf ein eigenes Volume gemappt.
Dieses Verzeichnis sollten sich alle drei Anwendungen teilen.

Zusätzlich können auch die Umgebungsvariablen in der ``docker-compose.yml``
bzw. in den ``.env``, ``api.env``, ``portal.env``, ``cms.env`` angepasst werden.

Um Beispielsweise die Culture der Anwendungen zu ändern kann die Umgebungsvariable 
``Localization__DefaultCulture`` angepasst werden.

.. note:: 

    Alle WebGIS Web-Anwendungen haben einen Endpoint ``/instance/_culture``, über den die aktuelle Culture 
    der Anwendung abgefragt werden kann, 
    und damit auch, ob die Anpassung der Umgebungsvariable erfolgreich war.

.. code::

   # .env

   # Beispiel: Setzen der Standard Culture auf Englisch (USA)
   # überschreiben der Standard Culture aus appsettings.json  
   
   Localization__DefaultCulture=en-US




