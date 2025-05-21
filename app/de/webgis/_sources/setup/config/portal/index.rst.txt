====================================
Konfiguration der Portal Applikation
====================================

Datei ``_config/portal.config``
===============================

Die Installation des Portals ist optional. Wenn WebGIS nur als API für HTML/JavaScript-Clients genutzt wird, kann darauf verzichtet werden. In diesem Fall können Kartenanwendungen jedoch nur ohne zusätzliche Werkzeuge erstellt werden. Zudem steht ohne die Installation des Portals auch kein **MapBuilder** zur Verfügung.

Diese Datei wird – falls nicht vorhanden – beim ersten Start der API mit ``Default-Werten`` angelegt. Dieser Abschnitt zeigt, wie die Datei an eigene Anforderungen für einen produktiven Betrieb angepasst werden kann.

Die Datei ist – ähnlich wie die ``api.config`` – eine XML-Datei, die verschiedene ``Schlüssel-Werte-Paare`` enthält.

.. code:: xml

  <?xml version="1.0" encoding="utf-8"?>
  <configuration>
    <appSettings>
      <!-- Shared Crypto Keys -->
      <add key="shared-crypto-keys-path" value="C:\apps\webgis/test/webgis-repository/security/keys" />

      <!-- Allgemein -->
      <add key="company" value="my-company" />
      <add key="portal-name" value="webGIS Portal" />
      <add key="portal-name-url" value="http://www.e-steiermark.com" />

      <!-- Security -->
      <!-- windows, token, clientid, forms, anonym (url) -->
      <add key="security" value="anonym" />
      <!-- erlaubte Methoden mit Beistrich getrennt, keine Leerzeichen !! -->
      <add key="security_allowed_methods" value="anonym" />

      <!-- Für die Erzeugung von Auswahllisten (Wenn Windows Auth verwendet wird) -->
      <add key="portal-windows-authentication-ldap-directory" value="LDAP://my-domain" />
      <add key="portal-windows-authentication-ldap-format" value="my-domain\{0}" />

      <add key="use-local-url-scheme" value="true" />
      <add key="allow-subscriber-user-access-page-settings" value="true" />

      <!-- Advanced Security -->
      <!-- default: true  wenn false, ist kein Login mehr möglich (Security: In Internet keine Konfiguration mehr) -->
      <add key="allow-subscriber-login" value="true" />

      <!-- Url zum Portal, so wie es auch vom Anwender sichtbar ist -->
      <add key="api" value="http://localhost:5001" />
      <!-- Url zum Portal, wie es von Server aus sichtbar ist -->
      <add key="api-internal-url" value="http://localhost:5001" />
      <add key="portal-url" value="http://localhost:5002" />

      <add key="portal-custom-content-rootpath"
        value="C:\apps\webgis/test/webgis-repository/portal-page-content" />
      <!-- EPSG Code der hauptsächlich verwendet wird und in dem Entfernungen gerechnet werden sollten  -->
      <add key="map-calc-crs" value="3857" />
      <!-- Progessive Web App true/false, zu Zeit nicht in Verwendung  -->
      <add key="register-serviceworker" value="false" />

      <!-- Cache  -->
      <add key="cache-provider" value="fs" />
      <!-- Gleicher Connectionstring wie in api.config  -->
      <add key="cache-connectionstring" value="C:\apps\webgis/test/webgis-repository/db/cache" />

      <!-- Cache Aside -->
      <!-- optional: leer, redis, inapp -->
      <add key="cache-aside-provider" value="inapp" />
      <!-- 3600 Sekunden caching -->  <!-- ConnectionString zu redis, zB localhost:6379 -->
      <add key="cache-aside-connectionstring" value="3600" />

      <!-- Subscriber Database -->
      <!-- GleicherConnectionstring wie in api.config  -->
      <add key="subscriber-db-connectionstring"
        value="fs:C:\apps\webgis/test/webgis-repository/db/subscriber" />

      <!-- Benutzerdefinierte Layouots erlauben   -->
      <add key="query-custom-map-layout" value="true" />
    </appSettings>
  </configuration>

Abschnitt ``Allgemein``
=======================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``company``
     - Eindeutige Kennung für das Unternehmen des Portalbetreibers (z. B. ``e``, ``kagis``, ``sagis``). Wird für das Styling verwendet. In einem Unterverzeichnis mit diesem Kürzel können Stylesheet-Dateien gespeichert werden, die bei einem Update nicht überschrieben werden.
   * - ``portal-name``
     - Text, der in der Titelzeile aller Portalseiten angezeigt wird (Standardwert: *WebGIS Portal*).
   * - ``portal-name-url``
     - URL zur Webseite des Portalbetreibers. Wird aufgerufen, wenn der Benutzer auf den Titelzeilen-Text klickt.

