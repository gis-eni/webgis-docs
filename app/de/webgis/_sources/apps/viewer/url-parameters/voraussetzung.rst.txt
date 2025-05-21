=============
Voraussetzung
=============

In diesem Dokument wird beschrieben, wie Karten, die für eine **Portalseite** erstellt wurden, mit **parametrierten URLs** aufgerufen werden können.  
Voraussetzung ist, dass eine **Portalseite existiert**, die Karten enthält.

Karten sind innerhalb einer Portalseite in **Kartensammlungen** organisiert. Jede Karte hat einen **Namen** und ist einer **Kategorie** zugeordnet:

.. image:: img/image1.png

Kartenaufruf und URL-Bestandteile
=================================

Eine Karte wird immer über die folgende URL-Struktur aufgerufen:

.. code-block::

    https://{Host}/{Portal-Applikation}/{Portal-Seite}/{Kategorie}/{Kartenname}

**Erklärung der URL-Bestandteile**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Bestandteil
     - Beschreibung
   * - ``Host``
     - Der Server, auf dem die Portal-Applikation installiert ist.
   * - ``Portal-Applikation``
     - Der Name der Portal-Applikation im IIS.
   * - ``Portal-Seite``
     - Die URL der Portalseite, wie sie vom Subscriber/Ersteller festgelegt wurde.
   * - ``Kategorie``
     - Die Kategorie, in der sich die Karte befindet.
   * - ``Kartenname``
     - Der Name der Karte.

.. caution::

    Enthält der Kartenname oder die Kategorie **Sonderzeichen**, müssen diese für die Darstellung in der URL **kodiert** werden.  
    **Leerzeichen** können entweder mit ``%20`` oder – zur besseren Lesbarkeit – mit einer **Tilde** (``~``) angegeben werden, z. B.:  
    ``Planung~und~Kataster``.

Beispielaufruf einer Basiskarte
-------------------------------

Soll die **Basiskarte** direkt aufgerufen werden, lautet die URL:

.. code-block::

    https://{host}/{portal-applikation}/{portal-seite}/Allgemein/Basiskarte
