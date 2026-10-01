Expressions
===========

With *expressions*, values can be calculated from the fields of a geo object or assembled into
texts, for example ``[AREA]m2`` or ``concat("Area: ", round([AREA], 2), " m2")``.

.. contents:: Contents of this page
   :local:
   :depth: 2

Where can expressions be used?
------------------------------

AutoValues
^^^^^^^^^^

For :doc:`AutoValues <../apps/cms/editing/fields_autovalues>`, a leading ``=`` marks an
expression. This is required to distinguish expressions from *named* AutoValues such as
``create_login``, ``shape_area`` or ``change_datetime_utc``.

.. code-block:: text

   create_login

is a named AutoValue.

.. code-block:: text

   =Object [NAME]

is a legacy template.

.. code-block:: text

   =concat([FIRSTNAME], " ", [LASTNAME])

is a structured expression.

The leading ``=`` belongs only to the AutoValue configuration. It is removed before the content is
classified as a legacy template or structured expression.

Table columns of type ``TableFieldExpression``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Table columns of type ``TableFieldExpression`` (see :doc:`../apps/cms/queries/index`) are always
expressions. A leading ``=`` is therefore **not** required. It has no special meaning here and is
not removed.

.. code-block:: text

   Object [NAME]

is a legacy template.

.. code-block:: text

   concat([FIRSTNAME], " ", [LASTNAME])

is a structured expression.

Structured expression or legacy expression?
-------------------------------------------

The selection is made **automatically**:

* Clearly structured syntax is evaluated with the new, typed expression parser
  (*structured expression*).
* Text templates and existing ``$...`` functions remain in the *legacy* path.

.. important::

   An expression that has been recognized as a structured expression does **not** silently fall
   back to legacy on a syntax or evaluation error. Instead, an error with its position is
   reported.

When is a structured expression recognized?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Function calls**

.. code-block:: text

   concat([FIRSTNAME], " ", [LASTNAME])
   round([AREA], 2)
   if([STATUS] == "A", "Active", "Inactive")
   coalesce([NAME], "Unknown")

An unknown function name is also classified as a structured expression:

.. code-block:: text

   unknown([VALUE])

This expression produces the error *Unknown function* and does not fall back to legacy.

**Field reference with operator**

.. code-block:: text

   [COUNT] + 1
   [AREA] / 10000
   [STATUS] == "A"
   [VALUE] >= 10 && [ACTIVE] == true

A single field without an operator, on the other hand, remains legacy:

.. code-block:: text

   [NAME]

**Literals**

.. code-block:: text

   42
   12.5
   -10
   "Text"
   true
   false
   null

**Parenthesized and unary expressions**

.. code-block:: text

   (1 + 2) * 3
   ![ACTIVE]

Overview
^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 55 45

   * - Configuration
     - Evaluation
   * - ``[NAME]``
     - Legacy
   * - ``Object [NAME]``
     - Legacy
   * - ``[FIRSTNAME] [LASTNAME]``
     - Legacy
   * - ``Object-ID [ID]``
     - Legacy
   * - ``$round2([AREA])``
     - Legacy
   * - ``Area: $round2([AREA]) m2``
     - Legacy
   * - ``Area: round([AREA], 2) m2``
     - Legacy; ``round`` is **not** executed
   * - ``[COUNT] + 1``
     - Structured
   * - ``[AREA] / 10000``
     - Structured
   * - ``[STATUS] == "A"``
     - Structured
   * - ``round([AREA], 2)``
     - Structured
   * - ``concat("Area: ", round([AREA], 2), " m2")``
     - Structured
   * - ``if([STATUS] == "A", "Active", "Inactive")``
     - Structured
   * - ``"Text"``
     - Structured
   * - ``42``
     - Structured
   * - ``(1 + 2) * 3``
     - Structured

Structured expressions
----------------------

Structured expressions are typed and support:

