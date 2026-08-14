ArcGIS Server Spatial-Query Workaround
=======================================

.. note::

   Betrifft nur Kartendienste vom Typ **ArcGIS Server (REST)**, die gegen einen **SQL Server**
   als Datenquelle arbeiten.

Das Problem
-----------

Bei einer **räumlichen Abfrage** (z. B. Identify per Fläche, Polygon-Selektion, Umringsuche)
wertet der **ArcGIS Server** die Anfrage gegen den **SQL Server** in zwei Schritten aus:

1. Zuerst wird ausschließlich anhand der **Bounding-Box** (dem rechteckigen Umkreis) der
   Abfragegeometrie gefiltert. Auf dieser Stufe wendet der ArcGIS Server bereits ein
   **Zeilenlimit** an.
2. Erst danach werden die so gefundenen Kandidaten gegen die **tatsächliche Abfragegeometrie**
   (z. B. das exakte Polygon) geschnitten, um die endgültigen Treffer zu bestimmen.

Das Problem dabei: Das Zeilenlimit aus Schritt 1 wird **vor** dem eigentlichen räumlichen
Schnitt angewendet. Bei Geometrien, deren Bounding-Box deutlich größer ist als die Geometrie
selbst (z. B. schmale, lang gestreckte oder diagonal verlaufende Polygone, große Ringe mit
kleiner Kernfläche, etc.), können daher viele der über die Bounding-Box gefundenen Zeilen
außerhalb der eigentlichen Abfragegeometrie liegen. Diese "unnötigen" Treffer verbrauchen das
Zeilenlimit aus Schritt 1, obwohl sie später in Schritt 2 ohnehin verworfen werden.

In der Praxis führt das dazu, dass eine Abfrage **weniger Ergebnisse liefert, als tatsächlich
innerhalb der Abfragegeometrie liegen** – im Extremfall sogar **gar keine Treffer**, obwohl
passende Objekte vorhanden wären. Der Effekt tritt umso eher auf, je dichter die Daten sind
und je ungünstiger das Verhältnis zwischen Bounding-Box und tatsächlicher Geometrie ist.

Der Workaround
---------------

Um dieses Verhalten zu umgehen, wird eine räumliche Abfrage nicht mehr in einem einzigen
Request an den ArcGIS Server gestellt, sondern in mehreren Schritten aufgelöst:

1. **Nur Objekt-IDs abfragen** (``returnIdsOnly``)

   Zunächst wird eine Abfrage ausgeführt, die für die Abfragegeometrie **nur die Objekt-IDs**
   liefert, nicht aber die eigentlichen Feature-Daten (Geometrie und Attribute). Diese Variante
   der Abfrage ist von dem oben beschriebenen Bounding-Box-Problem **nicht betroffen**, da der
   ArcGIS Server hier den räumlichen Schnitt korrekt und vollständig durchführt.

