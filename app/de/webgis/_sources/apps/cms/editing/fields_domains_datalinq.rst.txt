Auswahllisten aus WebServices (DataLinq)
========================================

*DataLinq* ist Teil der *WebGIS API* und wird hauptsächlich verwendet, um Berichte basierend auf verschiedenen Datenquellen zu erstellen.  
Zudem können parametrierte Abfragen als JSON über eine REST-Schnittstelle abgerufen werden. Diese REST-Schnittstelle  
kann auch als Quelle für **Auswahllisten** genutzt werden.

Vorteile gegenüber anderen Quellen
----------------------------------

Im Vergleich zu vorher gezeigten Methoden entfällt hier die Notwendigkeit, für jede Auswahlliste einen  
*ConnectionString* oder ein *SQL Statement* anzugeben.  
Dies hat mehrere Vorteile:  
✅ Die CMS-Parametrierung bleibt **frei von Verbindungseinstellungen und Datenbank-Passwörtern**.  
✅ Eine einmal definierte Liste kann **wiederverwendet** werden.  
✅ **Änderungen an der Liste wirken sich sofort** auf alle Editmasken aus.  

DataLinq kann verschiedene Datenquellen als Basis für eine REST-Schnittstelle verwenden:  
- **Datenbankabfragen**  
- **WebGIS API-Abfragen** auf Kartendienste, die über das *WebGIS CMS* parametriert wurden  
- **Einfache (Plain-Text-)Listen**  

In diesem Beispiel wird eine **Plain-Text-Liste** verwendet.  
Eine Datenbank ist hierfür nicht erforderlich – ähnlich wie bei **statischen Auswahllisten**,  
jedoch mit dem Vorteil, dass Änderungen an der Liste **direkt übernommen werden**.

.. note::  
   Grundkenntnisse zu *DataLinq* werden in diesem Abschnitt vorausgesetzt.

==================

DataLinq Endpoint anlegen
-------------------------

Zunächst wird ein neuer *DataLinq* Endpoint erstellt:

.. image:: img/datalinq-domains1.png

Als **Typ** wird ``PlainText`` angegeben. Ein *ConnectionString* ist für diesen Typ nicht erforderlich:

.. image:: img/datalinq-domains2.png

Unter **Security** können mit den ``Reset``-Buttons neue **Zugriffstokens** erstellt werden.  
Falls die Listen **nicht öffentlich zugänglich** sein sollen, müssen diese geschützt werden.  
Falls der Client kein Benutzer, sondern eine **Applikation** ist, erfolgt der Zugang nicht über *User/Passwort*,  
sondern über **Tokens**.  

Der Client, der die Listen abruft, ist in diesem Fall die **WebGIS Application**:

.. image:: img/datalinq-domains3.png

==================

DataLinq Abfrage anlegen
------------------------

Im nächsten Schritt wird unter dem **Endpoint** eine **Abfrage** erstellt:

.. image:: img/datalinq-domains4.png 

Anschließend kann unter **Statement** der Editor geöffnet werden:

.. image:: img/datalinq-domains5.png 

Falls die Datenquelle eine **Datenbank** ist, kann hier ein **SQL Statement** hinterlegt werden.  
Beim Typ **PlainText** werden die Werte für die Liste **direkt als Text** eingetragen:

.. image:: img/datalinq-domains6.png 

Formatierung der Werte
----------------------

- Jede Zeile entspricht einem **Eintrag** in der Auswahlliste.  
- Der Wert wird sowohl als **„value“** als auch als **„label“** (Anzeigename) verwendet.  
- Falls sich **„value“** und **„label“** unterscheiden sollen, werden sie mit ``:`` getrennt:

.. image:: img/datalinq-domains7.png

.. note::  
   - Eine Zeile mit nur einem ``:`` fügt eine **leere Option** zur Auswahlliste hinzu.  
   - Falls für leere Werte in der Geodatenbank der Wert **„0“** gespeichert werden soll, kann ``0:`` eingetragen werden.  
   - **Leerzeilen werden ignoriert.**  

