Basic Approach
=============================

When you create and publish a map with the *MapBuilder*, a JSON document with all settings is created
in the background on the server. This JSON is then interpreted by the map viewer, and the
map with all UI elements is generated from it.

In templates, parts of this map JSON file can now be encapsulated. If these parts contain additional
elements (e.g. tools, search services), these are also added to the map.

.. note::
   With *UI master templates*, elements can only be added to an existing map when it is loaded.
   It has an effect if an element in the master is defined with ``false`` (=do not apply), but it
   was already set in the map via the MapBuilder.

This also results in the order in which a map is loaded:

* Step 1: the map is loaded with all settings from the MapBuilder
* Step 2: if there is a *UI master template* for a map category, all elements set in it are added
* Step 3: if there is a *UI master template* for a portal page, all elements set in it are added.

.. note::
   No elements are inserted twice into a map. If a tool is already in the map in step 1, the same
   tool is not additionally inserted again via steps 2 and 3.
