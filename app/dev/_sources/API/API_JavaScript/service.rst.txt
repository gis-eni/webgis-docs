WebGIS 5.0 API: service
=======================

Members
-------

======================================  ===============================================================================================
Name	                                Beschreibung	                                                                               
======================================  ===============================================================================================
:ref:`getLayerAnchor`                   Gibt einen Layer aufgrund seiner Id zurück.
:ref:`getLayerFromNameAnchor`	        Gibt ein Layer aufgrund seines Namens zurück.
:ref:`getLayerIdsAnchor`                Gib eine Auflistung aller Layer Ids in einem Service zurück.
:ref:`getLayerIdsFromNamesAnchor`       Gibt ein Array mit den Ids der übergeben Layer zurück.
:ref:`getLegendUrlAnchor`               Erzeugt einen Link zum Abholen das aktuellen Legendbildes für den Dienst.
:ref:`getPreviewUrlAnchor`	            Mit dieser Methode kann eine Vorschaubild eines Dienstes in einer gewissen Größe abgeh...
:ref:`layerInScaleAnchor`               Überprüft, ob ein Layer im aktuellen Kartenmaßstab sichtbar ist.
:ref:`refreshAnchor`	                Erzwingt ein Neuzeichnen des Dienstes in der Karte.
:ref:`removeAnchor`	                    Entfernt einen Dienst aus einer Karte.
:ref:`setLayerVisibilityAnchor`	        Setzt die Sichtbarkeit von Layern über ihre Id.
:ref:`setOpacityAnchor`                 Gib die Transparenz für ein Service an.
:ref:`setServiceVisibilityAnchor`	    Setzt alle Layer mit einer ensprechenden Id sichbar und alle restlichen Layer unsichtbar.
======================================  ===============================================================================================


Properties
----------

=================================   ===============================================================================================
Name	                            Beschreibung	                                                                               
=================================   ===============================================================================================
:ref:`idPropertyAnchor`             Die Id des Dienstes.
:ref:`isBasemapPropertyAnchor`	    Gibt an, ob es sich bei diesem Service um einen Hintergrunddienst handelt.   
:ref:`layersPropertyAnchor`         Ein Array der Layer des Dienstes.
:ref:`mapPropertyAnchor`	        Das map Objekt der in dem das Service eingebunden ist.
:ref:`namePropertyAnchor`           Der Name des Services.
:ref:`opacityPropertyAnchor`	    Gibt die Transparenz des Dienstes an.
=================================   ===============================================================================================


Member Details
--------------

.. _getLayerAnchor :

getLayer (id)
^^^^^^^^^^^^^

*Beschreibung*

Gibt einen Layer aufgrund seiner Id zurück. Wenn der Layer im Dienst nicht gefunden wird, ist der Rückgabewert ``null``.


*Beispiel*


.. code-block:: javascript

    var layer = service.getLayer('2');
    if(layer != null) {

        // do something

    }


.. _getLayerFromNameAnchor :

getLayerFromName (name)
^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Gibt ein Layer aufgrund seines Namens zurück. Wenn der Layer im Dienst nicht gefunden wird, ist der Rückgabewert ``null``.


*Beispiel*

.. code-block:: javascript

    var layer = getLayerFromName('Verwaltungsdaten\\PLZ-Flächen');
    if(layer != null) {

    // do something

    }


.. _getLayerIdsAnchor :

getLayerIds ()
^^^^^^^^^^^^^^

*Beschreibung*

Gib eine Auflistung aller Layer Ids in einem Service zurück. Der Rückgabewert ist ein Array, das dann beispielsweise wieder an die Methode ``setLayerVisibility([],true/false)`` übergeben werden, um alle Layer in ein Dienst aus- oder einzuschalten.

*Beispiel*

Alle Layer in einem Dienst unsichtbar schalten. Der gleiche Effekt kann auch eleganter mit der Methode ``setServiceVisibility();`` erfolgen.


.. code-block:: javascript

    var layerIds = service.getLayerIds();
    service.setLayerVisibility(layerIds, false);
    //
    // Wieder alle Layer sichtbar schalten
    service.setLayerVisibility(layerIds, true);
    // bzw.
    service.setServiceVisibliity(service.getLayerIds());



