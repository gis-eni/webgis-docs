===================================
Tool ``XY (Coordinates/Elevation)``
===================================

.. note::

  In earlier **WebGIS 4.0** installations, the **API app directory** contained the
  folder ``system/proj``, in which projections were defined. This configuration has
  now been moved to the directory ``etc/coordinates/proj``.

h.xml
=====

In addition to this ``proj`` folder, a file ``h.xml`` can now optionally be created
in the directory ``etc/coordinates``. This file specifies which **elevation values**
are determined in addition to the coordinates.

The structure of ``h.xml`` corresponds to the configuration file of the elevation query tool
(``etc/heightabovedatum``).

default.xml
============

In the file ``proj/xy/default.xml``, you can define which coordinate systems can be queried with the
XYZ tool. Both **coordinates** and **elevation values** can be returned,
if the corresponding settings have been made in ``h.xml``.

.. code:: XML

  <?xml version="1.0" encoding="utf-8" ?>
  <projections>

    <projection id="31254" displayname="GK M28" minx="-200000" maxx="200000"/>
    <projection id="31255" displayname="GK M31" minx="-200000" maxx="200000"/>
    <projection id="31256" displayname="GK M34" minx="-200000" maxx="200000"/>
    <projection id="31287" displayname="Lambert (neu)" />

    <projection id="31257" displayname="BMN M28" maxx="300000"/>
    <projection id="31258" displayname="BMN M31" minx="300000" maxx="600000"/>
    <projection id="31259" displayname="BMN M34" minx="600000"/>
    <projection id="4326" displayname="WGS84" digits="6" />
    <projection id="4326" displayname="WGS84(GM)" displaystyle="dm" digits="2"/>
    <projection id="4326" displayname="WGS84(GMS)" displaystyle="dms" digits="1"/>
    <projection id="32632" displayname="UTM 32N" minx="-150000" maxx="850000" />
    <projection id="32633" displayname="UTM 33N" minx="-150000" maxx="850000" />

    <projection id="3857" displayname="web"  />

    <projection id="4326" displayname="UTMRef" displaystyle="mrgs" digits="5"/>

  </projections>

* **id**: EPSG code of the coordinate system
* **displayname**: display name in the XYZ tool
* **minx/maxx**: optionally, the minimum and maximum X coordinates can be specified here,
   to restrict the display of the projection in the XYZ tool.
* **digits**: number of decimal places to be shown in the XYZ tool
* **displaystyle**: optionally, the display format of the coordinates in the XYZ tool
   can be specified here. Possible values are:
   * **dm**: degrees and decimal minutes (e.g. 47°04.69')
   * **dms**: degrees, minutes, and seconds (e.g. 47°04'41.4'')
   * **<geo-code-name>**: name of a GeoCoder (https://docs.webgiscloud.com/de/webgis/annex/geocodes.html)

.. note::

   **GeoCodes** can also be queried with the XYZ tool (see appendix).
   These generally relate to **geographic coordinates (EPSG:4326)**;
   which GeoCoder is used can be specified via the display style.

   Geographic coordinates (EPSG:4326) can also be shown with a custom
   display style, e.g. as degrees and decimal minutes (47°04.69') ``dm`` or
   degrees, minutes, and seconds (47°04'41.4'') ``dms``.

tip.txt
=======

In the user interface of the XYZ tool, **input tips** are shown,
indicating how coordinates can be entered. The content of this tooltip can be
adjusted in the file ``tip.txt``.

.. note::

  The files ``default.xml`` and ``tip.txt`` do not necessarily have to exist.
  If they do not exist, WebGIS falls back to the default configuration,
  which is located in the files ``default_.xml`` and ``tip_.txt``.
