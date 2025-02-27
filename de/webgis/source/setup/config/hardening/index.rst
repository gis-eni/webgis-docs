================================
Sicherheitsmaßnahmen (Hardening)
================================

Eine sichere Konfiguration des *WebGIS Portals* ist essenziell, um **Datenverluste, unbefugten Zugriff und Manipulationen** zu verhindern. Selbst wenn die Anwendung nur **im Intranet** genutzt wird, sind zusätzliche Schutzmaßnahmen notwendig, da **die gleichen sensiblen Daten übertragen und gespeichert werden wie bei einer öffentlich zugänglichen Anwendung**.  

.. caution::

    Web-Security ist ein komplexes Thema, das je nach Organisation unterschiedliche Anforderungen haben kann. Diese Beschreibung dient daher lediglich als Orientierungspunkt und stellt eine empfohlene Mindestkonfiguration dar. Es wird empfohlen, weitere Sicherheitsmaßnahmen individuell an die spezifischen Gegebenheiten der eigenen IT-Infrastruktur anzupassen.

Dieser Abschnitt beschreibt empfohlene Sicherheitsmaßnahmen, um das System bestmöglich zu schützen. 


HTTPS auch im Intranet verwenden
================================

Viele glauben, dass ein Intranet automatisch sicher ist, weil es nicht direkt aus dem Internet erreichbar ist. Doch das ist ein Irrtum! Auch innerhalb eines Firmennetzwerks gibt es Risiken:

- **Mitarbeitergeräte können infiziert sein** (z. B. durch Phishing oder Malware) und so sensible Daten ausspähen.
- **Daten werden unverschlüsselt übertragen**, wenn kein HTTPS verwendet wird. Das bedeutet, dass Passwörter, Sitzungsinformationen und persönliche Daten von Angreifern oder Schadsoftware mitgelesen werden könnten.
- **Interne Angriffe sind möglich**: Personen mit Zugang zum Netzwerk könnten absichtlich oder versehentlich Daten abfangen oder manipulieren.
- **Zukünftige Browser-Versionen blockieren unverschlüsselte Verbindungen**, was langfristig zu Problemen führen kann.

Deshalb sollte das *WebGIS Portal* immer über **HTTPS** betrieben werden, auch wenn es nur intern genutzt wird. Weitere Informationen zur Bedeutung von HTTPS und möglichen Angriffen sind in der OWASP-Dokumentation zu finden:

`Transport Layer Security Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>`_

Standardpasswörter ändern
=========================

Bei der Erstinstallation enthält das System vordefinierte Benutzerkonten mit Standardpasswörtern, die allgemein bekannt sind. Diese Passwörter sollten **sofort nach der Installation** geändert werden, um unbefugten Zugriff zu verhindern.

Warum ist das wichtig?  
----------------------

Standardpasswörter wie ``admin123`` oder ``webgisauthor`` sind **besonders anfällig für Brute-Force-Angriffe**.  
Ein Brute-Force-Angriff ist eine Methode, bei der automatisierte Programme Millionen von Passwörtern ausprobieren, bis das richtige gefunden wird. Je kürzer und einfacher das Passwort, desto schneller kann es geknackt werden.  

Beispiel:  

- Ein Passwort wie ``admin123`` kann mit gängiger Hardware **in wenigen Sekunden** geknackt werden.  
- Ein sicheres Passwort mit **mindestens 12 Zeichen, Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen** benötigt hingegen **Jahre oder sogar Jahrhunderte**, um per Brute-Force entschlüsselt zu werden.  

.. tip::

    Für den **Author-Account** und den **Admin-Account in der API** sollten **starke, individuelle Passwörter** gewählt werden. Eine gute Passwortstrategie umfasst:  

    - **Mindestens 12 Zeichen** (besser 16+).  
    - **Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen**.  
    - **Kein Bezug zu realen Namen, Geburtsdaten oder Wörtern im Wörterbuch**.  
    - **Jedes Konto sollte ein eigenes, einmaliges Passwort haben**.  
    - Falls möglich: **Zwei-Faktor-Authentifizierung (2FA) aktivieren**.  

Zum Generieren und sicheren Speichern von Passwörtern empfiehlt sich die Verwendung eines **Passwortmanagers**.  

Mehr zur Sicherheit von Passwörtern und Brute-Force-Angriffen:  
`OWASP Authentication Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>`_

Author-Account
--------------

Dieses Konto wird für das **Bearbeiten und Veröffentlichen von Inhalten** genutzt. Wenn das Standardpasswort nicht geändert wird, könnten sich andere Personen unbefugt einloggen und Karten oder andere Daten manipulieren.

Admin-Account in der API
------------------------

Der API-Administrator hat **erweiterte Rechte**, um wichtige Einstellungen der Anwendung zu ändern. Ein Angreifer mit Zugriff auf dieses Konto könnte die gesamte Anwendung kontrollieren oder sogar Daten löschen. Deshalb ist es entscheidend, das Standardpasswort zu ersetzen.

Um einen **Admin-Benutzer** für die API anzulegen, folgen Sie diesen Schritten:

1. **Öffnen der Registrierungsseite**

   Rufen Sie die folgende URL im Browser auf: `http://hostname:5001/Subscribers/Login`. Der Hostname und das Port müssen an die jeweilige Konfiguration angepasst werden.

   .. image:: img/create_admin_1.png

2. **Registrierung starten**

   Klicken Sie auf **"Register as new subscriber"**.