Abschnitt ``Security``
======================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``security``
     - Legt die Authentifizierungsmethode für die Anmeldung am Portal fest. Mögliche Werte sind ``windows`` und ``anonym``. In kundenspezifischen Installationen stehen zusätzlich ``pvp``, ``pvp2`` und ``token`` zur Verfügung.
   * - ``security_allowed_methods``
     - Erlaubt die Anmeldung mit einer anderen Methode als der in ``security`` definierten. Der gewünschte Anmeldemodus kann als URL-Parameter übergeben werden (z. B. ``&security=anonym``). Die hier aufgeführten Methoden müssen **durch Komma getrennt** angegeben werden. Ist nur eine Methode zulässig, muss sie mit dem Wert in ``security`` übereinstimmen.
   * - ``allow-subscriber-user-access-page-settings``
     - Bestimmt, ob autorisierte Subscriber Inhalte auf Portalseiten bearbeiten dürfen. In geschlossenen Systemen kann dieser Wert auf ``false`` gesetzt werden.
   * - ``use-local-url-scheme``
     - ``true`` / ``false``  
       
       In lokalen oder Offline-Umgebungen kann dieser Wert auf ``true`` gesetzt werden. In diesem Fall erfolgt der Schlüsselaustausch über eine unverschlüsselte HTTP-Verbindung **ohne SSL**. Bei einem öffentlichen Portal sollte dieser Wert auf ``false`` gesetzt sein, sodass eine verschlüsselte Verbindung über **HTTPS** gewährleistet ist.

       .. danger::  
          Dieser Wert sollte nur in lokalen oder Offline-Umgebungen (z. B. für Testzwecke) auf ``true`` gesetzt werden. Auch für Intranetanwendungen wird heute eine verschlüsselte Verbindung über SSL empfohlen.

Abschnitt ``Auswahllisten``
===========================

Bei Verwendung der Windows-Authentifizierung können hier Konfigurationswerte für das **LDAP-Verzeichnis** definiert werden. Diese Werte werden beispielsweise genutzt, wenn einem Subscriber Berechtigungen für eine Portalseite zugewiesen werden. Die möglichen Optionen werden dann in **Auswahllisten** zur Verfügung gestellt.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``portal-windows-authentication-ldap-directory``
     - Gibt das **LDAP-Verzeichnis** an, das für die Authentifizierung verwendet wird.  
       Beispiel: ``LDAP://Domäne.at``
   * - ``portal-windows-authentication-ldap-format``
     - Definiert das **Format für die Anmeldung** im LDAP-Verzeichnis.  
       Beispiel: ``Domäne\{0}``

Abschnitt ``Cache Datenbank``
=============================

Diese Datenbank speichert die **Sessions**. Sie muss die Tabelle ``webgis_cache`` enthalten (siehe oben). Wird zusätzlich die **Portal-Anwendung** genutzt, müssen sowohl die **API** als auch das **Portal** denselben Session-Cache verwenden.

Die Werte müssen mit denen in der ``api.config`` übereinstimmen:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``cache-provider``
     - Definiert den Speicherort des Caches.  
       
       Mögliche Werte: 
       
       - ``db``: für eine Datenbank
       - ``fs``: für das Dateisystem
   * - ``cache-connectionstring``
     - Connection-String für die Datenbank oder Pfad im Filesystem.


Abschnitt ``Cache Aside`` (optional)
====================================

Die hier angegebenen Werte müssen mit denen in der ``api.config`` übereinstimmen.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``cache-aside-provider``
     - Bestimmt den **Cache-Mechanismus** für das **Cache-Aside-Verfahren**.  
       
       Mögliche Werte: ``redis``, ``inapp`` oder leer (kein Cache Aside).
   * - ``cache-aside-connectionstring``
     - Definiert die Verbindungseinstellungen für den Cache-Anbieter.  

       Beispiel: ``localhost:6379`` für Redis oder eine Zeitangabe in Sekunden für In-App-Caching (z. B. ``3600``)

Abschnitt ``Subscriber Datenbank``
==================================

Die hier angegebenen Werte müssen mit denen in der ``api.config`` übereinstimmen.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``subscriber-db-connectionstring``
     - Connection-String zur zuvor eingerichteten Datenbank oder Pfad zum entsprechenden Verzeichnis im Filesystem.

Abschnitt ``Urls``
==================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``api``
     - URL zur API, wie sie für den Anwender sichtbar ist.
   * - ``api-internal-url``
     - Interne URL, die vom Portal für die Kommunikation mit der API genutzt wird, z. B. für den Zugriff auf den Storage. Wenn beide Anwendungen auf demselben Server installiert sind, kann eine lokale Adresse verwendet werden, z. B. ``http://localhost/webgis-api``. Standardmäßig kann hier der gleiche Wert wie bei ``api`` gesetzt werden.
   * - ``portal-url``
     - URL des Portals (dieser Anwendung), wie sie für den Anwender sichtbar ist. Diese wird beispielsweise verwendet, um Links für das Teilen von Karten zu generieren.

Abschnitt ``Advanced Security``
===============================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``allow-subscriber-login``
     - Steuert, ob sich Subscriber an dieser Instanz anmelden können. Eine detaillierte Beschreibung dieses Schlüssels befindet sich in der ``api.config`` unter dem Abschnitt ``Subscriber Registration``.
   * - ``query-custom-map-layout``
     - Ermöglicht die Verwendung benutzerdefinierter Layouts im Kartenviewer, abhängig von der Bildschirmgröße. Mit diesem Schlüssel kann festgelegt werden, ob benutzerdefinierte Layouts zugelassen (``true``) oder untersagt (``false``) werden.

Abschnitt ``Logging``
=====================

.. code-block:: xml

   <!-- only for debugging, never in production -->
   <add key="trace" value="true" />
   <add key="tracePath" value="C:\\apps\\webgis\\local\\webgis-repository\\logs" />

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``trace``
     - Aktiviert das Logging für Debugging-Zwecke. Bei Aktivierung wird eine ``trace.log``-Datei im angegebenen Verzeichnis erstellt. Das Logging enthält beispielsweise Informationen zu den Anmeldeparametern eines Nutzers.
     
       .. danger::
      
          Diese Funktion sollte ausschließlich zu Debugging-Zwecken genutzt und niemals in einer Produktionsumgebung aktiviert werden.

   * - ``tracePath``
     - Definiert das Verzeichnis, in dem die ``trace.log``-Datei gespeichert wird.


