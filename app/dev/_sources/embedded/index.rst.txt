Eingebettete Karten
===================

Unter eingebetteten Karten, werden WebGIS API Anwendungen (Karten) verstanden, die auf einer Drittseite,
eingebunden (eingebettet) werden. Als Drittseite wird in Folge die Webseite bezeichnet, auf der die WebGIS
Karte eingebettet wird.

Es gibt dafür grundsätzlich zwei Methoden:

* Auf der Drittseite werden wie in der API Anleitung gezeigt die API Javascript Dateien geladen und damit eine Karte gebaut. 
  Die Karte wird dann einen DOM Element der drittseite angezeigt. Beim Erstellen der Karte wird ein *map* Objekt erstellt,
  auf das in der weiteren Folge mit den in der API Anleitung beschriebenen Methoden zugegriffen werden kann.



* Eine bestehende WebGIS Anwendung (Karte) wird über ein ``iframe`` auf einer Drittseite eingebunden. Dabei hat die Drittseite 
  in der Regel keinen Zugriff auf das auf der Unterseite erstellte *map* Objekt. Allerdings besteht die Möglichkeit über
  ``callback`` Funktionen auf Änderungen des Kartenausschnittes zu reagieren. 

  .. toctree::
    :maxdepth: 2

    iframe

