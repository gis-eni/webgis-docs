.. _mapmarkup:

Drawing (Map Markup & Annotations)
===================================

Drawing (map markup) is a very powerful map tool and can be used for various applications.
The basic idea of map markup is to extend the map with drawing elements (lines, polygons, text, symbols)
and to mark locations for a printout, to send, or otherwise make available.

Map markup should only be used to create short-lived drawings that also don't contain too many objects.
The drawings can be saved, but do not need to be kept forever on the server by the map viewer operator.

There is also the option to download the map markup and save it yourself. However, it should also
be noted that future versions of the software are not necessarily 100% compatible with old
project data, and certain properties may be lost.

If you are using the tool for the first time, you should perhaps consider the points listed below.

.. toctree::
   :maxdepth: 3

   manual.rst
   advanced-tools.rst
   manage.rst
   selection.rst

Examples of Good Use Cases
++++++++++++++++++++++++++++++++++

* Marking a location and printing or sharing the map

* Drawing short directions (also for printing or sharing)

* Drawing (hiking) trails and downloading the tracks in GPX format for a navigation device

* Uploading existing GPX files to print or share the tracks and waypoints

* Small, locally limited projects. Here, however, the drawings should be downloaded and saved after completion, to avoid data loss.

* Small, locally limited projects based on the map data, and downloading the drawn geo-objects in Esri Shape format for further processing in various software packages.


Examples of Bad Use Cases
+++++++++++++++++++++++++++++++++++++++

* Larger and locally extensive projects, and storing these projects on the map viewer operator's server

* Managing pipeline/sewer networks for an entire municipality/municipal association

* Managing/creating zoning plans

.. note::
   For the use cases listed here as bad examples, the editing tool is better suited!


Alternatives
++++++++++++

If you want to implement a project listed here with the map viewer, please contact the
operator of the map viewer, or the operator of http://webgiscoud.com.

The better approach here is to work with the editing tools. This stores the drawn geo-objects in a
geodatabase, which provides the following advantages:

* Data remains permanently stored

* Data can be more easily transferred from one geodatabase to another. So you can start small at first, using the map viewer as an edit client, and switch to your own GI system if needed.

* Maintaining attribute data: in addition to the geometry, any attribute data can also be linked to the geometry (zoning type, year of construction, material, ...)

* More options for the cartographic presentation of the data

* Better performance with large amounts of data (virtually no size limit for projects)

* Multi-user operation: several users can edit geodata at the same time (depending on permissions)
