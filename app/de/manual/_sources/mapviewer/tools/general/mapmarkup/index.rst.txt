.. _mapmarkup:

Zeichnen (Map Markup & Annotations)
===================================

Zeichnen (Map-Markup) ist ein sehr mächtiges Kartenwerkzeug und kann für verschiedene Anwendungen verwendet werden.
Die Grundidee von Map-Markup ist es, die Karte mit Zeichenelementen (Linien, Flächen, Texte, Symbole) zu erweitern
und Orte für einen Ausdruck zu markieren, zu verschicken oder anderweitig zur Verfügung zu stellen.

Mit Map-Markup sollten nur kurzlebige Zeichnungen erstellt werden, die auch nicht zu viele Objekte enthalten.
Die Zeichnungen können zwar gespeichert werden, müssen aber nicht ewig vom Kartenviewer-Betreiber auf dem Server
behalten werden.

Ebenfalls besteht die Möglichkeit, das Map-Markup herunterzuladen und selbst zu speichern. Allerdings sollte auch
hier darauf hingewiesen werden, dass zukünftige Versionen der Software nicht hundertprozentig kompatibel mit alten
Projektdaten sein müssen und gewisse Eigenschaften verloren gehen können.

Wenn Sie das Tool zum ersten Mal nutzen, sollten Sie eventuell die unten stehenden Punkte berücksichtigen.

.. toctree::
   :maxdepth: 3

   manual.rst
   advanced-tools.rst
   manage.rst
   selection.rst

Beispiele für gute Anwendungsfälle
++++++++++++++++++++++++++++++++++

* Markieren eines Standortes und Ausdrucken bzw. Teilen der Karte

* Einzeichnen von kurzen Wegbeschreibungen (ebenfalls zum Drucken oder Teilen)

* Einzeichnen von (Wander) Wegen und herunterladen der Tracks im GPX Format für ein Navigationsgerät

* Hochladen von bestehenden GPX Dateien, um die Tracks und Wegpunkte zu drucken oder zu teilen

* Kleinere lokal begrenzte Projektierungen. Dabei sollten die Zeichnungen nach der Fertigstellung allerdings heruntergeladen und gespeichert werden, um keinen Datenverlust zu erleiden.

* Kleinere lokal begrenzte Projektierungen auf Basis der Kartendaten und Herunterladen der gezeichneten Geo-Objekte im Esri Shape Format zum Weiterverarbeiten in unterschiedlichen Softwarepaketen.


Beispiele für schlechte Anwendungsfälle
+++++++++++++++++++++++++++++++++++++++

* Größere und lokal ausgedehnte Projekte und Verspeicherung dieser Projekte am Server des Kartenviewer Betreibers

* Verwalten von Leitungs-/Kanalnetzen für eine komplette Gemeinde/Kommunalverband

* Verwaltung/Erstellung von Flächenwidmungsplänen

.. note::
   Für die hier als schlechte Beispiele angeführten Anwendungsfälle eignet sich eher das Editing/Bearbeiten Werkzeug!


Alternativen
++++++++++++

Möchten Sie ein hier angeführtes Projekt mit dem Kartenviewer umsetzen, wenden Sie sich bitte an den 
Betreiber des Kartenviewers oder an den Betreiber von http://webgiscoud.com. 

Der bessere Ansatz ist hier, mit den Editwerkzeugen zu arbeiten. Damit werden die gezeichneten Geo-Objekte in einer
Geodatenbank gespeichert, was folgende Vorteile bringt:

* Daten bleiben dauerhaft gespeichert 

* Daten können aus einer Geodatenbank leichter in eine andere Geodatenbank überführt werden. Man kann also vorerst einmal klein beginnen und den Kartenviewer als Edit-Client verwenden und bei Bedarf auf ein eigenes GI-System umsteigen.

* Pflege von Sachdaten: Neben der Geometrie können auch beliebige Sachdaten mit der Geometrie verknüpft werden (Widmungsart, Baujahr, Material, ...)

* Mehr Möglichkeiten in der kartographischen Darstellung der Daten

* Bessere Performance bei großen Datenmengen (quasi keine Größenbeschränkung der Projekte)

* Mehrbenutzer Betrieb: Mehrere Anwender können gleichzeitig (je nach Berechtigung) Geodaten bearbeiten
