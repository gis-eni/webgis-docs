================
Spezielle Themen
================

Spatial Reference System
========================

Für eine WebGIS-Karte können verschiedene Koordinatensysteme verwendet werden. Bestimmte Berechnungen, wie das Messen einer Strecke, werden im jeweiligen Karten-Koordinatensystem *kartesisch* durchgeführt. *Kartesisch* bedeutet in diesem Zusammenhang, dass für die Berechnung direkt die ``(X, Y)``-Werte des aktuellen Koordinatensystems genutzt werden.

Dies kann zu Problemen führen, wenn das Koordinatensystem starke Verzerrungen aufweist, da dann auch die ``(X, Y)``-Werte nicht mehr maßstabsgetreu sind. Ein typisches Beispiel ist die **WebMercator-Projektion**, die in unseren Breitengraden eine starke Verzerrung in der **Nord-Süd-Richtung** aufweist.  
Gemessene Längen und Flächen in dieser Projektion sind daher immer größer als in der Realität.

Um dieses Problem zu lösen, kann die Variable ``calcCrs`` genutzt werden. Damit lässt sich der **EPSG-Code** eines Koordinatensystems angeben, in dem Berechnungen durchgeführt werden:

.. code-block:: javascript

    if (mapUrlName === "Basemap_at") {
        calcCrs = 31287;  // Lambert
    }

In diesem Beispiel werden Berechnungen im österreichweiten **Lambert-Koordinatensystem** durchgeführt. Alle für die Berechnung relevanten Koordinaten werden automatisch intern in **Lambert** umgerechnet, bevor die Berechnung stattfindet.

**Weitere Beispiele:**

.. code-block:: javascript

    calcCrs = 31256;    // Berechnungen im GK-M34

Falls ``calcCrs`` nicht gesetzt ist, erfolgt die Berechnung standardmäßig im jeweiligen **Karten-Koordinatensystem**. Falls dieses **geographisch** (Längen- und Breitengrade) oder **WebMercator** ist, wird empfohlen, ``calcCrs`` explizit zu setzen!

WebGIS und GNSS
===============

WebGIS kann mit einer externen **GNSS-Antenne** (GPS) zur Vermessung genutzt werden. Da es sich hierbei um eine spezielle Anwendung handelt, wird hier nur eine grundlegende Beschreibung gegeben. Eine detailliertere Dokumentation ist auf Nachfrage verfügbar.

Die relevanten Einstellungen für den ``custom.js``-Eintrag lauten:

.. code-block:: javascript

    webgis.currentPosition = webgis.currentPosition_watch;

    webgis.currentPosition.minAcc = 0.5;   // Mindestgenauigkeit in Metern
    webgis.currentPosition.maxAgeSeconds = 0.1;  // Maximales Alter der Positionsdaten in Sekunden
    webgis.currentPosition.useWithSketchTool = true;  

Die letzte Einstellung ermöglicht die Nutzung des GPS mit allen **Sketch-Tools**. Dazu erhält der Anwender eine zusätzliche *GPS-Bubble*. Diese ist standardmäßig **deaktiviert** (grau). Zieht man die Bubble aus dem **Inaktiv-Bereich**, wechselt sie ihre Farbe von **Rot** zu **Grün**, sobald die eingestellte **Genauigkeit** erreicht ist.  

Sobald sowohl die *Bubble* als auch das angezeigte **Fadenkreuz** grün sind, kann der Benutzer durch einen Klick auf die *Bubble* einen **Vertex** für den Sketch übernehmen. Dieser Vorgang kann beliebig oft wiederholt werden, solange die Bubble aktiv bleibt (die Karte folgt dem Fadenkreuz bei Bewegung). Wird die Bubble zurück in den **Inaktiv-Bereich** geschoben, wird die GNSS-Erfassung beendet.

.. image:: img/image7.png

.. important:: Solange die *GPS-Bubble* aktiv ist, kann ein **Vertex nur über dieses Werkzeug** gesetzt werden!

Helmert-Transformation (2D)
===========================

Falls eine zusätzliche **Helmert-Transformation (2D)** benötigt wird, um Spannungen im **Festpunktfeld** auszugleichen, kann diese folgendermaßen definiert werden:

.. code-block:: javascript

    webgis.continuousPosition.helmert2d = {
            srs: 31256,
            Cx:  0.600,
            Cy: -0.234,
            Rx: -67946.151,
            Ry: 215079.498,
            r: 399.9992 * Math.PI / 200,
            scale: 1 + (-6.576 * 1e-6)
    };

Transformationen über einen WebGIS-Dienst
-----------------------------------------

Falls für verschiedene Regionen unterschiedliche Transformationen benötigt werden, können diese über einen **Transformations-Info-Service** automatisch abgerufen werden:

.. code-block:: javascript

    webgis.continuousPosition.useTransformationService = true;

Dieser **Transformations-Info-Service** ist ein WebGIS-Dienst, der die Definitionen der jeweiligen Transformationen bereitstellt. Die Informationen zu den einzelnen Transformationen müssen im Verzeichnis ``etc/trafo`` in der Datei **helmert.json** gespeichert werden.

Die Struktur dieser Datei sieht beispielsweise so aus:

.. image:: img/image8.png
