Editierbare Felder
==================

.. image:: img/editing6.png

In diesem Abschnitt wird festgelegt, welche Sachdaten dem Anwender für ein Editthema zur Verfügung stehen.
Die einzelnen Attribute eines Geo-Objekts können dabei über Eingabefelder, Auswahllisten, Datumsfelder usw. eingegeben werden.

Müssen viele Attribute eingegeben werden, empfiehlt es sich, diese in verschiedene Kategorien aufzuteilen.
Die einzelnen Kategorien können in der Sachdaten-Maske dann einzeln aufgeklappt werden.

Im ersten Schritt muss daher zunächst mit dem Button ``Neue Kategorie`` eine Kategorie erstellt werden.
Für den Anfang reicht beispielsweise eine Kategorie namens ``Allgemein``. Klickt man danach auf eine Kategorie,
können darin Eingabefelder definiert oder bereits vorhandene bearbeitet werden.

Zum Hinzufügen eines neuen Eingabefelds (Attributs) muss innerhalb einer Kategorie auf ``Feld hinzufügen`` geklickt werden:

.. image:: img/editing15.png

Unter ``Feld`` wird das Attribut angegeben, das bearbeitet werden soll. Nach der Auswahl muss noch ein Name
vergeben werden, unter dem das Feld in der Eingabemaske angezeigt wird.

Ein neu erstelltes Eingabefeld wird nach dem Erstellen sofort in der Liste angezeigt. Ein Klick auf ein Eingabefeld öffnet einen
Dialog mit weiteren Eigenschaften:

.. image:: img/editing16.png

Die Art der Eingabe wird über den ``Eingabe Type`` bestimmt:

* **Text:** Ein einfaches Texteingabe-Feld.
* **Domain:** Eine Auswahlliste mit definierten Werten. Die Werte können im CMS statisch hinterlegt oder aus einer Datenbank abgerufen werden.
* **TextArea:** Ein mehrzeiliges Eingabefeld.
* **Date:** Ein Datums-Eingabefeld.
* **File:** Zum Hochladen von Dateien.
* **Info:** Ein reiner Informationstext (keine Interaktion mit dem Anwender).

  .. note::

    Der Text für Info kann auch ein (eingeschränkter) **Markdown-Text** sein. 
    Das ermöglicht die Verwendung von Links und anderen Formatierungen. 
    Der Text muss dazu mit ``md:`` beginnen.
    Links können dabei folgendermaßen eingebunden werden:
    
    * ``md: Beliebiger Text [Linktext](https://www.example.com)``: damit wird ein Link angezeigt,
      die Url wird ein einem neuen Tab geöffnet, wenn der Anwender darauf klickt.
      
    Die *Link Syntax* kann noch folgendermaßen erweitert werden:
    
    * ``[[Linktext]](https://www.example.com``: Anzeige des Links als Button.
    * ``{Linktext}(https://www.example.com)``: Der Link wird in einem Popup geöffnet.
    * ``{[Linktext]}(https://www.example.com)``: Der Link wird als Button angezeigt und in einem Popup geöffnet.

Zusätzlich gibt es unter ``Allgemein`` noch folgende Optionen für ein Eingabefeld:

* **Sichtbar:** Gibt an, ob das Feld für den Anwender sichtbar ist. Unsichtbare Felder können praktisch sein, wenn diese erst später über einen AutoValue berechnet werden.
* **Schreibgeschützt (Readonly):** Ähnlich wie bei "Sichtbar". Hier wird das Feld zwar angezeigt, kann vom Anwender aber nicht geändert werden.
* **Feld bestimmt die Legende:** Besitzt das Editierthema in der Karte eine Legende mit unterschiedlichen Symbolen, die vom Wert dieses Feldes abhängen, kann diese Option aktiviert werden. Der Anwender kann dann über die Auswahlliste neben dem Tabellenwert auch das zugehörige (Legenden-)Symbol auswählen.
* **Beständig (Resistant):** Der Wert des Feldes bleibt nach dem Speichern erhalten und muss nicht jedes Mal neu eingegeben werden. Das gilt auch, wenn es dasselbe Feld in unterschiedlichen Themen gibt. Z. B. kann eine Projektnummer, die auf jedem Objekt mitgespeichert wird, nur einmal eingegeben werden und bleibt im Formular "beständig", bis der Anwender eine andere Projektnummer vergibt.
* **Feld für Massen-Attributierung:** Falls die Massen-Attributierung (Änderung mehrerer ausgewählter Objekte gleichzeitig) erlaubt ist, kann hier festgelegt werden, ob das Feld über die Massen-Attributierung gesetzt werden darf.