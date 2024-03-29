Sketch/Entwurfswerkzeuge
========================

Beim Zeichnen eines Sketches (z.B. beim Redlining, Editieren, Höhenprofil erstellen, ...) stehen mehrere Optionen zur Verfügung, die je nach Anwendung sehr hilfreich sein können.

Dazu muss während des Zeichnens mit der rechten Maustaste auf den Sketch oder in die Karte geklickt werden. Je nach Typ des Sketches (Linie, Polygon) werden folgende Optionen angeboten:

.. image:: img/sketch1.png


.. note::
   Auf (mobilen) Geräten mit Touch Bedienung funktioniert der Klick in der Karte über das *Click Bubble* Werkzeug (siehe Abschnitt *Click Bubble* unter Werkzeuge).
   Der Vorteil der *Click Bubble* ist die Vermeidung von unabsichtlichen Klicks beim Navigieren und die höhere Präzision beim Klicken.


Rückgängig/Undo
---------------

Mit ``Rückgängig/Undo`` können die letzten Befehle, welche unter *Rückgängig/Undo* in grau angezeigt werden, rückgängig gemacht werden.

.. note:: Es gibt kein *Redo*.




Vertex Bearbeiten
-----------------

Vertices nennt man die sogenannten Stützpunkte der Linie, welche über verschiedene Arten nachträglich noch bearbeitbar sind.

* **Vertex verschieben:** Auf den Vertex klicken und mit gedrückter Maustaste den Vertex beliebig verschieben.

* **Vertex hinzufügen:** Dafür gibt es mehrere Möglichkeiten: in die Karte klicken, über *Richtung/Entfernung* (siehe unten) oder über *Koordinaten (absolut)* (siehe Konstruieren).

* **Vertex auf bestehender Linie hinzufügen:** Rechte Maustaste auf die Linie und dann *Vertex hinzufügen* wählen.

* **Vertex entfernen:** Rechte Maustaste auf den Vertex und dann *Vertex entfernen* wählen. 

* **Vertex fixieren/anschließen:** Rechte Maustaste auf den Vertex und dann *Vertex fixieren/anschließen* wählen. Diese Vertices bleiben dann beim Verschieben und Versetzen fixiert und sind als blaue größere Punkte erkennbar. Mit rechte Maustaste und dann *Fixierung aufheben* kann die Fixierung des Vertex wieder aufgehoben werden.


Shortcuts
---------

+------------+------------------------------------------------------------------------------------+
| ``A``      | neuen Vertex auf Liniensegement setzen                                             |
+------------+------------------------------------------------------------------------------------+
| ``D``      | Vertex löschen: ``D``-Taste gedrückt halten und Vertices zum Löschen auswählen     |
+------------+------------------------------------------------------------------------------------+
| ``O``      | aktiviert/deaktviert Orthogonalmodus                                               |
+------------+------------------------------------------------------------------------------------+
| ``T``      | aktiviert/deaktviert Trace-Modus                                                   |  
+------------+------------------------------------------------------------------------------------+
| ``S``      | Snapping Dialog anzeigen                                                           |
+------------+------------------------------------------------------------------------------------+
| ``Strg+Z`` | Undo                                                                               |
+------------+------------------------------------------------------------------------------------+
| ``Strg``   | Bei grückter Taste können Vertices selelktiert werden (siehe unten)                |
+------------+------------------------------------------------------------------------------------+


Vertices selektieren
--------------------

Mit **Strg** können mehrere Vertices ausgewählt werden. Dazu kann man mit geddrückter ``Strg``-Taste entweder mehrere Vertices durch Anklicken auswählen oder mit der Maus ein Rechteck aufziehen, wodurch alle im Rechteck liegenden Vertices ausgewählt werden.

.. image:: img/sketch11.png

Anschließend erscheinen im Menü nach dem rechten Mausklick folgende neuen Optionen:

.. image:: img/sketch10.png

* **Aufheben:** Hebt die Auswahl auf.

* **Umkehren:** Kehrt die Auswahl der Vertices um.

* **Entfernen:** Entfernt alle ausgewählten Vertices.


Sketch entfernen
----------------

Mit ``Sketch entfernen`` werden die gezeichneten Sketches entfernt. Falls dieser Befehl unabsichtlich ausgeführt wurde, können die Sketches mittels ``Rückgängig/Undo`` wiederhergestellt werden.
In den meisten Werkzeugen lässt sich der Sketch auch seitlich links im Menü über den ``Sketch entfernen`` Button entfernen.


Abschnitt schließen/neuen beginnen
----------------------------------

Mit ``Abschnitt schließen/neuen beginnen`` wird der aktuelle Sketch abgeschlossen und ein neuer Sketch kann begonnen werden.
Somit kann man mehrere Linien/Polygone zeichnen.




.. toctree::
   :maxdepth: 2

   segmentmodus
   sketchtools
   snapping
   construct
   presentation