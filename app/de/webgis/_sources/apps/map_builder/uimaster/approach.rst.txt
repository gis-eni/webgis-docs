Grundsätzliche Vorgehensweise
=============================

Erstellt und veröffentlicht man mit dem *MapBuilder* eine Karte, wird im Hintergrund am Server ein 
JSON Dokument mit allen Einstellungen angelegt. Dieses JSON wird dann vom Kartenviewer interpretiert 
und daraus die Karte mit allen Bedienungselementen erzeugt.

In den Vorlagen können nun Teile dieser Karten-JSON-Datei gekapselt werden. Enthalten diese Teile zusätzliche
Elemente (z.B. Werkzeuge, Suchdienste), werden diese ebenfalls zur Karte hinzugefügt.

.. note::
   Mit *UI Master Vorlagen* können nur Elemente zu einer bestehenden Karte beim Laden hinzugefügt werden.
   Es hat eine Auswirkung, wenn ein Element im Master mit ``false`` (=nicht anwenden) definiert wird, es aber
   in der Karte über den MapBuilder bereits gesetzt wurde.

Daraus ergibt sich auch die Reihenfolge beim Laden einer Karte:

* 1. Schritt: Karte wird mit allen Einstellungen aus dem MapBuilder geladen
* 2. Schritt: Gibt es eine *UI Master Vorlage* für eine Kartenkategorie, werden alle Element, die darin gesetzt sind, hinzugefügt
* 3. Schritt: Gibt es eine *UI Master Vorlage* für eine Portalseite, werden alle Elemente, die darin gesetzt sind, hinzugefügt.

.. note::
   Es werden keine Elemente doppelt in eine Karte eingefügt. Befindet sich ein Werkzeug in Schritt 1 bereits in der 
   Karte, wird das gleiche Werkzeug nicht mehr zusätzlich über Schritt 2 und 3 eingefügt. 