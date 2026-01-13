============================
Benutzerdefinierte Werkzeuge
============================

Benutzerdefinierte Werkzeuge sind Werkzeuge, die in der Werkzeugleiste des Viewers erscheinen, aber nicht zu den Standardwerkzeugen von WebGIS gehören. Diese Werkzeuge können beispielsweise einfache Buttons sein (z. B. für erweiterte Metadaten einer Karte) oder auf Interaktionen mit der Karte reagieren (Klick in die Karte oder Aufziehen eines Rechtecks). In allen Fällen wird nach einer Benutzeraktion (Klick auf den Button, Klick in die Karte oder Aufziehen eines Rechtecks) ein Link aufgerufen, an den entsprechende Werte übergeben werden können.

Werkzeuge mit Karteninteraktion
===============================

Benutzerdefinierte Werkzeuge werden in der ``custom.js`` mit folgendem Befehl dem Viewer hinzugefügt:

.. code-block:: javascript

    webgis.custom.tools.add({
        name: 'Super Tool',
        command: 'https://www.google.com/maps/@{y},{x},19z',
    });

Fügt man ein benutzerdefiniertes Werkzeug in die ``custom.js`` ein, wird es in allen Karten dieser Portalseite hinzugefügt. Soll das Werkzeug nur in bestimmten Karten erscheinen, kann dies über Bedingungen gesteuert werden. Beispielsweise steht in der Variablen ``mapUrlName`` der Name der aktuell aufgerufenen Karte:

.. code-block:: javascript

    if (mapUrlName === "Geoland") {
        webgis.custom.tools.add({
            name: 'Super Tool',
            command: 'https://www.google.com/maps/@{y},{x},19z'
        });
    }

.. tip:: Diese Methode kann auf alle hier beschriebenen Anwendungsfälle angewandt werden, z. B. für Marker oder Usability-Optimierungen.

Eigenschaften benutzerdefinierter Werkzeuge
===========================================

Der Übergabeparameter ist ein Objekt, das das Werkzeug beschreibt und mindestens die Eigenschaften ``name`` und ``command`` enthalten muss. Die folgende Tabelle beschreibt alle möglichen Eigenschaften:

.. list-table:: Eigenschaften benutzerdefinierter Werkzeuge
   :widths: 20 80
   :header-rows: 1

   * - **Eigenschaft**
     - **Beschreibung**
   * - ``name``
     - Name des Buttons.
   * - ``id`` (optional ab Build 5.22.2401)
     - Eine eindeutige ID für das Werkzeug, falls es über einen parametrierten Aufruf des Kartenviewers ausgewählt werden soll.
   * - ``command``
     - URL, die bei einer Benutzeraktion aufgerufen wird. Platzhalter können genutzt werden (siehe unten).
   * - ``command_target``
     - Steuert, wie der Link aufgerufen wird:

       - ``'self'``: Link öffnet sich im aktuellen Tab.
       - ``'dialog'``: Link wird in einem Dialog im Viewer geöffnet (kann bei Drittseiten wie Google Maps nicht funktionieren).
       - ``'_blank'`` (Standardwert): Link öffnet sich in einem neuen Tab.

   * - ``command_target: function(response) { }``
     - Führt den ``command`` als **fetch** aus und übergibt das Ergebnis an eine Callback-Funktion. ``response`` enthält folgende Eigenschaften:
       
       .. code-block:: javascript

          {
             result: result,  // Das Ergebnis der Abfrage (Objekt bei JSON oder ein Text)
             map: map,        // Das aktuelle Map-Objekt
             uiElement: uiElement  // Das UI-DOM-Element des Werkzeugs, in das beispielsweise Ergebnisse geschrieben werden können
          }

       Beispiel für ein Werkzeug mit Callback-Funktion:

       .. code-block:: javascript

          webgis.custom.tools.add({
              name: 'Fetch Tool',
              command: 'https://.../rest?x={x}&y={y}',
              tooltype: 'click',
              cursor: 'crosshair',
              image: 'cursor-plus-26-b.png',
              command_target: function(response) {
                  const map = response.map;
                  const result = response.result;
                      
                  // Remove the custom tool marker
                  map.removeMarkerGroup('custom-temp-marker');

                  // Add a custom tool marker
                  map.toMarkerGroup('custom-temp-marker', map.addMarker({
                      lat: result.lat, 
                      lng: result.lng,
                      text: '<div>'+result.text+'</div>',
                      openPopup: true,
                      buttons: [{
                          label: 'Marker entfernen',
                          onclick: function (map, marker) { map.removeMarker(marker); }
                      }]
                  }));

                  $('<pre>')
                      .text(JSON.stringify(response.result))
                      .appendTo($(response.uiElement));
              }
          });

   * - ``tooltype``
     - Art des Werkzeugs:

       - *keine Angabe* (Default): Werkzeug ist ein einfacher Button.
       - ``'click'``: Benutzer klickt in die Karte, um den ``command``-Link aufzurufen.
       - ``'box'``: Benutzer zieht ein Rechteck auf, um den ``command``-Link aufzurufen.

   * - ``container``
     - Bereich der Werkzeugleiste, in dem das Werkzeug angezeigt wird:

       - ``'Navigation'``
       - ``'Auswahl'``
       - ``'Werkzeuge'`` (Standard)
       - ``'Darstellung'``

   * - ``image``
     - Link zu einem 26x26px großen Icon für den Button. Kann ein absoluter Pfad oder ein Dateiname sein, falls das Icon in ``content/api/img/tools`` liegt.
   * - ``tooltip``
     - Text, der als Tooltip erscheint, wenn man mit der Maus über den Button fährt.
   * - ``description``
     - Beschreibung des Werkzeugs. Wird angezeigt, falls eine Benutzerinteraktion erforderlich ist.
   * - ``modify_event`` (optional ab Build 8.26.302)
     - hier kann optional eine Funktion angegeben werden, die vor dem Aufruf des ``command`` 
       ausgeführt wird. Diese Funktion erhält als Parameter das ``map`` und das ``event``-Objekt 
       und kann diese verändern (z. B. World Koordinaten verändern). Beispiel:

       .. code-block:: javascript

          modify_event: function(map, e) {
              // set the world coordinates to a different value (lng/lat multiplied by 100)
              // this coordinate will be used in the command URL placeholders {X} and {Y}
              e.world.X = e.world.lng*100;
              e.world.Y = e.world.lat*100;
              console.log('modified Event', e);
          }

       Die Methode kann beispielsweise dazu verwendet werden, um die Koordinaten in ein anderes Koordinatensystem 
       umzurechnen, bevor sie an die Ziel-URL übergeben werden.


