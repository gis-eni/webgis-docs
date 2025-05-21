Lokal ausführen (Windows Desktop Modus)
=======================================

.. Sowohl *gView.WebApps* als auch *gView.Server* können lokal auf dem Desktop gestartet werden.

.. Der Einsatz von *gView.Server* lokal macht hauptsächlich für Testzwecke Sinn.

.. .. note::

..     Ein möglicher Anwendungsfall wäre jedoch, den *gView.Server* innerhalb einer Offline-Lösung 
..     zu verwenden. Dazu müssten auf den Offline-Geräten folgende Komponenten vorhanden sein:

..     * Kartenserver (*gView.Server*)
..     * Alle notwendigen Daten (z.B. in einer SQLite-Datenbank)
..     * Eine WebGIS-Lösung, die über den Kartenserver Karten darstellt.

.. Da *gView.WebApps* die früheren Desktop-Anwendungen *gView.Carto* und *gView.DataExplorer* ablöst, kann 
.. es sinnvoll sein, diese Applikation nur bei Bedarf zu starten.

.. Dazu muss man in das Verzeichnis wechseln, in dem im vorherigen Schritt die Anwendung *deployed* wurde
.. (hier: C:\\apps\\gview-gis\\local\\6.24.1801)


.. .. note::

..     Die letzten beiden Unterverzeichnisse entsprechen dem Profil und der Versionsnummer des zuvor
..     erstellten *Deployments*.

.. In diesem Verzeichnis sollten sich folgende Dateien und Ordner befinden:

.. .. image:: img/run01.png

.. * ``gview-server.bat`` startet den *gView.Server* lokal.
.. * ``gview-web.bat`` startet *gView.WebApps* (*gView.Carto*, *gView.DataExplorer*) lokal.

.. Wenn man ``gview-web.bat`` startet, erhält man folgende Ausgabe:

Im Verzeichnis ``C:\apps\webgis`` befinden sich zwei ausführbare Batch-Dateien. Diese können verwendet werden, um WebGIS *local* zu starten. Das bedeutet, dass WebGIS hier wie eine Desktop-Anwendung gestartet wird.
Für die einzelnen Anwendungen wird dazu je eine *lokaler WebServer* gestartet und die Anwendungen über den Browser angezeigt.

.. code:: text

    C:\apps\webgis>
    └── webgis
        └── local
            ├── 7.25.701
            │   ├── _requirements
            │   ├── _scripts
            │   ├── start-webgis-cms.bat
            │   ├── start-webgis.bat
            │   ├── webgis-api
            │   ├── webgis-cms
            │   └── webgis-portal

* ``start-webgis.bat``:
  Startet die ``WebGIS API`` (lokaler WebServer unter HTTP Port 5001) und das ``WebGIS Portal`` (lokaler WebServer unter HTTP Port 5002). Zusätzlich wird ein Browserfenster geöffnet, in das WebGIS Portal angezeigt wird.

* ``start-webgis-cms.bat``:
  Startet die ``WebGIS CMS`` Anwendung in einem lokalen Server unter dem HTTP Port 5003. Zusätzlich wird ein Browserfenster geöffnet, in dem die CMS Anwendung angezeigt wird.

.. note::
   Bevor man *WebGIS* produktiv betreiben kann, sind einige *Konfigurationsschritte* notwendig. Jede Applikation im *WebGIS* Paket muss im Ordner ``_config`` eine entsprechende Konfigurationsdatei enthalten (``api.config``, ``portal.config``, ``cms.config``).
   Die Konfigurationsdateien befinden sich im Installationspaket. Allerdings wird eine Standardkonfiguration vom ersten Start der Anwendung erstellt. Diese kann dann für die individuelle Bedürfnisse angepasst werden.
   Siehe auch Abschnitt **Konfiguration**. 

Startet man ``start-webgis.bat`` zum ersten Mal, wird überprüft, ob es für die Anwendungen *WebGIS API* bzw. *WebGIS Portal* eine Konfigurationsdatei gibt (``webgis-api/_config/api.config`` bzw. ``webgis-portal/_config/portal.config``).
Falls dies nicht der Fall ist, wird ein Prototyp der WebGIS Konfiguration angelegt. Diese kann später angepasst werden. Neben den Konfigurationsdateien wird zusätzlich auch ein Verzeichnis ``webgis-repository`` angelegt.

.. code:: text

    C:\apps\webgis>
    └── webgis
        └── local
            └── webgis-repository
                ├── cms
                ├── configuration
                ├── db
                ├── output
                └── security

Dort werden zusätzliche Dateien angelegt, die für den Betrieb von *WebGIS* notwendig sind (Kartenprojekte, CMS Datenbank, ...).

