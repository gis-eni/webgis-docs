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

Die Konfiguration der WebGIS Anwendungen erfolgt über Umgebungsvariablen.
Die jeweiligen ``_config`` Verheichnisse für die Anwendungen wurde auf eigene Volumes gemappt.
Dort können die Konfigurationsdateien angepasst werden.
Die Konfigurationsdateien sind im Verzeichnis ``_config`` der jeweiligen Anwendung zu finden.

Das ``webgis-repository`` Verzeichnis wurde ebenfalls auf ein eigenes Volume gemappt.
Dieses Verzeichnis sollten sich alle drei Anwendungen teilen.

