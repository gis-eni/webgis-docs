.. _annex-security:

Sicherheitsmaßnahmen für das WebGIS Portal
==========================================

Dieses Kapitel richtet sich an **Administratoren und Betreiber**. Es beschreibt, welche Schutzmechanismen
*WebGIS* eingebaut hat, über welche Schlüssel in ``api.config``, ``portal.config`` und ``settings.config`` (CMS) sie
angepasst werden und welche Einstellungen für eine Installation im **Internet** bzw. im **Intranet** empfohlen sind.
Eine Anleitung zu den ersten Schritten nach der Installation (Standardpasswörter ändern, Selbstregistrierung und
Anmeldung abschalten) steht unter :doc:`Sicherheitsmaßnahmen (Hardening) </config/hardening/index>`.

Am Ende des Kapitels gibt die Tabelle :ref:`annex-security-keys` einen Überblick über **alle** sicherheitsrelevanten
Schlüssel mit Risikostufe und Empfehlung.

.. _annex-security-principles:

Grundprinzipien
---------------

- **Starke, individuelle Passwörter.** Standardpasswörter wie ``admin123`` oder ``webgisauthor`` sind besonders anfällig
  für Brute-Force-Angriffe, bei denen Programme automatisiert Millionen von Passwörtern ausprobieren. Ein Passwort wie
  ``admin123`` ist in Sekunden geknackt, ein Passwort mit mindestens 12 Zeichen (besser 16+) aus Groß- und Kleinbuchstaben,
  Zahlen und Sonderzeichen ohne Bezug zu Namen oder Wörterbuchbegriffen benötigt Jahre. Jedes Konto sollte ein eigenes
  Passwort haben, ein **Passwortmanager** hilft beim Erzeugen und Speichern. Wo möglich sollte die
  Zwei-Faktor-Authentifizierung verwendet werden (siehe :ref:`annex-security-mfa`).
  Mehr dazu: `OWASP Authentication Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>`_
- **HTTPS auch im Intranet.** Ein Intranet ist nicht automatisch sicher: Mitarbeitergeräte können infiziert sein,
  Passwörter und Sitzungsinformationen können im Netzwerk mitgelesen oder manipuliert werden und moderne Browser blockieren
  zunehmend unverschlüsselte Verbindungen. Das *WebGIS Portal* sollte daher immer über **HTTPS** betrieben werden.
  Mehr dazu: `Transport Layer Security Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>`_
- **Administration einschränken.** Der Zugriff auf die Administrationsoberflächen (CMS, Subscriber-Anmeldung der API)
  sollte auf einen bestimmten Personenkreis oder auf das interne Netzwerk beschränkt werden. In öffentlichen
  Instanzen sollte die Anmeldung ganz abgeschaltet werden (siehe :ref:`annex-security-subscriber-login`).
- **Browser-Schutzmechanismen nutzen.** Security-Header wie ``Strict-Transport-Security (HSTS)`` und
  ``Content-Security-Policy (CSP)`` werden am Webserver bzw. Reverse Proxy aktiviert.
- **Regelmäßig aktualisieren.** Sowohl *WebGIS* als auch Server, Datenbanken und Drittanbieter-Komponenten.
- **Anmeldungen überwachen.** Wer sich wann angemeldet hat, wird protokolliert. Häufige Fehlanmeldungen oder
  ungewöhnliche Zugriffe auf die Administration können auf einen Angriff hinweisen.
- **Angriffsszenarien kennen.** Auch Intranet-Anwendungen sind von Man-in-the-Middle-Angriffen, Session Hijacking oder
  Cross-Site Scripting (XSS) betroffen. Mehr dazu: `OWASP Top 10 Security Risks <https://owasp.org/www-project-top-ten/>`_

.. note::

   Die folgenden Abschnitte beschreiben das Verhalten bei **Standardwerten**. Die meisten Schutzmechanismen sind
   standardmäßig aktiv. Einstellungen, die einen Schutz abschwächen, sind in der Tabelle :ref:`annex-security-keys`
   als **Kompatibilitäts-Opt-out** gekennzeichnet.

.. _annex-security-subscriber-login:

Subscriber-Anmeldung und Subscriber-Datenbank
---------------------------------------------

Kartenautoren und Administratoren (*Subscriber*) melden sich über ``/Subscribers/Login`` der WebGIS API an.
Subscriber werden in einer **Subscriber-Datenbank** (SQL-Datenbank oder Dateisystem) gespeichert, die in ``api.config``
und ``portal.config`` mit demselben Wert ``subscriber-db-connectionstring``
(:ref:`api.config <api-config-subscriber-db>`, :ref:`portal.config <portal-config-subscriber-db>`) angegeben wird.
Der Zugriff auf die Datenbank bzw. das Verzeichnis sollte auf das notwendige Maß beschränkt werden (eigener
Datenbankbenutzer mit minimalen Rechten, Dateisystemrechte nur für den Anwendungsbenutzer).

Passwörter werden mit **PBKDF2-SHA256** gehasht; ältere Hashes werden bei der nächsten erfolgreichen Anmeldung
automatisch umgestellt. Fehlermeldungen der Anmeldung sind allgemein gehalten und gegen das Erraten von Benutzernamen
abgesichert, Anmeldungen werden protokolliert.

Ob die Subscriber-Anmeldung überhaupt zur Verfügung steht, steuern zwei Schlüssel (beide ohne Eintrag: ``false``):

- ``allow-subscriber-login`` (:ref:`api.config <api-config-subscriber-registration>`,
  :ref:`portal.config <portal-config-advanced-security>`): Ist der Wert ``false``, ist keine Anmeldung möglich. In
  **Internet-Instanzen** sollte er in **beiden** Dateien ``false`` sein, damit auch bei übernommener Konfiguration keine
  Konfiguration von außen möglich ist. Die Konfiguration erfolgt dann in einer internen Instanz, die sich den Storage teilt.
- ``allow-register-new-subscribers`` (:ref:`api.config <api-config-subscriber-registration>`): Erlaubt die
  Selbstregistrierung neuer Subscriber. Darf nur **während der Installation** auf ``true`` stehen, um den ersten
  Administrator anzulegen, und **nie im Internet**. Weitere Konten werden anschließend vom Administrator angelegt.

Für Installationen im Internet ist, wenn eine Anmeldung notwendig ist, die Anmeldung über einen Identity Provider
(OpenID Connect) die empfohlene Variante.

.. _annex-security-password:

Passwortregeln
~~~~~~~~~~~~~~

Beim Anlegen oder Ändern eines Passworts gelten (:ref:`Details <api-config-security-password-rules>`):

- Mindestlänge ``password-min-length`` (Standard ``12``).
- Das Passwort darf nicht in einer eingebauten Liste häufiger Passwörter stehen. Optional kann diese Liste mit
  ``password-blocklist-file`` erweitert werden (z. B. um Listen kompromittierter Passwörter).
- Benutzername, Vorname, Nachname und E-Mail-Adresse dürfen nicht enthalten sein; triviale Muster
  (``aaaaaaaaaaaa``, ``123456789012``) werden abgelehnt.
- Optional kann mit ``password-required-character-classes`` (``0`` - ``4``) eine Anzahl an Zeichenklassen gefordert
  werden. Standard ist ``0``: eine ausreichende Länge in Kombination mit der Sperrliste ist wirksamer als
  Kompositionsregeln.
- Das Standardpasswort ``webgisauthor`` der Erstinstallation kann nicht mehr gesetzt werden; wer sich damit anmeldet,
  muss es sofort ändern.

Die Regeln gelten nur für neue oder geänderte Passwörter, bestehende Passwörter bleiben gültig. Jeder Subscriber kann sein
Passwort auf der Seite **Konto** selbst ändern.

.. _annex-security-mfa:

