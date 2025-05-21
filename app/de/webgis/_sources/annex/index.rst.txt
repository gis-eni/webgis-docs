======
Anhang
======

Sicherheitsmaßnahmen für das WebGIS Portal
==========================================

Tipps zur Passwortsicherheit
----------------------------

Ein sicheres Passwort ist der erste Schritt, um das *WebGIS Portal* zu schützen. Hier sind einige Tipps, wie Sie ein starkes Passwort erstellen können:

Standardpasswörter wie ``admin123`` oder ``webgisauthor`` sind **besonders anfällig für Brute-Force-Angriffe**. Ein Brute-Force-Angriff ist eine Methode, bei der automatisierte Programme Millionen von Passwörtern ausprobieren, bis das richtige gefunden wird. Je kürzer und einfacher das Passwort, desto schneller kann es geknackt werden.  

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

HTTPS auch im Intranet verwenden
--------------------------------

Viele glauben, dass ein Intranet automatisch sicher ist, weil es nicht direkt aus dem Internet erreichbar ist. Doch das ist ein Irrtum! Auch innerhalb eines Firmennetzwerks gibt es Risiken:

- **Mitarbeitergeräte können infiziert sein** (z. B. durch Phishing oder Malware) und so sensible Daten ausspähen.
- **Daten werden unverschlüsselt übertragen**, wenn kein HTTPS verwendet wird. Das bedeutet, dass Passwörter, Sitzungsinformationen und persönliche Daten von Angreifern oder Schadsoftware mitgelesen werden könnten.
- **Interne Angriffe sind möglich**: Personen mit Zugang zum Netzwerk könnten absichtlich oder versehentlich Daten abfangen oder manipulieren.
- **Zukünftige Browser-Versionen blockieren unverschlüsselte Verbindungen**, was langfristig zu Problemen führen kann.

Deshalb sollte das *WebGIS Portal* immer über **HTTPS** betrieben werden, auch wenn es nur intern genutzt wird. Weitere Informationen zur Bedeutung von HTTPS und möglichen Angriffen sind in der OWASP-Dokumentation zu finden:

`Transport Layer Security Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>`_

Weitere empfohlene Sicherheitsmaßnahmen
---------------------------------------

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
----------------------------------------------

Es gibt eine Vielzahl von **möglichen Angriffsszenarien**, die auch Intranet-Anwendungen betreffen. Dazu gehören:

- **Man-in-the-Middle-Angriffe (MITM)**, bei denen ein Angreifer den Netzwerkverkehr mitliest.
- **Session Hijacking**, bei dem eine Sitzung eines Nutzers gestohlen wird, um sich als dieser auszugeben.
- **Cross-Site Scripting (XSS)**, bei dem Schadcode in das System eingeschleust wird.

Mehr zu diesen Angriffstechniken und wie man sich dagegen schützt, findet sich in der OWASP-Dokumentation:  
`OWASP Top 10 Security Risks <https://owasp.org/www-project-top-ten/>`_

Durch die Umsetzung dieser Maßnahmen wird das *WebGIS Portal* optimal geschützt und bleibt sicher und zuverlässig – egal ob im Intranet oder öffentlich im Internet.
