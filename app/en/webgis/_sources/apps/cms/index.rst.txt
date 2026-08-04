WebGIS CMS
==========

With the WebGIS CMS, administrators can define which services are offered via the WebGIS API. It also allows you to specify which topics can be queried from the services, how the query result is displayed, which topics may be edited, etc. The parameterization is stored on the server in a tree structure in the file system (roughly corresponding to the tree structure in the CMS interface). To communicate the changes made in the WebGIS CMS to the WebGIS API, a deploy is run in the CMS that builds an XML file from a CMS tree.

.. toctree::
    :maxdepth: 3
    :caption: Contents:

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
