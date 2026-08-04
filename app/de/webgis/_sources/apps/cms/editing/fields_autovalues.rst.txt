Editierbare Felder: Autovalues
==============================

*Autovalues* sind Felder, die nicht vom Anwender eingegeben werden müssen, sondern vor dem Speichern  
am Server *automatisch* gesetzt werden.  

Beispiele für solche Felder sind:  

- Der Benutzername des aktuellen Anwenders: ``create_login``, ``create_login_full``, ``create_login_short``, ... 

- Das Erstellungsdatum eines Objekts:  ``create_date``, ``create_time``, ... 

- Die Länge einer Liniengeometrie: ``shape_len``, ``shape_area``, ... 

- GUIDs
 
  * ``guid``: eine Guid in diesem Format ``4b2dd0dfeb1b40188b2583167886e886``
    eignet sich, wenn die GUID in der Datenbank als Text gespeichert werden soll.
  * ``guid_sql``: ein GUid in diesem Format ``{9e2702e4-169f-41ec-b3e3-fcf786182885}``
    eignet sich, wenn die GUID in einer SQL-Datenbank als GUID gespeichert werden soll.
  * ``guid_v7``, ``guid_v7_sql``: Wie oben, aber mit einer Version 7 GUID.
    Version 7 GUIDs eigenen sich für die Speicherung in Datenbanken, wenn die Zugrunde 
    liegenden Felder auch indiziert werden sollen. Die erzeugten GUIDs sind zeitlich nach 
    ihrem Wert sortiert, was in der Regel zu einer geringeren Fragmentierung der Indizes führt.

Diese Felder werden in der Eingabemaske meist als *readonly* oder nicht sichtbar definiert.

Im folgenden Beispiel wird die Länge der erstellten Liniengeometrie in ein Feld übernommen:

.. image:: img/editing18.png

Benutzerdefinierte Werte mit „custom“
-------------------------------------

Mit dem *Autovalue* ``custom`` können Werte direkt im Eingabefeld definiert werden.  
Beispielsweise kann für ein Feld **QUELLE** immer der Wert ``WEBGIS`` eingetragen werden:

``=WEBGIS``  

Zusätzlich lassen sich Werte aus den URL-Parametern des Viewers übernehmen.  
Dies funktioniert mit *originären* URL-Parametern (siehe Abschnitt: Aufruf des Viewers):

``url-parameter:project_id``  

Automatische Attributierung über räumliche Beziehungen
------------------------------------------------------

Auch räumliche Beziehungen zu anderen Featureklassen können zur automatischen Attributierung genutzt werden:  

``NR FROM GDBAbfrage SERVICE kataster``  

→ Hier wird das Attribut **NR** von Objekten aus dem Thema **GDBAbfrage** übernommen,  
   wenn diese sich räumlich mit dem gespeicherten Objekt decken.  
   Gibt es mehrere Treffer, werden diese mit **Strichpunkten** getrennt.

``TYP FROM kasten SERVICE strom@mycms BUFFERDIST 20 SEPARATOR space-space MAX 10``  

→ Hier wird das Attribut **TYP** von Objekten aus dem Thema **Kasten** übernommen,  
   wenn diese im Umkreis von **20 m** liegen (``BUFFERDIST 20``).  
   Mehrere Ergebnisse werden mit **Leerzeichen-Bindestrich-Leerzeichen** getrennt  
   (``SEPARATOR space-space``). Es werden maximal **10 Ergebnisse** übernommen (``MAX 10``).  

Automatische Werte aus einer Datenbankabfrage („db_select“)
-----------------------------------------------------------

Der Autovalue ``db_select`` ermöglicht das automatische Befüllen eines Feldes  
über eine Datenbankabfrage. Dazu müssen folgende Angaben gemacht werden:  

- **ConnectionString** → Die Verbindung zur Datenbank  
- **SQL Statement** → Die Abfrage für das gewünschte Feld  

.. image:: img/editing19.png

Mit **Platzhaltern** wie ``{{VORGANG_TEXT}}`` kann auf aktuelle Eingaben zugegriffen werden.

Autovalues über WebService (DataLinq)
-------------------------------------

Statt einer Datenbank kann auch ein WebService als Datenquelle für ``db_select`` genutzt werden.  
Ein Beispiel für eine *DataLinq*-Abfrage:

``https://localhost:44341/datalinq/select/auswahllisten(oJ...token)@color?value=4711``  

Diese Abfrage liefert folgendes JSON-Ergebnis:

.. code-block:: javascript

   [
      {
        "value": "4711",
        "name": "Blau"
      }
   ]

Für die Einbindung dieses Dienstes müssen die Felder **ConnectionString** und **SqlStatement**  
folgendermaßen befüllt werden:

**ConnectionString:**  

``https://localhost:44341/datalinq/select/auswahllisten(oJ...token)@color``  

**SqlStatement:**  

``value={{color}}``  

Hierbei ist ``color`` das Edit-Eingabe/Auswahllisten-Feld, das für diesen Autovalue verwendet wird.  
In diesem Beispiel würde als Autovalue der Wert **„Blau“** übernommen werden.

.. note::  
   - Es wird immer das **erste Ergebnis** der Abfrage verwendet.  
   - Bei einer URL-Abfrage wird der Wert aus dem Feld **„name“** übernommen.  
   - Bei *DataLinq PlainText*-Endpoints heißt das Feld per Definition immer **„text“**.  
   - Falls eine eigene SQL-Abfrage in *DataLinq* genutzt wird, sollte das gewünschte Feld umbenannt werden:  

     ``SELECT FARBE as name FROM TABLE WHERE ...``  

.. note::  
   **Sicherheitshinweis:**  
   - *ConnectionStrings* oder URLs mit Tokens sollten nicht direkt im CMS hinterlegt werden.  
   - Stattdessen sollten diese Werte im Abschnitt ``secrets`` gespeichert werden.  
   - Der ConnectionString kann dann mit einem **Platzhalter** angegeben werden:  

     ``{{select-datalinq-endpoint-auswahllisten}}@color``  