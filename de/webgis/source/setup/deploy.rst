.. _deploy:

Installation
============

Die Installation erfolgt über das Kommandozeilenprogramm webgis.deploy. Dieses Tool erledigt folgende Aufgaben:

- Neuinstallation von webgis-portal, webgis-api und webgis-cms
- Verwaltung von Deploy-Profilen (z.B. local, test, staging, production)
- Verteilung von Änderungen an der Konfiguration (z.B. api.config, cms.config, portal.config)
- Verteilung von Änderungen am Styling (default.css, portal.css)

Vorbereitung
------------

Das Deploymenttool sowie andere Pakete können unter *Releases* aus dem GitHub Repository https://github.com/e-netze/webgis/releases heruntergeladen werden.

Voraussetzung ist eine Installation der .NET App Runtime 9.0.x.

Microsoft bietet für die Ausführung von .NET-Anwendungen zwei Hauptvarianten der Runtime an:

1. **.NET Runtime (ohne IIS-Unterstützung):**  
   Diese Version enthält ausschließlich die notwendige Laufzeitumgebung, um .NET-Anwendungen als eigenständige Prozesse auszuführen – beispielsweise als Windows-Dienst oder in Containern. Sie eignet sich für Szenarien, in denen kein IIS verwendet wird.

2. **.NET Hosting Bundle (mit IIS-Unterstützung):**  
   Diese Variante enthält zusätzlich das ASP.NET Core Module für die Integration mit dem Internet Information Services (IIS). Dadurch können ASP.NET Core-Anwendungen direkt über den IIS bereitgestellt werden. Diese Version ist optimal für die Nutzung in Windows-Server-Umgebungen mit IIS.

.. raw:: html

   <p><a href="https://dotnet.microsoft.com/en-us/download/dotnet/9.0" target="_blank">Download .NET 8.0 Runtime</a></p>


**Windows:**

Unter Windows kann das Programm beispielsweise nach ``C:\deploy\webgis`` kopiert werden.
Danach kann dann die EXE-Datei einfach ausgeführt werden. 

**Linux:**

Coming Soon ...

.. note::

   Die nachfolgende Beschreibung erfolgt auf einem Windows-System. Unter Linux sollte die Installation
   aber aus dem Aufruf des *Deploy Tools* ähnlich erfolgen.

Neue Version Ausliefern
-------------------------------------------

Wenn man das Programm zum ersten Mal startet, muss zunächst ein Profil angelegt werden.
Das Profil kann beispielsweise ``test``, ``staging`` oder ``production`` sein und entspricht 
im Grund einer WebGIS Instanz. Da wir im ersten
Schritt *WebGIS* nur lokal testen wollen, bietet sich ein Profil mit dem Namen ``local`` 
für den Start an:


.. code-block:: text
   :emphasize-lines: 1,5

    C:\deploy\webgis\> .\webgis.deploy.exe

    ******************************************
    *                                        *
    *      WebGIS.Deploy Tool 7.25.701      *
    *                                        *
    ******************************************
    Work-Directory: C:\deploy\webgis
    Directory C:\deploy\webgis\_deploy_repository exists: True
    Try Write security keys: C:\deploy\webgis\_deploy_repository\keys.config
    succeeded
    Choose a profile or create a new by enter an unique name, eg. production, staging, test
    Input profile index [0]: local

Im nächsten Schritt bietet das Programm an, den aktuellen Release von *GitHub* herunterzuladen,
falls dieser noch nicht vorhanden ist.

.. code-block:: text

   Do you want to download latetest version from GitHub? Y/N [Y]

Ist das nicht möglich, kann der letzte Release auch manuell heruntergeladen werden. 
Dazu müssen die ZIP-Dateien in das ``download`` Verzeichnis gelegt werden.

Im Beispiel also hier: ``C:\deploy\webgis\download``

.. code-block:: text

    C:\deploy\webgis\>
    .
    ├── download
    │   └── webgis-win64-7.25.701.zip
    └── webgis.deploy.exe

Liegen ZIP-Dateien im ``download`` Verzeichnis, werden die verschiedenen Versionen angezeigt:

.. code-block:: text

    Choose a version
    0 ... 7.25.701
    Input version index [0]:

Die neueste Version bekommt den Index ``0``.

.. note::

   Alle Werte, die über das ``webgis.deploy`` eingegeben werden, müssen bei späteren
   Aufrufen nicht mehr eingegeben werden. Stattdessen werden diese Werte mit einer
   Indexnummer angezeigt. Man muss dann nur noch die entsprechende Nummer eingeben,
   oder es reicht einfach, ``ENTER`` zu drücken, wenn der gewünschte Index der
   vorgeschlagene Wert ist, z.B. ``Input version index [0]`` => ``ENTER`` => Version mit
   Index ``0``.

