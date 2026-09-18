Applikations-Logging (Konsole / OpenTelemetry / Serilog / Seq)
==================================================================

.. note::

   Diese Seite beschreibt ausschließlich die **Applikations-/Host-Logging**-Ebene - also wohin
   die vom ``Microsoft.Extensions.Logging``-Pipeline erzeugten Log-Ereignisse von ASP.NET Core
   selbst sowie von den WebGIS-internen Komponenten geschrieben werden. Sie ist unabhängig vom
   **GeoService Performance-/Exception-Logging** (``Api:logging-type``), das im Kapitel
   :doc:`../config/api/index` beschrieben ist und eigene ``webgis_performance``/
   ``webgis_exceptions``-Datensätze schreibt statt generischer Applikations-Log-Ereignisse - beide
   Ebenen können am Ende auf demselben Datenbankserver landen, nur in unterschiedlichen Tabellen.

Die Anwendungen ``Api``, ``Cms`` und ``Portal`` verwenden denselben Aufbau, alles Folgende gilt
daher für alle drei (Dateinamen entsprechend anpassen, z. B. ``Cms/appsettings.json``).

.. important::

   ``MicrosoftGeoServiceRequestLogger`` (der ``microsoft``-``IGeoServiceRequestLogger``, also das
   Request-Audit-Log pro Anfrage, im Unterschied zu den Performance-Zeitmessungen) loggt auf
   Level ``LogLevel.Trace`` - der ausführlichsten Stufe, die standardmäßig deaktiviert ist. Da
   ``Logging:LogLevel:Default`` normalerweise auf ``Information`` steht, wird für diese Kategorie
   nichts geschrieben, solange sie nicht explizit überschrieben wird (es genügt **nicht**, nur
   ``Default`` anzuheben, da ``Trace`` ausführlicher als ``Information`` ist):

   .. code-block:: json

      {
        "Logging": {
          "LogLevel": {
            "Default": "Information",
            "Api.Core.AppCode.Services.Logging.MicrosoftGeoServiceRequestLogger": "Trace"
          }
        }
      }

   Dies kann in ``appsettings.json``, ``_config/logging.json`` (siehe unten) oder als
   Umgebungsvariable
   ``Logging__LogLevel__Api.Core.AppCode.Services.Logging.MicrosoftGeoServiceRequestLogger=Trace``
   gesetzt werden. Besitzt ein bestimmter Provider (z. B. ``Console``) einen eigenen, engeren
   ``Logging:<Provider>:LogLevel``-Abschnitt, muss dieselbe Überschreibung auch dort gesetzt
   werden.

   Intern leitet WebGIS das Logging immer über Serilog, das normalerweise nur seinen eigenen
   Abschnitt ``Serilog:MinimumLevel`` beachtet und ``Logging:LogLevel`` komplett ignoriert; WebGIS
   überträgt ``Logging:LogLevel`` automatisch in Serilogs ``MinimumLevel``, sodass dieser
   Standard-ASP.NET-Core-Abschnitt weiterhin wie dokumentiert funktioniert. Ein expliziter
   ``Serilog:MinimumLevel``/``Override``-Eintrag für dieselbe Kategorie hat immer Vorrang vor dem
   überbrückten ``Logging:LogLevel``-Wert.

Konfiguration über ``_config`` (empfohlen für Produktion/Kubernetes)
-------------------------------------------------------------------------

Die meisten Kunden bearbeiten ausschließlich das ``_config``-Verzeichnis neben den
Anwendungs-Binaries (dort liegen auch ``api.config``/``cms.config``/``portal.config``) - in
einem Kubernetes-Deployment ist das typischerweise das einzige Verzeichnis, das per
ConfigMap/Secret-Volume gemountet wird, während ``appsettings.json`` und die
Umgebungsvariablen des Pods nicht (einfach) pro Instanz änderbar sind. Alles auf dieser Seite
kann daher auch über eine oder beide der folgenden optionalen Dateien in ``_config`` konfiguriert
werden, ganz ohne Rebuild und ohne Änderung der Pod-Spezifikation:

