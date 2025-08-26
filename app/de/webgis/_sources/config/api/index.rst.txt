=================================
Konfiguration der API-Applikation
=================================

Datei ``_config/api.config``
============================

Falls diese Datei nicht existiert, wird sie beim ersten Start der API mit Standardwerten automatisch angelegt. In diesem Abschnitt wird gezeigt, wie sie für den **produktiven Betrieb** angepasst werden kann.

Die Datei ist eine **XML-Konfigurationsdatei**, die verschiedene **Schlüssel-Werte-Paare** enthält.

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8" ?>
    <configuration>
        <appSettings>

            <!-- App Roles -->
            <add key="app-roles" value="all" />

            ...

        </appSettings>
    </configuration>


Im Folgenden findet sich eine Übersicht der wichtigsten Konfigurationsparameter.

Abschnitt ``CMS``
-----------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``cmspath_default``, ``cmspath_custom``
     - Pfade zu den CMS-Dateien, die in die API eingebunden werden. Die Namen der CMS-Dateien sollten nachträglich nicht mehr geändert werden, da sie zur eindeutigen Identifikation beim Erstellen von Karten verwendet werden.
   * - ``cmsgdischema_default``
     - Standardmäßig verwendetes GDI-Schema aus dem CMS. Falls leer, wird kein spezifisches Schema vorgegeben.
   * - ``outputPath``
     - Pfad zum Output-Verzeichnis, in dem Bilder und generierte Dateien abgelegt werden. Die Webapplikation sollte darauf zugreifen und Schreibrechte besitzen.
   * - ``outputUrl``
     - URL des Output-Verzeichnisses, die für den Anwender erreichbar sein muss. Dies kann ein virtuelles Verzeichnis sein, sollte aber nicht über den Browser aufgelistet werden können.
   * - ``server-side-configuration-path``
     - Pfad zur serverseitigen Konfiguration der API. In diesem Verzeichnis befinden sich Konfigurationsdateien für die komplette Instanz, einschließlich ``etc`` (z. B. Drucklayouts) und ``config``.

Abschnitt ``Proj4 Database``
----------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``p4database``
     - Connection-String zu einer Datenbank, die Projektionsinformationen enthält (Tabelle ``P4``). Hier kann die gleiche Datenbank angegeben werden, die auch von WebGIS genutzt wird. Dieser Schlüssel wird nur aus Kompatibilitätsgründen zu WebGIS bereitgestellt. Möchte man die Standard-Projektionsinformationen verwenden, reicht es, ``value="#"`` anzugeben.

Abschnitt ``Cache Datenbank``
-----------------------------

In dieser Datenbank werden die **Sessions** gespeichert. Sie muss die Tabelle ``webgis_cache`` enthalten (siehe unten). Wird zusätzlich die **Portal-Anwendung** genutzt, müssen beide Systeme denselben **Session-Cache** verwenden. Alternativ kann der Cache im **Dateisystem** abgelegt werden, wodurch keine Datenbank-Tabelle erforderlich ist.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``cache-provider``
     - Bestimmt, ob die Cache-Datenbank als **Datenbank** (``db``) oder im **Dateisystem** (``fs``) abgelegt wird.
   * - ``cache-connectionstring``
     - Connection-String zur Datenbank oder Pfad im Dateisystem.

Abschnitt ``Cache Aside``
------------------------------------

Um die Anzahl der Zugriffe auf die **Cache-Datenbank** zu reduzieren (da bei jedem API-Request darauf zugegriffen wird), empfiehlt es sich für **hoch ausgelastete Instanzen**, einen **zusätzlichen Cache** neben der Datenbank einzurichten. Dadurch werden schnelle Zugriffe ermöglicht.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``cache-aside-provider``
     - Definiert den verwendeten **Side-Cache**:

       - ``redis``: Redis-Cache verwenden (ermöglicht die gemeinsame Nutzung durch mehrere Instanzen).  
       - ``InApp``: InApp-Cache verwenden (Daten werden direkt im Speicher der Anwendung gehalten).  
       - ``""``: Kein Cache-Aside aktiv.
   * - ``cache-aside-connectionstring``
     - Der zugehörige **Connection-String**. 

       - Für **Redis** z. B. ``localhost:6379``.  
       - Für **InApp** wird hier die Zeit in Sekunden angegeben, für die ein Wert im Side-Cache gehalten werden soll (z. B. ``3600`` für eine Stunde).

Abschnitt ``Subscriber Datenbank``
----------------------------------

Subscriber sind Benutzer, die sich am **WebGIS-Portal** anmelden können, um Karten zu erstellen. Die Informationen dieser Benutzer können entweder in einer **Datenbank** oder vereinfacht im **Dateisystem** gespeichert werden.  
Für die Speicherung im Dateisystem kann der Connection-String wie folgt angegeben werden:  
``value="fs:C:\webgis\webgis-repository\..."``

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``subscriber-db-connectionstring``
     - Connection-String zur **Subscriber-Datenbank** oder zum Speicherort im Dateisystem.
   * - ``subscriber-admins``
     - Liste von **Administrator-Subscriber-Namen**, durch Komma getrennt (z. B. ``admin``). Diese Benutzer können andere Profile verwalten (löschen, ändern usw.).

