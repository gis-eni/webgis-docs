Using the Drawing (Map Markup) Tool
========================================

General Usage
--------------------

The drawing (map markup) tool is actually a collection of (sub-)tools that make it possible
to graphically augment the content of the map.
After opening the tool, the drawing (map markup) dialog is shown.
It offers all possible drawing tools.
In addition, there are buttons for managing drawings (load, save, share, upload, download).

.. image:: img/mapmarkup1.png
   :width: 320px

The buttons may vary depending on the end device. The figure shows all tools (desktop).
Below the buttons, the name of the currently active drawing tool is shown again, along with a *yellow*-highlighted
description of how to use this tool (e.g. click on the map, click on an existing drawing element, etc.).

Because of this description, the exact click sequence for the individual drawing tools is not covered here in detail;
instead, the options and differences between the tools are shown.

.. _mapmarkup-tool-groups:

Tool Groups
^^^^^^^^^^^

To save space, the tools are combined into groups:

* **Select:** shown directly

* **Draw:** Symbol, Text, Point, Freehand, Line, Polygon, Rectangle, Circle

* **Measure:** Dimensioning, Dimensioning Polygon, Hectometer Line, Field of View (Angle), Intersection Angle,
  Circular Arc, Perpendicular distance, Buffer zone, Object distance, Measurement grid, Distance Circle, Compass Rose
  (see :doc:`Special Tools <advanced-tools>`)

* **Import/Export:** Save/Load Drawing, Share, Upload, Download

Clicking a group (indicated by the small arrow at the top right) opens a selection with the tools of this group.
It closes again after a tool is selected (also when clicking outside of it or pressing ``Esc``).
The group then shows the icon of the last selected tool and is highlighted as long as one of its tools is active.
Tools that are not available on a device are not shown in the groups either.

Drawing a New Element
----------------------

If you create a new element (for example, a line), you must define at least two vertices by clicking on the map.
Once the line is recognized as valid (at least two vertices), it can be *applied* to the map.
Until it is *applied*, the draft sketch with the vertices is still shown. As long as the draft sketch is shown,
the line can still be changed:

* Draw further vertices

* Move vertices with the mouse

* Undo steps via the draft context menu (right mouse button)

* Change the presentation via the presentation options

That a drawn element is *valid* and can be applied to the map can be seen in the tool dialog.
As soon as, for example, two vertices have been set for a line, the following button appears in the tool
dialog:

.. image:: img/mapmarkup3.png

The drawing element is applied to the map with the button showing a checkmark icon. After applying, another line can be drawn right away.
Before applying a drawing element to the map, a description can optionally be specified.
For example, if the line describes a route, you could enter ``Directions to ...`` here.
Descriptions for drawing elements are optional, but help to identify and interpret the element later.

**Tip:** there are further ways to apply a drawing element to the map and draw another one:

* Finishing a draft with a double-click. Afterwards, you can immediately continue drawing an element of the same type.

* Changing the drawing tool: if you draw a line and then want to continue, for example, by drawing a polygon, it is enough to click on the *polygon* tool. A valid line is then automatically applied.

* Labeling a drawing element: in the *Apply* dialog shown above, a *T* (for text) is shown to the right of the input field. This switches to the text tool and allows the current element to be labeled (e.g. length of a line - see below)

Drawing elements already applied are shown not only on the map, but also as a list in the tool dialog
(see :ref:`Element List <mapmarkup-graphics-list>`).


Changing Symbology
^^^^^^^^^^^^^^^^^^

To change the symbology of the respective object, there is an icon to the left of the description (this icon differs depending on the object).

.. image:: img/mapmarkup3_1.png

Clicking it takes you to the menu for making changes to the symbology.
If you select the line tool, for example, the following presentation options are available:

.. image:: img/mapmarkup2.png

Normally, the option menus for color, line thickness, and line style are already expanded. To change the color of a line, for example, you just need to select it.
The same applies to line thickness and line style (solid, dashed, ...).

