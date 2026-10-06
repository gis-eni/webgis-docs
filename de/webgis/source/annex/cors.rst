.. _annex-cors:

CORS und der HMAC-Endpunkt
==========================

Wird eine WebGIS API Anwendung nicht im Portal selbst, sondern auf einer **Drittseite** (einem anderen Server) eingebunden,
muss diese Seite in der ``portal.config`` freigegeben werden. Dieses Kapitel erklärt, warum das notwendig ist und wie es konfiguriert wird.

.. contents:: Inhalt dieser Seite
   :local:
   :depth: 2

Hintergrund: Same-Origin-Policy und CORS
----------------------------------------

Ein Browser erlaubt es JavaScript-Code standardmäßig nur, Antworten von der **eigenen Origin** zu lesen.
Eine *Origin* besteht aus Schema, Host und Port, z. B. ``https://example.com`` (``https://example.com:8443`` und ``http://example.com`` sind jeweils andere Origins).
Das ist die sogenannte *Same-Origin-Policy*.

Soll eine Seite auf ``https://example.com`` trotzdem Antworten eines anderen Servers (z. B. ``https://webgisserver.com``) lesen dürfen,
muss der andere Server dies über *CORS* (*Cross-Origin Resource Sharing*) ausdrücklich erlauben.
Dazu sendet der Server den HTTP-Header ``Access-Control-Allow-Origin`` mit der erlaubten Origin zurück.
Fehlt dieser Header oder passt die Origin nicht, verwirft der Browser die Antwort und der Aufruf schlägt fehl.

Wozu dient der HMAC-Endpunkt?
-----------------------------

Das Portal stellt den Endpunkt ``https://webgisserver.com/portal/hmac`` bereit.
Über diesen werden Zugangsdaten (Keys) für den Zugriff auf die API für den **aktuell angemeldeten Benutzer** abgeholt.
Eine WebGIS API Anwendung ruft diesen Endpunkt auf, um sich gegenüber der API als dieser Benutzer auszuweisen.

Das Problem: Der Browser sendet bei einem solchen Aufruf die Anmeldung des Benutzers am Portal (Cookie) automatisch mit.
Ohne Schutz könnte daher **jede beliebige Webseite** im Hintergrund den ``hmac``-Request aufrufen und die Keys für den Besucher der Seite abfragen:

1. Ein angemeldeter Benutzer besucht eine Schadseite ``https://evil.example``.
2. Deren JavaScript ruft ``https://webgisserver.com/portal/hmac`` auf.
3. Ohne CORS-Schutz könnte die Seite die Antwort lesen und hätte damit Zugriff auf die API im Namen des Benutzers.

Mit der CORS-Policy beantwortet das Portal den ``hmac``-Request nur dann mit einem passenden ``Access-Control-Allow-Origin``-Header,
wenn die aufrufende Origin ausdrücklich freigegeben wurde. Für alle anderen Seiten verweigert der Browser das Lesen der Antwort.

Konfiguration
-------------

Die erlaubten Origins werden in der Datei ``_config/portal.config`` mit dem Schlüssel ``add-cors-origins-for-hmac``
als **kommagetrennte Liste** angegeben (Beschreibung des Schlüssels: :doc:`../config/portal/index`, Abschnitt ``Advanced Security``):

.. code-block:: xml

   <add key="add-cors-origins-for-hmac" value="https://localhost,https://example.com" />

Regeln:

* Es sind **alle Server** anzuführen, auf denen eine WebGIS API Anwendung eingebunden ist.
* Jeder Eintrag besteht aus Schema, Host und ggf. Port, **ohne Pfad und ohne abschließenden Schrägstrich**
  (``https://example.com`` bzw. ``https://example.com:8443``).
* Schema und Port müssen exakt stimmen: ``https://example.com`` erlaubt weder ``http://example.com`` noch ``https://www.example.com``.
* Einträge werden durch Komma getrennt, ohne Leerzeichen.
* Seiten, die vom selben Server wie das Portal ausgeliefert werden (gleiche Origin), benötigen keinen Eintrag.
* Nach einer Änderung der ``portal.config`` ist die Portal-Anwendung neu zu starten.

Beispiel
--------

Das Portal läuft auf ``https://webgisserver.com/portal``.
Die Gemeinde betreibt eine eigene Webseite ``https://gemeinde.example.org/karte.html``, in die eine WebGIS API Anwendung eingebunden ist.
Zusätzlich wird lokal entwickelt (``https://localhost``).
Die ``portal.config`` lautet dann:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <configuration>
     <appSettings>
       <!-- ... weitere Einstellungen ... -->

       <!-- Erlaubte Origins (CORS) für den HMAC-Endpunkt -->
       <add key="add-cors-origins-for-hmac"
            value="https://gemeinde.example.org,https://localhost" />
     </appSettings>
   </configuration>

Ergebnis:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Aufrufende Seite
     - Ergebnis
   * - ``https://gemeinde.example.org/karte.html``
     - erlaubt (Origin ``https://gemeinde.example.org`` ist eingetragen)
   * - ``https://localhost``
     - erlaubt
   * - ``http://gemeinde.example.org``
     - **blockiert** (anderes Schema)
   * - ``https://www.gemeinde.example.org``
     - **blockiert** (anderer Host)
   * - ``https://evil.example``
     - **blockiert** (nicht eingetragen)

Fehlersuche
-----------

Ist eine Origin nicht eingetragen, funktioniert die eingebundene Anwendung nicht wie erwartet (z. B. keine Anmeldung an der API).
In den Entwicklertools des Browsers (F12, Konsole bzw. Netzwerk) erscheint dann eine Meldung ähnlich:

.. code-block:: text

   Access to fetch at 'https://webgisserver.com/portal/hmac' from origin
   'https://gemeinde.example.org' has been blocked by CORS policy: No
   'Access-Control-Allow-Origin' header is present on the requested resource.

In diesem Fall ist die in der Meldung genannte Origin (hier ``https://gemeinde.example.org``) in ``add-cors-origins-for-hmac`` zu ergänzen.

Wildcard ``~``
--------------

Der Wert ``~`` ist ein Wildcard und erlaubt **alle** Seiten:

.. code-block:: xml

   <add key="add-cors-origins-for-hmac" value="~" />

.. danger::

   Der Wildcard hebt den oben beschriebenen Schutz vollständig auf. Er sollte nur in Ausnahmefällen zum Testen verwendet werden
   und **niemals in einer Produktionsumgebung**.