2. **Objekt-IDs in Blöcken abholen**

   Auch bei einer ``returnIdsOnly``-Abfrage muss verhindert werden, dass im schlechtesten Fall
   Millionen von IDs auf einmal zurückgegeben werden (z. B. wenn die Abfragegeometrie sehr viele
   Objekte umfasst). Der ArcGIS-Server-REST-Parameter dafür heißt ``resultRecordCount`` und
   existiert grundsätzlich in **allen** ArcGIS-Server-Versionen.

   Das eigentliche Problem: Bei ``returnIdsOnly``-Abfragen wird ``resultRecordCount`` erst ab
   **ArcGIS Server 11.5** tatsächlich berücksichtigt. Bei älteren Versionen (**AGS < 11.5**)
   wird der Parameter bei dieser Abfrageart schlicht **ignoriert** – der ArcGIS Server liefert
   dann unabhängig von der Anfrage maximal **1000 IDs** zurück, und zwar **ohne jeden Hinweis**
   darauf, dass es eigentlich mehr Treffer gäbe (kein ``exceededTransferLimit``-Flag oder
   Ähnliches, wie man es von normalen Feature-Abfragen kennt). Ob die 1000 gelieferten IDs
   bereits alle Treffer sind oder ob in Wirklichkeit noch weitere existieren, lässt sich aus der
   Antwort selbst also **nicht erkennen**. Genau das macht den Workaround notwendig und relativ
   aufwendig: Es muss aktiv weitergeblättert und geprüft werden, ob noch neue IDs dazukommen,
   statt sich auf ein Abbruch-Flag des Servers verlassen zu können.

   Für diesen Fallback-Fall (AGS < 11.5, unwirksames ``resultRecordCount`` bei
   ``returnIdsOnly``) wird die anzunehmende Blockgröße über den konfigurierbaren
   **Fallback-Wert** gesteuert (siehe ``ags-spatial-query-default-max-record-count-fallback``
   weiter unten), standardmäßig **1000 IDs** pro Anfrage.

   Um trotz dieser Begrenzung **alle** IDs zu erhalten, werden die IDs seitenweise abgeholt:

   - Die erste Anfrage liefert bis zu **[Blockgröße]** IDs, sortiert nach ``ORDER BY OBJECTID``.
   - Aus dem Ergebnis wird die **höchste gelieferte OBJECTID** ermittelt.
   - Die nächste Anfrage ergänzt die ursprüngliche Abfragegeometrie um die zusätzliche
     Bedingung ``AND OBJECTID > [höchste bisher gefundene ID]`` und liefert so den
     **nächsten Block** von IDs.
   - Dieser Vorgang wird so lange wiederholt, bis entweder

     - ein Request **keine weiteren IDs** mehr liefert (d. h. alle Treffer wurden gefunden),
       oder
     - die Gesamtzahl der gesammelten IDs das konfigurierte Limit
       ``ags-spatial-query-max-result-cap`` erreicht. In diesem Fall wird das Sammeln
       abgebrochen und das Ergebnis als **unvollständig** markiert
       (``FeatureCollection.HasMore``), da theoretisch weitere Treffer existieren könnten,
       die nicht mehr abgeholt wurden.

   Da bei diesem Vorgehen für jeden Block eine eigene ``returnIdsOnly``-Abfrage mit dem
   zusätzlichen ``OBJECTID >``-Filter an den ArcGIS Server gestellt wird, ist dieser Schritt
   ebenfalls nicht vom eingangs beschriebenen Bounding-Box-Problem betroffen: Jede einzelne
   dieser Teilabfragen wird vom ArcGIS Server korrekt gegen die tatsächliche Geometrie
   ausgewertet, nur eben in mehreren kleineren Portionen statt in einer einzigen.

3. **Features anhand der gesammelten IDs nachladen**

   Erst nachdem die vollständige (oder auf das Limit begrenzte) Liste der Objekt-IDs ermittelt
   wurde, werden die eigentlichen Feature-Daten (Geometrie und Attribute) über
   ``query by objectIds`` nachgeladen. Auch dieser Schritt erfolgt wieder **in Blöcken**, deren
   Größe sich – wenn vom Dienst bekannt – nach dem ``maxRecordCount`` des ArcGIS-Server-Dienstes
   richtet, andernfalls nach dem konfigurierten Fallback-Wert
   (``ags-spatial-query-default-max-record-count-fallback``). Um die Gesamtdauer der Abfrage zu
   verkürzen, können mehrere dieser Blöcke **parallel** angefragt werden (siehe
   ``ags-spatial-query-max-parallel-batch-requests``).

Konfiguration
-------------

Das Verhalten des Workarounds kann über die *Section* ``tool-identify`` in der ``api.config``
angepasst werden:

.. code-block:: xml

    <section name="tool-identify">
      <!-- ArcGIS Server spatial-query bounding-box workaround -->
      <add key="ags-spatial-query-max-result-cap" value="2000" />
      <add key="ags-spatial-query-default-max-record-count-fallback" value="1000" />
      <add key="ags-spatial-query-max-parallel-batch-requests" value="4" />
    </section>

Die Bedeutung der einzelnen Attribute ist im Kapitel
:doc:`../config/api/index` beim Werkzeug **Identify** beschrieben.