.. _getLayerIdsFromNamesAnchor :

getLayerIdsFromNames (layernames)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Gibt ein Array mit den Ids der übergeben Layer zurück. Übergeben wird ein Array von String mit den Layernamen.

Die Funktion ist nützlich, da die Ids beispielsweise für das setzen der Sichtbarkeit der Layer notwendig ist. Wenn sich bei Layer die Ids ändern können (zB beim AGS Services durch umsortieren der Layer), empfielt es die aktuellen Ids aus dem Namen zu holen.


*Beispiel*


.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');
    var layerIds=service.getLayerIdsFromNames(['Verwaltungsdaten\\PLZ-Flächen']);
    //console.log(layerIds);
    service.setLayerVisibility(layerIds,true);


.. _getLegendUrlAnchor :

getLegendUrl () 
^^^^^^^^^^^^^^^

*Beschreibung*

Erzeugt einen Link zum Abholen das aktuellen Legendbildes für den Dienst. Die Legende ist abhängig von der aktuellen Layer Sichtbarkeit und vom Kartenmaßstab. Die Url kann verwendet werden, um beispielsweise über einen AJAX Request die Legende abzuholen und das Ergebnis an ein Image Element zu übergeben. Der Rückgabewert ist ein JSON Objekt mit der Eigenschaft url. Diese Url ist ein Link auf das eigentliche Legenden Bild (png oder jpg). 

*Beispiel*


.. code-block:: javascript

    $.ajax({
        url: service.getLegendUrl(),
        type: 'get',
        success: function(result) {
            if (result && result.url) {
                webgis.$('<img>').attr('src', result.url).appendTo('body');
            }
        }
    });


.. _getPreviewUrlAnchor :

getPreviewUrl (r)
^^^^^^^^^^^^^^^^^

*Beschreibung*

Mit dieser Methode kann eine Vorschaubild eines Dienstes in einer gewissen Größe abgeholt werden. Der Rückgabewert ist eine Url die einen Bild entspricht (png oder jpg). Diese Vorschau ist abhängig vom aktuellen Kartenmaßstab. Anwendungen für diese Methode sind beispielsweise die Vorschaubilder für die Hintergrundkarten im TOC. 

Der Übergabeparameter muss ein Objekt mit den Werten ``width`` und ``height`` sein und gibt die Größe des Vorschaubildes an.

*Beispiel*


.. code-block:: javascript

    webgis.$("<div>").css('background', 'url(' + service.getPreviewUrl({width: 200, height: 200}) + ')').appendTo('body');


.. _layerInScaleAnchor :

layerInScale (id)
^^^^^^^^^^^^^^^^^

*Beschreibung*

Überprüft, ob ein Layer im aktuellen Kartenmaßstab sichtbar ist. Gewisse Layer in einem Service können Maßstabsanhängig sein. Es macht beispielsweise wenig Sinn Grundstücksgrenzen in sehr kleinen Maßstaben darzustellen. Um abzufragen, ob ein Layer im aktuellen Maßstabsbereich sichtbar ist, kann diese Methode verwendet werden. Der Übergabeparameter ist die Id des entsprechenden Layers. Der Funktionsrückgabe wert ist entweder ``true`` oder ``false``.

*Beispiel*

.. code-block:: javascript

    if(service.layerInScale('1')) {   // Layer mit Id 1
        // do something
    }


.. _refreshAnchor :

refresh ()
^^^^^^^^^^

*Beschreibung*

Erzwingt ein Neuzeichnen des Dienstes in der Karte. Durch diesen Befehl wird das Kartenbild für diesen Dienst neu vom Kartenserver abholt. Die Methode sollte in der Regel nicht aufgerufen werden müssen. Nach Änderungen in der Karte oder der Sichtbarkeit von Layern in diesem Dienst, wird die Methode automasich vom webGIS Framework ausgeführt.

*Beispiel*

.. code-block:: javascript

    service.refresh();


.. _removeAnchor :

