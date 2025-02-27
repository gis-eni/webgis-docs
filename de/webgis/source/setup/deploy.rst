.. _deploy:

Installation
============

Die Installation erfolgt über das Kommandozeilenprogramm webgis.deploy. Dieses Tool erledigt folgende Aufgaben:

- Neuinstallation von webgis-portal, webgis-api und webgis-cms
- Verwaltung von Deploy-Profilen (z.B. local, test, staging, production)
- Verteilung von Änderungen an der Konfiguration (z.B. deploy-model.json, api.config, cms.config, portal.config)

Vorbereitung
------------

Das Deploymenttool sowie andere Pakete können unter *Releases* aus dem GitHub Repository https://github.com/gis-eni/webgis/releases heruntergeladen werden.

Voraussetzung ist eine Installation der .NET App Runtime 8.0.x.

Microsoft bietet für die Ausführung von .NET-Anwendungen zwei Hauptvarianten der Runtime an:

1. **.NET Runtime (ohne IIS-Unterstützung):**  
   Diese Version enthält ausschließlich die notwendige Laufzeitumgebung, um .NET-Anwendungen als eigenständige Prozesse auszuführen – beispielsweise als Windows-Dienst oder in Containern. Sie eignet sich für Szenarien, in denen kein IIS verwendet wird.

2. **.NET Hosting Bundle (mit IIS-Unterstützung):**  
   Diese Variante enthält zusätzlich das ASP.NET Core Module für die Integration mit dem Internet Information Services (IIS). Dadurch können ASP.NET Core-Anwendungen direkt über den IIS bereitgestellt werden. Diese Version ist optimal für die Nutzung in Windows-Server-Umgebungen mit IIS.

.. raw:: html

   <p><a href="https://dotnet.microsoft.com/en-us/download/dotnet/8.0" target="_blank">Download .NET 8.0 Runtime</a></p>


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
Das Profil kann beispielsweise ``test``, ``staging`` oder ``production`` sein. Da wir im ersten
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
    │   └── webgis-7.25.701.zip
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

Das Deployment-Tool fägt hier noch einmal nach, ob tatsächlich die gewählte Version mit dem Profil deployed werden sollte:

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
  für das Funktionieren der Software notwendig sind, beispielsweise **TODO**. Der Repository-Ordner wird normalerweise im Verzeichnis
  des Profils (hier: ``C:\apps\webgis\local``) angelegt. Da der Ordner nicht im *Versions*-
  Ordner liegt, kann er von einer neu installierten Version gleich mit verwendet werden. Wichtig ist,
  dass unterschiedliche Profile ihr eigenes Repository-Verzeichnis verwenden.

* **WebGIS API Online-URL:** Eine URL, unter der der *webgis-api* zugänglich sein wird.
  Möchte man das ``local`` Profil testen und die Programme nur lokal ausführen, erfolgt das
  in der Regel über http://localhost:5001. **TODO: Der Vorteil, diesen Wert hier festzulegen, ist, dass später
  in der *gView.WebApps* App eine zusätzliche Kachel zum Aufruf des *gView.Servers* angeboten wird. Das
  erleichtert die Administration. Ohne diese URL würden nur die Kacheln für *gView.Carto* und
  *gView.Explorer* angezeigt werden.**

* **WebGIS API Internal-URL:** Eine URL, unter der der *webgis-api* zugänglich sein wird.
  Möchte man das ``local`` Profil testen und die Programme nur lokal ausführen, erfolgt das
  in der Regel über http://localhost:5001. **TODO: Der Vorteil, diesen Wert hier festzulegen, ist, dass später
  in der *gView.WebApps* App eine zusätzliche Kachel zum Aufruf des *gView.Servers* angeboten wird. Das
  erleichtert die Administration. Ohne diese URL würden nur die Kacheln für *gView.Carto* und
  *gView.Explorer* angezeigt werden.**

* **WebGIS Portal Online-URL:**

* **WebGIS Portal Internal-URL:**

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
   in die Applikationsverzeichnisse kopiert oder überschrieben werden sollen.
   Konfigurationsdateien sollten nie direkt im Applikationsverzeichnis (Deploy-Verzeichnis) geändert
   werden, sondern immer im *Override*-Verzeichnis. Damit wird sichergestellt, dass Änderungen
   an der Konfiguration auch beim nächsten Update eines Profils wieder kopiert werden.

Aktuelle Konfiguration ändern
-----------------------------

Fügt man Änderungen in der Konfiguration durch (z.B. ``api.config``), erfolgt dies im *Override*
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
Daten kopiert. Durchgeführt werden nur die *Overrides*.


TODOs
-----

Hier sind alle noch offenen Aufgaben aufgelistet:

.. todolist::

Layout übernommen von https://github.com/jugstalt/docs-gviewonline/blob/master/de/source/setup/index.rst


https://docs.webgiscloud.com/cloud/selfhosting/install/windows/index.html

https://docs.webgiscloud.com/cloud/selfhosting/install/iis/index.html


Anwendungen ausführten

Vorlage: https://docs.gviewonline.com/de/setup/run.html