3. **Formular ausfüllen**

   Geben Sie die erforderlichen Informationen im Registrierungsformular ein.  

   .. image:: img/create_admin_2.png  

   - Das Passwort muss mindestens **8 Zeichen** lang sein.

   .. danger::

     **Achten Sie auf ein starkes Passwort!** Die Mindestlänge ist eine technische Vorgabe, aber basierend auf den vorherigen Sicherheitshinweisen sollten Sie ein möglichst sicheres Passwort wählen.  

   .. important::

     Der Benutzername **muss** mit den Standard-Einstellungen zwingend ``admin`` sein. Die *WebGIS API* verwendet intern diesen **festgelegten Namen**, um den Benutzer der **Admin-Rolle** zuzuweisen. Ohne diesen Namen erhält der Benutzer keine Administratorrechte.

     Welche Benutzername die Administratorenrolle zugeordnet bekommen, wird in der Konfigurationsdatei der Api ``_config/api.config`` festgelegt
     
     .. code:: xml

        <?xml version="1.0" encoding="utf-8" ?>
        <configuration>
          <appSettings>
            ...
            <add key="subscriber-admins" value="admin" />
            ...
          </appSettings>
        <configuration>

Selbstregistrierung für Subscriber deaktivieren
===============================================

Sobald alle notwendigen Benutzerkonten angelegt wurden, sollte die **Selbstregistrierung für Subscriber** deaktiviert werden. Andernfalls könnten sich beliebige Nutzer eigenständig einen Account erstellen, was in den meisten Fällen nicht erwünscht ist.  

Nach der Deaktivierung können neue Benutzerkonten nur noch manuell über das **Admin-Konto** angelegt werden.

Die Selbstregistrierung wird deaktiviert, indem in der Konfigurationsdatei der API (``_config/api.config``) der Wert für ``allow-register-new-subscribers`` auf ``false`` gesetzt wird:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8" ?>
   <configuration>
      <appSettings>
         ...
         <add key="allow-register-new-subscribers" value="false" /> 
         ...
      </appSettings>
   </configuration>

Sobald diese Einstellung vorgenommen wurde, ist die **Selbstregistrierung für Subscriber deaktiviert**.

Anmeldemöglichkeiten in öffentlich zugänglichen Instanzen deaktivieren
======================================================================

Um zu verhindern, dass sich Benutzer in einer **öffentlichen Installation** von WebGIS anmelden können, muss die Anmeldung sowohl im **Portal** als auch in der **API** deaktiviert werden.

.. tip::

  Diese Einstellung ist besonders dann sinnvoll, wenn eine Konfiguration von **internen Installationen** auf eine **öffentlich zugängliche Instanz** übertragen wird, da sichergestellt werden muss, dass sich **keine externen Benutzer anmelden können**.

Die Anmeldung wird deaktiviert, indem in den Konfigurationsdateien der API (``_config/api.config``) und des Portals (``_config/portal.config``) der Wert für ``allow-subscriber-login`` auf ``false`` gesetzt wird:

API-Konfigurationsdatei (``_config/api.config``)
------------------------------------------------

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8" ?>
   <configuration>
      <appSettings>
         ...
         <add key="allow-subscriber-login" value="false" />
         ...
      </appSettings>
   </configuration>

Portal-Konfigurationsdatei (``_config/portal.config``)
------------------------------------------------------

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8" ?>
   <configuration>
      <appSettings>
         ...
         <add key="allow-subscriber-login" value="false" />
         ...
      </appSettings>
   </configuration>

Sobald diese Einstellung in beiden Konfigurationsdateien vorgenommen wurde, ist die **Anmeldung für Benutzer in der öffentlichen Instanz deaktiviert**.


Weitere empfohlene Sicherheitsmaßnahmen
=======================================

Neben HTTPS und der Änderung von Standardpasswörtern gibt es weitere wichtige Maßnahmen, um die Anwendung abzusichern:

- **Zugriff auf die Administrationsoberfläche einschränken**  
  Falls möglich, sollte nur ein **bestimmter Personenkreis oder nur Geräte aus dem internen Netzwerk** Zugriff auf die Administration haben.

- **Sicherheitsmechanismen des Browsers nutzen**  
  Es sollten Sicherheitsfunktionen wie ``Strict-Transport-Security (HSTS)`` und ``Content-Security-Policy (CSP)`` aktiviert werden, um Angriffe durch Schadcode zu verhindern.

- **Regelmäßige Updates durchführen**  
  Veraltete Software kann Sicherheitslücken enthalten. Es ist wichtig, sowohl das *WebGIS Portal* als auch alle verwendeten Server, Datenbanken und Drittanbieter-Komponenten regelmäßig zu aktualisieren.

- **Verdächtige Aktivitäten überwachen**  
  Das System sollte protokollieren, wer sich wann eingeloggt hat. Wenn sich jemand mit falschen Passwörtern anmeldet oder ungewöhnlich oft auf die Administration zugreift, könnte dies ein Hinweis auf einen Angriff sein. In diesem Fall sollten Administratoren benachrichtigt werden.

Weiterführende Informationen für Interessierte
==============================================

Es gibt eine Vielzahl von **möglichen Angriffsszenarien**, die auch Intranet-Anwendungen betreffen. Dazu gehören:

- **Man-in-the-Middle-Angriffe (MITM)**, bei denen ein Angreifer den Netzwerkverkehr mitliest.
- **Session Hijacking**, bei dem eine Sitzung eines Nutzers gestohlen wird, um sich als dieser auszugeben.
- **Cross-Site Scripting (XSS)**, bei dem Schadcode in das System eingeschleust wird.

Mehr zu diesen Angriffstechniken und wie man sich dagegen schützt, findet sich in der OWASP-Dokumentation:  
`OWASP Top 10 Security Risks <https://owasp.org/www-project-top-ten/>`_

Durch die Umsetzung dieser Maßnahmen wird das *WebGIS Portal* optimal geschützt und bleibt sicher und zuverlässig – egal ob im Intranet oder öffentlich im Internet.