Platzhalter für ``command``
===========================

Für die Eigenschaft ``command`` können verschiedene Platzhalter in die URL eingefügt werden, um Parameter aus der Karte an eine andere Web-Seite zu übergeben. Abhängig vom ``tooltype`` können unterschiedliche Platzhalter verwendet werden, die je nach Kontext eine spezifische Bedeutung haben.

.. list-table:: Platzhalter für ``command``
   :widths: 25 15 60
   :header-rows: 1

   * - **Platzhalter**
     - **ToolTypes**
     - **Beschreibung**
   * - ``{map.minx}, {map.miny}, {map.maxx}, {map.maxy}``
     - ``kein, click, box``
     - Die Ausdehnung des aktuellen Kartenausschnitts in geographischen Koordinaten. ``x`` entspricht hier dem Rechtswert (geographische Länge), ``y`` dem Hochwert (geographische Breite).
   * - ``{map.bbox}``
     - ``kein, click, box``
     - Die BoundingBox des aktuellen Kartenausschnitts in geographischen Koordinaten.  
       Entspricht: ``{map.minx}, {map.miny}, {map.maxx}, {map.maxy}``.
   * - ``{map.centerx}, {map.centery}``
     - ``kein, click, box``
     - Der Mittelpunkt des aktuellen Kartenausschnitts in geographischen Koordinaten.
   * - ``{map.scale}``
     - ``kein, click, box``
     - Der aktuelle Kartenmaßstab.
   * - ``{map.MINX}, {map.MINY}, {map.MAXX}, {map.MAXY}, {map.BBOX}, {map.CENTERX}, {map.CENTERY}``
     - ``kein, click, box``
     - Wie oben, jedoch werden hier keine geographischen Koordinaten übergeben, sondern Koordinaten im Karten-Koordinatensystem (z. B. GK-M34). ``x`` entspricht dem Rechtswert, ``y`` dem Hochwert.
   * - ``{x}, {y}``
     - ``click, box``
     - Der Punkt, auf den der Anwender geklickt hat, in geographischen Koordinaten. Falls der Anwender ein Fenster aufzieht, entspricht dieser Wert dem Mittelpunkt des Fensters.
   * - ``{X}, {Y}``
     - ``click, box``
     - Wie oben, jedoch im Karten-Koordinatensystem.
   * - ``{minx}, {miny}, {maxx}, {maxy}``
     - ``box``
     - Die Ausdehnung des aufgezogenen Rechtecks in geographischen Koordinaten.
   * - ``{bbox}``
     - ``box``
     - Die BoundingBox des aufgezogenen Rechtecks.  
       Entspricht: ``{minx}, {miny}, {maxx}, {maxy}``.
   * - ``{MINX}, {MINY}, {MAXX}, {MAXY}, {BBOX}``
     - ``box``
     - Wie oben, jedoch für das Karten-Koordinatensystem.
   * - ``{wkt}, {wkt_digits_1}, {wkt_digits_2}, {wkt_digits_3}, {wkt-4326}``
     - ``sketch0d (=point), sketch1d (=line), sketch2d (=polygon)``
     - Ermöglicht das Übergeben einer Sketch-Geometrie als Well-Known-Text (``POINT(...)``, ``LINESTRING(...)``, ``POLYGON(...)``). Die Geometrie kann entweder in WGS84 oder in der aktuellen Sketch-Projektion übergeben werden.  
       
       - ``{wkt}``: Übergibt die Geometrie mit voller Genauigkeit.  
       - ``{wkt_digits_1}``, ``{wkt_digits_2}``, ``{wkt_digits_3}``: Rundet die Koordinaten auf die angegebene Dezimalstellenzahl.

   * - ``{calc-srs}, {sketch-srs}``
     - ``sketch0d, sketch1d, sketch2d``
     - Gibt das Koordinatensystem an, in dem der Sketch, der über ``{wkt}`` übergeben wird, vorliegt. Beide Platzhalter liefern in der Regel dieselben Werte.

