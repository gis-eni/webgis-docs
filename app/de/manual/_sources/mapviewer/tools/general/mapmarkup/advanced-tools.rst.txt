Spezialwerkzeuge
================

Neben Linien, Flächen, Freihand, Texten, Rechtecken und Kreisen gibt es noch speziellere Graphiken auf die hier eingegangen wird.

Umgebungskreis
--------------

Mit diesem Werkzeug kann ein Kreis mit einem bestimmten Radius um einen Mittelpunkt definiert werden. Zum eigentlich Umgebungskreis werden noch Kreise mit Zwischenschritten angezeigt und beschriftet:

.. image:: img/advanced-tools1.png

.. image:: img/advanced-tools1_1.png

Das Ergebnis kann für Abstandsuntersuchungen verwendet werden.

Bemaßungslinie
--------------

Mit diesem Werkzeug kann eine (Poly-) Linie gezeichnet werden, bei der jedes Segment mit der entsprechenden Länge in Metern beschriftet wird:

.. image:: img/advanced-tools2.png

.. note::
   Die angezeigte Länge wird immer *live* aus den Stützpunkte im aktuellen Karten Koordinatensystem berechnet. Übernimmt man die Zeichnung (durch Speichern und Laden) in eine Karte mit einem anderen Koordinatensystem, 
   könne die Werte abweichen. Dies gilt für allen für Karten, in denen mit *WebMercator* gerechnet wird, weil es hier große Verzerrungen geben kann. Welches Koordinatensystem verwendet wird kann im *Kartenviewer*
   links unten abgelesen werden.
   
   .. image:: img/advanced-tools3.png

Hektometrierungslinie
---------------------

Bei dieser Linie werden Zwischenpunkte über einen vordefinierten Abstand (z.B. alle 100m) markiert und beschriftet:

.. image:: img/advanced-tools4.png

Als Anzeigeeinheit kann Meter [m] und Kilometer [km] angebeben werden.

.. note::
   Gleich wie bei der Bemaßungslinie werden auch hier die Abstandspunkte *live* berechnet und beziehen sich immer auf das aktuelle Kartenkoordinatensystem. Fügt man die Zeichnung in unterschiedliche Karten ein, kann es zu Abweichungen kommen!


Kompass
-------

Neu hinzugekommen zum Map-Markup ist das Spezialwerkzeug *Kompass*.

.. image:: img/advanced-tools5.png

Fügt man einen solchen ein, hat man unter *Symbolik bearbeiten* die Möglichkeit, Farbe, Linienstärke und Anzahl der Winkel dementsprechend anzupassen.  

.. image:: img/advanced-tools6.png