Abschnitt ``Subscriber Registration``
-------------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``allow-subscriber-login``
     - Gibt an, ob sich Subscriber in dieser Instanz anmelden können (``true`` oder ``false``).  
       Diese Option ist für geschlossene Instanzen sinnvoll, die ausschließlich von einem Administrator verwaltet werden. Dadurch wird böswilliger Zugriff auf die Konfiguration verhindert.

       Beispiel: Eine **Intranet-Instanz** könnte zur Konfiguration genutzt werden, während die **Internet-Instanz** für den Zugriff gesperrt ist. Beide Instanzen können sich den **Storage** teilen oder dieser kann zwischen ihnen kopiert werden.
   * - ``allow-register-new-subscribers``
     - Gibt an, ob sich neue Subscriber selbst für die API registrieren dürfen (``true`` oder ``false``).

       - Bei der **Erstinstallation** sollte dieser Wert auf ``true`` gesetzt werden, damit mindestens ein Administrator-Subscriber erstellt werden kann.  
       - Anschließend kann der Wert auf ``false`` gesetzt werden. Es empfiehlt sich dann, eine separate **Intranet- oder Testinstanz** der API bereitzustellen, auf die nur der Administrator Zugriff hat und über die bei Bedarf neue Subscriber angelegt werden können. Diese Instanz muss auf die gleiche **Datenbank** zugreifen.
   * - ``subscription-tools``
     - Bestimmt, welche Funktionen ein Subscriber im **Portal** erstellen darf.

       Mögliche Werte:  
       - ``clients``: Erlaubt das Erstellen von Clients.  
       - ``portal-pages``: Erlaubt das Erstellen von Portal-Seiten.  
       - ``dataLinq-endpoints``: Erlaubt das Erstellen von DataLinq-Endpunkten.


