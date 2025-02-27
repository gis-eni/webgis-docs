Berechtigungen (Security)
=========================

Standardmäßig sind alle Knoten des CMS Baumes für jeden Anwender (der Karten mit Diensten aus diesem CMS sehen kann) sichtbar.
Darf ein Anwender beispielsweise eine Karte nutzen, kann er theoretisch alle anderen Dienste aus dem CMS über den ``Dienste hinzufügen`` 
Button im **Karten Viewer** in die Karte einbinden (sofern dieser Button in der Karte angeboten wird).

Ist dies nicht erwünscht, können im CMS einzelnen Knoten des CMS Baumes berechtigt werden. Ist ein Knoten für einen Benutzer nicht berechtigt,
sind für diesen weder der Knoten, noch die darunter liegenden Knoten sichtbar. Ist beispielsweise der Knoten eines Kartendienstes berechtigt, 
gelten diese Berechtigungen auch für alle Abfragen und Editthemen dieses Dienstes.

.. note:: 
   Die Berechtigungen eines Knotens, werden an alle darunter liegenden Knoten vererbt.

Natürlich ist es dadurch auch möglich, dass beispielsweise ein Dienst für alle Anwender sichtbar und abfragbar, das Editieren von Themen
aber nur einem eingeschränkten Benutzerkreise vorbehalten ist. Und auch dabei können wieder einzelne Editierthemen unterschiedlich berechtigt sein.

.. toctree::
    :maxdepth: 2

    node
    security-button
    exclusive
    instanceroles