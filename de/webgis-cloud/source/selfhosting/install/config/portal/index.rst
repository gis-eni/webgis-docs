Konfiguration der Portal Applikation
====================================

Datei ``_config/portal.config``
-------------------------------

Die Installation des Portals ist optional. Wenn WebGIS 5 nur als API für HTML/Javascript Clients verwendet wird, 
kann darauf auch verzichtet werden. Allerdings können die Kartenanwendungen dann nur ohne Hilfsmittel
erstellt werden. Ohne die Installation des Portals, steht auch kein MapBuilder zur Verfügung.

Diese Datei wird (falls nicht vorhanden) beim ersten Start der API mit Default Werten angelegt.
In diesem Abschnitt wird gezeigt, wie diese Datei den eigenen Bedürfnissen für einen 
produktiven Betrieb angepasst werden kann:

Die Datei ist (wie die ``api.config``) ein XML Datei mit unterschiedlichen ``Schlüssel/Werte``-Paaren.

Abschnitt ``Allgemein``
+++++++++++++++++++++++

* ``company``
  Hier kann ein eindeutige Kennung für das Unternehmen des Portalbetreibers angeben werden 
  (z.B. e, kagis, sagis, …).
  Wird für das Styling verwendet (siehe unten). In einem Unterverzeichnis mit diesem Kürzel
  können Stylesheet Dateien angelegt werden, die bei einem Update nicht verändert werden.

* ``portal-name``
  Ein Text, der in der Titelzeile für alle Portalseiten angezeigt wird (default: *WebGIS Portal*).

* ``portal-name-url``
  Ein Link auf die Webseite des Portalbetreibers. 
  Diese wird aufgerufen, wenn der Anwender auf den Text in der Titelzeile klickt.

Abschnitt ``Security``
++++++++++++++++++++++

* ``security``
  Gibt an, mit welcher Methode sich ein Anwender beim Portal anmeldet. Mögliche Werte sind hier: 
  ``windows, anonym``.
  Bei benutzerdefinierten Kundeninstallation stehen hier noch weitere Methoden (``pvp``, ``pvp2``, ``token``)
  zur Verfügung.

* ``security_allowed_methods``
  Grundsätzlich kann sich ein Anwender auf dem Portal auch mit anderen als der unter security angeführten 
  Methode anmelden. Dazu übergibt er den gewünschten Anmeldemodus als Url-Parameter, z.B. ``&security=anonym``. 
  Welche Methoden hier möglich sind, wird in diesem Key definiert. Hier müssen die erlaubten Methoden mit 
  Beistrich getrennt angeführt werden. Erlaubt man nur eine Methode für die jeweilige Instanz, 
  muss hier aber mindestens der Wert angeben werden, der unter dem Key security steht.

* ``allow-subscriber-user-access-page-settings``
  Gibt an, ob autorisierte Subscriber Inhalte auf Portalseiten verändern dürfen. 
  Kann für geschlossene System auf ``false`` gesetzt werden.

* ``use-local-url-scheme``
  ``true`` / ``false``


  Für Lokale oder Offline Anwendung kann hier auf ``true`` gesetzt werden. 
  Der Austausch von Schlüsseln erfolgt dann über eine normale HTTP Verbindung ohne SSL. 
  Betreibt man ein Portal im Internet, sollte dieser Wert auf „false“ gesetzt werden. 
  Allerdings muss hier auch eine Verbindung per HTTPS möglich sein.

  .. note::
    
    Dieser Wert solle nur für Lokale oder Offline Lösung (oder im Testfall) auf ``false`` gesetzt werden. 
    Auch für Intranetanwendungen sollte eine Verbindung ohne SSL heute kein Thema mehr sein.

Abschnitt ``Auswahllisten``
+++++++++++++++++++++++++++

Verwendet man Windows Authentifizierung, können hier Keys für das LDAP Verzeichnis angeführt werden. 
Auf diese wird dann beispielsweise zugegriffen, wenn ein Subscriber Portalseite berechtigt. 
Die möglichen Werte werden ihm dann über Auswahllisten zur Verfügung gestellt.

* ``portal-windows-authentication-ldap-directory``
  z.B.: ``LDAP://Domäne.at``

* ``portal-windows-authentication-ldap-format``
  z.B.: ``Domöne\{0}``

Abschnitt ``Cache Datenbank``
+++++++++++++++++++++++++++++

In dieser Datenbank werden die „Sessions“ gespeichert. Darin muss sich die Tabelle ``webgis_cache``, 
siehe oben, befinden. Verwendet man auch die Portal Anwendung, müssen beide Anwendungen (API und Portal) 
den selben Session-Cache verwenden.

Hier die gleiche Werte, wie in der ``api.config`` angeben:

* ``cache-provider``
  ``db`` (Datenbank) oder ``fs`` (Filesystem)

* ``cache-connectionstring``
  Connection-String auf die Datenbank oder Pfad in Filesystem.

Abschnitt ``Cache Aside`` (optional)
++++++++++++++++++++++++++++++++++++

Hier die gleiche Werte, wie in der ``api.config`` angeben.

Abschnitt ``Subscriber Datenbank``
++++++++++++++++++++++++++++++++++

Hier die gleiche Werte, wie in der ``api.config`` angeben:

* ``subscriber-db-connectionstring``
  Connection-String zu der oben angelegen Datenbank oder Verzeichnis im Filesystem.

Abschnitt ``Urls``
++++++++++++++++++

* ``api``
  Die Url zur API, wie sie für den Anwender sichtbar ist.

* ``api-internal-url``
  Das Portal muss teilweise mit der API reden können, z.B. um auf den Storage zugreifen zu können. 
  Für diese Kommunikation empfiehlt sich hier eine Interne Url anzugeben. 
  Wenn beide Applikationen am gleichen Server installiert sind, 
  z.B.: http://localhost/webgis-api.
  Grundsätzlich kann hier der gleiche Wert wie bei ``api`` angegeben werden.

* ``portal-url``
  Die Url zum Portal (diese Anwendung), wie sie für den Anwender sichtbar ist. Diese Url wird beispielsweise 
  verwendet, um Links für das Teilen von Karten zu erzeugen.

Abschnitt ``Advanced Security``
+++++++++++++++++++++++++++++++

* ``allow-subscriber-login``
  Verhindert das Anmelden von Subscribern für diese Instanz. 
  Eine Beschreibung für diesen Key steht in der Auflistung der Keys für die ``api.config`` im Abschnitt 
  ``Subscriber Registration``.

* ``query-custom-map-layout``
  Für den Kartenviewer lassen sich benutzerdefinierte Layouts anlegen (je nach Bildschirmgröße). 
  Mit diesem Key kann man Benutzerdefinierte Layouts zulassen bzw. untersagen (``true`` / ``false``).


Abschnitt ``Logging``
+++++++++++++++++++++

.. code:: xml

  <!-- only for debugging, never in production -->
  <add key="trace" value="true" />
  <add key="tracePath" value="C:\\apps\\webgis\\local\\webgis-repository\\logs">

Mit ``trace`` wird in das oben angeführte Verzeichnis eine ``trace.log`` geschrieben.
Hier wir zB mitgeloggt, mit welchen Parametern eine User angemeldet wird.
``trace`` sollte nur dem Debugging dienen und niemals in einer Produktionsumgebung verwendet werden.    
