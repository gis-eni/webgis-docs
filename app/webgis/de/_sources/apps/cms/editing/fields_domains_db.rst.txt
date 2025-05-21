Auswahlliste aus Datenbank
--------------------------

.. image:: img/editing20.png

Um eine **Auswahlliste aus einer Datenbank** zu erstellen, muss zuerst ein **ConnectionString** zur Datenbank definiert werden.  
Das Präfix ``SQL:`` gibt an, dass es sich um eine **SQL Server**-Datenbank handelt.  

Anschließend werden folgende Parameter festgelegt:  

- **Tabelle (oder View):** Die Datenquelle, aus der die Werte für die Auswahlliste stammen.  
- **Db-Feld:** Die Spalte, die den **Wert (*value*)** eines Listenelements enthält.  
  - Wird eine Auswahl getroffen, wird dieser Wert in die **Geo-Datenbank** gespeichert.  
- **Db-Anzeige Feld:** Die Spalte, die dem Anwender den **Anzeigenamen (*label*)** anzeigt.  
  - Diese Spalte kann identisch mit *Db-Feld* sein.  
  - Falls die gespeicherten Werte nicht sprechend sind, kann hier eine alternative, verständliche Spalte angegeben werden.  

Zusätzlich können folgende **optionale Einstellungen** vorgenommen werden:  
✅ **Where-Bedingung:** Einschränkung der Werte per SQL-FILTER.  
✅ **Sortierspalte:** Festlegen der Sortierreihenfolge der Werte.  

==================

Dynamische Abhängigkeiten zwischen Auswahllisten
------------------------------------------------

Normalerweise werden Auswahllisten beim Erstellen der **Eingabemaske** durch den **Kartenviewer** befüllt.  
Es gibt jedoch Anwendungsfälle, in denen der Inhalt erst später definiert wird – beispielsweise wenn eine  
Liste von einer **anderen Auswahlliste abhängig** ist.  

**Beispiel:**  
- Erst wenn der Anwender in **Liste A** eine Auswahl trifft, soll **Liste B** entsprechend gefiltert werden.  

Um solche Abhängigkeiten zu ermöglichen, können **Platzhalter** in der **Where-Bedingung** verwendet werden:

.. image:: img/editing21.png

In diesem Beispiel ist ``SYSTEM`` ein Eingabefeld mit einer **Auswahlliste**.  
Ändert sich dort die Auswahl, wird auch die abhängige Auswahlliste **automatisch aktualisiert**.  
Die Abhängigkeit ergibt sich durch den Platzhalter:  

``WHERE ... = '{{SYSTEM}}'``

==================

Weitere Platzhalter-Möglichkeiten
---------------------------------

Zusätzlich können auch **Rollenparameter** verwendet werden, um Listen weiter einzuschränken.  
Ein Beispiel dafür ist:  

``{{role-parameter:gemnr,GEM_NR like '{0}'}}``

Hier würde das **Rollenparameter „gemnr“** eines Anwenders genutzt, um die **Auswahlliste dynamisch zu filtern**.  
Welche Möglichkeiten **Rollenparameter** bieten, wird im **Whitepaper „Extended Role Parameters“** näher erläutert.
