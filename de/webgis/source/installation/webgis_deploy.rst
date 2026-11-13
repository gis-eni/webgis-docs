.. _deploy:

Installation mit webgis.deploy 
===============================

Die Installation erfolgt über das Kommandozeilenprogramm webgis.deploy. Dieses Tool erledigt folgende Aufgaben:

- Neuinstallation von webgis-portal, webgis-api und webgis-cms
- Verwaltung von Deploy-Profilen (z.B. local, test, staging, production)
- Verteilung von Änderungen an der Konfiguration (z.B. api.config, cms.config, portal.config)
- Verteilung von Änderungen am Styling (default.css, portal.css)

Vorbereitung
------------

Das Deploymenttool sowie andere Pakete können unter *Releases* aus dem GitHub Repository https://github.com/e-netze/webgis/releases heruntergeladen werden.

Voraussetzung ist eine Installation der .NET App Runtime 10.0.x.

Microsoft bietet für die Ausführung von .NET-Anwendungen zwei Hauptvarianten der Runtime an:

1. **.NET Runtime (ohne IIS-Unterstützung):**  
   Diese Version enthält ausschließlich die notwendige Laufzeitumgebung, um .NET-Anwendungen als eigenständige Prozesse auszuführen – beispielsweise als Windows-Dienst oder in Containern. Sie eignet sich für Szenarien, in denen kein IIS verwendet wird.

2. **.NET Hosting Bundle (mit IIS-Unterstützung):**  
   Diese Variante enthält zusätzlich die ASP.NET Core Module für die Integration mit dem Internet Information Services (IIS). Dadurch können ASP.NET Core-Anwendungen direkt über den IIS bereitgestellt werden. Diese Version ist optimal für die Nutzung in Windows-Server-Umgebungen mit IIS.

.. raw:: html

   <p><a href="https://dotnet.microsoft.com/en-us/download/dotnet/10.0" target="_blank">Download .NET 10.0 Runtime</a></p>

Das *Deploy Tool* ist eine einzelne Datei (``webgis.deploy.exe`` unter Windows, ``webgis.deploy`` unter Linux)
und verwendet die installierte .NET Runtime.

**Windows:**

Unter Windows kann das Programm beispielsweise nach ``C:\deploy\webgis`` kopiert werden.
Danach kann dann die EXE-Datei einfach ausgeführt werden. 

**Linux:**

Unter Linux kann das Programm beispielsweise nach ``/opt/deploy/webgis`` kopiert werden.
Danach muss die Datei ausführbar gemacht werden und kann gestartet werden:

.. code-block:: bash

    chmod +x webgis.deploy
    ./webgis.deploy

.. note::

   Die nachfolgende Beschreibung erfolgt auf einem Windows-System. Unter Linux sollte die Installation
   aber aus dem Aufruf des *Deploy Tools* ähnlich erfolgen.

.. _deploy-console-ui:

Bedienung
---------

.. versionchanged:: 9.26.4502
   Das *Deploy Tool* hat eine neue Konsolenoberfläche mit Auswahllisten, Fortschrittsbalken, Farben und Symbolen.

* **Auswahllisten** (Profil, Version): Mit den Pfeiltasten ``↑`` / ``↓`` auswählen und mit ``ENTER`` bestätigen.
* **Mehrfachauswahl** (Komponenten): Mit ``LEERTASTE`` einzelne Einträge an- bzw. abwählen und mit ``ENTER`` bestätigen.
* **Ja/Nein-Fragen**: ``y`` oder ``n`` eingeben. Mit ``ENTER`` wird der Vorschlagswert in Klammern übernommen.
* **Eingaben**: Der Vorschlagswert steht in Klammern und wird mit ``ENTER`` übernommen.

Die Ausgabe ist in Abschnitte (*Download*, *Repository*, *Deploy*, *Configure*) gegliedert.
Pro Schritt erscheint nur eine Zeile mit ``✔`` und der Anzahl der Dateien. Details wie einzelne
Dateien und Pfade werden nur mit dem Parameter ``--verbose`` ausgegeben (siehe :ref:`deploy-automate`).

.. note::

   Für die korrekte Darstellung von Farben und Symbolen sollte ein modernes Terminal verwendet werden
   (z.B. *Windows Terminal*). Wird die Ausgabe umgeleitet (z.B. in eine Datei), stellt das Programm
   keine Fragen und gibt keine Farben aus.

Neue Version Ausliefern
-------------------------------------------

Wenn man das Programm zum ersten Mal startet, muss zunächst ein Profil angelegt werden.
Das Profil kann beispielsweise ``test``, ``staging`` oder ``production`` sein und entspricht 
im Grund einer WebGIS Instanz. Da wir im ersten
Schritt *WebGIS* nur lokal testen wollen, bietet sich ein Profil mit dem Namen ``local`` 
für den Start an:


.. code-block:: text
   :emphasize-lines: 1,10

    C:\deploy\webgis\> .\webgis.deploy.exe

    ╔════════════════════════════════════╗
    ║    WebGIS.Deploy Tool 9.26.4502    ║
    ╚════════════════════════════════════╝
    Work-Directory: C:\deploy\webgis

    Choose a profile:

    > <new...>

    Enter a name for the new profile (eg. production, staging, test): local

Beim ersten Start gibt es nur den Eintrag ``<new...>``. Damit wird ein neues Profil angelegt.
Bei späteren Aufrufen werden die bestehenden Profile in der Liste angezeigt.

Im nächsten Schritt bietet das Programm an, den aktuellen Release von *GitHub* herunterzuladen.

.. code-block:: text

   Do you want to download the latest version from GitHub? [y/n] (y): y

   ── Download ───────────────────────────────────────────────
   ✔ Download webgis-win64-9.26.4502.zip (95 MB)

Während des Downloads wird ein Fortschrittsbalken angezeigt. Ist die aktuelle Version bereits im
``download`` Verzeichnis vorhanden, wird sie nicht erneut heruntergeladen.

Ist das nicht möglich, kann der letzte Release auch manuell heruntergeladen werden. 
Dazu müssen die ZIP-Dateien in das ``download`` Verzeichnis gelegt werden.

Im Beispiel also hier: ``C:\deploy\webgis\download``

.. code-block:: text

    C:\deploy\webgis\>
    .
    ├── download
    │   └── webgis-win64-9.26.4502.zip
    └── webgis.deploy.exe

Liegen ZIP-Dateien im ``download`` Verzeichnis, werden die verschiedenen Versionen angezeigt:

.. code-block:: text

    Choose a version:

    > 9.26.4502
      9.26.4301

Die neueste Version steht ganz oben und ist vorausgewählt.

.. note::

   Alle Werte, die über das ``webgis.deploy`` eingegeben werden, müssen bei späteren
   Aufrufen nicht mehr eingegeben werden. Bestehende Profile werden in der Auswahlliste
   angezeigt und können mit den Pfeiltasten ausgewählt werden.

Das Deployment-Tool zeigt eine Zusammenfassung und fragt noch einmal nach, ob tatsächlich die gewählte Version mit dem Profil deployed werden sollte:

.. code-block:: text

    ╭──────────┬───────────╮
    │ Profile  │ local     │
    │ Version  │ 9.26.4502 │
    │ Platform │ win64     │
    ╰──────────┴───────────╯
    Do you want to continue? [y/n] (y):

Wenn man ein Profil (hier ``local``) das erste Mal publiziert, müssen noch einige 
Werte angegeben werden. Möchte man den Standardwert (in Klammern) verwenden, reicht es, die Frage
mit ``ENTER`` zu bestätigen.

