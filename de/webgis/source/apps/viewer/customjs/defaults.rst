========
Defaults
========

Mit dem *Javascript Objekt* ``webgis.defaults`` können diverse Default-Werte
festgelegt werden.

So werden beispielsweise Benutzer Einstellungen, die der Anwender im Viewer über 
**Einstellungen** (Burger-Menü) einstellt, im lokalen Browser Storage abgelegt:

.. image:: img/defaults-storage.png

Steigt ein Anwender in den Viewer ein und hat noch keine Einstellungen getroffen,
können mit ``webgis.defaults`` Standardwerte gesetzt werden:

.. code:: javascript

    // sets the default language
    webgis.defaults["map.properties.language"] = "en";  // de

    // sets the default styling (here: space-saving)
    webgis.defaults["map.properties.cssClass"] = "_space-saving";  // default

    //sets the default color scheme (here: Light)
    webgis.defaults["map.properties.colorScheme"] = "_bg-light";  // default, _bg-dark

    // sets the default viewer layout for larger screens (here: desktop)
    webgis.defaults["map.properties.template.1200"] = "desktop";  // touch