These options always relate to the currently active element. If you change a presentation option, the presentation on the map
changes immediately.

.. note::
   If you are drawing a new object, you will only notice the changes once you click on the map to create vertices
   for the element.

.. _mapmarkup-symbology-panel:

Symbology Panel (Desktop)
^^^^^^^^^^^^^^^^^^^^^^^^^

On desktop devices, the symbology is shown in a separate panel to the right of the map. The panel
is not modal: the toolbar and the element list stay visible and drawing can continue.

* When a drawing or measuring tool is selected, the panel opens automatically. This allows the symbology
  to be set before drawing; it then applies to all further elements of this type.
* Hints for the current tool (e.g. what to do next) are also shown in this panel.
* If the panel is closed (X), it stays closed until the drawing tool is opened again.
  It can be reopened at any time with the *Symbology: {tool}* button in the tool dialog.
* If one or more elements are selected in the element list (several with the ``SHIFT`` key pressed),
  the panel shows the symbology for the selection (*Symbology: Selection*). Selected elements are also highlighted
  on the map. Selecting another drawing tool clears the selection.

In the element list, lines and polygons are shown with a colored border in the color of the element,
symbols with their actual symbol. Changes to the symbology are applied to the list immediately.

Whether the panel opens automatically can be configured by the administrator in ``custom.js``.

.. _mapmarkup-graphics-list:

Element List
------------

All applied drawing elements are shown as a list in the tool dialog below the tool buttons:

.. image:: img/mapmarkup4.png
   :width: 320px

Each entry shows:

* on the left a colored border in the color of the element and an icon for the type (line, polygon, text, dimensioning, ...)
* the description of the element or, if none was entered, the type with a running number (e.g. *Line 1*)
* depending on the type, a *T button* (label, see below), a *magnifier* (zoom to the element),
  a *delete button* (trash can) and an *edit button* (pencil)

Hovering over an entry highlights the element on the map. For composite measuring elements, a meaningful
geometry is shown (e.g. only the reference line for a perpendicular distance).

The order of the list can be reversed with the arrow button above the list.

Selecting Elements
^^^^^^^^^^^^^^^^^^

Clicking an entry selects the element, clicking it again clears the selection.

* With the ``CTRL`` key pressed, individual elements are added to or removed from the selection.
* With the ``SHIFT`` key pressed, all elements between the clicked element and the next already
  selected element are selected.

Selected elements are highlighted on the map. The following functions for the selection are available above the list:
change the symbology of all selected elements (*Symbology: Selection*, see above), clear the selection,
delete the selected elements and *Move to group…* (see below).

Groups
^^^^^^

Drawing elements can be organized in groups, e.g. to keep survey results apart from annotations.
Each element belongs to exactly one group; without further groups, all elements are in the group *General*.

* **Add a group:** Use the plus button next to the drop-down list to create a new group and enter a name.
  The new group immediately becomes the active group.
* **Active group:** Newly drawn elements (including elements taken from a selection) are added
  to the active group. When *All groups* is shown, the text below the drop-down list indicates which group new elements
  are drawn into (e.g. *New objects → Survey*).
* **Show groups:** The drop-down list restricts the list to one group (*All groups* shows all elements,
  structured by group). If a single group is selected, it can be renamed or deleted with the buttons next to the
  drop-down list. If a group to be deleted contains elements, you can choose whether they are moved
  to the group *General* or deleted as well. The group *General* cannot be deleted.
* **Move elements:** Select elements in the list and choose the target group via the drop-down list *Move to group…*.
* **Show/hide:** The checkbox at the group heading (or next to the drop-down list) shows or hides a group
  on the map. Hidden groups are marked *hidden* in the drop-down list and are **not printed**.
  Drawing into a hidden group shows it again automatically.

The groups (including their visibility) are stored when a drawing is saved and restored when it is loaded.

Filtering the List
^^^^^^^^^^^^^^^^^^

