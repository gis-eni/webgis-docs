======================
App-Menü-Einträge
======================

Über die ``custom.js`` lässt sich zusätzlich zu benutzerdefinierten Werkzeugen (siehe :doc:`customtools`) auch das **App-Menü** (Burger-Menü, oben rechts im Viewer) um eigene Einträge erweitern. Dies eignet sich beispielsweise für Links zu einem Login/Logout via SAML, zu einer externen Anwendung oder zu weiterführenden Informationen.

.. code-block:: javascript

    webgis.custom.appMenuItems.add({
        name: 'Login',
        command: 'https://login.example.com/samllogin?target=/webgis/map/demo/basemap',
        tooltip: 'Anmelden',
        command_target: 'self',
        image: 'https://cdn.example.com/icons/box-arrow-in-right.svg'
    });

    webgis.custom.appMenuItems.add({
        name: 'Logout',
        command: 'https://login.example.com/profile/SAML2/POST/SLO',
        tooltip: 'Abmelden',
        command_target: 'self',
        image: 'https://cdn.example.com/icons/box-arrow-right.svg'
    });

Wie bei benutzerdefinierten Werkzeugen gilt: Wird ``webgis.custom.appMenuItems.add(...)`` in der ``custom.js`` aufgerufen, erscheint der Eintrag in allen Karten dieser Portalseite. Soll der Eintrag nur in bestimmten Karten angezeigt werden, kann dies wie gewohnt über die Variable ``mapUrlName`` eingeschränkt werden (siehe :doc:`allgemeines`).

Eigenschaften eines App-Menü-Eintrags
======================================

Der Übergabeparameter ist ein Objekt, das mindestens die Eigenschaften ``name`` und ``command`` enthalten muss.

.. list-table:: Eigenschaften eines App-Menü-Eintrags
   :widths: 20 80
   :header-rows: 1

   * - **Eigenschaft**
     - **Beschreibung**
   * - ``name``
     - Beschriftung des Menüeintrags.
   * - ``command``
     - URL, die beim Klick auf den Menüeintrag aufgerufen wird.
   * - ``tooltip``
     - Text, der als Tooltip erscheint, wenn man mit der Maus über den Menüeintrag fährt.
   * - ``command_target``
     - Steuert, wie der Link aufgerufen wird:

       - ``'self'``: Link öffnet sich im aktuellen Tab.
       - ``'_blank'``: Link öffnet sich in einem neuen Tab.
       - ``'dialog'``: Link wird in einem Dialog im Viewer geöffnet (kann bei Drittseiten nicht funktionieren).

   * - ``image``
     - Icon für den Menüeintrag. Kann eine absolute URL (z. B. zu einem SVG-Icon) oder ein Dateiname sein, falls das Icon in ``content/api/img/tools`` liegt.

.. tip::

    Ein typischer Anwendungsfall ist die Anmeldung/Abmeldung über SAML, wie im obigen Beispiel gezeigt: Der Eintrag **Login** ruft den SAML-Login-Endpunkt auf und leitet nach erfolgreicher Anmeldung wieder auf die Karte zurück (``target``-Parameter). Der Eintrag **Logout** ruft den Single-Logout-Endpunkt (SLO) auf.