Das Deployment-Tool fragt hier noch einmal nach, ob tatsächlich die gewählte Version mit dem Profil deployed werden sollte:

.. code-block:: text

    Deploy version 7.25.701 to profile local
    Do you want to continue? Y/N [Y]

Wenn man ein Profil (hier ``local``) das erste Mal publiziert, müssen noch einige 
Werte angegeben werden. Möchte man den Standardwert verwenden, reicht es, die Frage
mit ``ENTER`` zu bestätigen.

.. code-block:: text

    Company [my-company]: foo
    Target installation path [C:\apps\webgis]:
    Repsitory path [C:\apps\webgis/local/webgis-repository]:
    Api online url [http://localhost:5001]:
    Api internal url [http://localhost:5001]:
    Portal online url [http://localhost:5002]:
    Portal internal url [http://localhost:5002]:

.. todo:
    
    Hier noch die fehlenden Beispiele einfügen

* **Zielpfad der Installation:** Der Pfad, in dem WebGIS installiert werden sollte.
  Unter diesem Verzeichnis legt das Deployment-Werkzeug noch einen Ordner mit dem Profilnamen
  und der Version an. Hier würde die App unter ``C:\apps\webgis\local\7.25.701``
  installiert werden.

* **Repository-Pfad:** Im Repository-Pfad werden unterschiedliche Dateien gespeichert, die
  für das Funktionieren der Software notwendig sind, beispielsweise der CMS Baum, Drucklayouts, etc. 
  Der Repository-Ordner wird normalerweise im Verzeichnis
  des Profils (hier: ``C:\apps\webgis\local``) angelegt. Da der Ordner nicht im *Versions*-
  Ordner liegt, kann er von einer neu installierten Version gleich mit verwendet werden. Wichtig ist,
  dass unterschiedliche Profile ihr eigenes Repository-Verzeichnis verwenden.

* **WebGIS API Online-URL:** Eine URL, unter der der *webgis-api* zugänglich sein wird, 
  zB https://my-server.com/webgis-api.
  Möchte man das ``local`` Profil testen und die Programme nur lokal ausführen, erfolgt das
  in der Regel über http://localhost:5001. Wird WebGIS als Anwendung im IIS betrieben, muss hier 
  die Url eingegeben werden, mit der die WebGIS API über den Browser erreichbar ist.
  
* **WebGIS API Internal-URL:** *WebGIS API* und *WebGIS Portal* müssen miteinander Kommunizieren können.
  Dazu muss hier eine Url angeführt werden, unter der die *WebGIS Portal* Anwendung auf die API direkt 
  zugreifen kann. Die sollte ohne eine notwendige Authentifizierung erfolgen. Der einfachste Weg ist hier auch 
  unter einer produktiv Umgebung einen ``localhost`` Pfad anzugeben, zB http://localhost/webgis-api oder 
  für das ``local`` Profil den vorgeschlagen Wert http://localhost:5001

* **WebGIS Portal Online-URL:** Hier muss die Url eingegeben werden, unter der das *WebGIS Portal* aufgerufen 
  wird. Also beispielsweise https://my-server.com/webgis-api.
  Für das ``local`` Profil kann wieder der vorgeschlagene Wert http://localhost:5002 übernommen werden.

* **WebGIS Portal Internal-URL:** Gleich wie oben bei der *WebGIS API* muss hier eine Url angeführt werden,
  mit der die *WebGIS API* Anwendung direkt auf die *WebGIS Portal* Anwendung zugreifen kann, zB
  http://localhost/webgis-api. Für das ``local`` Profil kann der vorgeschlagene Wert übernommen werden.

.. note::

  Die hier festgelegten Werte werden in der ``_deploy_repository\profiles\{profil}\deploy-model.json``
  Datei abgelegt und können dort auch nachträglich geändert werden.

Im letzten Schritt muss noch angegeben werden, welche Komponenten von WebGIS installiert werden sollte.
Theoretisch können alle Komponenten (*WebGIS API*, *WebGIS Portal* und *WebGIS CMS*) extra installiert werden.
Für die erste Installation kann man hier einmal alle Optionen mit YES [Y] beantworten.

.. code-block:: text

  Do you want to deploy WebGIS API? Y/N [Y]
  Do you want to deploy WebGIS Portal? Y/N [Y]
  Do you want to deploy WebGIS CMS? Y/N [Y]

.. note::

   Möchte man WebGIS in Internet Anbieten braucht man in der Regel *WebGIS API* und *WebGIS Portal*.
   Das *WebGIS CMS* ist nur für die Konfiguration durch einen Administrator notwendig und soll nicht 
   öffentlich zugänglich sein. Idealerweise installiert man das *WebGIS CMS* nur *local* oder im *Intranet* 
   für eine *Test-Instanz*. Dort erfolgt die Administration durch den Administrator. Die Konfiguration vor 
   von diese Instanz dann auf alle anderen Instanzen verteilt. 

Danach startet der Deploy-Vorgang:


.. code-block:: text

    ************************************************************************************************************************

    Create a new webgis repositiry C:\apps\webgis/local/webgis-repository

    ************************************************************************************************************************

    ...succeeded 71 items created
    ...succeeded 0 items created
    ...succeeded 167 items created

    Deploy version 7.25.701
    Deploy WebGIS API:
    ...succeeded 6659 items created
    Deploy WebGIS Portal:
    ...succeeded 951 items created
    Deploy WebGIS CMS:
    ...succeeded 1670 items created
    Deploy WebGIS Scripts:
    ...succeeded 4 items created
    Deploy WebGIS Scripts:
    ...succeeded 4 items created
    Copy root files
    ...succeeded 2 items created
    Append keys.config
    Overrides
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\api.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\application-security.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\portal.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\cms.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\datalinq.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\settings.config
    ...succeeded 4 items created/overridden
    Create Custom CSS
    Build default.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\default.css not exits
    Build portal.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\portal.css not exits


    ########################################################################################################################

    Deploy succeeded

    ########################################################################################################################

    Press ENTER to quit...

Es werden sowohl *webgis-portal*, *webgis-api* als auch *webgis-cms* deployed. Nach dem Entpacken der ZIP-Dateien
werden benutzerspezifische Dateien aus dem Verzeichnis ``_deploy_repository\profiles\{profile}\webgis-[api|cms|portal]\override``
in das jeweilige Applikationsverzeichnis kopiert.
Hierbei wird die Konfiguration aus dem Installationspaket mit der Konfiguration aus dem
aktuellen Profil überschrieben.

.. note::

   In die *Override*-Verzeichnisse können beliebige Dateien kopiert werden, die zusätzlich
   in die Applikationsverzeichnisse kopiert oder überschrieben werden sollen, zB Logos, etc.
   Konfigurationsdateien sollten nie direkt im Applikationsverzeichnis geändert
   werden, sondern immer für die jeweilige Applikation im 
   ``_deploy_repository\profiles\{profile}\webgis-[api|cms|portal]\override`` Verzeichnis.
   Damit wird sichergestellt, dass Änderungen
   an der Konfiguration auch beim nächsten Update eines Profils wieder kopiert werden.

Aktuelle Konfiguration ändern
-----------------------------

Fügt man Änderungen in der Konfiguration durch (z.B. ``api.config``), erfolgt dies im *override*
Verzeichnis. Danach führt man erneut ``webgis.deploy.exe`` aus und erhält folgende Meldung:

.. code-block:: text

    ******************************************
    *                                        *
    *      WebGIS.Deploy Tool 7.25.701      *
    *                                        *
    ******************************************
    Work-Directory: C:\deploy\webgis
    Choose a profile or create a new by enter an unique name, eg. production, staging, test
    0 ... local
    Input profile index [0]:

    Do you want to download latetest version from GitHub? Y/N [Y]
    Download not implementet! Comming soon. Please download laytest Versions manually...

    Choose a version
    0 ... 7.25.701
    Input version index [0]:

    Deploy version 7.25.701 to profile local
    Do you want to continue? Y/N [Y]
    Company: foo
    Target installation path: C:\apps\webgis
    Repsitory path: C:\apps\webgis/local/webgis-repository
    Api online url: http://localhost:5001
    Api internal url: http://localhost:5001
    Portal online url: http://localhost:5002
    Portal internal url: http://localhost:5002

    Deploy version 7.25.701


    ***********************************************************************************************************************************************************************************

    Warning: version already deployed

    ***********************************************************************************************************************************************************************************

    Append keys.config
    Overrides
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\api.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\application-security.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\portal.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\cms.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\datalinq.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\settings.config
    ...succeeded 4 items created/overridden
    Create Custom CSS
    Build default.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\default.css not exits
    Build portal.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\portal.css not exits


    ###################################################################################################################################################################################

    Deploy succeeded

    ###################################################################################################################################################################################

    Press ENTER to quit...


Es erscheint die Warnung, dass diese Version bereits deployed wurde. Aus den ZIP-Dateien werden keine 
Daten kopiert. Durchgeführt werden nur die *Overrides* und Änderungen an den Style ``default.css`` und
``portal.css``

Styling der Anwendungen 
-----------------------

Für das Styling der Anwendungen sind hauptsächlich zwei *CSS Dateien* verantwortlich:

* ``default.css`` liegt im ``webgis-api/wwwroot/content/...`` Verzeichnis. Hier werden alle Styles für 
  den WebGIS Karten Viewer festgelegt.

* ``portal.css`` liegt im ``webgis-portal/wwwroot/content/...`` Verzeichnis. Hier werden die Styles für 
  die Portalseiten (Einstiegsseite mit den Kartensammlungen) festgelegt.

.. note::

  Diese Daten sollte nie direkt geändert werden. Da WebGIS ständig weiterentwickelt wird ändern sich diese 
  Dateien mit jeder Version. Überschreibt man diese Dateien eigenständig können sie Dinge verloren gehen
  und neue Features nicht zugänglich sein. 

  Möchte man Styles ändern, sollte das unbedingt nach den hier gezeigten Methoden erfolgen.

Zum Anpassen von Styles (zB Farben) wird von ``webgis.deploy`` Tool unter 
``_deploy_repository\profiles\{profile}`` ein Ordner ``css-modify`` angelegt. Darunter gibt es für jede 
der beiden *CSS Dateien* weiter Unterordner und Dateien:

.. code-block:: text

    C:\deploy\webgis\_deploy_repository\profiles\{profile}>
    .
    ├── css-modify
        └── default.css
        |   └── modify.json
        |   └── append.css
        └── portal.css
            └── modify.json
            └── append.css

* **modify.json** ist eine Datei, in der Styles durch simple Textersetzung geändert werden können.
  Solche Ersetzungen eigenen sich besonders gut für ändern der CI (Corporate Identity) Farben:

  .. code-block:: json

  {
    "mode": "shrink",
    "modifiers": [
      {
         "pattern": "#b5dbad",  // CI Color 
         "replace": "#ccc"
      },
      {
         "pattern": "#82C828",  // CI Color (Button Borders, etc) 
         "replace": "#aaa"
      }
    ]
  }

 Hier wird jeweils ein ``pattern`` (aktuelle CI Farben von WebGIS) durch einen anderen Wert ``replace`` ersetzt.
 Mit ``mode=shrink`` wird angegeben, dass die neu erstellte Datei nur die notwendigen Eigenschaften 
 der geänderten Styles übernimmt (empfohlen).

* **append.css** Hierbei handelt es sich um eine *CSS Datei*, mit der beliebige Styles Klassen aus den 
  Original Dateien überschrieben werden, Beispielsweise eine andere Schriftart. 

Werden an diesen Dateien Änderungen vorgenommen, kann das ``webgis.deploy`` Tool wieder auf eine 
bestehende *WebGIS Instanz* angewendet werden. Die aktualisierten *CSS Dateien* werden so an die richtige
Stelle verteilt.

.. note::

  Die originalen *CSS Dateien* werden nie überschrieben. Stattdessen werden zusätzlich *CSS Dateien* 
  angelegt in im Browser immer zu einem späteren Zeitpunkt als das Original geladen werden.
  Die Styles werden damit *nur* überschrieben. Daher ist es wichtig auch in der **append.css** nur jene 
  Eigenschaften von den gewünschten Klassen anzuführen, die auch wirklich geändert werden sollten! 


Update automatisieren
---------------------

Zum automatisieren von Updates kann das ``webgis.deploy`` mit Parametern aufgerufen.
Der Parameter ``--help`` gibt aus, welche Parameter möglich sind:

.. code-block:: text

  .\webgis.deploy.exe --help
   ******************************************
   *                                        *
   *      WebGIS.Deploy Tool 7.25.1001      *
   *                                        *
   ******************************************
   Work-Directory: C:\deploy\webgis
   usage: webgis.deploy [options]

   Options:
     -h,       --help            Show this help message and exit
     -p,       --profile         Choose a profile
     -d,       --download-latest Download latest version
     -v,       --version         Choose a version, --version latest ... latest version
     -cms,     --deploy-cms      Deploy WebGis CMS
     -portal,  --deploy-portal   Deploy WebGIS Portal
     -api,     --deploy-api      Deploy WebGIS API

   Examples:
     webgis.deploy -p production -v latest --download-latest --deploy-cms --deploy-portal --deploy-api