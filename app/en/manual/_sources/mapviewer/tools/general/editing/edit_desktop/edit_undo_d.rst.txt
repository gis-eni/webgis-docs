.. _undo_d:

Undoing an Editing Step (Undo)
============================================

This tool can be used to undo editing steps. The following can be undone:

* Editing an existing object
* Deleting an existing object

If it is possible to undo steps, an *Undo* button appears in the edit dialog.

.. image:: img/rueckgaengig.png

Selecting it shows a list of the steps that can be undone. Moving the mouse over a step highlights the object that the action was performed on.

.. image:: img/rueckgaengig_1.png

.. note::
   An undo function is not available for every map service type. When editing, you should therefore not
   rely on the update being offered.

.. note::
   Despite the undo option, caution is advised when editing geo-objects. Even with an *undo*,
   geo-objects are not restored 100% identically. For example, deleting and later undoing changes
   the internal database ID (OBJEKT_ID) of the object. Automatically set attributes such as **last
   editor** or **last edit time** are also set anew by database triggers.

.. note::
   The *undo* option is only available for the current session. If the map viewer is closed or you
   switch to a different map, editing steps can no longer be undone.
