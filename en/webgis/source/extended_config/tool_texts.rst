======================
Customizing Tool Texts
======================

All tool texts (labels, descriptions, hints, error messages, input tips, ...)
are multilingual and stored in language files (Markdown). The installation package contains
a directory per language (``l10n/de``, ``l10n/en``, ...) and in it **one file per tool**,
e.g. ``Tools.Coordinates.md``.

These files in the installation package should **not be modified**, because they are overwritten
again on an update. Customized texts are stored in the ``etc`` directory instead.

Procedure
=========

1. Create the folder ``api/l10n`` in the ``etc`` directory.
2. Create a subfolder for each affected language in it (``de``, ``en``, ...).
3. Copy the tool's file from the installation package there,
   e.g. ``etc/api/l10n/de/Tools.Coordinates.md``.
4. In the copied file, **keep only the entries that are actually to be changed**.
   Delete all other entries.
5. Restart the application pool (ApplicationPool).

.. code:: text

  etc/
  └── api/
      └── l10n/
          ├── de/
          │   └── Tools.Coordinates.md
          └── en/
              └── Tools.Coordinates.md

.. important::

  The texts are read **only when the application starts**. After making changes, the
  **ApplicationPool must therefore be restarted**.

How the application loads the texts
-----------------------------------

1. First, all Markdown files from the installation package are read.
2. Then the files in ``etc/api/l10n`` are searched. The values they contain
   **overwrite** the values already read.

Entries that do not appear in the customized file therefore keep the default value from the installation package.
This way, new or changed default texts are picked up on an update without losing your own customizations.

File structure
==============

The files are written in **Markdown**. The **headings** define the id of a text,
followed by a colon. The translation follows after it. For longer texts, the text is not on
the heading line but below it as **body**.

.. code:: text

  # name: Coordinates / Elevation

  Query coordinates and elevation values

  # container: Queries

  # enter-coordinates: Enter coordinates

  # upload:
  ## label1:

  Coordinates can be uploaded here. ...

  ## exception-too-many-points: A maximum of {0} coordinate rows may be uploaded

.. important::

  Whether a text is placed **directly on the heading line** or **in the body** cannot be chosen freely;
  it is dictated by the application. As a rule, simple translations (labels) are on the line,
  longer descriptions in the body. It is best to keep the form used in the installation package.

Hierarchy
---------

The **heading hierarchy** (``#``, ``##``, ``###``, ...) must be preserved. It forms the
id path used by the application to access the text. This also applies if the customized file contains
only a single entry: the parent headings must be included.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Id
     - Position in the file
   * - ``upload.label1``
     - Body text under ``# upload:`` / ``## label1:``
   * - ``upload.sketch.label1``
     - Text after ``# upload:`` / ``## sketch:`` / ``### label1:``

Ids must therefore not be renamed and levels must not be moved; only the texts themselves may be changed.

Placeholders such as ``{0}`` must be kept. The application replaces them with values.

Tools have the entries ``# name:`` (display name of the tool) and ``# container:``
(display name of the container in which the tool is listed).

Example: coordinate tool
========================

File ``etc/api/l10n/en/Tools.Coordinates.md``. A paragraph (body) under
``upload`` / ``label1``, a simple label (``tip-label``) and the input tip (``tip``) are changed.
All other texts remain unchanged and are therefore not in the file:

.. code:: text

  # upload:

  ## label1:

  Coordinates can be uploaded. The coordinates must be provided as CSV files
  with a semicolon as separator. The columns of the CSV file should correspond to
  point name/number, easting and northing. The first row is interpreted as the table header.

  # tip-label: Input hint

  # tip:

  md:There are projected coordinates (GK-M34, Web Mercator, ...) and geographic coordinates (WGS 84, GPS).
  When entering coordinates, the coordinate system should therefore always be selected first.

  **GK-M34**
  Easting: -67772.43
  Northing: 215837.13

The prefix ``md:`` at the beginning of the text marks the content as Markdown.
The input tip used to be configured via the file ``tip.txt`` in the ``etc`` directory.
This file is no longer used.