.. code-block:: text

    Company (my-company): foo
    Target installation path (C:\apps\webgis):
    Repsitory path (C:\apps\webgis/local/webgis-repository):
    Api online url (http://localhost:5001):
    Api internal url (http://localhost:5001):
    Portal online url (http://localhost:5002):
    Portal internal url (http://localhost:5002):

.. todo:
    
    Hier noch die fehlenden Beispiele einfügen

* **Zielpfad der Installation:** Der Pfad, in dem WebGIS installiert werden sollte.
  Unter diesem Verzeichnis legt das Deployment-Werkzeug noch einen Ordner mit dem Profilnamen
  und der Version an. Hier würde die App unter ``C:\apps\webgis\local\9.26.4502``
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
Alle Komponenten sind vorausgewählt. Mit ``LEERTASTE`` können einzelne Komponenten abgewählt werden.
Für die erste Installation kann man hier einfach mit ``ENTER`` bestätigen.

.. code-block:: text

  Select the components to deploy:

  > [X] WebGIS API
    [X] WebGIS Portal
    [X] WebGIS CMS

  (Press <space> to toggle a choice and <enter> to accept)

.. note::

   Möchte man WebGIS in Internet Anbieten braucht man in der Regel *WebGIS API* und *WebGIS Portal*.
   Das *WebGIS CMS* ist nur für die Konfiguration durch einen Administrator notwendig und soll nicht 
   öffentlich zugänglich sein. Idealerweise installiert man das *WebGIS CMS* nur *local* oder im *Intranet* 
   für eine *Test-Instanz*. Dort erfolgt die Administration durch den Administrator. Die Konfiguration vor 
   von diese Instanz dann auf alle anderen Instanzen verteilt. 

Danach startet der Deploy-Vorgang:


.. code-block:: text

    ── Repository ─────────────────────────────────────────────
    ✔ Create repository (webgis-api) (71 files)
    ✔ Create repository (webgis-portal)
    ✔ Create repository (webgis-cms) (167 files)

    ── Deploy WebGIS 9.26.4502 ────────────────────────────────
    ✔ WebGIS API (6,659 files)
    ✔ WebGIS Portal (951 files)
    ✔ WebGIS CMS (1,670 files)
    ✔ WebGIS Scripts (4 files)
    ✔ WebGIS Requirements (4 files)
    ✔ Root files (2 files)

    ── Configure ──────────────────────────────────────────────
    ✔ Security keys
    ✔ Overrides webgis-api (2 files)
      webgis-api
      └── _config
          ├── api.config
          └── application-security.config
    ✔ Overrides webgis-portal (2 files)
      webgis-portal
      └── _config
          ├── application-security.config
          └── portal.config
    ✔ Overrides webgis-cms (4 files)
      webgis-cms
      └── _config
          ├── application-security.config
          ├── cms.config
          ├── datalinq.config
          └── settings.config
    ✔ Custom CSS (0 files)

    ╭─ ✔ WebGIS 9.26.4502 deployed ──────────────────────────╮
    │                                                        │
    │  Profile       local                                   │
    │  Components    API, Portal, CMS                        │
    │  Installation  C:\apps\webgis\local\9.26.4502          │
    │  Repository    C:\apps\webgis/local/webgis-repository  │
    │  Duration      1:28 min                                │
    │                                                        │
    ╰────────────────────────────────────────────────────────╯

    Press ENTER to quit...

Während des Entpackens wird für jeden Schritt ein Fortschrittsbalken angezeigt.
Es werden sowohl *webgis-portal*, *webgis-api* als auch *webgis-cms* deployed. Nach dem Entpacken der ZIP-Dateien
werden benutzerspezifische Dateien aus dem Verzeichnis ``_deploy_repository\profiles\{profile}\webgis-[api|cms|portal]\override``
in das jeweilige Applikationsverzeichnis kopiert.
Hierbei wird die Konfiguration aus dem Installationspaket mit der Konfiguration aus dem
aktuellen Profil überschrieben.

.. _deploy-override-tree:

Unter jeder *Overrides*-Zeile wird als Baum angezeigt, welche Dateien kopiert wurden. Die Pfade sind
relativ zum jeweiligen Applikationsverzeichnis (``webgis-api``, ``webgis-portal``, ``webgis-cms``),
also so, wie die Dateien im Ziel abgelegt wurden.

.. versionadded:: 9.26.4502

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
Verzeichnis. Danach führt man erneut ``webgis.deploy.exe`` aus, wählt das bestehende Profil und die Version
und erhält folgende Ausgabe:

.. code-block:: text

    ╭──────────┬───────────╮
    │ Profile  │ local     │
    │ Version  │ 9.26.4502 │
    │ Platform │ win64     │
    ╰──────────┴───────────╯
    Do you want to continue? [y/n] (y): y
    Company: foo
    Target installation path: C:\apps\webgis
    Repsitory path: C:\apps\webgis/local/webgis-repository
    Api online url: http://localhost:5001
    Api internal url: http://localhost:5001
    Portal online url: http://localhost:5002
    Portal internal url: http://localhost:5002

    ── Deploy WebGIS 9.26.4502 ────────────────────────────────
    ⚠ Version already deployed, files are not extracted again

    ── Configure ──────────────────────────────────────────────
    ✔ Security keys
    ✔ Overrides webgis-api (2 files)
      webgis-api
      └── _config
          ├── api.config
          └── application-security.config
    ...
    ✔ Custom CSS (0 files)

    ╭─ ✔ WebGIS 9.26.4502 deployed ──────────────────────────╮
    │  ...                                                   │
    ╰────────────────────────────────────────────────────────╯

Es erscheint die Warnung, dass diese Version bereits deployed wurde. Aus den ZIP-Dateien werden keine 
Daten kopiert. Durchgeführt werden nur die *Overrides* und Änderungen an den Style ``default.css`` und
``portal.css``

Styling der Anwendungen 
------------------------

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
        |   └── modify.json
        |   └── append.css
        └── site.css
            └── modify.json
            └── append.css

* **modify.json** ist eine Datei, in der Styles durch simple Textersetzung geändert werden können.
  Solche Ersetzungen eigenen sich besonders gut für ändern der CI (Corporate Identity) Farben:

  .. code-block:: json

    {
      "mode": "shrink",
      "modifiers": [
        {
          "pattern": "#82C828",  // --webgis-brand-primary (CI Color)
          "replace": "#ccc"
        }
        /*,{
          "pattern": "#ccc",  // optional weitere Farb-Codes
          "replace": "#aaa"
        }*/
      ]
    }

 Hier wird jeweils ein ``pattern`` (aktuelle CI Farben von WebGIS) durch einen anderen Wert ``replace`` ersetzt.
 Mit ``mode=shrink`` wird angegeben, dass die neu erstellte Datei nur die notwendigen Eigenschaften 
 der geänderten Styles übernimmt (empfohlen).

* **append.css** Hierbei handelt es sich um eine *CSS Datei*, mit der beliebige Styles Klassen aus den 
  Original Dateien überschrieben werden, Beispielsweise eine andere ``root:`` Variablen:

.. code-block:: css

    // site.css
    :root {
        --webgis-brand-primary: #ccc;
        --webgis-brand-primary-light: #eee;
        --webgis-brand-primary-light-text-color: #333;
        --webgis-brand-logo: url(https://my-server.com/webgis-repository/content/companies/foo/img/logo.png);
    } 

    // default.css
    .webgis-container, body {
        --webgis-brand-primary: #ccc;
        /* ... */
    }

Werden an diesen Dateien Änderungen vorgenommen, kann das ``webgis.deploy`` Tool wieder auf eine 
bestehende *WebGIS Instanz* angewendet werden. Die aktualisierten *CSS Dateien* werden so an die richtige
Stelle verteilt.

Eine genauere Beschreibung der einzelnen *CSS Dateien* und deren Geltungsbereich, Variablen, etc. ist in der :doc:`../config/css-styling/index` Dokumentation zu finden.

.. note::

  Die originalen *CSS Dateien* werden nie überschrieben. Stattdessen werden zusätzlich *CSS Dateien* 
  angelegt in im Browser immer zu einem späteren Zeitpunkt als das Original geladen werden.
  Die Styles werden damit *nur* überschrieben. Daher ist es wichtig auch in der **append.css** nur jene 
  Eigenschaften von den gewünschten Klassen anzuführen, die auch wirklich geändert werden sollten! 

.. note::

  Für die Anpassung der Styles (Farben) von Viewer und Portalseiten ist die ``default.css`` verantwortlich.

.. note::

  Anpassungen und der ``site.css`` betreffen die Standardwerte für alle WebGIS Anwendungen. Hier geht es hauptsächlich
  um die Anpassung der CI Farben für Login und Admin Seiten.


.. _deploy-automate:

Update automatisieren
---------------------

Zum automatisieren von Updates kann das ``webgis.deploy`` mit Parametern aufgerufen.
Der Parameter ``--help`` gibt aus, welche Parameter möglich sind:

.. code-block:: text

  .\webgis.deploy.exe --help

  usage: webgis.deploy [options]

  Options:
  -h, --help                Show this help message and exit
  -p, --profile             Choose a profile (runs without further questions)
  -d, --download-latest     Download latest version
  -v, --version             Choose a version, --version latest ... latest version
  --cms, --deploy-cms       Deploy WebGIS CMS
  --portal, --deploy-portal Deploy WebGIS Portal
  --api, --deploy-api       Deploy WebGIS API
  --portable                Only list/use portable (self-contained) ZIPs, skip GitHub download
  --non-interactive         Never prompt (also automatic if input/output is redirected)
  --no-color                Disable colors and ANSI sequences
  --verbose                 Show detailed output (files, paths, ...)

  Examples:
    webgis.deploy -p production -v latest --download-latest --deploy-cms --deploy-portal --deploy-api

Wird ein Profil mit ``-p`` angegeben, entfallen die Bestätigung und die Auswahl der Komponenten. Es werden nur die
Komponenten deployed, die über ``--api``, ``--portal`` bzw. ``--cms`` angegeben werden.
Für einen Aufruf ganz ohne Rückfragen (z.B. in Skripten) zusätzlich ``--non-interactive`` angeben.

.. versionadded:: 9.26.4502
   Die Parameter ``--non-interactive``, ``--no-color`` und ``--verbose``.

* ``--non-interactive``: Das Programm stellt keine Fragen. Fehlt ein notwendiger Wert (z.B. Profil oder
  Version), bricht das Programm mit einem Fehler ab. Für Werte des Profils, die noch nicht gesetzt sind,
  werden die Standardwerte verwendet. Dieser Modus wird automatisch verwendet, wenn Ein- oder Ausgabe
  umgeleitet werden (z.B. in Skripten oder CI-Pipelines).
* ``--no-color``: Keine Farben und Steuerzeichen in der Ausgabe, z.B. für Logdateien.
* ``--verbose``: Gibt zusätzlich Details aus, z.B. einzelne kopierte Dateien und Pfade.

.. versionchanged:: 9.26.4502
   Im nicht-interaktiven Modus (``--non-interactive`` oder umgeleitete Ein-/Ausgabe) wird die neueste Version
   nur noch von *GitHub* heruntergeladen, wenn ``-d`` / ``--download-latest`` angegeben ist.

Der Rückgabewert (*Exit Code*) ist ``0``, wenn das Deployment erfolgreich war, und ``1`` bei einem Fehler.