.. note::
   Einige Dateien im ``webgis-repository`` werden verschlüsselt abgelegt. Ebenfalls wird die interne Kommunikation zwischen den einzelnen WebGIS Web-Applikationen und Anmeldungscookies verschlüsselt.
   Die ``Keys`` für diese Verschlüsselungen werden nach dem ersten Start unter ``webgis-repository/security/keys`` abgelegt. Die darin enthalten Dateien sollte nicht an Dritte weitergegeben werden.
   Betreibt man WebGIS sowohl im Internet/Intranet als auch als *Offline Lösung*, sollten für die *Offline Lösung* nicht die gleichen ``keys`` verwendet werden, wie am Server. Bei einer *Offline Lösung* erhalten
   die Anwender ein Paket mit allen Programm- und Konfigurationsdateien.

Startet man ``start-webgis.bat``, öffnen sich zwei Konsolenfenster, in denen die lokalen WebServer laufen:

.. image:: img/install_1.png


In einem Browserfenster wird die *WebGIS Portal* Anwendung angezeigt:

.. image:: img/install_2.png

.. note::

    Gerade beim ersten Start werden einige Konfigurationsdateien erstellt und kopiert. Dabei kann es leider vorkommen, dass die *WebGIS API* langsamer startet und für das *WebGIS Portal* rechtzeitig zur Verfügung steht.
    WebGIS zeigt in diesen Fall eine Fehlermeldung dar (``No connection could be made because the target machine actively refused it.``). Dieser Fehler kann einfach behoben werden, indem man die Browser mit ``F5`` neu lädt.
    Sobald die API mit der Erstkonfiguration fertig ist, sollte das Portal richtig angezeigt werden.

Über die Standardkonfiguration steht bereits eine Basiskarte zur Verfügung. Ebenfalls funktionieren die darin angeboten Werkzeuge (Schnellsuche nach Adressen, Koordinaten- und Höhenabfrage, 3D Model) bereits.

Möchte man zusätzliche Kartendienste (WMS, ArcGISServer Dienste) einbinden, kann das ebenfalls über die Benutzeroberfläche des Viewers erfolgen (``Dienste hinzufügen``). Möchte man Dienste in Karten immer wieder verwenden,
kann das über die *WebGIS CMS Web-Applikation* erfolgen. Die grobe Vorgehensweise beim erstellen von WebGIS Karten ist folgende:

1. Einbinden von Diensten (WMS, AGS, ...) ins CMS.

2. Parametrieren von speziellen Eingenschaften der Dienste (mögliche Abfragen, Inhaltsverzeichnis bzw. Darstellungsvarianten, Bearbeitungsmasken, Berechtigungen).

3. CMS veröffentlichen (damit werden diese Einstellung für eine WebGIS API Instanz sichtbar gemacht).

4. Einsteigen als Administrator/Kartenautor ins *WebGIS Portal*, von dort eine bestehend Karte im *MapBuilder* öffnen oder direkt über den *MapBuilder* eine neue Karte erstellen.

5. Im *MapBuilder* die gewünschten Dienste und Werkzeuge einer Karte hinzufügen.

6. Karte über den *MapBuilder* für das *WebGIS Portal* veröffentlichen. Damit steht diese Karte anderen Anwendern zur Verfügung.

Das *WebGIS CMS* kann lokal über die Batch-Datei ``start-webgis-cms.bat`` gestartet werden. Auch wird beim ersten Start eine *Default Konfiguration* angelegt. 

**Standard-Zugangsdaten**

Die vordefinierten Zugangsdaten für das CMS-System lauten:

- **Benutzername:** ``author``
- **Passwort:** ``webgisauthor``

.. warning::
    
    Falls das CMS auf einem anderen System als einem geschützten Testsystem läuft oder öffentlich zugänglich ist,  
    **muss** aus Sicherheitsgründen das Standardpasswort dringend geändert werden!  
    Andernfalls besteht ein hohes Risiko für unbefugten Zugriff.

Die Applikation startet als lokale Server Anwendung (HTTP Port 5003) und wird in einem Browser angezeigt:

.. image:: img/install_3.png

**Standardkonfiguration der WebGIS CMS-Bäume**

In der *Default-Konfiguration* werden zwei WebGIS CMS-Bäume automatisch erstellt:

1. **``WebGIS Release Default``**  
   - Enthält vordefinierte **Basiskartendienste** (z. B. *Basemap.at*).  
   - Diese wurde von den *WebGIS-Entwicklern* erstellt und dient als **unveränderbare Basis** für Kartenanwendungen.  
   - Änderungen an diesem Baum sind **nicht empfohlen**.  

2. **``WebGIS Custom``**  
   - Hier können und **sollten eigene Dienste** konfiguriert werden.  
   - Dieser Baum dient als individuelle Anpassungsebene für spezifische Anforderungen.  

Zusätzlich wird eine **Kachel für die Basisinstallation von DataLinq** angezeigt.  
Weitere Informationen dazu sind in der offiziellen `DataLinq-Dokumentation <LINK_ZUR_DOKU>`_ verfügbar.

