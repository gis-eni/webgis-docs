CMS Web-Oberfläche
==================

Über die Eigenschaften-Seite des CMS-Accounts gelangt man mit dem Button ``Open CMS Account`` zur 
eigentlichen CMS Web-Oberfläche (der erste Aufruf kann einige Sekunden dauern, da hier noch der CMS-Baum angelegt wird).

.. image:: img/image114.png

Im ersten Schritt sollten zunächst Hintergrunddienste angelegt werden.

**Hinweis:** In der Praxis würde man in einem leeren CMS zuerst auch eine Rechteckausdehnung definieren. 
Diese ist im WebGIS 5 notwendig, um überhaupt eine Karte initialisieren zu können. In diesem Objekt wird 
nicht nur die koordinative Ausdehnung einer Karte, sondern auch die Maßstäbe (Resolutionen) angegeben. Diese 
müssen den Auflösungen der eingebundenen Tile-Caches entsprechen. In der Cloud kann man jedoch später 
vorgefertigte Ausdehnungen für WebMercator aus dem öffentlichen CMS „webgiscloud“ verwenden.  
In der öffentlichen Cloud CMS „webgiscloud“ sind ebenfalls die Basemap.at-Tiles bereits vorhanden 
und könnten verwendet werden. Trotzdem werden diese hier zur Demonstration eingebunden.
