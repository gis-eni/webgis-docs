WebGIS 5.0 API: webgis
======================

Members
-------

========================    ===================================================================================
Name                        Beschreibung                                                                
========================    ===================================================================================
:ref:`createMapAnchor`      Mit dieser Methode wird eine neue Karte in einem HTML (div) Element erzeugt.                                
:ref:`initAnchor`           Einstiegspunkt für jede WebGIS-API Anwending.
:ref:`projectAnchor`        Projektziert Koordinaten von WGS84 in ein projekziertes Koordinatensystem.                                       
:ref:`registerCRSAnchor`    Registriert ein Koordinatensystem für die Projektion.
:ref:`unprojectAnchor`      Projektziert Koordinaten aus einen projekzierten Koordinatensystem nach WGS84.                                      
========================    ===================================================================================



Properties
----------

=============================       =============================================================================
Name                                Beschreibung                                                                
=============================       =============================================================================
:ref:`clientidPropertyAnchor`       Die Client Id für die WebGIS-API Anwendung.                                     
=============================       =============================================================================


Member Details
--------------

.. _createMapAnchor :

createMap (elemId, options)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Mit dieser Methode wird eine neue Karte in einem HTML (div) Element erzeugt. Als Parameter werden hier die Id des Ziel HTML Elements und ein Objekt, dass die Karte beschreibt übergeben. In diesem Objekt werden mindestens der Karten-Extent (entpricht Ausdehung und Koordinatensystem der Karte) und die zu ladenden Dienste angeführt.

*Beispiel*

.. code-block:: javascript

    var map = webgis.createMap('map', {
        extent: 'stmk_m34@ccgis_sdep',
        services: 'ortsplan@ccgis_sdep,estag_basis_ags@ccgis_sdep,estag_dkm_ags@ccgis_sdep'
    });

Die Name der Extents und Dienste sind von der jeweiligen API Betreiber abhängig und können über die REST Schnittstelle eingesehen werden.



.. _initAnchor :

init (oninit)
^^^^^^^^^^^^^

*Beschreibung*

Einstiegspunkt für jede WebGIS-API Anwending. Diese Methode initialisiert die alle notwendigen API Elemente. Als Parameter wird eine Funktion übergeben, die nach der Initialisierung aufgerufen wird. Erst nach der Initialsierung kann begonnen werden, Karten zu erzeugen.

*Beispiel*

.. code-block:: javascript

    webgis.init(function() {
        // ab hier können Karten erzeugt werden
        var map = webgis.createMap('map', {
            extent: 'stmk_m34@ccgis_sdep',
            services: 'ortsplan@ccgis_sdep,estag_basis_ags@ccgis_sdep,estag_dkm_ags@ccgis_sdep'
        });
    });




.. _projectAnchor :

project (id, lnglat)
^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Projektziert Koordinaten von WGS84 in ein projekziertes Koordinatensystem. Als Parameter werden die Id des Koordinatensystems (EPSG Code) und eine Array mit den Koordinaten [geographicse Länge, geographische Breite] übergeben. Wenn die Zielkoordinatensystem nicht das Kartenkoordinatensystem ist, muss dieses zuerst mit ``webgis.registerCRS`` registriert werden. Ansonsten wird ein Eingabewert zurückgegeben. Das Ergebnis ist wieder ein Array mit den projekzierten Koordinaten [X,Y]

*Beispiel*

.. code-block:: javascript

    var xy=webgis.project(31259, [15, 47]);
    var X=xy[0];
    var Y=xy[1];




.. _registerCRSAnchor :

registerCRS (id)
^^^^^^^^^^^^^^^^

*Beschreibung*

Registriert ein Koordinatensystem für die Projektion. Intern wird in der Karte mit geographischen Koordinaten (EPSG:4326) gerechnet. Zum Umrechnenen von projezierten Koordinaten in dieses System gibt es die Methoden ``webgis.project`` und ``webgis.unproject``. Durch das Laden einer Karte mit ``webgis.createMap`` ist eine Projektion zwischen dem Kartensystem (Extent) und den geographischen Koordinaten möglich. Sollten auch noch andere Koordinatensystem projeziert werden, müssen diese mit dieser Methode registriert werden.  

*Beispiel*

.. code-block:: javascript

    webgis.registerCRS(31259);

Registriert zusätzlich zum Karten-Koordinatensystem BMN-M34. Danach kann mit den Methoden ``webgis.project`` und ``webgis.unproject`` projeziert werden.



.. _unprojectAnchor :

unproject (id, xy)
^^^^^^^^^^^^^^^^^^

*Beschreibung*

Projektziert Koordinaten aus einen projekzierten Koordinatensystem nach WGS84. Als Parameter werden die Id des Koordinatensystems (EPSG Code) und eine Array mit den Koordinaten  [X,Y] übergeben. Wenn die Zielkoordinatensystem nicht das Kartenkoordinatensystem ist, muss dieses zuerst mit ``webgis.registerCRS`` registriert werden. Ansonsten wird eine Eingabewert zurückgegeben. Das Ergebnis ist wieder ein Array mit den geographischen Koordinaten [geographicse Länge, geographische Breite]

*Beispiel*

.. code-block:: javascript

    var ll=webgis.unproject(31259, [682467.9, 215093.3]);
    var lat=ll[0];
    var lng=ll[1];


Property Details
----------------


.. _clientidPropertyAnchor :

clientid
^^^^^^^^

*Beschreibung*

Die Client Id für die WebGIS-API Anwendung. Entwickelt man einen API Client, muss man diesen erst als API Subscriber erstellen. Die dabei erzeugte Client Id muss hier angeben werden und gilt nur für Clients die unter einer bestimmter Domäne laufen (HTTP-Referer).

**Achtung:** Die Client Id muss noch vor dem Aufruf von ``webgis.init()`` zugewiesen werden!


*Beispiel*

.. code-block:: javascript

    webgis.clientid='meine client id';