Nach dem Eintragen der Werte den Editor mit **„Close“** schließen und zum **Security-Bereich** wechseln.  
Hier sollte der User ``*`` hinzugefügt werden.  
Das bedeutet, dass jeder Client, der Zugriff auf den *Endpoint* hat, auch die Abfrage abrufen kann.  

Die Berechtigungen könnten weiter eingeschränkt werden – für dieses Beispiel reicht es jedoch,  
den *Endpoint* zu schützen:

.. image:: img/datalinq-domains8.png 

Zum Abschluss wird die Abfrage mit **„Create“** erstellt.

==================

Abfrage testen
--------------

Zum Testen kann der Abfragedialog geöffnet werden:  
**Statement → Test**  

Das Ergebnis sollte folgendermaßen aussehen:

.. image:: img/datalinq-domains9.png

Falls der Link in einem **anderen Browser oder Incognito-Fenster** aufgerufen wird, erscheint eine Fehlermeldung:

.. image:: img/datalinq-domains10.png 

Dies liegt daran, dass der Zugriff auf den *Endpoint* **nicht öffentlich** ist.  
Damit der Client später auf die Abfrage zugreifen kann, muss eines der zuvor erstellten **Tokens** übergeben werden.

Dafür gibt es zwei zulässige Methoden:  

``http://...../datalinq/select/endpoint(ENDPOINT-TOKEN)@query(QUERY-TOKEN)``  
``http://...../datalinq/select/endpoint@query?endpoint_token=ENDPOINT_TOKEN&query_token=QUERY_TOKEN``  

Da in diesem Beispiel nur **Endpoint-Tokens** definiert wurden, kann die URL entsprechend angepasst werden.  
Die Abfrage funktioniert dann auch im *Incognito-Fenster*:

.. image:: img/datalinq-domains11.png

Diesen Link muss man anschließend ins **CMS** eintragen.

.. note::  
   Welcher der beiden Tokens verwendet wird, ist egal.  
   **Beide Tokens sind gleichwertig.**  
   Der Grund für zwei separate Tokens ist, dass später ein **nahtloser Wechsel** zwischen ihnen möglich bleibt.

==================

Auswahlliste im CMS einbinden
-----------------------------

Beim jeweiligen **Domain-Feld** (Edit-Maske) wird unter **ConnectionString** der Link zur Abfrage eingetragen:

.. image:: img/datalinq-domains12.png 

.. note::  
   - Da sich die WebGIS-Anwendung **nicht mit User/Passwort** bei *DataLinq* anmelden kann, muss hier ein **Token** mit angegeben werden.  
   - Grundsätzlich kann hier jedes **WebService** genutzt werden, das ein **JSON-Array** zurückgibt.  
   - Das Array muss Objekte mit den **Properties** ``value`` und ``name`` enthalten.  
   - Falls abweichende Property-Namen verwendet werden, können diese über ``DB-Feld`` und ``DB-Anzeige Feld`` angegeben werden.  
   - In diesem Beispiel entsprechen die Werte **bereits den Defaultwerten**, sodass sie leer bleiben können.

==================

Kaskadierende Auswahllisten
---------------------------

Auswahllisten können auch von einer **übergeordneten Liste** abhängig gemacht werden.  
Beim Typ ``PlainText`` wird dies durch **Einrückungen (2x Leerzeichen)** umgesetzt:

.. image:: img/datalinq-domains13.png 

Wenn die Abfrage ohne Parameter aufgerufen wird, wird die **Liste mit Automarken** zurückgegeben:

.. image:: img/datalinq-domains14.png

Soll nur eine bestimmte **Marke** gefiltert werden, kann der Parameter ``level0={value}`` übergeben werden:

.. image:: img/datalinq-domains15.png

.. note::  
   - Durch **weitere Einrückungen** können **beliebig viele Ebenen** definiert werden.  
   - Die Filterung erfolgt dann über die URL mit Parametern:  

     ``level0={value0}&level1={value1}&level2={value2}``  

Im **CMS** kann die Einschränkung über die **„DB-Where Clause“** definiert werden:

.. image:: img/datalinq-domains16.png 

.. note::  
   Hier ist ``MARKE`` das **Datenbank-Feld**, in das die Automarke über die Auswahlliste geschrieben wird.
