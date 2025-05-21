Fläche messen
=============

Mit diesem Werkzeug kann ein *Sketch* (Entwurfspolygon) gezeichnet werden. 
Sobald das Polygon gültig ist (mindestens drei Stützpunkte aufweist), wird in den Eingabefeldern im 
Werkzeugdialog der Umfang in Metern und die Fläche in m² angezeigt:

.. image:: img/area1.png

Mit dem *Sketch entfernen* Button kann ein neues Polygon begonnen werden.
Als Zusatzinformation wird im Dialog noch die *Sketch Information* des aktuellen Liniensegments angezeigt (Länge und Azimut).

Es können alle Möglichkeiten der *Sektch* Werkzeuge genutzt werden (Konstruieren, Objektfang, Trace, ...).

.. note::
   Ist das Polygon nicht gültig, wird als Fläche 0 angegeben. Ein Polygon ist ungültig, wenn es weniger als drei
   Stützpunkte aufweist oder sich einzelne Segmente schneiden (Self-Intersecting-Polygon). 