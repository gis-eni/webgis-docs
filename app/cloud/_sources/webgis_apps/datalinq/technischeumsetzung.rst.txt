.. sectnum::
    :start: 2

Technische Umsetzung
====================

Struktur
--------

WebGIS DataLinq besteht aus drei Komponenten, die hierarchisch aufgebaut sind und unterschiedliche Aufgaben haben.

* Endpoint (Endpunkt)

    * Verbindung zur Datenbank, Rest-Schnittstelle oder einer weiteren DataLinq Anwendung

* Query (Abfrage)

    * Abfrage an den jeweiligen Endpunkt

    * Ergebnisse können als Rohdaten (JSON) oder als View (s.u.) bereitgestellt werden

* View (Ansicht)

    * Darstellung der Ergebnisse der o.g. Abfrage

    * Wenn nur Rohdaten des Ergebnisses gewünscht sind, ist kein View notwendig


.. image:: img/ad2_1.png


