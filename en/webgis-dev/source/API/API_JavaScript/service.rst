WebGIS 5.0 API: service
=======================

Members
-------

=================================  ===================================================================================
Name                               Description
=================================  ===================================================================================
:ref:`getLayerAnchor`              Returns a layer based on its id.
:ref:`getLayerFromNameAnchor`      Returns a layer based on its name.
:ref:`getLayerIdsAnchor`           Returns a list of all layer ids in a service.
:ref:`getLayerIdsFromNamesAnchor`  Returns an array with the ids of the given layers.
:ref:`getLegendUrlAnchor`          Creates a link for fetching the current legend image for the service.
:ref:`getPreviewUrlAnchor`         With this method, a preview image of a service can be fetched at a certain size.
:ref:`layerInScaleAnchor`          Checks whether a layer is visible at the current map scale.
:ref:`refreshAnchor`               Forces the service to be redrawn on the map.
:ref:`removeAnchor`                Removes a service from a map.
:ref:`setLayerVisibilityAnchor`    Sets the visibility of layers via their id.
:ref:`setOpacityAnchor`            Sets the transparency for a service.
:ref:`setServiceVisibilityAnchor`  Sets all layers with a corresponding id visible and all remaining layers invisible.
=================================  ===================================================================================


Properties
----------

==============================  =======================================================
Name                            Description
==============================  =======================================================
:ref:`idPropertyAnchor`         The id of the service.
:ref:`isBasemapPropertyAnchor`  Indicates whether this service is a background service.
:ref:`layersPropertyAnchor`     An array of the service's layers.
:ref:`mapPropertyAnchor`        The map object in which the service is included.
:ref:`namePropertyAnchor`       The name of the service.
:ref:`opacityPropertyAnchor`    Indicates the transparency of the service.
==============================  =======================================================


Member Details
--------------

.. _getLayerAnchor :

getLayer (id)
^^^^^^^^^^^^^

*Description*

Returns a layer based on its id. If the layer is not found in the service, the return value is ``null``.


*Example*


.. code-block:: javascript

    var layer = service.getLayer('2');
    if(layer != null) {

        // do something

    }


.. _getLayerFromNameAnchor :

getLayerFromName (name)
^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Returns a layer based on its name. If the layer is not found in the service, the return value is ``null``.


*Example*

.. code-block:: javascript

    var layer = getLayerFromName('AdministrativeData\\ZIP-Areas');
    if(layer != null) {

    // do something

    }


.. _getLayerIdsAnchor :

getLayerIds ()
^^^^^^^^^^^^^^

*Description*

Returns a list of all layer ids in a service. The return value is an array, which can then, for example, be passed back to the ``setLayerVisibility([],true/false)`` method, to switch all layers in a service on or off.

*Example*

Sets all layers in a service invisible. The same effect can also be achieved more elegantly with the ``setServiceVisibility();`` method.


.. code-block:: javascript

    var layerIds = service.getLayerIds();
    service.setLayerVisibility(layerIds, false);
    //
    // Set all layers visible again
    service.setLayerVisibility(layerIds, true);
    // or
    service.setServiceVisibliity(service.getLayerIds());



.. _getLayerIdsFromNamesAnchor :

getLayerIdsFromNames (layernames)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Returns an array with the ids of the given layers. An array of strings with the layer names is passed.

The function is useful because the ids are needed, for example, for setting the visibility of layers. If the ids for a layer can change (e.g. for AGS services, by reordering the layers), it is recommended to fetch the current ids from the name.


*Example*


.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');
    var layerIds=service.getLayerIdsFromNames(['AdministrativeData\\ZIP-Areas']);
    //console.log(layerIds);
    service.setLayerVisibility(layerIds,true);


.. _getLegendUrlAnchor :

getLegendUrl ()
^^^^^^^^^^^^^^^

*Description*

Creates a link for fetching the current legend image for the service. The legend depends on the current layer visibility and the map scale. The URL can be used, for example, to fetch the legend via an AJAX request and pass the result to an image element. The return value is a JSON object with a ``url`` property. This URL is a link to the actual legend image (png or jpg).

*Example*


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

*Description*

With this method, a preview image of a service can be fetched at a certain size. The return value is a URL pointing to an image (png or jpg). This preview depends on the current map scale. Applications for this method include, for example, the preview images for the background maps in the TOC.