- **``_config/logging.json``** - eine reguläre JSON-Datei, die in die Standard-Konfiguration
  eingemischt wird, d. h. alles, was sonst nur über ``appsettings.json`` oder
  Umgebungsvariablen konfigurierbar wäre (``Logging``, ``Serilog``, ``OTEL_*``-Schlüssel, ...),
  kann stattdessen hier hinterlegt werden. Alle JSON-Beispiele dieser Seite funktionieren
  unverändert auch als Inhalt von ``_config/logging.json``.
- **``_config/logging.env``** - eine einfache Datei mit ``SCHLÜSSEL=WERT`` pro Zeile (wie eine
  Docker ``--env-file``, ``#`` leitet eine Kommentarzeile ein), die vor dem Start der Anwendung
  als echte Prozess-Umgebungsvariablen geladen wird. Nützlich für die unten gezeigten
  Standard-OpenTelemetry-Variablen ``OTEL_*``, da diese normalerweise als Umgebungsvariablen und
  nicht als verschachteltes JSON gesetzt werden. Eine bereits auf dem Prozess/Pod gesetzte
  Umgebungsvariable hat immer Vorrang vor der Datei.

Beispiel ``_config/logging.env``:

.. code-block:: text

   OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
   OTEL_EXPORTER_OTLP_PROTOCOL=grpc

Beide Dateien sind optional und wirken für ``Api``, ``Cms`` und ``Portal`` gleichermaßen; fehlt
eine Datei, hat das keine Auswirkung. ``_config/logging.json`` wird nach ``appsettings.json``/
``appsettings.<Environment>.json`` geladen und überschreibt diese somit (genau wie
``_config/*.config`` bereits heute andere Defaults überschreibt).

Konsole (Standard)
--------------------

Ohne weitere Konfiguration werden Logs an die Konsole (stdout) geschrieben, formatiert als
Klartext - das ist der ASP.NET-Core-Standard und erfordert keine Einstellung. Log-Level werden
wie gewohnt über den Abschnitt ``Logging:LogLevel`` in ``appsettings.json`` oder über
Umgebungsvariablen gesteuert (``Logging__LogLevel__Default=Information``, ...).

Für strukturierte JSON-Ausgabe auf der Konsole (nützlich, wenn ein Container-Log-Collector wie
Filebeat/Fluent Bit/Promtail stdout parst), wird der Konsolen-Formatter umgestellt:

.. code-block:: json

   {
     "Logging": {
       "Console": {
         "FormatterName": "json"
       }
     }
   }

OpenTelemetry (OTLP) - für die meisten Backends empfohlen
--------------------------------------------------------------

Die Anwendungen ``Api``, ``Cms`` und ``Portal`` exportieren Logs, Metriken und Traces über das
OpenTelemetry-Protokoll (OTLP), sobald ein OTLP-Endpunkt konfiguriert ist. Das wird ausschließlich
über die üblichen OpenTelemetry-Umgebungsvariablen gesteuert - es ist keine weitere Konfiguration
und kein Rebuild nötig:

.. code-block:: text

   OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
   OTEL_EXPORTER_OTLP_PROTOCOL=grpc        # oder "http/protobuf" für Port 4318
   OTEL_SERVICE_NAME=webgis-api            # optional, Default: Name des Hosts

Ist ``OTEL_EXPORTER_OTLP_ENDPOINT`` nicht gesetzt, wird kein OTLP-Exporter erzeugt und es
entsteht kein Overhead.

Diese Variablen können als reguläre Prozess-/Pod-Umgebungsvariablen gesetzt werden, oder - falls
nur das ``_config``-Verzeichnis verfügbar ist - über ``_config/logging.env`` (siehe oben).

Das ist der Weg mit dem geringsten Aufwand, um WebGIS an die meisten modernen
Observability-Backends anzubinden, da sie alle nativ OTLP sprechen (kein WebGIS-spezifischer
Sink nötig): ein OpenTelemetry Collector (der dann beliebig weiterverteilen kann),
Grafana-Stack (Loki/Tempo/Mimir), Elastic (ab 8.x / Elastic Cloud), Seq, Jaeger, Zipkin,
Honeycomb, Datadog, New Relic, Azure Monitor, AWS X-Ray/ADOT usw.

.. note::

   Bisher war das nur für die lokale Entwicklung verdrahtet (.NET Aspire). Es steht nun auch in
   Release-Builds von ``Api``, ``Cms`` und ``Portal`` zur Verfügung.

Request-Log-Einträge im Trace
++++++++++++++++++++++++++++++++

Jeder GeoService-Request (``GetMap``, ``GetSelection``, ..., Druckjobs) läuft innerhalb einer
eigenen ``geoservice:{command} {service}``-Trace-Span (``WebGIS.GeoServices``-``ActivitySource``,
mit den Tags ``webgis.category``/``command``/``server``/``service``/``map``/``success``). Solange
diese Span aktiv ist, wird jeder ``IGeoServiceRequestLogger.LogString(...)``-Aufruf (das
Request-Audit-Log - z. B. der zugrunde liegende HTTP-Request/Response an den echten GIS-Server)
zusätzlich als OpenTelemetry-Span-Event (``webgis.geoservice.request``, mit den Tags
``webgis.server``/``service``/``command``) an sie angehängt. In einem Trace-Viewer (z. B. der
Trace-Detailansicht des Aspire-Dashboards oder der dortigen Aktion "View Logs" für die
korrelierten Log-Einträge) bedeutet das, dass das Request-Audit-Log eines Aufrufs direkt neben
bzw. an seiner Span angezeigt wird, statt nur über einen separat gefilterten Log-Level sichtbar
zu sein. Das Aufzeichnen des Span-Events hängt nicht vom eigenen ``LogLevel.Trace`` des
``microsoft``-``IGeoServiceRequestLogger`` ab (siehe oben) - es entfällt nur, wenn niemand den
Trace sampelt/mitliest.

Request und Response werden als zwei getrennte Tags gehalten statt zu einem String
zusammengefügt:

- ``webgis.requestResult`` - die Antwort (bzw., bei Aufrufstellen, die nur einen einzelnen Wert
  loggen, dieser Wert) - typischerweise JSON, und für Tooling weiterhin als solches erkennbar, da
  nichts davorgestellt wird.
- ``webgis.requestBody`` - nur vorhanden, wenn tatsächlich ein Request-Body separat geloggt
  wurde (z. B. der ausgehende Request an den vorgelagerten GIS-Server).

Dieselbe Aufteilung gilt auch für den strukturierten Log-Eintrag selbst: Ist ein Request-Body
vorhanden, loggt der Request-Logger ``requestBody`` und ``message`` als getrennte, benannte
Platzhalter (statt eines vorab zusammengefügten Strings), sodass eine JSON-Antwort von
Log-Backends, die strukturierte Felder erkennen, weiterhin als JSON geparst wird.

Serilog-Sinks (SQL Server / PostgreSQL / Seq)
--------------------------------------------------

Für Deployments, bei denen Logs direkt in eine relationale Datenbank geschrieben werden sollen -
ohne einen OpenTelemetry Collector aufzusetzen - betreiben ``Api``, ``Cms`` und ``Portal``
zusätzlich `Serilog <https://serilog.net/>`_ parallel zur Standard-Logging-Pipeline, das diese
also ergänzt statt OTLP/Konsole zu ersetzen. Serilog ist rein konfigurationsgesteuert: Ohne
vorhandenen ``Serilog``-Abschnitt ändert sich nichts am Standardverhalten (nur Konsolenausgabe).

Um einen Sink hinzuzufügen, wird ein ``Serilog``-Abschnitt in ``appsettings.json`` (oder
``appsettings.Production.json`` bzw. Umgebungsvariablen) ergänzt - oder äquivalent in
``_config/logging.json`` (siehe oben).

SQL Server
++++++++++

.. code-block:: json

   {
     "ConnectionStrings": {
       "LogsDb": "Server=sql-host;Database=WebGisLogs;User Id=webgis;Password=***;TrustServerCertificate=True"
     },
     "Serilog": {
       "WriteTo": [
         {
           "Name": "MSSqlServer",
           "Args": {
             "connectionString": "LogsDb",
             "sinkOptions": {
               "tableName": "Logs",
               "autoCreateSqlTable": true
             }
           }
         }
       ]
     }
   }

PostgreSQL
++++++++++

Der PostgreSQL-Sink benötigt sein Konfigurations-Zusatzpaket, das explizit über ``Using``
eingebunden werden muss, und hat - anders als ``MSSqlServer``, das sinnvolle Standardspalten
mitbringt - **keine** eingebauten Defaults: Ein ``Columns``-Abschnitt, der beschreibt, welche
Spalten wie geschrieben werden, muss immer angegeben werden. Fehlt er, schlägt der Start sofort
fehl mit:

.. code-block:: text

   System.InvalidOperationException: 'Columns' section not found in provided configuration path:

Der ``Columns``-Abschnitt muss ein Schlüssel auf **oberster Ebene** der Konfiguration sein - ein
Geschwister von ``Serilog``/``ConnectionStrings``, *nicht* verschachtelt innerhalb von
``Serilog`` (das wird leicht falsch angenommen, da alles andere Serilog-Bezogene im
``Serilog``-Abschnitt liegt). Soll er an anderer Stelle liegen (z. B. um einen Namenskonflikt zu
vermeiden), kann explizit über ``Serilog:WriteTo:Args:configurationPath`` darauf verwiesen
werden.

.. code-block:: json

   {
     "ConnectionStrings": {
       "LogsDb": "Host=pg-host;Port=5432;Database=webgis_logs;Username=webgis;Password=***"
     },
     "Serilog": {
       "Using": [ "Serilog.Sinks.PostgreSQL.Configuration" ],
       "WriteTo": [
         {
           "Name": "PostgreSQL",
           "Args": {
             "connectionString": "LogsDb",
             "tableName": "logs",
             "needAutoCreateTable": true
           }
         }
       ]
     },
     "Columns": {
       "message": "RenderedMessageColumnWriter",
       "message_template": "MessageTemplateColumnWriter",
       "level": {
         "Name": "LevelColumnWriter",
         "Args": { "renderAsText": true, "dbType": "Varchar" }
       },
       "raise_date": "TimestampColumnWriter",
       "exception": "ExceptionColumnWriter",
       "properties": "LogEventSerializedColumnWriter"
     }
   }

Beide Sinks sind Batching-Sinks (periodisches Bulk-Insert) und haben daher vernachlässigbare
Auswirkungen auf die Request-Latenz.

Seq
+++

Anders als die DB-Sinks oben ist `Seq <https://datalust.co/seq>`__ keine relationale Datenbank,
sondern ein kleiner, selbst hostbarer Log-Server mit eigener Storage-Engine und UI (siehe
`Seq einrichten`_ weiter unten). Der Sink benötigt lediglich eine URL und optional einen
API-Key - keine Tabellen/Spalten-Definition:

.. code-block:: json

   {
     "Serilog": {
       "WriteTo": [
         {
           "Name": "Seq",
           "Args": {
             "serverUrl": "http://seq-host:5341",
             "apiKey": "***"
           }
         }
       ]
     }
   }

Auch das ist ein Batching-Sink mit vernachlässigbarer Latenz-Auswirkung und kann parallel zum
SQL-Server-/PostgreSQL-Sink laufen (z. B. DB für Langzeitaufbewahrung, Seq für die tägliche
Suche) - Serilog schreibt problemlos in beliebig viele konfigurierte Sinks gleichzeitig.

Oracle
++++++

Für Oracle gibt es derzeit keinen gut gepflegten Serilog-Sink, daher wird kein direkter DB-Sink
für Oracle angeboten. Ist das Log-Backend ausschließlich Oracle, sollte stattdessen der
OTLP-Weg verwendet werden (z. B. ein OpenTelemetry Collector mit einem Oracle-/JDBC-Exporter,
oder Export in ein OTLP-natives Backend, das dort abgefragt wird).

Logs anzeigen & analysieren
-------------------------------

Welches Werkzeug sinnvoll ist, hängt davon ab, welche(r) Sink(s) aktiv sind:

- **Nur SQL-Server-/PostgreSQL-Sink, punktuelle Fehlersuche**: Ein gewöhnlicher DB-Client genügt
  - kein zusätzliches Tool nötig. Azure Data Studio/SSMS (SQL Server) oder pgAdmin/DBeaver
  (PostgreSQL). Die strukturierte Spalte ``Properties``/``properties`` ist JSON
  (``NVARCHAR``/``jsonb``) und direkt abfragbar, z. B.:

  .. code-block:: sql

     -- SQL Server
     SELECT TOP 100 * FROM Logs
     WHERE Level = 'Warning' AND JSON_VALUE(Properties, '$.RequestPath') LIKE '%GetMap%'
     ORDER BY TimeStamp DESC;

     -- PostgreSQL
     SELECT * FROM logs
     WHERE level = 'Warning' AND properties->>'RequestPath' LIKE '%GetMap%'
     ORDER BY raise_date DESC LIMIT 100;

  Das ermöglicht weder Volltextsuche noch Dashboards, Alerting oder Trace-Korrelation - es
  eignet sich für den "schnellen Blick", nicht für laufende Analyse.

- **Dashboards/Alerting/Suche - empfohlen: Grafana** (Open Source, selbst hostbar, kostenlos).
  Es kann direkt auf das bereits Konfigurierte zeigen, ohne einen weiteren Sink hinzuzufügen:

  - Direkt auf die **SQL-Server-/PostgreSQL-Sink-Tabelle** über Grafanas eingebaute
    SQL-Datenquellen - Dashboards/Alerts auf Basis von Daten, die schon heute geschrieben
    werden.
  - Auf den **OTLP-Weg** über Loki (Logs) + Tempo (Traces) + Prometheus/Mimir (Metriken) - der
    De-facto-Open-Source-Stack für OpenTelemetry und naheliegend, da ``Api``/``Cms``/``Portal``
    bereits OTLP exportieren, sobald ``OTEL_EXPORTER_OTLP_ENDPOINT`` gesetzt ist (siehe oben).
    Das ermöglicht zusätzlich Trace-/Log-/Metrik-Korrelation (z. B. von einem langsamen
    ``GetMap``-Trace direkt in dessen Log-Zeilen springen), was die DB-Sinks allein nicht
    bieten können.

- **Einfachste "Zeig mir einfach die Logs"-Option, ohne Grafana-Setup**:
  `Seq <https://datalust.co/seq>`__ - ein einzelner Docker-Container, versteht Serilogs
  strukturierte Ereignisse nativ, kostenlos für einen einzelnen Benutzer/ein kleines Team, und
  nimmt auch direkt OTLP entgegen (siehe unten für die Schritt-für-Schritt-Einrichtung).

- **Kunde betreibt bereits eine Cloud-/Enterprise-Observability-Plattform**:
  ``OTEL_EXPORTER_OTLP_ENDPOINT`` darauf richten - Azure Monitor/Application Insights, AWS
  CloudWatch, Elastic/OpenSearch + Kibana, Datadog, New Relic, ... nehmen alle nativ OTLP
  entgegen (direkt oder über einen OpenTelemetry Collector), ohne Codeänderungen.

Seq einrichten
++++++++++++++++

Anders als Grafana kennt Seq kein Konzept einer "SQL-Datenquelle" - es kann nur Ereignisse
anzeigen, die ihm direkt gesendet wurden, entweder per OTLP oder als Serilog-Sink. Es **kann
nicht** einfach auf eine bereits gefüllte ``Logs``-/``logs``-Tabelle in SQL Server/PostgreSQL
gerichtet werden, um diese dort zu durchsuchen; ist genau das das Ziel (das, was der DB-Sink
bereits sammelt, ansehen/analysieren, ohne sonst etwas zu ändern), sollte stattdessen Grafanas
eingebaute SQL-Datenquelle auf diese Tabelle verwendet werden (siehe oben) - kein Dual-Write,
kein zusätzlicher Sink nötig.

Wird trotzdem Seqs eigene UI/Suche bevorzugt, muss WebGIS zusätzlich Ereignisse an Seq senden -
entweder als der oben dokumentierte `Seq`_-Sink (Dual-Write, parallel zum bestehenden
SQL-Server-/PostgreSQL-Sink, falls vorhanden) oder per OTLP wie unten beschrieben - beide Wege
sind bereits vollständig verdrahtet.

Für den OTLP-Weg unten ist kein WebGIS-spezifischer Sink/Paket nötig - Seq
`implementiert OTLP-Ingestion nativ <https://docs.datalust.co/docs/ingestion-with-opentelemetry>`_,
sodass dieser Weg nur darin besteht, den bestehenden OTLP-Exporter darauf zu richten.

1. Seq starten (persistiert die Daten in ``<lokaler Pfad>``, ``<Passwort>`` durch das initiale
   Admin-Passwort ersetzen):

   .. code-block:: bash

      docker run --name seq -d --restart unless-stopped \
        -e ACCEPT_EULA=Y \
        -e SEQ_FIRSTRUN_ADMINPASSWORD=<Passwort> \
        -v <lokaler Pfad>:/data \
        -p 5341:80 \
        datalust/seq

2. In der Seq-UI (``http://<seq-host>:5341``) unter *Settings > API Keys* einen eigenen API-Key
   pro Anwendung anlegen (empfohlen, nicht zwingend) - dadurch lässt sich später unter
   *Data > Ingestion* leicht unterscheiden, ob ein Ereignis von ``Api``, ``Cms`` oder ``Portal``
   stammt.

3. WebGIS' OTLP-Exporter auf Seqs OTLP-Endpunkt richten - entweder als echte
   Umgebungsvariablen oder über ``_config/logging.env`` (siehe oben):

   .. code-block:: text

      OTEL_EXPORTER_OTLP_ENDPOINT=http://<seq-host>:5341/ingest/otlp
      OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
      OTEL_EXPORTER_OTLP_HEADERS=X-Seq-ApiKey=<api-key-aus-schritt-2>

   Zu beachten: Der Endpunkt ist Seqs Ingestion-Pfad (``/ingest/otlp``), nicht nur die
   Host-Wurzel - der Exporter hängt ``/v1/logs``/``/v1/traces`` selbst an. Wurde in Schritt 2
   kein API-Key angelegt, kann ``OTEL_EXPORTER_OTLP_HEADERS`` entfallen.

   Alternativ - keine Traces, dafür strukturierte Ereignisse mit voller Feldtreue und weniger
   Konfiguration - kann stattdessen der `Seq`_-Sink mit derselben URL/demselben API-Key
   in ``_config/logging.json`` eingetragen werden.

4. ``Api``/``Cms``/``Portal`` neu starten (Umgebungsvariablen werden nur beim Prozessstart
   gelesen, sodass Änderungen an ``_config/logging.env`` einen Neustart erfordern - anders als
   ``_config/logging.json``, das automatisch übernommen wird). Logs und Traces (einschließlich
   der oben beschriebenen GeoService-Request-/Performance-Spans) erscheinen sofort in der
   Seq-UI - mit vollständiger Trace-/Span-Korrelation über das *Trace*-Menü jedes Ereignisses.

Der SQL-Server-/PostgreSQL-Sink kann parallel weiterlaufen, falls bereits konfiguriert (z. B.
für Langzeitaufbewahrung/Compliance) - Seq ist einfach ein weiterer, unabhängiger Konsument
derselben Telemetriedaten.

Hinweise
--------

- Alles auf dieser Seite (Serilog-Sinks, OTLP, Seq, Grafana, ...) betrifft, *wohin*
  Applikations-Log-Ereignisse gehen; es ist unabhängig vom ``Api:logging-type``-Schalter für das
  GeoService-Performance-/Exception-Logging aus :doc:`../config/api/index`, der - da er nun auch
  ``sqlserver``/``postgres``/``sqlite``/``oracle`` unterstützt - am Ende auf demselben
  Datenbankserver landen kann, allerdings in einer eigenen, dafür vorgesehenen Tabelle
  (``webgis_performance``/``webgis_exceptions``) statt der generischen ``Logs``-Tabelle, in die
  die Serilog-DB-Sinks schreiben.
- Es können mehrere Sinks gleichzeitig aktiv sein (z. B. Konsole + OTLP + SQL Server) - es sollte
  nur aktiviert werden, was tatsächlich benötigt wird.
