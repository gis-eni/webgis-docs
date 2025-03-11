=================================
Konfiguration der CMS Applikation
=================================

Datei ``_config/cms.config``
============================

Die Konfiguration der CMS-Anwendung erfolgt über die Datei ``webgis-cms/_config/cms.config``.

Dabei handelt es sich um eine JSON-Datei (**JavaScript Object Notation**), ein strukturiertes Datenformat, das unabhängig von JavaScript ist. Beim Bearbeiten der Datei ist darauf zu achten, dass sie weiterhin gültiges JSON bleibt. Insbesondere dürfen keine Kommentare eingefügt und Schlüssel müssen als Strings in Anführungszeichen geschrieben werden.

.. note:: Hinweis zur JSON-Syntax

    - Attribute und Werte werden durch ``:`` getrennt, z. B.: ``"force-https": false``
    - Objekte (mit mehreren Attributen) werden in geschweifte Klammern gesetzt: ``{ … }``
    - Arrays werden durch eckige Klammern gekennzeichnet: ``[ … ]``. Die einzelnen Werte werden durch Kommas getrennt.
    - In einem Array können Objekte aufgelistet werden (z. B. ``cms-items``): ``[ { "object1": ... }, { "object2": ... } ]``
    - In einem Array können einzelne Werte (Strings, Zahlen) aufgelistet werden (z. B. ``http-get``): ``[ "url1", "url2" ]``
    - Ein Backslash ``\`` ist in einer Zeichenkette in JSON ein besonderes Zeichen. Um tatsächlich einen Backslash anzugeben, muss ein doppelter ``\\`` verwendet werden (z. B. in Pfaden). Andernfalls ist die Konfigurationsdatei kein gültiges JSON mehr!

Die Vorlage hat folgendes Format:

.. code-block:: json

    {
      "shared-crypto-keys-path": "C:\\apps\\webgis/local/webgis-repository/security/keys",
      "company": "",
      "elasticsearch-endpoint": null,
      "force-https": false,
      "services-default-url-scheme": "http://",
      "webgis-portal-instance": "http://localhost:5002",
      "cms-display-url": "https://myserver.com/cms",
      "cms-items": [
        {
          "id": "webgis-release-default",
          "name": "WebGIS Release Default",
          "path": "C:\\apps\\webgis/local/webgis-repository/cms/param/webgis-release-default",
          "scheme": "webgis",
          "deployments": [
            {
              "name": "default",
              "target": "C:\\apps\\webgis/local/webgis-repository/cms/publish/cms-default.xml",
              "replacement-file": "",
              "postEvents": {
                "commands": [],
                "http-get": ["http://localhost:5001/cache/clear"]
              }
            }
          ]
        },
        {
          "id": "webgis-custom",
          "name": "WebGIS Custom",
          "path": "C:\\apps\\webgis/local/webgis-repository/cms/param/webgis-custom",
          "scheme": "webgis",
          "deployments": [
            {
              "name": "default",
              "target": "C:\\apps\\webgis/local/webgis-repository/cms/publish/cms-custom.xml",
              "replacement-file": "",
              "postEvents": {
                "commands": [],
                "http-get": ["http://localhost:5001/cache/clear"]
              }
            }
          ]
        }
      ]
    }

Im Folgenden findet sich eine Übersicht der wichtigsten Konfigurationsparameter.

Abschnitt ``Root-Element``
--------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``webgis-portal-instance``
     - Die interne URL zum **WebGIS-Portal**. Dieser Parameter wird benötigt, wenn CMS-Knoten autorisiert werden sollen. Über diese URL ruft die CMS-Applikation die verfügbaren **Benutzer und Gruppen** ab (z. B. **AD-Benutzer/Gruppen**). Da diese Abfrage direkt von Server zu Server erfolgt, kann hier auch eine **interne URL** verwendet werden. Befinden sich beide Applikationen auf demselben Server, kann beispielsweise auch ``http://localhost/webgis-portal`` genutzt werden.
   * - ``cms-display-url`` *(optional)*
     - Dieser optionale Parameter ist hilfreich, wenn das CMS hinter einem **Reverse-Proxy-Server** betrieben wird und die Applikation nicht automatisch ermitteln kann, welche URL für den Anwender sichtbar ist. In diesem Fall kann hier die gewünschte **externe URL** angegeben werden.

