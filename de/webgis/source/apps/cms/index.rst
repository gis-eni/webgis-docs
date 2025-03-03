WebGIS CMS  
==========

Über das WebGIS CMS können Administratoren definieren, welche Dienste über die WebGIS API angeboten werden. Außerdem kann hier festgelegt werden, welche Themen aus den Diensten abgefragt werden können, wie das Abfrageergebnis dargestellt wird, welche Themen bearbeitet werden dürfen, etc. Die Parametrierung wird am Server in einer Baumstruktur im Filesystem abgelegt (entspricht in etwa der Baumstruktur in der CMS-Oberfläche). Um die Änderungen im WebGIS CMS der WebGIS API mitzuteilen, wird im CMS ein Deploy ausgeführt, der aus einem CMS-Baum eine XML-Datei baut.

.. toctree::
    :maxdepth: 3
    :caption: Inhaltsverzeichnis:

    ui
    add_wmts_service
    add_ags_service
    queries/index
    layers
    presentations
    editing/index
    secrets/index.rst
    security/index
    deploy