The parameter must be an object with the values ``width`` and ``height``, and specifies the size of the preview image.

*Example*


.. code-block:: javascript

    webgis.$("<div>").css('background', 'url(' + service.getPreviewUrl({width: 200, height: 200}) + ')').appendTo('body');


.. _layerInScaleAnchor :

layerInScale (id)
^^^^^^^^^^^^^^^^^

*Description*

Checks whether a layer is visible at the current map scale. Certain layers in a service can be scale-dependent. For example, it makes little sense to show parcel boundaries at very small scales. This method can be used to query whether a layer is visible in the current scale range. The parameter is the id of the corresponding layer. The function's return value is either ``true`` or ``false``.

*Example*

.. code-block:: javascript

    if(service.layerInScale('1')) {   // layer with id 1
        // do something
    }


.. _refreshAnchor :

refresh ()
^^^^^^^^^^

*Description*

Forces the service to be redrawn on the map. This command fetches the map image for this service from the map server again. This method generally should not need to be called. After changes to the map or the visibility of layers in this service, the method is automatically executed by the webGIS framework.

*Example*

.. code-block:: javascript

    service.refresh();


.. _removeAnchor :

remove ()
^^^^^^^^^

*Description*

Removes a service from a map.

*Example*

.. code-block:: javascript

    service.remove();


.. _setLayerVisibilityAnchor :

setLayerVisibility (layerids, visible)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Sets the visibility of layers via their id. The corresponding ids are passed as an array, along with the boolean value for visibility: true=visible, false=invisible.

*Example*

.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');
    service.setLayerVisibility(['1','2','3'],true);


.. _setOpacityAnchor :

setOpacity (opacity)
^^^^^^^^^^^^^^^^^^^^

*Description*

Sets the transparency for a service. The value must be between 0.0 and 1.0:

0.0 ... fully transparent

1.0 ... not transparent

*Example*


.. code-block:: javascript

    var service=map.getService('estag_basis_ags@ccgis_default');
    service.setOpacity(0.5);



.. _setServiceVisibilityAnchor :

setServiceVisibility (layerids)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Description*

Sets all layers with a corresponding id visible and all remaining layers invisible. The parameter is an array with the layer ids. If an empty array or nothing is passed, all layers in a service are set invisible.

*Example*


.. code-block:: javascript

    // set only layers 1,2,3 visible
    service.setServiceVisibility(['1', '2', '3']);

    // set all layers in a service invisible
    service.setServiceVisibility();

    // set all layers visible
    service.setServiceVisibility(service.getLayerIds());




Property Details
----------------


.. _idPropertyAnchor :

id
^^

*Description*

The id of the service. This id can also be used to find a service via a ``map`` object with the ``getService(id)`` method.

*Example*

The following example shows the relationship between service id and map object.

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

*Description*

Indicates whether this service is a background service.

*Example*


.. code-block:: javascript

    if(service.isBasemap == true) {
        // Do something
    }


.. _layersPropertyAnchor :

layers
^^^^^^^^

*Description*

An array of the service's layers. The individual values in turn have properties such as ``id`` and ``name``.

*Example*

For finding layers, there are actually the methods ``getLayer()``, ``getLayerFromName()``, and ``getLayerIdsFromNames()``, which should be used. In exceptional cases, however, it can also be important to list the individual layers

.. code-block:: javascript

    for(var l = 0; l < service.layers.length; l++) {
        var layer = service.layers[l];

        console.log(layer.id+" "+layer.name)
    }


.. _mapPropertyAnchor :

map
^^^

*Description*

The map object in which the service is included.

*Example*


.. code-block:: javascript

    var serviceMap = service.map;
    map.zoomTo([10,40,20,50]);



.. _namePropertyAnchor :

name
^^^^

*Description*

The name of the service.


.. _opacityPropertyAnchor :

opacity
^^^^^^^

*Description*

Indicates the transparency of the service. The value can be between 0.0 (fully transparent) and 1.0 (not transparent).

The value should not be changed. To set the transparency, the :ref:`setOpacityAnchor` method should be used.

*Example*


.. code-block:: javascript

    var currentOpacity = service.opacity;
