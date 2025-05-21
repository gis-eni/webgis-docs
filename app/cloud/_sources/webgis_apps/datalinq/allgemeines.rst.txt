.. sectnum::
    :start: 1

Allgemeines
===========

WebGIS DataLinq ist ein Werkzeug zur einfachen Abfrage von Datenbeständen aus verschiedenen Quellen sowie zur Bereitstellung und Darstellung der Ergebnisse. 
Der Fokus liegt auf dem einfachen, lesenden und schreibenden Datenzugriff.  

Ziele
-----

Um DataLinq möglichst universell aus allen möglichen Applikationen einsetzen zu können, wurden folgende Ziele definiert:

* Leichtes Einbinden/Aufrufen von unterschiedlichen Datenquellen
* Berechtigungen für Abfrage und Darstellung sind getrennt verwaltbar
* Ergebnisse als Rohdaten bzw. in aufbereiteter Form verfügbar
* Erstellung von Formularen zum Bearbeiten von Datensätzen
* Einfaches und schnelles Bearbeiten von Datensätzen
* Statistische Auswertung und Analyse von Datensätze
* Darstellung von Datensätzen und der Auswertung in Diagrammform

Datenquellen
------------

Folgende Datenquelle können für die Abfrage herangezogen werden:

* Datenbanken
* WebGIS REST-API Abfragen
* GeoJson
* GeoRss
* Plain Text: die Abfragen sind Listen von Werten als Text. Ideal für Auswahllisten
* Eine andere WebGIS DataLinq Anwendung

Ausgabemöglichkeiten
------------------------

Die Ausgabe der Ergebnisse ist in folgender Form verfügbar:

* Rohdaten der Abfrage als JSON
* Darstellung als HTML über ASP.NET Razor Markup