* Field references
* String, number, boolean and ``null`` literals
* Arithmetic operators
* Comparisons
* Logical operators
* Conditions
* String functions
* Null/empty-value functions
* Numeric functions
* Date functions
* For AutoValues additionally GIS/geometry functions

Field references
^^^^^^^^^^^^^^^^

Fields are written in square brackets:

.. code-block:: text

   [NAME]
   [AREA]
   [STATUS]

* A **missing** field yields ``null``.
* An **existing** field with empty content yields an **empty string**, not ``null``.

Literals
^^^^^^^^

**Strings** are written in double quotes:

.. code-block:: text

   "Text"
   "Active"
   "Area: "

Supported escape sequences:

.. list-table::
   :widths: 20 80

   * - ``\"``
     - Quotation mark
   * - ``\\``
     - Backslash
   * - ``\n``
     - Line feed
   * - ``\r``
     - Carriage return
   * - ``\t``
     - Tab

**Numbers** are written invariantly with a decimal point:

.. code-block:: text

   42
   12.5
   -10

**Boolean values:** ``true``, ``false``

**Null value:** ``null``

Operators
^^^^^^^^^

**Arithmetic:** ``+  -  *  /  %``

.. code-block:: text

   [COUNT] + 1
   [AREA] / 10000
   ([WIDTH] * [HEIGHT]) / 2

.. note::

   ``+`` is used for numeric addition only. Strings are joined with ``concat(...)``.
   ``"Text" + "Text"`` is therefore invalid.

**Comparisons:** ``==  !=  <  <=  >  >=``

.. code-block:: text

   [STATUS] == "A"
   [AREA] >= 1000
   [MISSING] == null

**Logical operators:** ``&&  ||  !``

.. code-block:: text

   [STATUS] == "A" && [AREA] > 1000
   [TYPE] == "A" || [TYPE] == "B"
   ![ACTIVE]

``&&`` and ``||`` are evaluated *lazily*. A right-hand branch that is not needed is not
calculated.

Conditions
^^^^^^^^^^

.. code-block:: text

   if(condition, trueValue, falseValue)

Example:

.. code-block:: text

   if([STATUS] == "A", "Active", "Inactive")

``if(...)`` is also evaluated *lazily*. Only the branch that is actually selected is calculated.

String functions
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Function
     - Description
   * - ``concat(...)``
     - Joins any number of values into one text
   * - ``upper(value)``
     - Upper case
   * - ``lower(value)``
     - Lower case
   * - ``trim(value)``
     - Removes whitespace at the start and end
   * - ``substring(value, start)``
     - Substring from position ``start`` (0-based, the first character has index ``0``)
   * - ``substring(value, start, length)``
     - Substring with the given length
   * - ``replace(value, oldValue, newValue)``
     - Replaces parts of the text
   * - ``length(value)``
     - Length of the text

``start`` and ``length`` must be non-negative integers. If ``start`` lies outside the string, or ``start + length``
extends beyond the end of the string, an expression error is raised.

.. code-block:: text

   substring("abcdef", 0, 3)  ->  "abc"
   substring("abcdef", 2, 3)  ->  "cde"
   substring("abcdef", 2)     ->  "cdef"

More examples:

.. code-block:: text

   concat([FIRSTNAME], " ", [LASTNAME])
   upper([NAME])
   lower([CODE])
   trim([DESCRIPTION])
   substring([CODE], 0, 3)
   replace([NAME], "-", " ")
   length([NAME])

Null and empty-value functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Function
     - Description
   * - ``coalesce(...)``
     - Returns the first value that is not ``null``. An empty string is **not** skipped.
   * - ``is_null(value)``
     - Checks for ``null`` only
   * - ``is_empty(value)``
     - ``true`` for ``null`` or an empty string
   * - ``null_if_empty(value)``
     - Converts an empty string to ``null``

Examples:

.. code-block:: text

   coalesce([DISPLAY_NAME], [NAME], "Unknown")
   is_null([MISSING])
   is_empty([DESCRIPTION])

Because ``coalesce`` does not skip empty strings, it is often combined with ``null_if_empty``:

.. code-block:: text

   coalesce(null_if_empty([DISPLAY_NAME]), [NAME], "Unknown")

Numeric functions
^^^^^^^^^^^^^^^^^

.. code-block:: text

   round(value)
   round(value, digits)
   abs(value)
   min(...)
   max(...)

Examples:

.. code-block:: text

   round([AREA], 2)
   round([AREA] / 10000, 2)
   abs([DIFFERENCE])
   min([VALUE1], [VALUE2], 0)
   max([VALUE1], [VALUE2], 100)

Date functions
^^^^^^^^^^^^^^

.. code-block:: text

   format_date(value, format)
   year(value)
   month(value)
   day(value)

Examples:

.. code-block:: text

   format_date([CREATED], "yyyy-MM-dd")
   year([CREATED])
   month([CREATED])
   day([CREATED])

Date values are interpreted as ISO 8601 first. As a compatibility fallback, the current culture is
used.

GIS/geometry functions (AutoValues only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These functions are available in the AutoValue context only:

.. code-block:: text

   shape_len()               shape_len(SRefId)
   shape_area()              shape_area(SRefId)
   shape_perimeter()         shape_perimeter(SRefId)
   shape_centroid_x()        shape_centroid_x(SRefId)
   shape_centroid_y()        shape_centroid_y(SRefId)

* Without an argument, calculations are performed in the coordinate system of the feature geometry.
* With an ``SRefId`` (EPSG code), a **transformed copy** of the geometry is used. The original
  feature geometry is not modified.

Examples:

.. code-block:: text

   =shape_area()
   =shape_area(31256)
   =round(shape_area(31256), 2)
   =shape_centroid_x(4326)
   =concat("Area: ", round(shape_area(31256), 2), " m2")

Text output in structured expressions
-------------------------------------

A structured expression must be a valid expression **as a whole**. Free text before or after a
function call does not automatically turn it into a structured expression.

This input

.. code-block:: text

   Area: round([AREA], 2) m2

is recognized as a **legacy template**. Only ``[AREA]`` is replaced; ``round(...)`` is not executed
as a new function. With ``AREA = 123.456`` the result is approximately:

.. code-block:: text

   Area: round(123.456, 2) m2

For a calculated text output, ``concat(...)`` must be used:

.. code-block:: text

   concat("Area: ", round([AREA], 2), " m2")

For AutoValues, additionally with the leading ``=``:

.. code-block:: text

   =concat("Area: ", round([AREA], 2), " m2")

The result is:

.. code-block:: text

   Area: 123.46 m2

More examples (expressions may be written over several lines):

.. code-block:: text

   concat("Name: ", upper([NAME]))

.. code-block:: text

   concat(
       "Status: ",
       if([STATUS] == "A", "Active", "Inactive")
   )

.. code-block:: text

   concat(
       "Area: ",
       round([AREA] / 10000, 2),
       " ha"
   )

Legacy expressions
------------------

Legacy expressions remain fully supported for compatibility. If the configured expression contains
a ``$...`` function, it is evaluated after the placeholders have been replaced.

.. important::

   ``$...`` expressions coming from **feature attribute values** are not executed. Only functions
   that are already part of the configured expression are evaluated. This prevents expression
   injection through attribute data (see :ref:`expressions-security`).

Simple text templates
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   [NAME]
   [FIRSTNAME] [LASTNAME]
   Object [NAME]
   Object-ID [ID]
   Name: [NAME], Area: [AREA]

Examples:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Expression
     - Result
   * - ``Object [NAME]``
     - ``Object Main Street``
   * - ``[FIRSTNAME] [LASTNAME]``
     - ``Ada Lovelace``

Placeholders and formatting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Syntax
     - Description
   * - ``[!FIELD]``
     - Required field: if the field value is empty, the **entire** legacy expression yields an
       empty string (e.g. ``[!NAME]``)
   * - ``[~FIELD]``
     - Retained for backward compatibility
   * - ``[FIELD:format]``
     - Formatted value, e.g. ``[AREA:0.00]``, ``[COUNT:0000]``
   * - ``[url-encode:FIELD]``
     - URL encoding (UTF-8)
   * - ``[url-encode-latin1:FIELD]``
     - URL encoding (Latin-1)

Example of URL encoding:

.. code-block:: text

   https://example.com/?name=[url-encode:NAME]

Spatial placeholders
^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   [BBOX]
   [spatial::bbox]
   [spatial::bbox::4326]

   [spatial::point]
   [spatial::point::4326]

   [spatial::latlng]
   [spatial::lnglat]
   [spatial::lat]
   [spatial::lng]

Legacy dollar functions
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   $eval(...)
   $sin(...)   $cos(...)   $tan(...)
   $asin(...)  $acos(...)  $atan(...)

   $round0(...) ... $round5(...)
   $n0(...)     ... $n5(...)
   $n0_de(...)  ... $n5_de(...)

   $pi()

Examples:

.. code-block:: text

   $eval(1+2*3)
   $round2([AREA])
   Area: $round2([AREA]) m2
   [NAME]: $n2_de([VALUE])

A description of the individual functions (including notes on nesting) can be found in the chapter
:doc:`../apps/cms/queries/index`.

Examples
--------

AutoValues
^^^^^^^^^^

.. code-block:: text

   create_login                                              (named AutoValue)

   =Object [NAME]                                            (legacy)
   =[FIRSTNAME] [LASTNAME]                                   (legacy)

   =concat([FIRSTNAME], " ", [LASTNAME])                     (structured)
   =round([AREA] / 10000, 2)                                 (structured)
   =if([STATUS] == "A", "Active", "Inactive")                (structured)
   =concat("Area: ", round(shape_area(31256), 2), " m2")     (structured)

TableFieldExpression
^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   Object [NAME]                                             (legacy)
   [FIRSTNAME] [LASTNAME]                                    (legacy)
   Area: $round2([AREA]) m2                                  (legacy)

   concat([FIRSTNAME], " ", [LASTNAME])                      (structured)
   round([AREA] / 10000, 2)                                  (structured)
   if([STATUS] == "A", "Active", "Inactive")                 (structured)
   concat("Area: ", round([AREA], 2), " m2")                 (structured)

Error behavior
--------------

Structured expressions report clear errors with a source position, among others for:

* invalid syntax
* unknown function
* wrong number of arguments
* wrong data type
* division by zero
* modulo by zero
* invalid SRefId
* invalid substring range

Examples of invalid structured expressions:

.. code-block:: text

   round(
   unknown([VALUE])
   "Text" + "Text"
   [VALUE] / 0

Structured expressions do not silently fall back to legacy on errors.

.. _expressions-security:

Security
--------

The configured structured expression is compiled once into a fixed syntax tree before rendering.
Feature attribute values are then inserted only as **typed values**. They are not tokenized or
parsed again.

An attribute value such as

.. code-block:: text

   round(12.345, 2) || unknown()

therefore remains plain text and cannot inject an additional function or operation.

In the legacy path, too, ``$...`` functions are executed only if they are already part of the
configured expression. Content such as ``$round`` or ``$eval`` originating from attribute values is
not executed.

Performance
-----------

For table columns of type ``TableFieldExpression``, the feature-independent preparation is carried
out only **once per table field**:

* Selection between structured and legacy
* Parsing and compiling the structured expression
* Determining the legacy placeholders
* Detecting configured legacy dollar functions

When the individual objects are rendered, the prepared syntax tree or the cached legacy parameters
are used. Parser selection and parsing are therefore not repeated for every single object.
