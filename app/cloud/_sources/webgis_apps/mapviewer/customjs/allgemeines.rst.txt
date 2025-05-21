Allgemeines
===========

Wenn man Karten über Portalseiten aus dem WebGIS 5 Portal publiziert, kann man natürlich nicht in den Sourcecode der einzelnen Karten eingreifen. 
Aus diesem Grund wurde die Datei custom.js eingeführt. Diese Datei sollte sich im Verzeichnis portal5/scripts/portals/{url-id-des-portals} befinden. 
Bei der Installation befindet sich eine solche Datei im portal5/scripts/portals/eni Verzeichnis. Auf deren Inhalt soll hier eingegangen werden. 

Grundsätzlich kann für jede Portalseite eine custom.js Datei angelegt werden. 
Der Viewer versucht bei jedem Laden einer Karte diese Datei zu laden. Wenn es diese Datei nicht gibt, zeigt der Link ins Leere und hat keine Auswirkung.
Es kann allerdings sein, dass solche Zugriffe in den Server-Logdateien auftauchen. Es ist also ratsam, wenigstens eine leere Datei mit diesem Namen ins entsprechende Verzeichnis zu legen.

Da diese Datei bei jedem Viewer-Aufruf eingebunden wird, eignet sie sich perfekt dazu, vorgegebene Werte aus der API zu überschreiben, wie beispielsweise die Marker.

**Tipp:** Alle hier gezeigten Methoden gelten  immer für alle Karten einer Portalseite. Soll eine Methode (beispielsweise ein benutzerdefiniertes Werkzeug) nur in einer bestimmten Karte oder bestimmten Karten auftauchen, 
kann dies über entsprechende Bedingungen gelöst werden. So steht beispielsweise in der Variable ``mapUrlName`` der Name der aktuell aufgerufenen Karte:


.. code-block :: JavaScript

    if (mapUrlName === "Geoland") {
        webgis.custom.tools.add({
            name: 'Super Tool',
            command: 'https://www.google.com/maps/@{y},{x},19z'
        });
    }