Mit einem **Web-CMS** können mehrere Bäume verwaltet werden. Für jeden Baum wird ein Objekt im ``cms-items``-Array angelegt. Der Wert von ``cms-items`` muss ein **Array** sein, das einzelne ``cms-item``-Objekte enthält.

Ein ``cms-item``-Objekt besitzt verschiedene Attribute. Die beiden hervorgehobenen Werte (``path``, ``target``) geben beispielsweise an: 

- ``path``: Wo sich die Wurzel des CMS-Baums befindet.  
- ``target``: Wohin ein CMS veröffentlicht wird.

Abschnitt ``cms-item``
----------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``id``
     - Eine eindeutige ID für das CMS. Sie sollte nur aus Kleinbuchstaben und Zahlen bestehen (keine Umlaute).
   * - ``name``
     - Ein sprechender Name für das CMS.
   * - ``path``
     - Pfad zum Wurzelverzeichnis des CMS-Baums.
   * - ``scheme``
     - Muss immer auf ``webgis`` gesetzt werden.
   * - ``secrets-password`` *(optional)*
     - Wenn in diesem CMS auf Secrets zugegriffen werden soll, erscheint ein Passwortdialog. Hier kann das Passwort festgelegt werden, das für den Zugriff erforderlich ist. Dieser Wert kann auch weggelassen oder leer gelassen werden – der Dialog erscheint dann trotzdem im CMS, muss jedoch ohne Eingabe bestätigt werden.
   * - ``deployments``
     - Ein Array von Deployment-Objekten. Pro Baum können mehrere Deployments (1:n) angelegt werden. Das Ergebnis eines Deployments ist eine ``cms.xml``-Datei, die ins WebGIS eingebunden werden kann.

       **Beispiel für Deployments:**
       
       .. code-block:: json

           [
               {
                   "deployment": "Deployment 1"
               },
               {
                   "deployment": "Deployment 2"
               }
           ]

       Mehrere Deployments können hilfreich sein, um für Test-, Ausfall-, Schulungs- und Produktivsysteme unterschiedliche XML-Dateien zu erzeugen.

Abschnitt ``deployments``
-------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``name``
     - Ein sprechender Name für das Deployment (z. B. *localhost*, *Entwicklung*, *Schulung*, *Test*, *Produktion*).
   * - ``target``
     - Der Pfad für die CMS-Datei. Das CMS erstellt im gleichen Ordner ein Verzeichnis ``_archive``, in dem bestehende XML-Dateien vor dem Überschreiben gesichert werden. Falls diese Sicherungen nicht mehr benötigt werden, kann der Ordner manuell gelöscht werden. Hier kann auch eine URL zur API angegeben werden, z. B.: ``https://localhost/api/cache/upload/{cms-name}``. ``{cms-name}`` entspricht dem CMS-Namen, wie er in der ``api.config`` definiert ist, z. B.:  
      
       .. code-block:: xml

           <add key="cms_my_cms" value="{path-to-cms.xml}" />

       Ergibt die URL: ``https://.../cache/upload/my-cms``

       Der Upload von CMS XML-Dateien hat den Vorteil, dass **WebGIS-CMS** keinen direkten Zugriff auf das Dateisystem der **WebGIS API**-Anwendung benötigt.

       .. danger::

           In diesem Fall müssen jedoch ein **Client** und ein **Secret** definiert werden, um sicherzustellen, dass der Upload nur von einer autorisierten CMS-Instanz durchgeführt wird.

   * - ``client`` und ``secret`` *(erforderlich, wenn ``target`` eine API-URL ist)*
     - Hier kann ein beliebiger *Client* und ein beliebiges *Secret* definiert werden. Das *Secret* sollte ein sicheres Passwort mit mindestens **24 Zeichen** sein. Damit die **WebGIS API** den Upload akzeptiert, muss in der ``api.config`` ein Abschnitt ``<section name='cms-upload-{cms-name}'>`` vorhanden sein, in dem derselbe *Client* und dasselbe *Secret* hinterlegt ist.
   * - ``replacement-file`` *(optional)*
     - Pfad zu einer **Ersatzdatei** (*Replacement File* aus einem alten CMS), die für dieses Deployment verwendet werden soll.
   * - ``ignoreAuthentication`` *(optional)*
     - Wenn dieser Wert auf ``true`` gesetzt ist, werden Berechtigungen im CMS ignoriert. Dies kann für **Schulungs- oder Testsysteme** nützlich sein, in denen alle Benutzer uneingeschränkten Zugriff haben sollen.
   * - ``postEvents`` *(optional)*
     - Ein Array von Ereignissen, die nach erfolgreicher Erstellung ausgeführt werden sollen.
   * - ``environment`` *(optional)*
     - Gibt die Umgebung für das Deployment an. Dies ist z. B. für ``Secrets`` relevant, da für jede Umgebung ein eigener Wert hinterlegt werden kann (z. B. unterschiedliche *ConnectionStrings* für Test- und Produktivsysteme). **Mögliche Werte:** ``Default``, ``Test``, ``Staging``, ``Production``.