remove () 
^^^^^^^^^

*Beschreibung*

Entfernt einen Dienst aus einer Karte.

*Beispiel*

.. code-block:: javascript

    service.remove();


.. _setLayerVisibilityAnchor :

setLayerVisibility (layerids, visible)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Setzt die Sichtbarkeit von Layern über ihre Id. Übergeben werden die entspechenden Ids als Array und der Bool-Wert, für die Sichtbarkeit: true=sichtbar, false=unsichtbar.

*Beispiel*

.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');
    service.setLayerVisibility(['1','2','3'],true);


.. _setOpacityAnchor :

setOpacity (opacity)
^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Gib die Transparenz für ein Service an. Der Wert muss zwischen 0.0 und 1.0 liegen:

0.0 ... komplett durchlässig

1.0 ... nicht transparent

*Beispiel*


.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');
    service.setOpacity(0.5);



.. _setServiceVisibilityAnchor :

setServiceVisibility (layerids)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Beschreibung*

Setzt alle Layer mit einer ensprechenden Id sichbar und alle restlichen Layer unsichtbar. Der Übergabe Parameter ist ein Array mit den Layer-Ids. Wird ein leeres Array oder Nichts übergeben, werden alle Layer in einem Dienst unsichtbar gesetzt.

*Beispiel*


.. code-block:: javascript

    // Nur die Layer 1,2,3 sichtbar setzen
    service.setServiceVisibility(['1', '2', '3']);

    // Alle Layer in einen Dienst unsichtbar setzten
    service.setServiceVisibility(); 

    // Alle Layer sichtbar schalten
    service.setServiceVisibility(service.getLayerIds());




Property Details
----------------


.. _idPropertyAnchor :

id 
^^

*Beschreibung*

Die Id des Dienstes. Mit dieser Id kann ein Dienst auch in über ein ``map`` Objekt mit der Method ``getService(id)`` gefunen werden.

*Beispiel*

Das folgende Beispiel zeigt den Zusammenhang zwischen Dienst-Id und Karten Objekt.

.. code-block:: javascript

    // get service id
    var serviceId = service.id

    // get service map
    var map = service.map;

    // get service with id from map
    var service_with_id = map.getService(id);  


.. _isBasemapPropertyAnchor :

isBasemap
^^^^^^^^^

*Beschreibung*

Gibt an, ob es sich bei diesem Service um einen Hintergrunddienst handelt.

*Beispiel*


.. code-block:: javascript

    if(service.isBasemap == true) {
        // Do something
    }


.. _layersPropertyAnchor :

layers 
^^^^^^^^

*Beschreibung*

Ein Array der Layer des Dienstes. Die einzelnen Werte des besitzen wieder eigenschaften wie ``id`` und ``name``. 

*Beispiel*

Zum Suchen von Layern gibt es eigentlich die Methoden ``getLayer()``, ``getLayerFromName()``, und ``getLayerIdsFromNames()`` die verwendet werden sollten. In Ausnahme Fällen kann es aber auch wichtig sein die einzelen Layer aufzulisten

.. code-block:: javascript

    for(var l = 0; l < service.layers.length; l++) {
        var layer = service.layers[l];

        console.log(layer.id+" "+layer.name)
    }


.. _mapPropertyAnchor :

map
^^^

*Beschreibung*

Das map Objekt der in dem das Service eingebunden ist.

*Beispiel*


.. code-block:: javascript

    var serviceMap = service.map;
    map.zoomTo([10,40,20,50]);



.. _namePropertyAnchor :

name
^^^^

*Beschreibung*

Der Name des Services.


.. _opacityPropertyAnchor :

opacity
^^^^^^^

*Beschreibung*

Gibt die Transparenz des Dienstes an. Der Wert kann zwischen 0.0 (komplett tranzparent) und 1.0 (nicht transparent) liegen.

Der Wert sollte nicht gändert werden. Zum setzen der Transparenz soll die Methode :ref:`setOpacityAnchor` verwendet werden.

*Beispiel*


.. code-block:: javascript

    var currentOpacity = service.opacity;
