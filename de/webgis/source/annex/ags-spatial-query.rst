ArcGIS Server Spatial-Query Workaround
=======================================

.. note::

   Betrifft nur Kartendienste vom Typ **ArcGIS Server (REST)**, deren Daten in einem
   **SQL Server** oder einer **Oracle**-Datenbank liegen (siehe unten).

Das Problem
-----------

Bei einer **räumlichen Abfrage** (z. B. Identify per Fläche, Polygon-Selektion, Umringsuche)
wertet der **ArcGIS Server** die Anfrage intern in zwei Schritten aus:

1. Zuerst wird nur die **Bounding-Box** (der rechteckige Umkreis) der Abfragegeometrie an die
   Datenbank geschickt – inklusive des dort geltenden **Zeilenlimits** (``maxRecordCount``).
2. Erst danach wird das so ermittelte Ergebnis gegen die **tatsächliche Abfragegeometrie**
   (z. B. das exakte Polygon) verschnitten (*geclippt*), um die endgültigen Treffer zu
   bestimmen.

Das Problem dabei: Das Zeilenlimit aus Schritt 1 wird **vor** dem eigentlichen räumlichen
Verschnitt angewendet. Bei großen bzw. schmalen Geometrien (z. B. lang gestreckte Linien oder
Polygone) kann es daher passieren, dass unter den ersten über die Bounding-Box gefundenen
Kandidaten **zu wenige oder gar keine echten Treffer** sind, obwohl in Wirklichkeit deutlich
mehr Objekte innerhalb der Abfragegeometrie liegen. Das Ergebnis einer Abfrage kann dadurch
**weniger Treffer liefern als tatsächlich vorhanden sind**, im Extremfall sogar **null Treffer**.

**ESRI bestätigt** dieses Verhalten, stuft es jedoch als **"as designed"** ein – es ist also nicht
mit einem Fix seitens ArcGIS Server zu rechnen.

Nicht betroffen von diesem Problem sind reine **Zählungen** (``returnCountOnly``) sowie Abfragen,
die **nur die Objekt-IDs** liefern (``returnIdsOnly``): Bei diesen beiden Abfragearten wird nach
Beobachtung tatsächlich die reale Abfragegeometrie an die Datenbank übergeben, nicht nur deren
Bounding-Box. Genau darauf baut der weiter unten beschriebene Workaround auf.

.. important::

   Das Problem tritt nur auf, wenn die Daten des ArcGIS-Server-Dienstes in einem **SQL Server**
   oder einer **Oracle**-Datenbank liegen. Bei **PostGIS** als Datenquelle tritt dieses Verhalten
   nach bisheriger Beobachtung **nicht** auf.

Konfigurierbar pro Dienst: ``QueryStrategy`` (CMS)
----------------------------------------------------

Da sich unterschiedliche ArcGIS-Server-Instanzen bzw. die dahinterliegenden Datenbanken
unterschiedlich verhalten (siehe oben, PostGIS ist z. B. nicht betroffen), wird der Workaround
**nicht global**, sondern **pro Dienst** aktiviert. Dazu gibt es im **CMS** auf dem jeweiligen
**ArcServerService** die Eigenschaft **``QueryStrategy``**:

* **``Default``** – normale Abfrage (Feature-Query mit Geometrie/Where-Klausel direkt an den
  ArcGIS Server), ohne zusätzliche Requests. Dies ist immer die **schnellste Variante** und wird
  überall dort verwendet, wo sie sicher korrekte Ergebnisse liefert.
* **``BoundingBoxProblem``** – aktiviert den weiter unten beschriebenen **Ids-first-Workaround**
  für Dienste, bei denen das Bounding-Box-Problem tatsächlich auftritt.

Ablauf bei ``BoundingBoxProblem`` (Entscheidungskaskade)
-----------------------------------------------------------

Auch wenn ein Dienst auf ``BoundingBoxProblem`` konfiguriert ist, wird nicht blind der
aufwendigere Workaround verwendet. Vor dessen Einsatz gibt es mehrere **Vorprüfungen**, die auf
``Default`` zurückfallen, wenn das Problem für die konkrete Abfrage gar nicht auftreten kann bzw.
unschädlich wäre:

1. **Geometrie-Check**

   Reine **Attributabfragen** (ohne Geometrie), Abfragen mit einer **Envelope-Geometrie**
   (die Bounding-Box entspricht hier bereits der Abfragegeometrie, es gibt also keinen
   Unterschied) oder mit einem **Punkt** (die Bounding-Box eines Punktes ist der Punkt selbst)
   können das Problem prinzipiell nicht auslösen → es wird ``Default`` verwendet.

2. **Bbox-Kandidaten-Check**

   Für alle anderen Geometrietypen (Linie, Polygon, Multipoint) wird zunächst kostengünstig
   gezählt, wie viele Objekte in der **Bounding-Box** der Abfragegeometrie liegen
   (``returnCountOnly``, selbst nicht vom Problem betroffen). Liegt dieser Wert **unter** dem
   serverseitigen Zeilenlimit (``maxRecordCount``), kann im internen Bbox-Schritt nichts
   abgeschnitten worden sein, bevor der eigentliche Verschnitt passiert → auch hier reicht
   ``Default``.