Abschnitt ``postEvents``
------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``commands`` *(optional, Array von Strings)*
     - Eine Liste von Kommandozeilen-Befehlen, die nach der Erstellung des CMS ausgeführt werden. Dies kann nützlich sein, wenn die erzeugte CMS-Datei an einen anderen Speicherort kopiert werden soll.  

       **Anwendungsfall:**  
       Wenn mehrere WebGIS-Instanzen hinter einem Load-Balancer betrieben werden, kann das XML-File so automatisch auf alle Instanzen verteilt werden.
   * - ``http-get`` *(optional)*
     - Eine Liste von **HTTP-GET-Anfragen**, die nach der Erstellung des CMS ausgeführt werden. Dies kann z. B. genutzt werden, um nach einem Deployment ein ``cache/clear`` einer WebGIS-Instanz auszulösen. Dadurch wird sichergestellt, dass das neue XML-File direkt in den Cache geladen wird.

       .. note::

          Wird die **CMS.xml** per Upload an die **WebGIS API** übertragen, kann auf einen manuellen ``cache/clear``-Aufruf verzichtet werden, da dies von der WebGIS API automatisch ausgeführt wird.


Weitere Attribute
-----------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``company``
     - Ein Kürzel für die Firma. Optional kann später eine ``wwwroot/css/{company}/site.css`` Datei angelegt werden, um CSS-Stile für das CMS zu überschreiben. Dadurch lassen sich Farben und weitere Design-Elemente anpassen.
   * - ``force-https``
     - Sollte für **Kundeninstallationen** immer auf ``false`` gesetzt werden.
   * - ``service-default-url-scheme``
     - Gibt an, welches **Protokoll** (``http://`` oder ``https://``) verwendet wird,wenn Karten-Dienste eingebunden werden. In der Erstellungsmaske wird oft nur der **Servername** eingegeben. Dieses Attribut steuert, ob die vollständige URL zum Karten-Dienst mit  
       ``http://`` oder ``https://`` generiert wird.
   * - ``webgis-portal-instance`` *(optional)*
     - Falls im CMS **Berechtigungen** konfiguriert werden, muss das CMS im Hintergrund eine WebGIS-Portal-Instanz abfragen, um verfügbare **Anmeldemöglichkeiten und Benutzer** zu ermitteln.  

       Diese Abfrage kann auch direkt im Web-CMS erfolgen, indem die Instanz manuell angegeben wird. Wird der Wert hier vordefiniert, erhöht sich der **Eingabekomfort**, da die Information nicht jedes Mal erneut eingegeben werden muss.


Datei ``_config/datalinq.config``
=================================

Die CMS-Applikation enthält auch **DataLinq.Code** zum Bearbeiten von **DataLinq-Endpoints**, **Queries** und **Views**. Die eigentliche **DataLinq-Engine** läuft innerhalb einer **WebGIS-API-Instanz**.

Welche Instanzen über die CMS-Startseite zum Editieren angezeigt werden, kann über die Datei ``_config/datalinq.config`` gesteuert werden:

.. code-block:: json

   {
      "instances": [
         {
            "name": "Local WebGIS API",
            "description": "My local WebGIS test and development API",
            "url": "https://my-server/webgis-api"
         }
      ],
      "useAppPrefixFilters": true,
      "autoLogin": "author"
   }

Übersicht der wichtigsten Konfigurationsparameter
-------------------------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``instances``
     - Ein **Array**, in dem mehrere **DataLinq-API-Instanzen** definiert werden können. Wird eine dieser Instanzen über die **CMS-Startseite** aufgerufen, erscheint ein Anmeldefenster. Dort muss man sich mit einem **Subscriber** für die jeweilige API-Instanz anmelden.

       .. note::

          Die jeweilige **API-Instanz** kann in der Konfiguration (``api.config``) unter ``datalinq => allowed-code-api-clients`` festlegen, **von welchen URLs DataLinq.Code-Editing erlaubt ist**. Ist die entsprechende **CMS-Instanz** dort nicht eingetragen, erscheint eine Fehlermeldung (*Invalid Client*).
   * - ``useAppPrefixFilters``
     - Wird diese Option auf ``true`` gesetzt, können die einzelnen **Endpoints** beim Start der **DataLinq.Code**-Anwendung gefiltert werden.  

       **Namenskonvention für Endpoints:**

       Die Endpoints sind nach folgendem Schema organisiert:

       .. code-block::

          {APPLICATION}-{db/lov/...}-{etc...}

       Vor dem ersten ``-`` steht der **Name der Applikation**. Dahinter folgen optional weitere Beschreibungen zur Unterscheidung der **Endpoints**.  

       **Typische Endpoint-Struktur:**  

       Eine Applikation hat in der Regel mehrere Endpoints, darunter:

       - **ein** Endpoint für **lesende Datenbankzugriffe**
       - **ein** Endpoint für **schreibende Datenbankzugriffe**  
       - **PlainText-Endpoints** für Auswahllisten  
       
       Wird beim Start der Anwendung eine oder mehrere Applikationen ausgewählt, werden nur deren Endpoints im Baum dargestellt. Dies verbessert die Performance und erhöht die Übersichtlichkeit, insbesondere wenn viele Applikationen existieren. Der Filter kann jederzeit neu gesetzt werden, indem auf die Überschrift **"DataLinq.Code" über dem Baum** geklickt wird.


Datei ``_config/settings.config``
=================================

In dieser optionalen Datei können allgemeine Einstellungen für die WebGIS-CMS-Applikation hinterlegt werden. Ein Anwendungsfall ist die Konfiguration eines **Logging-Files** oder die Einrichtung eines **Proxy-Servers**.  

Wenn externe Dienste eingebunden werden, kann für den Zugriff ein **Proxy-Server** erforderlich sein. Mit den folgenden Einstellungen kann über diese Datei ein Proxy-Server definiert werden, der für sämtliche Internetzugriffe genutzt wird:

.. code-block:: json

   {
      "logging_connection_string": "C:\\cms\\cms-logging.csv",
      "proxy": {
         "use": true,
         "server": "webproxy.mydomain.com",
         "port": 8080,
         "user": "",            // optional
         "password": "",        // optional
         "domain": "",          // optional
         "ignore":"localhost;my-intranet.com;.my-domain.com$;"
      }
   }

Übersicht der wichtigsten Konfigurationsparameter
-------------------------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Attribut**
     - **Beschreibung**
   * - ``logging_connection_string``
     - Pfad zur **Logging-Datei**.  
       Damit kann nachverfolgt werden, welche Benutzer Änderungen im CMS vorgenommen haben bzw. wann und von wem ein CMS zuletzt veröffentlicht wurde.  

       Falls die Datei die Endung ``.csv`` hat, wird eine **CSV-Datei** mit ``;`` als Trennzeichen erstellt. Andernfalls werden die Logs als **Textdatei** gespeichert, wobei jede Zeile einen Eintrag darstellt.  

       .. note::

          Die Datei kann über **DataLinq** (Endpoint mit Connection Type *TextFile*) eingelesen werden, um die Logs im Browser verfügbar zu machen.

   * - ``proxy``
     - Ermöglicht die Konfiguration eines **Proxy-Servers** für Internetzugriffe.  

       - ``user``, ``password`` und ``domain`` sind optional.  
       - Im Feld ``ignore`` können mehrere Regeln durch ``;`` getrennt angegeben werden. Wenn der aufgerufene Server mit einer dieser Zeichenketten beginnt, wird der Proxy ignoriert.  
       - Auch **reguläre Ausdrücke** können hier verwendet werden.


Datei ``_config/application-security.config``
=============================================

Standardmäßig ist das Web-CMS für alle Benutzer zugänglich, die die URL kennen. Um den Zugriff mit **Benutzername und Passwort** einzuschränken, kann diese Datei verwendet werden.  

Existiert die Datei **nicht**, ist das CMS **frei zugänglich**.

.. danger::
   **Sicherheitsrisiko bei Nutzung im Internet!**  

   Dieser Mechanismus bietet lediglich einen **einfachen Schutz** über Benutzername und Passwort. Er ist **nicht für den Einsatz im Internet** geeignet, da er mit böswilligen Methoden umgangen werden kann.  

   Falls das Web-CMS auf einem **öffentlichen Server** installiert werden muss, sollte es **nicht direkt in IIS eingebunden und nicht über das Internet freigegeben** werden.  

   **Empfohlene Sicherheitsmaßnahmen:**

   - Das CMS sollte **nur im Intranet** betrieben werden, da hier ein einfacher Schutz in der Regel ausreichend ist.  
   - Falls **ein Fernzugriff erforderlich ist**, sollte das CMS **nicht** als klassische Web-Anwendung in IIS laufen. Stattdessen sollte es als **lokale Desktop-Anwendung** auf einem **Jumphost** ausgeführt werden.  
   - Für eine **sichere Authentifizierung** sollten **Windows-Authentifizierung** oder **OpenID Connect** genutzt werden. Diese Methoden werden weiter unten beschrieben.

Gesicherter Benutzerzugang
--------------------------

Passwortgeschützten Zugriff auf das CMS einrichten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um den Zugriff auf das CMS mit einem **Benutzername-Passwort-Schutz** zu versehen,  
gehen Sie folgendermaßen vor:

1. Das CMS im Browser mit der URL ``/admin/CreateLogin`` aufrufen.

   .. image:: img/config-security1.png

   .. note::

      Diese URL kann nur aufgerufen werden, wenn noch **keine** ``application-security.config`` Datei existiert. Falls die Datei bereits vorhanden ist, muss eine Anmeldung erfolgen, um auf diese Seite zuzugreifen.

2. Benutzername und Passwort in das Formular eingeben und auf ``Create`` klicken.

.. image:: img/config-security2.png

3. Das generierte Code-Snippet kopieren und in die Datei ``_config/application-security.config`` einfügen:

   .. code-block:: json

    {
        "users": [
          {
          "name": "admin",
          "password": "tcwXYZ55..."
          }
        ]
    }

   .. note::

      Das Feld ``users`` ist ein **Array**. Es können mehrere Benutzer angelegt  
      und durch Kommas getrennt hinzugefügt werden:

        .. code-block:: json

            {
              "users": [
                {
                  "name": "admin",
                  "password": "tcwXYZ55..."
                },
                {
                  "name": "admin2",
                  "password": "dA8NR..."
                }
              ]
            }


Beim nächsten Aufruf des Web-CMS ist eine Anmeldung mit Benutzername und Passwort erforderlich.

.. tip::

  Falls der Zugriff weiterhin ungeschützt ist, muss möglicherweise der **Application Pool** im IIS neu gestartet werden.

Neben der klassischen Anmeldung über ein Login-Formular kann das CMS auch über **Windows-Authentifizierung** oder **OpenID Connect** abgesichert werden.

Windows-Authentifizierung
~~~~~~~~~~~~~~~~~~~~~~~~~

Für eine **Windows-basierte Anmeldung** kann die ``application-security.config`` folgendermaßen konfiguriert werden:

   .. code-block:: json

      {
         "identityType": "windows",
         "users": [
           {
            "name": "domain\\user1"
           },
           {
            "name": "domain\\user2"
           },
           {
            "name": "domain\\admin123"
           }
         ]
      } 

Diese Konfiguration erlaubt es drei **Windows-Domänenbenutzern**, auf das CMS zuzugreifen.

.. tip::

    Damit diese Methode funktioniert, muss die Web-Applikation im **IIS** so konfiguriert werden, dass **Windows-Authentifizierung aktiviert** und **anonyme Anmeldung deaktiviert** ist.

Anmeldung über OpenID Connect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Möchte man eine **OpenID-Connect-konforme Authentifizierung** nutzen, kann die ``application-security.config`` folgendermaßen aussehen:

   .. code-block:: json

      {
         "identityType": "oidc",
         "oidc": {
            "authority": "https://server.com/identity",
            "clientId": "cms-local-oidc",
            "clientSecret": "secret123",
            "requiredRole": "gis-admin-webgis-cms"
         }
      } 

Mit dieser Konfiguration dürfen **nur Benutzer mit der Rolle** ``gis-admin-webgis-cms`` auf das CMS zugreifen.  

.. tip::

    Damit diese Methode funktioniert, müssen folgende Voraussetzungen erfüllt sein:

    - Die **Client-ID** und das **Client-Secret** müssen am **OpenID-Server** registriert sein.  
    - Als **Scopes** müssen mindestens ``openid``, ``profile`` und ``role`` aktiviert werden.
 

