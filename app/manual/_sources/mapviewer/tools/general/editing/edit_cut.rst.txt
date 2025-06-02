Geo-Objekte teilen (cut)
========================

Mit diesem Werkzeug kann ein Linien- oder Flächenobjekt mittels einer Schnittlinie 
in mehrere Teile geteilt werden. Voraussetzung ist, dass das entsprechende Geo-Objekt
mit dem Abfragewerkzeug ausgewählt (selektiert) in der Karte angezeigt wird.
Außerdem darf für diesen Vorgang nur exakt ein Geo-Objekt ausgewählt sein.

Wechselt man zum Bearbeiten (Edit) Werkzeug, wird das *Objekte Teilen* Werkzeug angeboten:

.. image:: img/edit17.png

Klickt man auf das *Objekt teilen* Werkzeug, öffnet sich ein Dialog, in dem die Sachdaten
des Geo-Objektes angezeigt werden. In der Karte kann man eine Linie zeichnen, die zum Teilen
des Objektes verwendet wird. Diese Linie sollte die Geometrie des Geo-Objektes (Linie oder Fläche)
komplett schneiden:

.. image:: img/edit18.png

Mit dem ``Teilen`` Button wird das Objekte *geteilt*. Durch ein erfolgreiches Teilen 
entstehen mindestens zwei neue Objekte. Die Sachdaten aus dem ursprünglichen Objekte werden in 
den neuen Objekte übernommen. Im angezeigten Dialog kann man entscheiden, ob das ursprüngliche 
Objekt erhalten oder gelöschte werden soll:

.. image:: img/edit19.png

Entscheidet man sich für ``Ursprüngliches Objekt löschen`` wird das am Anfang selektierte Objekte
gelöscht.

.. note::
   Löscht man das ursprüngliche Objekt, kann es später theoretisch mit *Undo* wiederhergestellt werden
   (siehe voriges Kapitel).

