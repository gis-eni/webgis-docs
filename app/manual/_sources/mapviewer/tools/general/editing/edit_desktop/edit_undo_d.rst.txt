.. _undo_d:

Bearbeitungsschritt rückgängig machen (Undo)
============================================

Mit diesem Werkzeug können Bearbeitungsschritte wieder rückgängig gemacht werden. Rückgängig gemacht werden können:

* Bestehendes Objekt bearbeiten
* Bestehendes Objekt löschen

Wenn es möglich ist, Schritte rückgängig zu machen, erscheint im Edit-Dialog ein *Rückgängig*-Button. 

.. image:: img/rueckgaengig.png

Wählt man diesen aus, erscheint eine Liste mit den Schritten, die rückgängig gemacht werden können. Fährt man mit der Maus über einen Schritt, wird das Objekt, für das die Aktion durchgeführt wird, hervorgehoben. 

.. image:: img/rueckgaengig_1.png

.. note::
   Eine Undo Funktion steht nicht für jeden Kartendienst Type zur Verfügung. Man sollte sich beim 
   Bearbeiten daher nicht darauf verlassen, dass das Update auch angeboten wird.

.. note::
   Trotz der Undo Möglichkeit ist beim Bearbeiten von Geo-Objekten Vorsicht geboten. Selbst durch ein *Undo* 
   werden Geo-Objekte nicht mehr zu 100% gleich wiederhergestellt. So ändert sich durch das Löschen und späterem Rückgängig 
   machen die interne Datenbank ID (OBJEKT_ID) des Objektes. Auch werden automatisch gesetzte Attribute wie **letzter 
   Bearbeiter** oder **letzter Bearbeitungszeitpunkt** durch Datenbank Trigger neu gesetzt.

.. note::
   Die Möglichkeit des *Undo* besteht nur für die aktuelle Session. Wird der Kartenviewer geschlossen oder auf eine
   andere Karte gewechselt, können Bearbeitungsschritte nicht mehr rückgängig gemacht werden.    