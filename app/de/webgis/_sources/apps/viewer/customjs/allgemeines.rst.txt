===========
Allgemeines
===========

Beim Publizieren von Karten über Portalseiten im WebGIS Portal besteht kein direkter Zugriff auf den Sourcecode der einzelnen Karten. Um dennoch Anpassungen vorzunehmen, kann eine **custom.js**-Datei verwendet werden. Diese Datei sollte sich im Verzeichnis ``portal5/scripts/portals/{url-id-des-portals}`` befinden. Bei der Installation existiert eine solche Datei bereits unter ``portal5/scripts/portals/eni``.

.. note::

   Der Viewer lädt diese Datei automatisch bei jedem Start einer Karte. Falls sie nicht existiert, hat dies keine Auswirkungen, kann jedoch zu Log-Einträgen auf dem Server führen. Es ist daher ratsam, zumindest eine leere Datei mit diesem Namen zu hinterlegen.

Da die Datei bei jedem Viewer-Aufruf eingebunden wird, eignet sie sich zur **Überschreibung von API-Werten**, z. B. für Marker oder benutzerdefinierte Werkzeuge.

.. tip::

    Die hier gezeigten Methoden gelten für **alle Karten einer Portalseite**. Falls eine Methode nur für **bestimmte Karten** aktiv sein soll, kann dies über eine **Bedingung** gesteuert werden.

    Die Variable ``mapUrlName`` enthält den Namen der aktuell geladenen Karte und kann zur Einschränkung auf bestimmte Karten verwendet werden.

    **Beispiel:** 

    Ein benutzerdefiniertes **Werkzeug** nur für die Karte **"Geoland"** hinzufügen:

    .. code-block:: JavaScript

        if (mapUrlName === "Geoland") {
            webgis.custom.tools.add({
                name: 'Super Tool',
                command: 'https://www.google.com/maps/@{y},{x},19z'
            });
        }
