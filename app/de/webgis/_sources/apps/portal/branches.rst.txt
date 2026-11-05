.. _portal-branches:

CMS-Branches testen
===================

.. versionadded:: 9.26.4102

Wurde im WebGIS CMS ein Arbeitszweig als Branch deployt (siehe :ref:`cms-deploy-branch`), kann dieser Stand im WebGIS getestet werden, ohne dass andere Anwender davon etwas merken. Alle anderen Anwender sehen weiterhin den veröffentlichten Stand (main).

Voraussetzung ist, dass die WebGIS API Branches erlaubt (``allow-branches`` in der ``api.config``, siehe :doc:`../../config/api/index`). Branch-Deploys sind in der Regel nur auf Entwicklungs- und Testsystemen vorgesehen.

Branch im Portal auswählen
--------------------------

Kartenautoren und Besitzer einer Portalseite sehen im Kopfbereich der Portalseite eine Auswahlliste mit den deployten Branches:

.. image:: img/branch-select.png

Neben *main* werden alle deployten Branches angezeigt. Der Tooltip eines Eintrags zeigt Bearbeiter, Datum und Commit des Branch-Deploys.

Die Auswahl gilt für **alle Karten in diesem Browser**, bis wieder *main* ausgewählt wird. Die Karten werden dann mit dem CMS des gewählten Branches geladen. Wurde ein CMS im Branch nicht deployt, wird für dieses CMS automatisch der veröffentlichte Stand verwendet. Ein Branch muss daher nur die CMS enthalten, die tatsächlich geändert wurden.

Branch im Kartenviewer
----------------------

Wird eine Karte mit einem Branch geladen, wird das im Kartenviewer deutlich angezeigt: Der Name des Branches steht im Titel des Inhaltsverzeichnisses und links unten erscheint ein Kennzeichen *Branch: ...*:

.. image:: img/branch-viewer.png

Mit dem ``×`` im Kennzeichen wird wieder zu *main* gewechselt. Ein Klick auf das Kennzeichen öffnet den Dialog **CMS-Branch wählen**:

.. image:: img/branch-dialog.png

Hier kann ebenfalls zwischen *main* und den deployten Branches gewechselt werden.

Branch-Links für Tester
~~~~~~~~~~~~~~~~~~~~~~~

Anwender, die keine Kartenautoren sind, können keinen Branch auswählen. Damit sie einen Branch trotzdem testen können, kann über die Schaltflächen *Link 1 h* bzw. *Link 1 Tag* ein **zeitlich begrenzter Link** auf die aktuelle Karte erzeugt und in die Zwischenablage kopiert werden. Wer diesen Link öffnet, sieht die Karte mit dem jeweiligen Branch. Der Link ist nur für die gewählte Dauer gültig.

.. note::

    Wird ein Branch-Deploy im CMS entfernt, wird beim nächsten Aufruf der Portalseite automatisch wieder *main* ausgewählt und ein entsprechender Hinweis angezeigt.