Abschnitt ``Api/Portal Url``
----------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``api-url``
     - URL der API, wie sie für den Anwender sichtbar ist.
   * - ``portal-url``
     - URL des Portals, wie es für den Anwender sichtbar ist.
   * - ``portal-internal-url``
     - Die API muss mit dem Portal kommunizieren können, z. B. um Auswahllisten für die Authentifizierung zu befüllen. Hier empfiehlt sich eine **interne URL**, falls beide Anwendungen auf demselben Server installiert sind (z. B. ``http://localhost/webgis-portal``). Wird dieser Wert nicht gesetzt, nutzt die API automatisch ``portal-url`` für interne Anfragen.

Abschnitt ``Storage``
---------------------

Benutzerprojekte, Inhalte von Portalseiten usw. werden hier gespeichert. Es handelt sich **nicht** um eine klassische Datenbank, sondern um eine **Dateisystem-basierte Speicherung** (Blobs).

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``storage-rootpath``
     - Pfad zu einem Verzeichnis, das als **Storage** verwendet wird. Das Verzeichnis kann jederzeit geändert werden, indem der Inhalt an einen anderen Speicherort kopiert wird.

       .. important::  
          Die API-Applikation benötigt **Lese- und Schreibrechte** für dieses Verzeichnis!

Abschnitt ``Marker``
--------------------

* ``default-marker-colors``
  Verwendet man dynamische Marker (empfohlen), können hier die Standardfarbwerte für die Marker definiert werden. Der Wert muss mit Beistrich getrennt aus drei Hexwerten für Füllfarbe, Umrandungsfarbe und Textfarbe bestehen, z.B.: ``82C828,b5dbad,fff``.
  
  Wie Dynamische Marker in den Viewer eingebunden werden, wird in der ``custom.js`` Beschreibung gezeigt:
 
  https://docs.webgiscloud.com/de/webgis/apps/viewer/customjs/benutzerdefmarker.html
  
  Verwendet man die ``custom-recommendtion.js``, werden dynamische Marker automatisch für Suchergebnisse verwendet.

  .. note::

     Änderung dieses Wertes werden nicht zwingend sofort sichtbar, weil Marker am Client gecached werden => Browser Cache leeren!

* ``default-text-download-encoding``
  Werden vom Anwender beispielsweise CSV Dateien heruntergeladen, muss das Encoding so eingestellt werden, dass alle enthaltenen Sonderzeichen richtig codiert werden. Der Name des *Encodings* kann hier eingestellt werden. Der Default Wert ist ``iso-8859-1`` und sollte alle deutschen Sonderzeichen berücksichtigen. Welche Werte möglich sind, ist ersichtlich, wenn man ``/admin/info`` Seite für die API aufruft. Dort wird auch angezeigt, welches *Encoding* aktuell verwendet wird.

Abschnitt ``Logging``
---------------------

.. code-block:: xml

  <!-- Logging (optional) -->
  <add key="logging-type" value="files" />  
  <!-- Pfad für das Logging: Verzeichnis muss für WebGIS Schreibrechte aufweisen -->
  <add key="Log_Path" value="C:\\apps\\webgis\\local\\webgis-repository\\logs" />   

  <add key="logging-log-performance" value="true" />
  <add key="Log_Performance_Columns" value="SESSIONID;MAPREQUESTID;CLIENTIP;DATE;TIME;MAPNAME;USERNAME;X;Y;SCALE" />
  <add key="logging-log-exceptions" value="true" />

  <add key="trace" value="true" />
  <!-- Nur für Debugging, nicht in Produktion verwenden -->
  <add key="logging-log-service-requests" value="true" />  

Das Logging kann in Dateien erfolgen (``logging-type = files``).  

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``logging-log-performance``
     - Speichert **Karten-Requests** und deren Zugriffszeiten in einer **CSV-Logdatei**.
   * - ``logging-log-exceptions``
     - Protokolliert **Exceptions**, die während der Laufzeit der **WebGIS API** auftreten.
   * - ``logging-log-service-requests``
     - Speichert **Anfragen an den Kartenserver** sowie deren Antworten.

       Diese Einstellung sollte **nur zum Debugging** verwendet werden, da sie eine **große Datenmenge** erzeugt und die **Performance** negativ beeinflussen kann.
       
       .. important::
          **Wichtig:** Die Requests werden nur geloggt, wenn zusätzlich ``trace=true`` gesetzt ist.

Werkzeug Konfiguration
----------------------

Einige Werkzeuge, die im **WebGIS Viewer** angeboten werden, benötigen eigene Konfigurationseinträge. Diese befinden sich in der ``api.config``. Damit die ``api.config`` übersichtlich bleibt, werden die Einträge über *Sections* gruppiert.  

``<section>``-Tags müssen sich innerhalb des ``<appSettings>``-Tags befinden.

Hier die Werkzeuge, für die eine eigene Konfiguration notwendig ist:

Werkzeug ``MapMarkup``
~~~~~~~~~~~~~~~~~~~~~~

Die Konfiguration für das **MapMarkup-Werkzeug** sieht folgendermaßen aus:

.. code:: xml

    <section name="tool-mapmarkup">
      <add key="allow-add-from-selection" value="true" />
      <add key="allow-add-from-selection-max-features" value="1000" />
      <add key="allow-add-from-selection-max-vertices" value="10000" />
      <add key="allow-download-from-selection" value="true" />
      <add key="default-download-epsg" value="4326" />
    </section>

.. important::

    Beim **MapMarkup (Zeichnen)** müssen alle Objekte direkt im **Client (Browser)** gerendert werden. Daher kann eine **sehr hohe Anzahl an Objekten** oder **Objekte mit vielen Vertices** (z. B. **katastergenaue Bezirksgrenzen**) zu **Leistungsproblemen** führen.  

    Es sollten daher, dem Anwendungsfall entsprechend, Einschränkungen bezüglich der Max-Werte vorgenommen werden. Besonders wichtig bei (freien) Internet Anwendungen.

Werkzeug ``Koordinaten (XY)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: xml

    <section name="tool-coordinates">
      <add key="allow-upload-max-rows" value="200" />
    </section>

Das **XY-Werkzeug** ermöglicht das **Hochladen von Koordinatenlisten**. Es kann zur **Visualisierung** oder zur **Projektion** genutzt werden, wenn die Koordinaten nach der Verarbeitung wieder heruntergeladen werden.

Zusätzlich werden zu den Koordinaten **automatisch Höhenwerte ermittelt**:

1. Koordinaten werden hochgeladen.  
2. Abhängig von der Konfiguration im ``etc``-Verzeichnis (siehe unten) werden **Höhenwerte** berechnet und als Attribute hinzugefügt.  
3. Beim **Download** werden diese Höhenwerte ebenfalls mit ausgegeben.  

Die **Anzahl der hochladbaren Koordinaten** kann über den folgenden Parameter begrenzt werden:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``allow-upload-max-rows``
     - Legt die maximale Anzahl an Zeilen fest, die über das **XY-Werkzeug** hochgeladen werden dürfen.

Werkzeug ``Drucken``
~~~~~~~~~~~~~~~~~~~~

Die Konfiguration ermöglicht die Festlegung verfügbarer **Druckqualitäten (DPI)**.

.. tip::

  Eine höhere DPI verbessert die **Lesbarkeit**, insbesondere von Texten, erhöht jedoch auch die **Dateigröße** der erzeugten PDFs und die **Serverlast**. In **öffentlichen Internetanwendungen** sollte eine **Druckauflösung über 150 DPI** vermieden werden, da sie bei großen Papierformaten die Server stark belasten kann.


Die Konfiguration in der ``api.config`` sieht folgendermaßen aus:

.. code-block:: xml

    <section name="tool-print">
        <add key="qualities-dpi" value="150:Hoch (150 dpi),120:Mittel (120 dpi),225:Sehr hoch (225 dpi)" />
        <add key="scales" value="1000000,500000,250000,100000,50000,25000,10000,5000,3000,2000,1000,500,250,100" />
        <add key="default-format" value="A4.Landscape" />
        <add key="scale-wysiwyg" value="false" />
    </section>

**Druckqualitäten und Maßstäbe**

Die einzelnen Werte werden durch **Kommas** getrennt. Jeder Eintrag besteht aus einer **DPI-Zahl (Integer)** und einer **Beschreibung**, getrennt durch einen Doppelpunkt ``:``. Im **Viewer** werden die DPI-Werte **sortiert** angezeigt (z. B. 120, 150, 225). Der erste Wert in der Liste dient als **Standardwert** und wird beim ersten Öffnen des Druckwerkzeugs vorausgewählt.

Optional können auch die Maßstäbe für den Druck festgelegt werden. Falls keine Werte angegeben sind, verwendet das System die verfügbaren **Kartenzoomstufen**.

Eine alternative Möglichkeit zur Definition von Druckmaßstäben besteht darin, diese direkt im **Drucklayout-File** festzulegen:

.. code-block:: xml

    <?xml version="1.0" encoding="iso-8859-1" ?>
    <layout scales="5000,2500,1000,500">
      ...
    </layout>

.. tip::

  Die Einstellungen im **Layout-File** haben Vorrang vor den Werten in der ``api.config`` und den Kartenmaßstäben. Es wird empfohlen, die Maßstäbe direkt im Layout-File zu definieren, da so für jedes Layout passende Maßstäbe vorgegeben werden, die der Benutzer nutzen muss.

Werkzeug ``LiveShare``
~~~~~~~~~~~~~~~~~~~~~~

Damit **LiveShare** genutzt werden kann, muss die URL des **Hubs** in der ``api.config`` angegeben werden.

.. code-block:: xml

    <section name="tool-liveshare">
      <add key="simplify-session-ids" value="true" />

      <add key="hub" value="https://liveshare.webgiscloud.com" />
      <add key="clientId" value="gültige client Id" />
      <add key="clientSecret" value="gültiges client secret" />
    </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``simplify-session-ids``
     - Wandelt die **Session-IDs** in eine **vereinfachte 9-stellige Zahl** um.
   * - ``hub``
     - URL des **LiveShare-Hubs**, über den die Echtzeit-Sitzungen verwaltet werden.
   * - ``clientId``
     - Eindeutige **Client-ID**, erforderlich, wenn der Hub nicht öffentlich zugänglich ist.
   * - ``clientSecret``
     - Geheimes **Client-Token**, erforderlich, wenn der Hub nicht öffentlich zugänglich ist.

Falls der **Hub nicht öffentlich zugänglich** ist, müssen eine **Client-ID** und ein **Client-Secret** hinterlegt werden. Diese Zugangsdaten werden vom Betreiber des Hubs bereitgestellt.

Werkzeug ``3D-Messen``
~~~~~~~~~~~~~~~~~~~~~~

Damit **3D-Messungen** funktionieren, müssen folgende Werte in der ``api.config`` konfiguriert werden:

.. code-block:: xml

  <section name="tool-threed">
    <add key="min-resolution" value="5" />
    <add key="max-resolution" value="100" />
    <add key="max-model-size" value="1500" />
    <add key="max-scale" value="100000" />
    <add key="texture-ortho-service" value="geoland_bm_of@default:0" /><!-- serviceId:layerId -->
    <add key="texture-streets-overlay-service" value="geoland_bm_ov@default:0" /><!-- serviceId:layerId -->
  </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``min-resolution``
     - Minimale **Auflösung** des 3D-Modells in **Metern**.
   * - ``max-resolution``
     - Maximale **Auflösung** des 3D-Modells in **Metern**.
   * - ``max-model-size``
     - Maximale **Modellgröße** in **Pixeln** (z. B. ``1500 x 1500``).
   * - ``max-scale``
     - **Maximaler Maßstab**, über dem kein 3D-Modell mehr erstellt wird.
   * - ``texture-ortho-service``
     - Definiert den **Dienst für Luftbild-Texturen**, bestehend aus **Dienst-CMS-ID** und **Layer-ID** im Format ``Dienst-CMS-Id : Layer-Id``.
   * - ``texture-streets-overlay-service``
     - Definiert den **Dienst für Straßenkarten-Texturen**, bestehend aus **Dienst-CMS-ID** und **Layer-ID** im Format ``Dienst-CMS-Id : Layer-Id``.


Werkzeug ``Karte speichern``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mit dem Werkzeug **Karte speichern** können Anwender die aktuelle Karte (Dienste, Sichtbarkeit, Redlining) als **Projekt** speichern. Dabei können folgende Einstellungen konfiguriert werden:

.. code-block:: xml

  <section name="tool-savemap">
    <add key="name-maxlength" value="40" />
  </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``name-maxlength``
     - Gibt an, wie viele Zeichen der **Projektname** maximal enthalten darf.  
       Das Projekt wird auf dem **Server im Dateisystem** gespeichert (inklusive Verschlüsselung).  
       Diese Einstellung verhindert, dass die **Dateinamen zu lang** werden.

Werkzeug ``Karte Laden``
~~~~~~~~~~~~~~~~~~~~~~~~

Mit dem Werkzeug **Karte Laden** können gespeicherte Karten vom Anwender erneut geöffnet werden.  

Wird eine gespeicherte Karte über die **Portalseite (Meine Projekte)** geöffnet, wird ein **Link** generiert, über den die Karte aufgerufen werden kann. Dieser Link wird in der **Adresszeile des Browsers** angezeigt und kann somit kopiert und weitergegeben werden.

Mit den folgenden Einstellungen kann festgelegt werden, wer gespeicherte Karten öffnen darf. Standardmäßig können Karten nur von dem Benutzer geöffnet werden, der sie gespeichert hat.

.. code-block:: xml

  <section name="tool-loadmap">
    <add key="allow-collaboration" value="false" />
    <add key="allow-anonymous-collaboration" value="false" />
  </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``allow-collaboration``
     - Standardmäßig können gespeicherte Karten **nur vom Ersteller** geöffnet werden.  
       Falls ein anderer Benutzer versucht, die Karte über einen Link zu öffnen, erhält er eine Fehlermeldung (*Collaboration of projects is not allowed*).  
       Um das **Teilen gespeicherter Karten** zu ermöglichen, muss diese Option auf ``true`` gesetzt werden.
   * - ``allow-anonymous-collaboration``
     - Falls ``allow-collaboration`` auf ``true`` gesetzt ist, können nur **angemeldete Benutzer** geteilte Links öffnen.  
       Sollten auch **anonyme Benutzer** Zugriff auf die Karten erhalten, muss diese Option ebenfalls auf ``true`` gesetzt werden.

.. danger:: 

  Aus Datenschutzgründen sollte das Weitergeben gespeicherter Links nicht erlaubt werden. Über einen Link kann jederzeit auf den aktuellen Stand der Karte, einschließlich **Redlining**, zugegriffen werden!

  Der empfohlene Weg zum Teilen einer Karte ist das Werkzeug **Karte teilen**. Dabei wird ein **Snapshot** der aktuellen Karte erstellt und weitergegeben. Spätere Änderungen, insbesondere am **Redlining**, sind in der geteilten Version nicht mehr sichtbar.

Werkzeug ``CMS Upload``
~~~~~~~~~~~~~~~~~~~~~~~

In der Konfiguration kann festgelegt werden, ob **CMS.xml**-Dateien von einer **WebGIS CMS**-Instanz hochgeladen werden dürfen.

.. code-block:: xml

  <section name="cms-upload-{cms-name}">
    <add key="allow" value="true" />
    <add key="client" value="cms-upload-client" />
    <add key="secret" value="my-super-secret-with-min-length-24" />
  </section>

``{cms-name}`` ist der **CMS-Name**, wie er in der ``api.config`` definiert ist. Beispiel:
  
.. code-block:: xml

  <add key="cms_my_cms" value="{path-to-cms.xml}" />

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``allow``
     - Muss auf ``true`` gesetzt sein, damit ein **Upload** erlaubt ist.
   * - ``client``
     - Definiert einen beliebigen **Client-Namen**, der für den Upload autorisiert ist. Dieser Wert muss mit dem in der ``cms.config`` im Abschnitt ``deployment`` übereinstimmen.
   * - ``secret``
     - Sicheres **Passwort** mit mindestens **24 Zeichen** zur Authentifizierung des Uploads. Der Wert muss mit dem in der ``cms.config`` im Abschnitt ``deployment`` übereinstimmen.

Werkzeug ``Karte teilen``
~~~~~~~~~~~~~~~~~~~~~~~~~

Karten können über einen **Hyperlink** geteilt werden. Dabei wird die aktuelle Karte, einschließlich **Redlining** und **Layerschaltung**, auf dem **Server gespeichert**.

Um eine unnötige Speicherung von Karten im **WebGIS Storage** zu vermeiden, haben diese Links ein **Ablaufdatum**. Der Anwender kann festlegen, wie lange ein Link gültig sein soll.  

Standardwerte: **ein Tag, eine Woche oder ein Monat**.

.. image:: img/config-tools7.png 

Falls andere Werte zur Auswahl stehen sollen, kann dies über die ``api.config`` konfiguriert werden:

.. code-block:: xml

  <section name="tool-share">
    <add key="duration" value="1:1 Tag, 7:1 Woche, 31:1 Monat, 365: 1 Jahr, 36500:Für immer" />
  </section> 

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``duration``
     - Definiert die **Gültigkeitsdauer** für geteilte Karten. Der Wert besteht aus einer **Anzahl an Tagen** (Integer) und einer **Bezeichnung**, getrennt durch ``:``.  Mehrere Werte können durch **Kommas** getrennt angegeben werden.

       Die Syntax für ``duration`` lautet: ``[Anzahl der Tage (Integer)]:[Anzeigetext], [weitere Werte]…``

Werkzeug ``Identify``
~~~~~~~~~~~~~~~~~~~~~

Mit dem **Identify-Werkzeug** können **Geo-Objekte** abgefragt werden. Klickt der Anwender auf die Karte (**Punkt-Identify**), wird innerhalb einer bestimmten **Pixel-Toleranz** nach Objekten gesucht.  
Diese Toleranz legt fest, wie groß der Bereich um den Klickpunkt ist, in dem Objekte erfasst werden.  
Sie ist notwendig, da es schwierig sein kann, ein gewünschtes **punkt- oder linienförmiges** Objekt exakt zu treffen.

Standardmäßig wird mit einer **Toleranz von ±20 Pixeln** um den Mauszeiger gesucht.  
Für **flächenhafte Objekte** kann dies unerwünscht sein. Daher kann die **Toleranz pro Geometrietyp** in der ``api.config`` angepasst werden:

.. code-block:: xml

   <section name="tool-identify">
      <add key="tolerance" value="20" />
      <add key="tolerance-for-point-layers" value="10" />
      <add key="tolerance-for-line-layers" value="5" />
      <add key="tolerance-for-polygon-layers" value="0" />

      <add key="show-layer-visibility-checkboxes" value="true" />
      
      <add key="max-vertices-for-hover-highlighting" value="0" />

      <add key="result-date-format" value="dd.MM.yyyy" />  <!-- optional -->
      <add key="result-time-format" value="HH.mm" />
      <add key="result-date-time-culture" value="de-AT" />
   </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``tolerance``
     - Allgemeine **Toleranz** in **Pixeln**, innerhalb derer nach Objekten gesucht wird.
   * - ``tolerance-for-point-layers`` *(optional)*
     - Spezifische **Toleranz** für **punktförmige Objekte**.
   * - ``tolerance-for-line-layers`` *(optional)*
     - Spezifische **Toleranz** für **linienförmige Objekte**.
   * - ``tolerance-for-polygon-layers`` *(optional)*
     - Spezifische **Toleranz** für **flächenhafte Objekte**. 
     
       .. tip::

          Wird oft auf ``0`` gesetzt, um eine exakte Auswahl zu gewährleisten.

   * - ``show-layer-visibility-checkboxes`` *(optional)*
     - Gibt an, ob im in der Liste der gefunden Themen auch eine Checkbox angezeigt wird,
       mit dem man den betroffenen Layer in der Karte ein- oder ausblenden kann.
   * - ``max-vertices-for-hover-highlighting`` *(optional)*  
     - Legt die maximale Anzahl an **Vertices** fest, die für das **Hover-Highlighting** 
       von Objekten verwendet werden. Das **Hover-Highlighting** tritt in Kraft, wenn der 
       Anwender den Mauszeiger über die Zeile in der Ergebnistabelle bewegt.
       Da hier die Geometrie des Objekts bei der Abfrage an den Client geschickt wird, 
       sollte hier ein Maximalwert gesetzt werden, um die Performance nicht zu beeinträchtigen.
       Der Standardwert ist ``1000``. Ein Wert von ``0`` deaktiviert das **Hover-Highlighting**.
       
       .. tip::
       
         Hat mindestens ein Feature in einer Abfrage mehr als die angegebene Anzahl an Vertices,
         wird das Hover-Highlighting für alle Features dieser Abfrage deaktiviert, da es ansonsten
         für den Anwender verwirrend ist, warum nur bestimmte Features hervorgehoben werden. In diesen 
         Fall muss der Anwender auf eine Zeile in der Tabelle klicken um ein Feature hervorzuheben.

   * - ``result-date-format`` *(optional)*
     - Legt das **Datumsformat** für die Ergebnisse fest. Der Standardwert ist ``dd.MM.yyyy``.
       Dieser Wert wird für alle **Datum-Felder** in den Ergebnissen verwendet.

   * - ``result-time-format`` *(optional)*
     - Legt das **Zeitformat** für die Ergebnisse fest. Der Standardwert ist ``HH.mm:ss``.
       Dieser Wert wird für alle **Zeit-Felder** in den Ergebnissen verwendet.

   * - ``result-date-time-culture`` *(optional)*
     - Legt die **Kultur** für die Datums- und Zeitformate fest. 
       Der Standard wird ist die Culture unter der die Applikation betrieben wird (Server Betriebssytem).  
       Dieser Wert beeinflusst die Formatierung von Datums- und Zeitangaben in den Ergebnissen.

       .. tip::

         Die Werte für Datums-, Uhrzeitformat und **Kultur** entsprechenden der ``C#``/``dotnet`` 
         Nomenklatur (https://learn.microsoft.com/de-de/dotnet/standard/base-types/custom-date-and-time-format-strings).

Abschnitt ``Secured Tiles``
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kartenkacheln werden immer von Client abgeholt (WMTS Dienste). Sind die Dienste allerdings geschützt, hat das den Nachteil, dass der Client auch Information über die Credentials (User, Passwort oder Token) braucht. Diese Credentials sollte allerdings nie an den Client weitergereicht werden.

Ein Workaround ist die **Secured-Tiles-Redirect API**. Damit werden die Tiles über einen Aufruf auf die WebGIS API abholt. Die WebGIS API fungiert hier als Reverse Proxy zum geschützten WMTS Dienst. Die Credentials bleiben so am Server.

**Client** => TileRequest => **WebGIS API** => TileRequest+Credentials => **WMTS Server**  

Die **Secured-Tiles-Redirect API** Muss explizit über die ``api.config`` aktiviert werden:

.. code:: XML

  <section name="secured-tiles-redirect">
    <add key="use-with-ogc-wmts" value="true" />  <!-- default: false -->
    <add key="referers" value="www.server1.com,www.server2.com" />  <!-- optional -->
  </section>

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``use-with-ogc-wmts``
     - Erst wenn dieser Wert auf ``true`` gesetzt wird, wird bei geschützten WMTS Diensten die **Secured-Tiles-Redirect API** verwendet. Ohne diesen Eintrag funktionieren geschützte wMTS Dienst nicht.
   * - ``referers`` *(optional)*
     - Beschränkt den Zugriff auf die **Secured-Tiles-Redirect API** auf bestimmte **Referer**. Hier können die **Domains** der Server eingetragen werden, auf denen der *WebGIS Viewer* läuft. Wird kein Wert angegeben, kann **jeder Client** auf die API zugreifen.

Proxy Server
------------

Falls **Dienste aus dem Internet** eingebunden werden, kann ein **Proxy-Server** erforderlich sein.  
Die Konfiguration erfolgt in der optionalen *Section* ``proxy`` in der ``api.config``:

.. code-block:: xml

  <section name="proxy">
      <add key="use" value="true" />
      <add key="server" value="webproxy.mydomain.com" />
      <add key="port" value="8080" />
      <add key="user" value="" />
      <add key="pwd" value="" />
      <add key="domain" value="" />
      <add key="ignore" value="localhost;localhost:8080;.my-domain.com$;^8\.;" />
  </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``use``
     - Gibt an, ob der **Proxy-Server** verwendet werden soll.
   * - ``server``
     - Hostname oder IP-Adresse des **Proxy-Servers**.
   * - ``port``
     - Port, über den der **Proxy-Server** erreichbar ist.
   * - ``user`` *(optional)*
     - **Benutzername** für den Proxy-Server.
   * - ``pwd`` *(optional)*
     - **Passwort** für den Proxy-Server.
   * - ``domain`` *(optional)*
     - **Domänenname** für die Anmeldung am Proxy.
   * - ``ignore`` *(optional)*
     - Liste von **Regeln**, anhand derer bestimmte Server vom Proxy **ausgenommen** werden. Mehrere Regeln können mit ``;`` getrennt angegeben werden. Es sind auch **reguläre Ausdrücke** möglich.

HttpClient
----------

.. code-block:: xml

  <section name="httpclient">
      <add key="default-timeout-seconds" value="300"/> <!-- default:0 = 100 secs --> 
  </section> 

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``default-timeout-seconds``
     - Gibt die maximale Wartezeit an, die ein Http Request (zB auf ein MapService wartet)
       Ist der Wert auf ``0`` oder nicht gesetzt, 
       wird der Standardwert **100 Sekunden** verwendet. 

       Der Wert, wie lange auf einen MapServer Dienst gewartet wird, wird eigentlich im CMS 
       für jeden Dienst extra konfiguriert. Werte die höher sind als der hier gesetzte Wert,
       werden ignoriert. Der hier angeführte Werte ist der **maximale Timeout** für alle Request.

       Ein Erhöhen oder setzen dieses Wertes macht nur Sinn, wenn es Kartendienste gibt, die beim
       Drucken mit großen Papierformaten und Auflösungen länger als 100 Sekunden brauchen.
       WebGIS wartet beim Drucken immer maximal 100 Sekunden auf einen Dienst, egal was im CMS
       konfiguriert ist. Ist im CMS ein höher Wert konfiguriert, muss dieser auch hier gesetzt werden.

DataLinq 
--------

Über die *Section* kann angegeben werden, ob **DataLinq** von einer **WebGIS API Instanz** angeboten wird.

.. code-block:: xml

   <section name="datalinq">
      <add key="include" value="true" />
      <add key="allow-code-editing" value="true" />

      <!-- optional: Engine & Serverside Encryption -->     
      <add key="razor-engine" value="default" /> <!-- default, legacy -->
      <add key="api-encryption-level" value="DefaultStaticEncryption" /> <!-- DefaultStaticEncryption, None, RandomSaltedPasswordEncryption -->

      <!-- optional -->
      <add key="allowed-code-api-clients" value="https://my-server/cms" />
      <add key="environment" value="production" /> <!-- default, production, development, test -->
      <add key="add-namespaces" value="" />
      <add key="add-razor-whitelist" value="DXImageTransform.Microsoft." />
      <add key="add-razor-blacklist" value="ForbiddenNamespace." />
      <add key="add-css" value="-/content/styles/my-company/default.css?{version}" />
      <add key="add-js" value="-/scripts/api/three_d.js?{version}" />

      <!-- optional: SelectEngines>
      <add key="SelectEngines:TextFileEngine:AllowedPaths:0" value="C:\datalinq\data\" />
      <add key="SelectEngines:TextFileEngine:AllowedPaths:1" value="C:\webgis\data\" />
      <add key="SelectEngines:TextFileEngine:AllowedExtensions:1" value=".txt" />
      <add key="SelectEngines:TextFileEngine:AllowedExtensions:0" value=".csv" />
   </section>

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``include``
     - Gibt an, ob **DataLinq** über diese Instanz angeboten wird.
   * - ``allow-code-editing``
     - Steuert, ob **DataLinq-Objekte** (Endpoints, Queries, Views) über eine **DataLinq.Code-Instanz** bearbeitet werden können.
       
       .. danger::

          Aus **Sicherheitsgründen** sollte dies nur für **lokale oder Intranet-Instanzen** aktiviert sein. Auf **Produktivsystemen** sollte DataLinq nur als **Read-Only** verwendet werden.
   * - ``razor-engine``
     - Gibt an, welche **Razor-Engine** verwendet wird. Standardmäßig ist dies die **DataLinqLanguageEngineRazor** (``default``).  
       Die **LegacyEngine** (``legacy``) ist eine ältere Version, die nicht mehr weiterentwickelt wird. 
       Diese sollte nur eingesetzt werden, wenn nach dem Umstieg von einer älteren WebGIS Version (6.x)
       Probleme beim rendern bestehender *Views* auftreten.
   * - ``api-encryption-level``
     - In den DataLinq Endpoints und Queries können teils sensible Daten wie Connection Strings und
       SQL Statements stehen. Der Wert hier gibt an mit welchen Verschlüsselungslevel 
       **serverseitig** gespeicherte *Connection Strings* und *Query Statements* verspeichert werden.
       
       - ``DefaultStaticEncryption`` (default): Daten werden im Storage mit einem fixen Password verschlüsselt
       - ``None``: Sensible Daten werden im Storage Unverschlüsselt abgelegt
       - ``RandomSaltedPasswordEncryption``: Daten werden mit einem hier zufällig für die Instanz
         generierten Password und einem zufällig generierten Salt verschlüsselt. 
       
       Die letzte Variante ist die sicherste, es kann jedoch passieren, dass unterschiedliche 
       Instanzen die DataLinq Objekte nicht mehr lesen können, da sie mit einem anderen Password
       verschlüsselt wurden. Empfohlen wird daher die Variante ``DefaultStaticEncryption``, hier sind 
       die Daten verschlüsselt, können aber von allen Instanzen gelesen werden.
       
       .. important::

          Bei der Verwendung von **DataLinq** ist es wichtig, dass die **Verschlüsselung** für alle Instanzen gleich ist.  
          Andernfalls können **DataLinq-Objekte** nicht mehr gelesen werden.  
          Dies gilt insbesondere für **WebGIS-Instanzen**, die auf verschiedene **Server verteilt** sind. 

   * - ``allowed-code-api-clients``
     - Falls **Code-Bearbeitung** erlaubt ist, können hier die **URLs** der **autorisierten DataLinq.Code-Instanzen** angegeben werden (mit Komma getrennt). In einer WebGIS-Umgebung ist dies meist die URL zum **WebGIS CMS**. Falls eine nicht autorisierte DataLinq.Code-Instanz versucht, Änderungen vorzunehmen, wird eine Fehlermeldung ausgegeben.
   * - ``environment``
     - Gibt an, welche **Umgebung** für die Instanz verwendet wird. Dies beeinflusst z. B., welcher **Connection-String** für Endpunkte verwendet wird.  
       **Mögliche Werte:** ``production``, ``development``, ``test``.
   * - ``add-namespaces``
     - Liste zusätzlicher **Namespaces**, die in **Views** genutzt werden dürfen (getrennt durch Komma).

       .. danger::

          Jeder zusätzliche Namespace kann ein **Sicherheitsrisiko** darstellen. Standardmäßig sind ``System``, ``System.Linq`` und ``System.Text`` eingebunden.
   * - ``add-razor-whitelist``
     - Liste von **Ausnahmen**, die bei der **Validierung von Razor Views** ignoriert werden. Dies kann verwendet werden, um bestimmte Werte aus der **Blacklist** explizit zuzulassen.

       Beispiel: Styles mit ``DXImageTransform.Microsoft...`` werden standardmäßig blockiert, da ``Microsoft.`` in der **Blacklist** enthalten ist.  

       Um **gezielte Ausnahmen** zuzulassen, sollte hier nur der **nötige spezifische Wert** eingetragen werden.
   * - ``add-razor-blacklist``
     - Liste zusätzlicher Begriffe, die in Razor Views **gesperrt** werden.  Standardmäßig enthält die **Blacklist** bereits: ``System.``, ``Microsoft.``.  Hier können weitere Begriffe hinzugefügt werden, um potenzielle **Sicherheitslücken** zu vermeiden.
   * - ``add-css``
     - Liste von **benutzerdefinierten CSS-Dateien**, die in **allen Report Views** geladen werden.  
       
       **Syntax:** Absolute Pfade (``https://...``) oder **relative Pfade** (``-/...``).  
       
       Der Platzhalter ``{version}`` sorgt dafür, dass nach einem API-Update keine veralteten CSS-Dateien aus dem **Cache** geladen werden.
   * - ``add-js``
     - Liste von **benutzerdefinierten JavaScript-Dateien**, die in **allen Report Views** eingebunden werden. Funktioniert analog zu ``add-css`` und ermöglicht das **Einbinden eigener Skripte**.

   * - ``SelectEngines``
     - Manche **SelectEngines** benötigen erweiterte Einstellungen 
     
       (siehe https://docs.webgiscloud.com/de/datalinq/configuration-api.html#datalinq-api)
       
       Einstellungen für die einzelnen **SelectEngines** können wie oben Beispiel angeben werden
       
       (``dotnet-config`` Konvention: ``:`` Unterteilt *Section*, Arrays mit Indexwerten, ...).
       
       Ein Beispiel ist die **TextFileEngine**, die es erlaubt Textfiles vom Server 
       auszugeben. Hier kann angeführt werden, auf welche Verzeichnisse und 
       Dateierweiterungen zugegriffen werden darf.

**Überprüfung der DataLinq-Konfiguration**
Um zu prüfen, ob die **DataLinq-Einstellungen** korrekt gesetzt sind, kann die **API** mit folgendem Pfad aufgerufen werden:

.. image:: img/config-tools9.png