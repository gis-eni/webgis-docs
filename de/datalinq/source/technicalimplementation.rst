Technische Umsetzung
====================

Die Architektur von **WebGIS DataLinq** basiert auf einer modularen und hierarchischen Struktur, die eine flexible und effiziente Datenabfrage sowie -darstellung ermöglicht. Das System besteht aus drei zentralen Komponenten:

- **Endpoint (Endpunkt)**
- **Query (Abfrage)**
- **View (Ansicht)**

===============

.. image:: img/ad2_1.png

===============

Struktur der Komponenten
------------------------

1. Endpoint (Endpunkt)
----------------------
Der **Endpunkt** stellt die Verbindung zu den Datenquellen her und dient als Schnittstelle für externe Systeme. Er kann verschiedene Quellen ansprechen, darunter:

- **Datenbanken**  
- **REST-APIs**  
- **Weitere WebGIS DataLinq-Instanzen**  

Ein Endpunkt definiert somit die Grundlage für Datenabfragen und bestimmt, woher die Daten stammen.

2. Query (Abfrage)
------------------
Die **Abfrage (Query)** ermöglicht den Zugriff auf die Daten, die über den Endpunkt bereitgestellt werden. Sie kann:

- Spezifische Informationen aus der Datenquelle abrufen  
- Daten in Form von **Rohdaten (JSON)** oder als aufbereitete **Ansicht (View)** zurückgeben  

Die Abfragen sind flexibel konfigurierbar und können Parameter enthalten, um gezielte Datensätze zu filtern.

3. View (Ansicht)
-----------------
Die **Ansicht (View)** dient der **Visualisierung und Präsentation** der Abfrageergebnisse. Sie ermöglicht:

- Die formatierte Darstellung der Daten in einer lesbaren Form  
- Die Umsetzung von Diagrammen oder strukturierten Reports  
- Eine nutzerfreundliche Präsentation von Analyseergebnissen  

Falls nur eine **Rohdatenausgabe (JSON)** benötigt wird, kann auf die Erstellung einer Ansicht verzichtet werden.


