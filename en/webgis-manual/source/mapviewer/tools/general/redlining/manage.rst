Managing Drawings
=====================

This section covers further concepts of the drawing (redlining) tool:

* Saving drawings

* Loading drawings

* Sharing drawings

* Uploading drawings

* Downloading drawings

Saving a Drawing
-------------------

.. note::
   Loading and saving drawings is only intended for intranet applications, where the users
   are known via the login to the company network. For anonymous access via the internet, the alternative
   is the *Share Map* tool, the *Share* tool, or *download* and *upload* of drawings.

To be able to use a drawing again later, it can be saved with this tool.
In the dialog, a unique name must be assigned to the drawing. If you enter a name
that has already been used, the *old* drawing is automatically overwritten (without confirmation).

.. note::
   The drawing is stored on the servers of the map viewer operator. It is up to
   them to delete "old" drawings from time to time, since the redlining tool should actually only be used to create temporary
   drawings (see the description "good use cases for redlining").

.. note::
   If drawings need to be saved long-term, it is recommended to save them on your own
   hard drive using the *download* tool described below.

Nevertheless, the *Save Drawing* tool offers advantages over *download*:

* Access can be done from different devices. A project can be created on desktop and later reopened on a phone.

* Only visible to your own user.

Loading a Drawing
-----------------

Drawings that were saved on the map viewer operator's server with the *Save Drawing* tool
can be loaded again with this tool.

Sharing a Drawing
-----------------

Drawings are generally only visible to the user who created them. This tool
can be used to share a drawing with other users via a link.

.. note::
   The button is *only* a shortcut to the *Share Map* tool. A detailed
   description is given in the *Map Tools* section. When sharing, the link shares not only the drawing,
   but also all other settings of the map view (shown topic layers).

Downloading a Drawing
-----------------------

This can be used to permanently save a drawing to your own computer. Depending on the format, this file
can be uploaded again at a later time.

The following formats are available:

**Redlining Project (GeoJSON):**

The drawing is downloaded as a text file in GeoJSON format. GeoJSON is a standard for
geodata, and the geometry of the drawing can also be reused in other programs. The *properties*
of the individual elements also describe the presentation (colors...), though this is not standardized and
can only be interpreted again by the redlining tool when uploaded later.

This format is suitable for permanently saving drawings, since it also offers the option of uploading.
When uploading, all settings from the drawing (colors, descriptions, ...) are restored.

**GPX:**

GPX is a format that can be used to transfer *tracks* (routes) and *waypoints* to navigation devices.
Drawings should only be downloaded in this format if the target is a navigation device.
The files can be uploaded again later, but some data loss may occur:

.. note::
   When downloading in GPX format, only lines (become *tracks*) and text (become *waypoints*)
   are taken into account. All other geometry types are ignored!
   The presentation (colors, ...) also cannot be carried over into a GPX file.

**Esri Shapefile:**

*Esri shapefiles* are a standard format for processing geodata, since they can be loaded by virtually any GI software.
To be able to transfer created projects into any GI system, the
download is offered in this format.

.. note::
   For *Esri shapefiles*, there is later no way to upload them again. Do **not** use this format
   to back up drawings, only if they need to be transferred into additional GI systems.

The result of the **Esri Shapefile** download is a ZIP file containing the *shapefiles*.
A shapefile is created for each geometry type (symbol, text, line, ...). Each *shapefile* in turn consists
of at least 3 files. In addition to the attribute data, information about the presentation (color codes) and the description/text
of the individual element are carried over.

Uploading a Drawing
-------------------

*GPX* and *GeoJSON* (redlining projects that were previously downloaded) files can be uploaded.

.. note::
   The viewer determines the file type based on the file extension (\*.gpx, \*.json, ...).
   Make sure to use the correct file extension.

For *GPX* files, files that were not previously downloaded with the *drawing* tool can also be uploaded. Uploading also allows
*GPX* files created with a navigation device to be uploaded, in order to visualize them on the map. This
takes over *tracks* and *waypoints*.
