Editierbare Felder: Autovalues
==============================

*Autovalues* sind Felder, die nicht vom Anwender eingegeben werden müssen, sondern aufgrund von anderen Kriterien 
vor dem Speichern vom am Server *automatisch* gesetzt werden.
So kann damit beispielsweise der Username des aktuellen Anwenders oder das Erstellungsdatum in ein Feld übertragen 
werden. Diese Felder werden für die Eingabemaske in der Regel als *readonly* oder nicht sichtbar angeführt.

Im folgenden Beispiel wir beispielsweise die Länge der erstellten Liniengeometrie in ein Feld übernommen:

.. image:: img/editing18.png

Wird als *Autovalue* Custom verwendet, kann im Eingabefeld der Autovalue eingegeben werden.
Hier könnten beispielsweise Konstante Werte mit ``=WEBGIS`` eingegeben werden, wenn man möchte,
dass ein Feld (zB QUELLE) immer  ``WEBGIS`` eingetragen werden sollte.

Weiters sind auch automatische Attributierungen über räumliche Beziehungen zu anderen Featureklassen möglich,
beispielsweise:

``NR FROM GDBAbfrage service kataster``

In das Feld wird das Attribut NR jener Objekte aus dem Thema GDBAbfrage geschrieben, welche sich mit dem gespeicherten 
Objekt räumlich decken. Gibt es mehrer Ergebnisse, werden diese mit Strichpunkten getrennt.

``TYP FROM kasten service strom@mycms BUFFERDIST 20 SEPERATOR space-space MAX 10``

In das Feld wird das Attribute TYP jener Objekte aus dem Thema kasten geschrieben, welche im Umkreis von 20m
liegen (BUFFERDIST 20). Gibt es mehrer Ergebnisse werden diese mittels Leerzeichen-Bindestrich-Leerzeichen 
voneinander getrennt (SEPERATOR space-space). Es werden jedoch maximal zehn Ergebnisse übernommen (MAX10).

Der Autovalue ``db_select`` erfordert ebenfalls die Eingabe weiterer Werte in die beiden Eingabefelder.
Mit diesem Autovalue wird vor dem Speichern eine Wert über eine Datenbankabfrage befüllt. In die Felder
muss hier der *ConnectionString* und das *SQL Stamtement* eingeben werden:

.. image:: img/editing19.png

Über Platzhalter wie ``{{VORGANG_TEXT}}`` kann dabei auf aktuelle Eingaben zugegriffen werden.