Benutzerdefinierte Werkzeuge mit Eingabefeldern
===============================================

Falls bereits im Viewer Parameter ausgewählt werden sollen, die an die Zielseite übergeben werden, kann dies über die ``uiElements``-Eigenschaft erfolgen. Dadurch können vor der eigentlichen Ausführung des Werkzeugs Eingabefelder zur Verfügung gestellt werden, um benutzerdefinierte Werte an die URL zu übergeben.

**Beispiel:**  
Ein Werkzeug für Höhenprofile, bei dem der Benutzer vor der Ausführung Parameter wie Überhöhung und Stützpunktabstand eingeben kann.

.. code-block:: javascript

   webgis.custom.tools.add({
        name: 'Höhenprofil',
        command: 'https://server.com/profile?ueberhoehung={ueberhoehung}&hintergrund=bmapgrau&stuetzpunktabstand={stuetzpunktabstand}&title={profile_title}&polygonzug={wkt}&crs=31256',
        command_target: 'dialog',
        tooltype: 'sketch1d',
        image: 'profil.png',
        uiElements: [
            { type: 'label', label: 'Titel' },
            { id: 'profile_title', type: 'input-text' },
            { type:'label', label:'Überhöhung' },
            { id: 'ueberhoehung', type: 'select', options: [
                { label: '1:1', value: 1 },
                { label: '2:1', value: 2 },
                { label: '3:1', value: 3 }
            ]},
            { type: 'label', label: 'Punktabstand [m]' },
            { id: 'stuetzpunktabstand', type: 'select', options: [
                { label: '1 m', value: 1 },
                { label: '2 m', value: 2 },
                { label: '3 m', value: 3 }
            ]}
        ]
    });

.. note:: In diesem Beispiel kann der Benutzer vor der Ausführung des Werkzeugs verschiedene Parameter anpassen. Die ``id`` der Eingabefelder kann als Platzhalter in der ``command``-URL verwendet werden.

Typen von Eingabefeldern
------------------------

Für die ``uiElements``-Eigenschaft gibt es verschiedene Eingabefeldtypen:

.. list-table:: Verfügbare Eingabefeldtypen
   :widths: 20 80
   :header-rows: 1

   * - **Typ**
     - **Beschreibung**
   * - ``input-text``
     - Einfaches einzeiliges Textfeld.
   * - ``input-textarea``
     - Mehrzeiliges Textfeld für längere Eingaben.
   * - ``input-number``
     - Eingabefeld für numerische Werte.
   * - ``input-date``
     - Datumsfeld mit Uhrzeit.
   * - ``select``
     - Dropdown-Liste zur Auswahl eines vordefinierten Wertes. Die verfügbaren Optionen müssen als Array definiert werden (siehe Beispiel oben).

Der Werkzeugdialog für das obige Beispiel würde wie folgt aussehen:

.. image:: img/custom1.png