Zwei-Faktor-Authentifizierung (2FA/TOTP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subscriber können auf der Seite **Konto** eine Zwei-Faktor-Authentifizierung mit einer Authenticator-App (TOTP) und
Wiederherstellungscodes einrichten. Der Schlüssel ``mfa-required`` (:ref:`Details <api-config-security-mfa>`) legt fest,
wer sie verwenden muss: ``none`` (Standard, optional), ``admins`` oder ``all``. Betroffene Subscriber werden bei der nächsten
Anmeldung durch die Einrichtung geführt. ``mfa-issuer`` bestimmt den Namen in der Authenticator-App.

- **Internet:** mindestens ``admins``, besser ``all``.
- **Intranet:** ``admins`` empfohlen.
- Bei einer SQL-Datenbank muss nach dem Update einmal die **Setup**-Seite der API ausgeführt werden (Tabelle
  ``webgis_api_subscriber_mfa``). Solange die Tabelle fehlt, funktioniert die Anmeldung **ohne** zweiten Faktor
  (auch bei ``mfa-required``), es wird eine Warnung protokolliert.
- *Basic Authentication* und *DataLinq* verwenden weiterhin nur Benutzername und Passwort.
- Die MFA-Schlüssel sind mit dem Crypto-Key der API verschlüsselt. Wird dieser geändert, muss die
  Zwei-Faktor-Authentifizierung der Subscriber zurückgesetzt werden (Administratoren können das).

.. _annex-security-captcha-lockout:

Captcha, Sperre und IP-Drosselung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Anmeldung ist gegen Brute-Force-Angriffe geschützt (:ref:`Details <api-config-security-subscriber-login>`):

- **Captcha:** Nach ``login-captcha-after-failed-attempts`` Fehlversuchen (Standard ``3``, pro Benutzername oder
  Client-IP) muss ein Captcha gelöst werden. Jedes Captcha ist einmal verwendbar und nur
  ``captcha-lifetime-minutes`` (Standard ``5``) gültig.
- **Sperre pro Benutzername:** Nach ``login-lockout-after-failed-attempts`` Fehlversuchen (Standard ``10``, ``0`` = keine
  Sperre) wird der Benutzername vorübergehend gesperrt. Die Dauer steigt gemäß ``login-lockout-minutes`` (Standard
  ``1,5,15``, der letzte Wert wird wiederholt). Der Zähler wird nach ``login-failed-attempts-reset-minutes``
  (Standard ``60``) ohne weitere Fehlversuche zurückgesetzt.
- **Drosselung pro Client-IP:** Ab ``login-ip-max-failed-attempts`` Fehlversuchen (Standard ``30``, ``0`` = aus) innerhalb von
  ``login-ip-window-minutes`` (Standard ``15``) erfordert jede Anmeldung von dieser IP ein Captcha und wird verzögert. Eine harte
  Sperre einer IP erfolgt bewusst nicht (gemeinsame Adressen, z. B. hinter NAT).
- **Mehrere Instanzen:** Die Zähler liegen standardmäßig im Speicher der jeweiligen Instanz. Bei Load Balancing können sie
  über **Redis** geteilt werden: ``login-throttle-redis-connectionstring``.
- **Passwort-Cache:** Erfolgreiche Passwortprüfungen bei *Basic Authentication* und *DataLinq* werden
  ``password-verification-cache-seconds`` (Standard ``300``) im Speicher gehalten, weil das Hashen bewusst aufwendig ist.
  ``0`` deaktiviert den Cache.

.. important::

   Die IP-Drosselung setzt voraus, dass die API die **echte Client-IP** sieht. Hinter einem Reverse Proxy müssen daher
   die *X-Forwarded*-Header korrekt konfiguriert sein (siehe :ref:`annex-security-proxy`).

.. _annex-security-sessions:

Sitzungen und Cookies
---------------------

Das Anmelde-Cookie der API ist ``HttpOnly`` und ``SameSite=Lax``. Es enthält einen Sicherheitsstempel, sodass eine Änderung
des Passworts oder der Zwei-Faktor-Authentifizierung andere Sitzungen ungültig macht
(:ref:`Details <api-config-security-subscriber-login>`):

- ``cookie-secure``: ``auto`` (Standard) setzt das *Secure*-Flag bei HTTPS-Aufrufen (inkl. ``X-Forwarded-Proto``), lokale
  Installationen über ``http://localhost`` funktionieren weiterhin. ``always`` setzt es immer (nur mit HTTPS), ``never``
  nie. ``never`` ist im Internet nicht zulässig.
- ``session-max-lifetime-minutes``: maximale Dauer einer Anmeldung unabhängig von der Aktivität (Standard ``480``,
  ``0`` = unbegrenzt, nicht empfohlen).
- ``session-idle-timeout-minutes``: Abmeldung nach Inaktivität (Standard ``0`` = aus). Im Internet z. B. 30 bis 60 Minuten.

.. _annex-security-redirects:

Weiterleitungen nach der Anmeldung
----------------------------------

Das Weiterleitungsziel der Subscriber-Anmeldung wird geprüft, bevor ein Zugangs-Token angehängt wird (Schutz vor
*Open Redirect*). Immer erlaubt ist der Host von ``portal-url``; alle anderen Ziele werden mit ``400 Bad Request`` abgelehnt.
Ist das Portal unter einem anderen Hostnamen erreichbar, können diese Hosts mit
``subscriber-login-allowed-redirect-hosts`` (:ref:`Details <api-config-subscriber-registration>`) freigegeben werden. Es sollten
nur **eigene** Hosts eingetragen werden.

.. _annex-security-cors:

Portal-CORS
-----------

Der ``hmac``-Endpunkt des Portals liefert Zugangsdaten für die API an den angemeldeten Benutzer. Er darf nur von
freigegebenen Seiten per Browser aufgerufen werden, sonst könnte eine Schadseite im Hintergrund Keys für ihre Besucher
abfragen. Alle anderen Seiten des Portals sind standardmäßig nur von Portal und API selbst mit Anmeldung (Cookies) aufrufbar
(:ref:`Details <portal-config-advanced-security>`, ausführlich: :ref:`annex-cors`):

- ``add-cors-origins-for-hmac``: Drittseiten, die den ``hmac``-Endpunkt aufrufen dürfen (Wert ``~`` = alle Seiten, nur zum Testen).
- ``add-cors-origins-for-default``: zusätzliche Origins, die die übrigen Portal-Seiten mit Anmeldung aufrufen dürfen.
  Normalerweise ist kein Eintrag notwendig. Wert ``~`` = alle Seiten (nur zum Testen, Warnung im Logfile).
- ``cors-default-allow-any-origin-without-credentials``: Standard ``false``. Bei ``true`` dürfen fremde Origins öffentliche
  Portal-Seiten **ohne** Anmeldung lesen.

Die Wildcard ``~`` darf in produktiven Umgebungen nicht verwendet werden.

.. _annex-security-dynamic-content:

Dynamischer Inhalt (SSRF-Schutz)
--------------------------------

Der ``DynamicContentProxy`` lädt Inhalte (GeoRSS, GeoJSON, API-Abfragen) im Auftrag des Viewers. Damit er nicht für Angriffe
auf interne Systeme missbraucht werden kann (*Server-Side Request Forgery*), gilt
(:ref:`Details <api-config-dynamic-content>`):

- Nur ``http`` und ``https`` ohne Benutzerinformation sind erlaubt. Ziele, die auf Loopback, private, Link-Local
  (z. B. Cloud-Metadaten) oder andere nicht öffentliche Adressen zeigen, werden abgelehnt. Das gilt auch für jeden
  Redirect. Zertifikate werden geprüft.
- Der Proxy lädt nur **signierte URLs**. Die API signiert die URLs beim Laden einer Karte.
- ``allow-hosts``: Hostnamen oder Muster, die auch auf interne Adressen zeigen dürfen. Standard leer. Nur konkrete interne
  Quellen eintragen, keine breiten Muster.
- ``allow-unsigned``: Standard ``false``. ``true`` lässt auch nicht signierte URLs zu (nur für Karten, die nicht über die
  API geladen werden, z. B. MapBuilder-HTML oder ``custom.js``).
- ``timeout-seconds`` (Standard ``20``), ``max-response-bytes`` (Standard 50 MB) und ``max-redirects`` (Standard ``5``)
  begrenzen den Abruf.

Auch die Suchbegriffe der Auswahllisten (VisFilter-Lookups) werden geprüft: ``term-whitelist`` in der Section ``lookup``
(:ref:`Details <api-config-lookup>`) legt fest, welche Zeichen erlaubt sind.

.. _annex-security-tls:

Ausgehende TLS-Verbindungen
---------------------------

Serverzertifikate bei ausgehenden HTTPS-Verbindungen (Kartendienste, ArcGIS, WMS usw.) werden geprüft. Interne Dienste mit
selbstsignierten Zertifikaten oder Zertifikaten einer internen CA sollten über die Installation der CA im
**Zertifikatsspeicher des Servers** angebunden werden. Nur wenn das nicht möglich ist, kann die Prüfung abgeschaltet werden
(Man-in-the-Middle-Risiko). Der Schlüssel heißt:

- ``allow-untrusted-server-certificates`` in Section ``security`` der ``api.config``
  (:ref:`Details <api-config-security-untrusted-certificates>`) und der ``portal.config``
  (:ref:`Details <portal-config-security>`),
- ``allow_untrusted_server_certificates`` in der ``settings.config`` des CMS (:ref:`Details <cms-config-settings-security>`).

Standard ist jeweils ``false``. In der Praxis sollte ``true`` nur für Legacy-Dienste in vertrauenswürdigen Netzen verwendet werden.

Für das Portal gilt zusätzlich: ``use-local-url-scheme`` (``portal.config``, :ref:`Details <portal-config-security>`) darf nur
in lokalen oder Offline-Umgebungen ``true`` sein, weil der Schlüsselaustausch dann unverschlüsselt über HTTP erfolgt.

.. _annex-security-csrf:

Schutz vor CSRF
---------------

Die Formulare der Subscriber-Verwaltung der API (Anmeldung, Registrierung, Konto, Zwei-Faktor-Authentifizierung) und weitere
schreibende Endpunkte sind durch **Anti-Forgery-Token** gegen *Cross-Site Request Forgery* geschützt. Der Schlüssel ``disable-anti-forgery`` (Section ``security`` der ``api.config``, :ref:`Details <api-config-security>`)
schaltet diese Prüfung ab (Standard ``false``). Das ist nur in Sonderfällen sinnvoll, z. B. wenn die API ausschließlich als
Backend für eine andere Anwendung dient oder ein Reverse Proxy die Prüfung verhindert. Im Internet nicht verwenden.

.. _annex-security-endpoints:

Gesicherte Endpunkte
--------------------

Wartungsendpunkte wie ``cache/clear`` sind standardmäßig **ohne Anmeldung** erreichbar, damit die Wartung (z. B. nach einem
CMS-Deployment) funktioniert. Sobald in Section ``security`` der ``api.config`` bzw. der ``portal.config`` Zugangsdaten
hinterlegt sind, ist der Endpunkt nur noch mit gültigen Credentials erreichbar
(:ref:`api.config <api-config-security>`, :ref:`portal.config <portal-config-security>`):

- ``secure-endpoint-url-password``: Passwort, das als Query-Parameter ``pwd`` übergeben wird.
- ``secure-endpoint-basicauth-username`` und ``secure-endpoint-basicauth-password``: Zugangsdaten für HTTP Basic Authentication.

In öffentlich zugänglichen Instanzen müssen diese Schlüssel gesetzt werden; im Intranet wird es empfohlen.

.. _annex-security-proxy:

Reverse Proxy und Client-IP
---------------------------

Läuft die API hinter einem Reverse Proxy, sieht sie standardmäßig die IP-Adresse des Proxies statt jener des Clients.
Das beeinträchtigt u. a. die IP-Drosselung der Anmeldung (:ref:`Details <api-config-middleware>`):

- ``use-x-forwarded-headers`` (Section ``middleware``): übernimmt die *X-Forwarded*-Header (Standard ``false``). Nur hinter einem
  Reverse Proxy aktivieren.
- ``x-forwarded-known-proxies`` und ``x-forwarded-known-networks``: Die Header werden nur von diesen vertrauenswürdigen Proxies
  (IP-Adressen bzw. Netzwerke in CIDR-Schreibweise) übernommen, standardmäßig nur von ``localhost``. Nur die tatsächlich
  verwendeten Proxies eintragen, keine breiten Netze.
- ``use-x-forwarded-headers-logging``: protokolliert die Header (nur zur Fehlersuche).

.. _annex-security-keys:

Übersicht aller sicherheitsrelevanten Schlüssel
-----------------------------------------------

**Kategorien**

- **Kompatibilitäts-Opt-out:** Ein Schutz ist standardmäßig aktiv und kann aus Gründen der Abwärtskompatibilität abgeschaltet
  oder aufgeweicht werden. Die Aktivierung der Ausnahme schwächt die Sicherheit und sollte nur bei Bedarf und mit Kenntnis des
  Risikos erfolgen.
- **Feature-Freischaltung:** Eine Funktion ist erst nach Aktivierung verfügbar. Die Aktivierung vergrößert die Angriffsfläche.
- **Feinjustierung:** Werte, mit denen ein Schutzmechanismus angepasst wird (Zeiten, Grenzwerte, Zugangsdaten, Listen).

**Risikostufen** (Auswirkung eines unsicheren Wertes bzw. der Aktivierung der Ausnahme; Standardwerte sind sicher gewählt)

- **Hoch:** Ein Angriff ist direkt möglich oder ein Schutzmechanismus wird vollständig ausgehebelt (z. B. Übernahme von
  Konten, Zugriff auf interne Systeme, Abhören oder Manipulation des Datenverkehrs).
- **Mittel:** Der Schutz wird spürbar geschwächt; ein Angriff benötigt zusätzliche Voraussetzungen.
- **Niedrig:** Geringe Auswirkung; Defense in Depth.
- **Info:** Keine direkte Auswirkung auf die Sicherheit; Betriebs- oder Hinweisschlüssel.

Die Schlüssel sind als ``section:key`` angegeben, wenn sie in einer *Section* der Konfigurationsdatei stehen (z. B.
``security:cookie-secure``); der Link führt zur Beschreibung in der jeweiligen Konfigurationsdokumentation. Die
Empfehlungen gelten für Standardinstallationen. Dort, wo nicht anders angegeben, entspricht die Empfehlung dem Standardwert.

.. list-table::
   :widths: 20 9 12 7 26 26
   :header-rows: 1

   * - **Schlüssel**
     - **Datei**
     - **Kategorie**
     - **Risiko**
     - **Empfehlung Internet**
     - **Empfehlung Intranet**
   * - :ref:`allow-subscriber-login <api-config-subscriber-registration>`
     - api.config
     - Feature-Freischaltung
     - Hoch
     - ``false``
     - ``true`` nur, wenn Kartenautoren/Administratoren sich anmelden müssen (ohne Eintrag: ``false``)
   * - :ref:`allow-subscriber-login <portal-config-advanced-security>`
     - portal.config
     - Feature-Freischaltung
     - Hoch
     - ``false``
     - ``true`` nur, wenn Kartenautoren/Administratoren sich anmelden müssen (ohne Eintrag: ``false``)
   * - :ref:`allow-register-new-subscribers <api-config-subscriber-registration>`
     - api.config
     - Feature-Freischaltung
     - Hoch
     - ``false`` (nie aktivieren)
     - Nur während der Installation ``true`` (ersten Administrator anlegen), danach ``false``
   * - :ref:`subscriber-db-connectionstring <api-config-subscriber-db>`
     - api.config
     - Feinjustierung
     - Info
     - Zugriff auf Datenbank bzw. Verzeichnis einschränken; Wert in api.config und portal.config identisch
     - Wie Internet
   * - :ref:`subscriber-db-connectionstring <portal-config-subscriber-db>`
     - portal.config
     - Feinjustierung
     - Info
     - Wie in api.config
     - Wie in api.config
   * - :ref:`subscriber-login-allowed-redirect-hosts <api-config-subscriber-registration>`
     - api.config
     - Feinjustierung
     - Mittel
     - Leer lassen oder nur eigene Hosts eintragen
     - Wie Internet
   * - :ref:`security:cookie-secure <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``auto`` (korrekte Proxy-Konfiguration vorausgesetzt) oder ``always``; nie ``never``
     - ``auto``; ``always`` bei durchgängigem HTTPS
   * - :ref:`security:session-max-lifetime-minutes <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``480`` oder kürzer; nicht ``0``
     - ``480``
   * - :ref:`security:session-idle-timeout-minutes <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - z. B. ``30`` bis ``60``
     - Optional
   * - :ref:`security:password-min-length <api-config-security-password-rules>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``12`` oder mehr
     - ``12`` oder mehr
   * - :ref:`security:password-required-character-classes <api-config-security-password-rules>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``0`` (Länge und Sperrliste sind wirksamer)
     - ``0``
   * - :ref:`security:password-blocklist-file <api-config-security-password-rules>`
     - api.config
     - Feinjustierung
     - Niedrig
     - Empfohlen: Liste kompromittierter Passwörter
     - Optional
   * - :ref:`security:login-captcha-after-failed-attempts <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``3`` oder weniger
     - ``3``
   * - :ref:`security:login-lockout-after-failed-attempts <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``10`` oder weniger; nicht ``0``
     - ``10``
   * - :ref:`security:login-lockout-minutes <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``1,5,15`` oder länger
     - ``1,5,15``
   * - :ref:`security:login-failed-attempts-reset-minutes <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``60``
     - ``60``
   * - :ref:`security:login-ip-max-failed-attempts <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``30`` oder weniger; nicht ``0``
     - ``30``
   * - :ref:`security:login-ip-window-minutes <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``15``
     - ``15``
   * - :ref:`security:login-throttle-redis-connectionstring <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - Bei mehreren Instanzen (Load Balancing) setzen
     - Nur bei mehreren Instanzen
   * - :ref:`security:captcha-lifetime-minutes <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``5``
     - ``5``
   * - :ref:`security:password-verification-cache-seconds <api-config-security-subscriber-login>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``300`` oder weniger
     - ``300``
   * - :ref:`security:mfa-required <api-config-security-mfa>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``admins`` oder ``all``
     - ``admins`` empfohlen; ``none`` möglich
   * - :ref:`security:mfa-issuer <api-config-security-mfa>`
     - api.config
     - Feinjustierung
     - Info
     - Name in der Authenticator-App
     - Name in der Authenticator-App
   * - :ref:`security:allow-untrusted-server-certificates <api-config-security-untrusted-certificates>`
     - api.config
     - Kompatibilitäts-Opt-out
     - Hoch
     - ``false``; interne CA im Zertifikatsspeicher des Servers installieren
     - ``false``; ``true`` nur für Legacy-Dienste in vertrauenswürdigen Netzen
   * - :ref:`security:allow-untrusted-server-certificates <portal-config-security>`
     - portal.config
     - Kompatibilitäts-Opt-out
     - Hoch
     - ``false``; interne CA im Zertifikatsspeicher des Servers installieren
     - ``false``; ``true`` nur für Legacy-Dienste in vertrauenswürdigen Netzen
   * - :ref:`allow_untrusted_server_certificates <cms-config-settings-security>`
     - settings.config (CMS)
     - Kompatibilitäts-Opt-out
     - Hoch
     - ``false``; interne CA im Zertifikatsspeicher des Servers installieren
     - ``false``; ``true`` nur für Legacy-Dienste in vertrauenswürdigen Netzen
   * - :ref:`security:disable-anti-forgery <api-config-security>`
     - api.config
     - Kompatibilitäts-Opt-out
     - Hoch
     - ``false``
     - ``false``; ``true`` nur in Sonderfällen (Backend für andere Anwendung, Reverse Proxy)
   * - :ref:`security:secure-endpoint-url-password <api-config-security>`
     - api.config
     - Feinjustierung
     - Mittel
     - Setzen (starkes Passwort)
     - Setzen empfohlen
   * - :ref:`security:secure-endpoint-basicauth-username <api-config-security>`
     - api.config
     - Feinjustierung
     - Mittel
     - Setzen (gemeinsam mit dem Passwort)
     - Setzen empfohlen
   * - :ref:`security:secure-endpoint-basicauth-password <api-config-security>`
     - api.config
     - Feinjustierung
     - Mittel
     - Setzen (starkes Passwort)
     - Setzen empfohlen
   * - :ref:`security:secure-endpoint-url-password <portal-config-security>`
     - portal.config
     - Feinjustierung
     - Mittel
     - Setzen (starkes Passwort)
     - Setzen empfohlen
   * - :ref:`security:secure-endpoint-basicauth-username <portal-config-security>`
     - portal.config
     - Feinjustierung
     - Mittel
     - Setzen (gemeinsam mit dem Passwort)
     - Setzen empfohlen
   * - :ref:`security:secure-endpoint-basicauth-password <portal-config-security>`
     - portal.config
     - Feinjustierung
     - Mittel
     - Setzen (starkes Passwort)
     - Setzen empfohlen
   * - :ref:`use-local-url-scheme <portal-config-security>`
     - portal.config
     - Kompatibilitäts-Opt-out
     - Hoch
     - ``false``
     - ``false`` (auch im Intranet HTTPS verwenden); ``true`` nur in Offline-/Testumgebungen
   * - :ref:`dynamic-content:allow-hosts <api-config-dynamic-content>`
     - api.config
     - Kompatibilitäts-Opt-out
     - Hoch
     - Leer (nur öffentliche Ziele)
     - Nur konkrete interne Hostnamen, keine breiten Muster
   * - :ref:`dynamic-content:allow-unsigned <api-config-dynamic-content>`
     - api.config
     - Kompatibilitäts-Opt-out
     - Hoch
     - ``false``
     - ``false``; ``true`` nur, wenn unsignierte Karten (MapBuilder-HTML, ``custom.js``) zwingend benötigt werden
   * - :ref:`dynamic-content:timeout-seconds <api-config-dynamic-content>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``20`` oder weniger
     - ``20``
   * - :ref:`dynamic-content:max-response-bytes <api-config-dynamic-content>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``52428800`` (50 MB) oder weniger
     - ``52428800``
   * - :ref:`dynamic-content:max-redirects <api-config-dynamic-content>`
     - api.config
     - Feinjustierung
     - Niedrig
     - ``5`` oder weniger
     - ``5``
   * - :ref:`lookup:term-whitelist <api-config-lookup>`
     - api.config
     - Feinjustierung
     - Mittel
     - Standard; nur um tatsächlich benötigte Zeichen erweitern
     - Standard
   * - :ref:`add-cors-origins-for-hmac <portal-config-advanced-security>`
     - portal.config
     - Feinjustierung
     - Hoch
     - Nur benötigte Drittseiten; nie ``~``
     - Nur benötigte Drittseiten; nie ``~``
   * - :ref:`add-cors-origins-for-default <portal-config-advanced-security>`
     - portal.config
     - Feinjustierung
     - Hoch
     - Leer; nie ``~``
     - Leer; nie ``~``
   * - :ref:`cors-default-allow-any-origin-without-credentials <portal-config-advanced-security>`
     - portal.config
     - Kompatibilitäts-Opt-out
     - Niedrig
     - ``false``
     - ``false``
   * - :ref:`middleware:use-x-forwarded-headers <api-config-middleware>`
     - api.config
     - Feinjustierung
     - Mittel
     - ``true`` nur hinter einem Reverse Proxy
     - ``true`` nur hinter einem Reverse Proxy
   * - :ref:`middleware:x-forwarded-known-proxies <api-config-middleware>`
     - api.config
     - Feinjustierung
     - Mittel
     - Nur die tatsächlich verwendeten Proxies
     - Nur die tatsächlich verwendeten Proxies
   * - :ref:`middleware:x-forwarded-known-networks <api-config-middleware>`
     - api.config
     - Feinjustierung
     - Mittel
     - Nur die Netze der verwendeten Proxies (CIDR), keine breiten Netze
     - Nur die Netze der verwendeten Proxies (CIDR), keine breiten Netze
   * - :ref:`middleware:use-x-forwarded-headers-logging <api-config-middleware>`
     - api.config
     - Feinjustierung
     - Info
     - ``false`` (nur zur Fehlersuche)
     - ``false`` (nur zur Fehlersuche)
