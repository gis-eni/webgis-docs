Editing (Editing Geo-Objects)
==================================

In addition to displaying geodata, data can also be created or edited. In the map viewer, there is
a dedicated tool for this (editing) with which both the geometry and the attribute data of geo-objects
can be edited.

This requires a (map) service that enables the editing of data.
Map services that meet this requirement are, for example, ArcGIS Server FeatureServer services.
These offer the corresponding methods via a REST interface. Certain
settings and permissions must be set on the ArcGIS Server for this, which are not described in this
documentation. It is assumed here that the selected service meets all the necessary requirements.

.. note::
   Editing of geodata is done exclusively via (feature) services and not directly in a database.
   Since various geodatabases often offer more than "flat" tables, i.e. often also more complex relationships
   and versioning, write access to these databases should always go through a service.
   The service is then responsible for ensuring that all relationships are handled correctly
   when writing data.

.. note::
   When ArcGIS Server services are mentioned here, what is actually meant are services that support the
   GeoServices REST interface introduced by ArcGIS Server. This (free) interface
   can theoretically also be supported by other map servers, such as gView Server https://github.com/jugstalt/gview5.

If you want to enable editing via an ArcGIS Server service through the CMS, it is assumed here
that the display service and the editing service (MapServer/FeatureServer) are identical.

This tutorial assumes a service intended for planning power line projects.
The ArcGIS Server service contains corresponding point, line, and polygon topics. The description of the available options
is shown using a few selected topics.

.. toctree::
    :maxdepth: 2
    :caption: Contents:

    create_edittheme
    theme_properties
    fields
    fields_validation
    fields_autovalues
    fields_domains
    fields_domain_behaviour
    snapping