If the list contains many elements, a filter field (*Filter…*) is shown above it. Only entries whose
description or type contains the entered text are then shown. *Select matches* selects all
filtered elements (e.g. to change their symbology together or to move them to a group),
*Clear filter* removes the filter again.

The number of elements from which the filter field is shown can be configured by the administrator in ``custom.js``.

Different Behavior of Element Types
--------------------------------------------

The behavior described above is not the same for all element types. Here are a few differences/special cases:

**Symbol:** symbols only require one vertex. After placing the point, it is not necessary to click the
*Apply / Draw another* button; instead, it is enough to click on the map again
to draw another symbol. This allows several symbols to be drawn quickly by simply clicking
on the map (one symbol is placed on the map per click).

**Freehand:** with this tool, a "freehand" line can be drawn while holding down the mouse button. When the
mouse button is released, it is immediately applied to the map. This allows several
freehand lines to be drawn very quickly and conveniently.

**Text:** to place text on the map, after selecting the text tool, click on the map
to set the position of the text. This makes the text position *valid*, and the actual
text can be changed via the text field and via *Apply / Draw another*. A change should be visible on the
map right away. If the position needs to be changed again, this can be done with another click
on the map (or by dragging the insertion point). Clicking the checkmark permanently applies the text
to the map.

.. _mapmarkup-text-rotation:

**Rotating text:**

While a text is being edited, a rotate icon appears to the right of the end of the first text line.
Dragging it with the mouse rotates the text around the insertion point (clockwise, relative to the map).
With the ``SHIFT`` key pressed the text rotates in 5° steps, with the ``CTRL`` key pressed in 15° steps.
Near 0°, 90°, 180° and 270° the text snaps automatically.

Alternatively, the angle can be entered in the symbology under *Rotation (°)* and set with *Apply rotation*;
the *0°* button makes the text horizontal again. This also works for several
selected texts (*Symbology: Selection*). Every new text starts horizontally (0°).

The rotation is kept when saving, printing and downloading as a shape file (attribute ``ROTATION``).


Changing an Existing Element
-----------------------------

There are two ways to change an already drawn element.

* Via the *Select* drawing tool (finger): clicking on the object on the map marks the element, which can then be changed.

* Via the list of already existing elements: clicking on an element in the list marks it for editing. The pencil icon can then be used to edit the object.

The second method is practical when several elements overlap and a geographic selection is difficult/impossible.

**Tip:** elements in the list can be identified more easily if they were described before being applied,
since the description is shown in the list.

Once an element has been marked for changing, the draft *sketch* for the element is shown on the map. In addition, a new
*symbology* icon appears above the list, taking you to the menu for editing the presentation.

.. image:: img/mapmarkup5.png
    :width: 200px
    :height: 80px

The draft *sketch* can be used to change the geometry of the element. The presentation can likewise be adjusted via the
presentation options. To finish the changes, you must confirm with the checkmark button to apply them.

Deleting an Existing Element
----------------------------

There are two ways to delete an element:

* Mark the element via the *Select* (finger) tool and click the *delete button* (trash can) to the right of the description input field.

* Click the *delete icon* (trash can) in the list of existing elements.

The advantage of the first method is that you can first see which element is actually being deleted.
If the elements have not been *described*, deleting from the list can result in deleting the wrong element,
because the text shown is not unambiguous.

.. note::
   Deletion is permanent. The drawing (map markup) tool does not offer an **undo**!


Labeling Elements
--------------------

Some element types offer labeling based on certain properties:

* **Lines:** label with the length [m / km] of the line

* **Polygons:** label with the area [m² / km²]

Labeling is done semi-automatically. Only the text value is determined automatically; the positioning of the text
on the map is done by the user.

The procedure for labeling is as follows:

* Click the *T icon* (text) for the corresponding object in the tool dialog.

For the current element, the button is located to the right of the text field for the element's optional description.
Elements already applied to the map show this icon in the list of created elements.

* Click on the map to position the point.

* Optionally change the presentation (font size) or extend/change the text.

* Click *Apply / Draw another* to apply the text to the map.
