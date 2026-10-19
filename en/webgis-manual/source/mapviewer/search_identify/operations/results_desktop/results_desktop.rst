Results in Desktop Layout
============================

The result table in the desktop layout differs slightly from the table in the mobile layout.

Detail Results
----------------

The table for detail results is shown the same way as when several results are shown as a table.

.. image:: img/tabelle_detailergebnisse.png


Result List
-------------

.. image:: img/tabelle_liste_ergebnisse.png
    :width: 800px
    :height: 200px


Table Tools
------------------

The following table tools are available in the tables:

.. image:: img/icons_tabelle.png

The functions of the table tools are identical to those in the mobile layout.


If you select entries in a table with several results, two additional table tools appear. These are used to either remove the unselected results or to delete the selected result from the list.

.. image:: img/nicht_ausgew_entfernen.png

.. image:: img/ausgew_entfernen.png

.. _results-query-restriction:

Restricting a Query Result
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 9.26.4104

If a query or identify returns too many results, the result can be narrowed down with the **Restrict** table tool.
This opens the :ref:`Query Builder <toc-querybuilder>`, where conditions (**Field**, **Operator**, **Value**) for the results are defined.

**Apply** runs the original query again. The query geometry (e.g. identify point, rectangle or buffer) and the inputs of the detail search are kept,
and the conditions from the Query Builder are added. Afterwards, the table only shows the matching results.

* The Query Builder shows where the result comes from, e.g. from a query geometry or from a detail search with the entered values.
  **Show** briefly displays the query geometry in the map.
* A restricted result is marked with a hint in the table. The restriction can be removed with the **×** in the hint or with
  **Remove restriction** in the Query Builder. The original query is then run again without the restriction.
* For slow services, a loading indicator is shown while the query runs; the buttons cannot be clicked again during this time.
* If the query with the conditions returns no results (or a condition is invalid for the field), a hint is shown.
  The Query Builder stays open with the entered conditions and the table remains unchanged.
* If the table was opened via the context menu of the table of contents (see :ref:`toc-table`), the result is based on all
  features of the layer (including active display filters); this is also shown in the Query Builder.

.. note::
   The restriction only affects the query result in the table. It is **not a display filter**; the way the layer is drawn in the map does not change.
   The tool is only available if the Query Builder is allowed for the service and fields are enabled for it.


Table Tabs
-------------

Another difference from the mobile layout is the presence of tabs. A tab opens for each query topic. The number of results is shown to the right of the tab label.

.. image:: img/ergebnis_tab.png

If you query a topic again, the previously provided tab is replaced by the updated query result. How to prevent already-open tables from being closed by a new query is described in the next subchapter.

Results History
-------------------

There is no classic history like in the mobile layout in the desktop layout. Instead, it is possible to pin the tabs. To do this, click on the pin icon to the left of the label.

.. image:: img/tab_anpinnen.png

Then, an individual description must be entered into the label field.

Pinning prevents these results from being lost. It is also possible for the table to be shared as well when using *Share Map*.