3. **Ids-first-Workaround**

   Erst wenn keine der beiden Vorprüfungen zutrifft, kommt der eigentliche Workaround
   (intern ``BoundingBoxProblemAgsQueryStrategy``) zum Einsatz. Er läuft in drei Schritten ab:

   **Schritt A – Kandidatenzahl gegen die echte Geometrie**

   Zunächst wird per ``returnCountOnly`` gegen die **tatsächliche** Abfragegeometrie bzw.
   Where-Klausel gezählt (nicht gegen die Bounding-Box). Liegt dieser echte Treffer-Count
   **unter** dem konfigurierbaren Schwellwert ``ags-spatial-query-ids-paging-threshold``
   (Standardwert: ``50000``), genügt eine einzige, **unpaginierte** ``returnIdsOnly``-Abfrage:
   Der ArcGIS Server liefert dabei zuverlässig **alle** IDs ohne Zeilenlimit, solange kein
   ``resultRecordCount`` mitgegeben wird.

   **Schritt B – Paging bei großen Ergebnismengen**

   Liegt der echte Treffer-Count über dem Schwellwert (potenziell hunderttausende oder
   Millionen Treffer), werden die IDs stattdessen **seitenweise per Keyset-Pagination**
   abgeholt: Jede Anfrage ergänzt die Bedingung ``{ID-Feld} > {höchste bisher gefundene ID}``
   (aufsteigend sortiert), die Seitengröße entspricht dabei dem ``maxRecordCount`` des Dienstes.
   Dieser Vorgang wird abgebrochen, sobald eine der folgenden Bedingungen eintritt:

   * Eine Seite liefert **keine** weiteren IDs mehr → alle Treffer wurden gefunden.
   * Das konfigurierte **Zeitbudget** (``ags-spatial-query-ids-timeout-seconds``, Standardwert:
     ``20`` Sekunden) wird überschritten → Abbruch, das Ergebnis wird als **unvollständig**
     markiert.
   * Es gibt **keinen Fortschritt** mehr (die höchste gefundene ID steigt nicht weiter) →
     Abbruch, als Schutz vor Endlosschleifen bzw. Duplikaten.
   * Es werden **mehr als 50 aufeinanderfolgende** Seiten empfangen, die zwar laut Server
     abgeschnitten sind, aber fast leer ausfallen → Abbruch.

   Unabhängig vom Abbruchgrund wird das Gesamtergebnis client-seitig zusätzlich auf
   ``ags-spatial-query-max-result-cap`` (Standardwert: ``2000``) gekappt.

   **Schritt C – Laden der eigentlichen Features**

   Erst nachdem die Objekt-IDs auf eine der beiden Arten ermittelt wurden, werden die
   eigentlichen Feature-Daten (Geometrie und Attribute) geladen. Dies geschieht in **Batches**
   (Batchgröße: ``ags-spatial-query-default-max-record-count-fallback``), die parallel
   angefragt werden können (siehe ``ags-spatial-query-max-parallel-batch-requests``), über
   ``query by objectIds`` – ein Abfragetyp, der ebenfalls nicht vom Bounding-Box-Problem
   betroffen ist.

Kurz zusammengefasst
---------------------

``Default`` ist immer die bevorzugte, günstigste Strategie. ``BoundingBoxProblem`` wird nur für
Dienste aktiviert, bei denen das Problem tatsächlich auftreten kann (SQL Server/Oracle als
Datenquelle), und selbst dann wird mehrfach geprüft, ob der aufwendigere Ids-first-Umweg
überhaupt nötig ist (Geometrietyp, Anzahl der Bbox-Kandidaten, Anzahl der echten Kandidaten).
Nur im ungünstigsten Fall – viele echte Treffer bei einer problematischen Geometrie – kommt das
vollständige Paging-Verfahren (Schritt B) zum Einsatz.

Konfiguration
-------------

Die Zahlenwerte des Ids-first-Workarounds (Schritte A bis C) können über die *Section*
``tool-identify`` in der ``api.config`` angepasst werden:

.. code-block:: xml

    <section name="tool-identify">
      <!-- ArcGIS Server spatial-query bounding-box workaround -->
      <add key="ags-spatial-query-max-result-cap" value="2000" />
      <add key="ags-spatial-query-default-max-record-count-fallback" value="1000" />
      <add key="ags-spatial-query-max-parallel-batch-requests" value="4" />
      <add key="ags-spatial-query-ids-timeout-seconds" value="20" />
      <add key="ags-spatial-query-ids-paging-threshold" value="50000" />
    </section>

Die Bedeutung der einzelnen Attribute ist im Kapitel
:doc:`../config/api/index` beim Werkzeug **Identify** beschrieben.

Die ``QueryStrategy`` selbst (``Default`` / ``BoundingBoxProblem``) ist **kein**
``api.config``-Wert, sondern wird pro Dienst am **ArcServerService** im **CMS** eingestellt.
