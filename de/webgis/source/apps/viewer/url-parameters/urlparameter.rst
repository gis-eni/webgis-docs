=============
URL-Parameter
=============

Zusätzlich zum normalen Aufruf können Parameter übergeben werden:

.. code-block::

    https://{Host}/{Portal-Applikation}/{Portal-Seite}/{Kategorie}/{Kartenname}?param1=1&param2=2

Kartenausschnitte und Marker
============================

Kartenauschnitte
----------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - **Parameter**
     - **Beschreibung**
   * - ``bbox``
     - Gibt eine Bounding-Box an, auf die die Kartenansicht automatisch zoomt.  
       Syntax: ``[x-min],[y-min],[x-max],[y-max]`` bzw. bei geographischen Koordinaten  
       ``[lng-min],[lat-min],[lng-max],[lat-max]``, wobei **lng** für Längengrad  
       und **lat** für Breitengrad steht.  
       **Werte werden mit Beistrich getrennt**, Dezimalzahlen nutzen ``.`` als Trennzeichen.  
       
       Beispiel:
       
       .. code-block:: text

          &bbox=14.6,47.3,15.2,48.1
   * - ``center``
     - Definiert das Zentrum, auf das die Kartenansicht nach dem Start springt.  
       Syntax: ``[x],[y]`` bzw. ``[lng],[lat]``.  
       **Werte werden mit Beistrich getrennt**, Dezimalzahlen nutzen ``.`` als Trennzeichen.  
       
       Beispiel:
       
       .. code-block:: text

          &center=14.6,47.3
       
       Wird kein Maßstab angegeben (``scale``), zoomt die Ansicht auf **1:1000**.
   * - ``srs``
     - Gibt das **Koordinatensystem** an, falls die Koordinaten nicht in WGS 84 vorliegen.  
       Erwartet wird der **EPSG-Code** als Ganzzahl (ohne ``EPSG:``-Präfix).  
       
       Beispiel (GK-M34):
       
       .. code-block:: text

          &srs=31256
   * - ``scale``
     - Definiert den **Maßstab**, in den gezoomt wird.  
       Wird nur berücksichtigt, wenn auch die Parameter ``center`` oder ``marker`` übergeben werden.
   * - ``marker``
     - Zeigt einen **Marker** auf der Karte.  
       Erwartet ein **JavaScript-Objekt** mit Eigenschaften für die Position und ggf. Beschriftung.  
       
       Beispiel:
       
       .. code-block:: text

          &marker={lng:14.7,lat:47.2}
       
       - Das Objekt wird in **geschweiften Klammern** notiert.  
       - Eigenschaften werden mit **Beistrich** getrennt.  
       - Die Zuweisung erfolgt in der Form **Eigenschaft:Wert** (z. B. ``lng:14.2``).  
       - **Strings** müssen in **einfachen Hochkommata** stehen:  
       
         .. code-block:: text

            'Popup Text'
       
       Wenn keine anderen Parameter (``center`` oder ``bbox``) definiert sind, zoomt die Karte auf den Marker.  
       Der Maßstab kann mit ``scale`` angegeben werden.

Einen Marker übergeben
----------------------

Wie oben beschrieben, kann über den Parameter ``marker`` ein Marker beim Aufruf einer Karte übergeben werden. Die Übergabe erfolgt als **JSON** mit verschiedenen Eigenschaften.  

Formattierungsregeln:

- Double-Werte nutzen einen Punkt (``.``) als Dezimaltrennzeichen
- Integer-Werte bestehen nur aus Zahlen
- Strings müssen in Hochkommata stehen ``'``

.. list-table::
   :widths: 15 15 70
   :header-rows: 1

   * - **Eigenschaft**
     - **Datentyp**
     - **Beschreibung**
   * - ``lng``
     - Double
     - Geographischer **Längengrad**, an dem der Marker eingefügt wird.
   * - ``lat``
     - Double
     - Geographischer **Breitengrad**, an dem der Marker eingefügt wird.
   * - ``x``
     - Double
     - Falls keine geographischen Koordinaten genutzt werden, können hier **X/Y-Koordinaten**  
       sowie das Koordinatensystem als ``srs``-Wert übergeben werden.  
       Werden diese Werte angegeben, sind ``lng`` und ``lat`` nicht erforderlich.
   * - ``y``
     - Double
     - Falls keine geographischen Koordinaten genutzt werden, können hier **X/Y-Koordinaten**  
       sowie das Koordinatensystem als ``srs``-Wert übergeben werden.  
       Werden diese Werte angegeben, sind ``lng`` und ``lat`` nicht erforderlich.
   * - ``srs``
     - Integer
     - EPSG-Code des Koordinatensystems (ohne ``EPSG:``-Präfix), wenn ``x`` und ``y`` genutzt werden.
   * - ``icon``
     - String
     - **(Derzeit nicht genutzt)** – Standardmarker wird immer verwendet.
   * - ``text``
     - String
     - Textinformation des Markers, wird als **Popup-Text** beim Klick angezeigt. Bilder können eingebunden werden, indem sie mit ``img:`` als Präfix angegeben werden.  
         
       Beispiel:
        
       .. code-block:: text

           img:http://…../bild.jpg
   * - ``openPopup``
     - Boolean
     - Gibt an, ob der Popup-Text automatisch angezeigt wird oder erst nach einem Klick.

**Beispiele:**

Ein Marker mit dem Text **"Hallo Welt"**:

.. code-block:: text

    &marker={lng:14.7,lat:47.2,text:'Hallo Welt'}

Ein Marker mit projizierten Koordinaten:

.. code-block:: text

    &marker={x:-68014.6,y:215601.4,srs:31256}

Ein Marker mit **Text und Bild**, das automatisch beim Laden geöffnet wird (``openPopup=true``):

.. code-block:: text

    &marker={ 
        lng:15.4,
        lat:47.09,
        openPopup:true,
        text:
        'Das ist ein Bild img:https://upload.wikimedia.org/wikipedia/de/6/68/Nandu_gesamtes_Bild.jpg mit Subtext'
    }

.. image:: img/image2.png

Mehrere Marker übergeben
------------------------

Über den Parameter ``markers`` können mehrere Marker übergeben werden. Die Syntax entspricht einem **Array** aus einzelnen Markern.

**Hinweise:**

- Die Marker werden nicht nur in der Karte angezeigt, sondern auch als **Dynamischer Inhalt** übernommen.
- Über den optionalen Parameter ``markers_name`` kann ein Name definiert werden, unter dem der **Dynamische Inhalt** im TOC angezeigt wird.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``markers``
     - Array
     - Eine Liste von Markern, die in der Karte angezeigt werden sollen.  
       Jedes Element im Array entspricht einem **Marker-Objekt** mit denselben Eigenschaften wie beim ``marker``-Parameter.
   * - ``markers_name``
     - String
     - Definiert den **Anzeigenamen** für den *Dynamischen Inhalt* im TOC.

**Beispiel:**

Mehrere Marker mit individuellen Popup-Texten:

.. code-block:: text

   &markers_name=Ziele&markers=[{lng:14.7,lat:47.2,text:'Ziel 1'},
                                {lng:14.9,lat:46.8,text:'Ziel 2'},
                                {lng:14.8,lat:47.4,text:'Ziel 3'},
                                {lng:15.8,lat:47.1,text:'Ziel 4'},
                                {lng:15.2,lat:46.9,text:'Ziel 5'}]

Abfragen
========

An den Viewer kann beim Aufruf eine Abfrage mit Werten übergeben werden. Diese Abfrage wird dann automatisch als **aktuelles Abfrage-/Identifythema** im Viewer aktiv.  

**Funktionsweise:**
- Wird die Abfrage ohne Werte übergeben, wird das Abfragethema in der Benutzeroberfläche aktiviert.
- Werden zusätzlich **Abfragewerte** übergeben, wird die Abfrage ausgeführt und auf die **Ergebnisse gezoomt**.
- Ergebnisse werden in der Karte **selektiert und mit Markern markiert**.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``query``, ``abfragethema``
     - String
     - Name der Abfrage, wie sie im CMS definiert wurde.  
       **Beispiel:** ``&query=gemeinden``
   * - Abfragewerte (``name``, ``plz``, ``str``, ``hnr``, …)
     - String
     - Die Abfragewerte heißen so, wie sie im CMS festgelegt wurden.
   * - ``query2``, ``abfragethema2``, ``querythemeid``
     - String
     - Setzt das voreingestellte Abfragethema für **Identify** und **Suche** auf ein anderes Thema.  
       
       **Beispiel:**

       - ``querythemeid=bezirke``  
       - ``querythemeid=%23``

.. note::
   Die Abfrage-ID für **"sichtbare Themen"** ist ``#``. Da das Zeichen ``#`` in URLs reserviert ist, muss es als ``%23`` kodiert werden.

Darstellungsfilter
==================

Werden in einer Karte **Darstellungsfilter** angeboten, kann ein Filter über einen **URL-Parameter** übergeben werden.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``filter``
     - String
     - ID des Filters, wie im CMS definiert.
   * - ``filterarg_{argument}``
     - String
     - Platzhalter für **Filterargumente**. Für jedes Argument des Filters muss ein Wert übergeben werden.
   * - ``filterservice`` (optional)
     - String
     - Falls die **Filter-ID nicht eindeutig** ist und in verschiedenen Diensten vorkommt, kann hier die **Dienst-ID** angegeben werden. Ohne diese Angabe wird der Filter für **alle passenden Dienste** angewendet.  
       
       - **Format der Dienst-ID:** ``{Dienst-ID}@{CMS-ID}``  
       - Alternativ kann die Dienst-ID direkt in ``filter`` kombiniert werden:  
         ``{service-id}~{filterid}``.

.. note::
   Falls der Filter auch im **Darstellungsfilter-Werkzeug** angezeigt werden soll (wenn der Benutzer auf das Werkzeug **"Darstellungsfilter"** klickt), **MUSS** die Dienst-ID mit übergeben werden.

**Beispiele:**

Ein einfacher Filter:

.. code-block::

   &filter=my-filter&filterarg_WERT1=abc

Ein Filter mit eindeutiger **Dienstzuweisung**:

.. code-block::

   &filter=my-filter&filterservice=my-service@my-cms&filterarg_WERT1=abc

Oder alternativ:

.. code-block::

   &filter=my-service@my-cms~my-filter&filterarg_WERT1=abc

Werkzeuge
=========

Der Viewer kann mit einem voreingestellten **Werkzeug** aufgerufen werden.

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``tool``
     - String
     - ID des Werkzeugs, das beim Laden der Karte **automatisch ausgewählt** werden soll.  
       **Beispiel:**  
       
       .. code-block::

          &tool=webgis.tools.measureline

.. note::
   Es können **nur Werkzeuge**, aber keine einfachen Werkzeug-Buttons übergeben werden.  
   *Einfache Werkzeug-Buttons* sind Werkzeuge, die beim Anklicken direkt eine Aktion ausführen,  
   z. B. *Gesamter Ausschnitt*, *Refresh*, *Zurück*.

Die möglichen **Werkzeug-IDs** können unter folgendem Link nachgeschlagen werden:  
`https://api.webgiscloud.com/rest/tools <https://api.webgiscloud.com/rest/tools>`_

Erweiterte Parameter für das **Edit-Werkzeug**  
----------------------------------------------

Für das Editwerkzeug ``&tool=webgis.tools.editing.edit`` können zusätzlich folgende Parameter übergeben werden:

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``editthemeid``
     - String
     - ID des **Edit-Themas**, das aktiv gesetzt werden soll.  
       Die ID ist im **CMS** beim entsprechenden Editthema hinterlegt.
   * - ``ed_[FIELD_NAME]``
     - String
     - Wert für ein Feld in der **Editmaske**.  
       Das Feld muss im Editthema definiert sein.
   * - ``tooloption``
     - String
     - Gibt an, welches **Edit-Subwerkzeug** ausgewählt werden soll.

       **Beispiel:**  

       .. code-block::

          &tooloption=newfeature

       Öffnet die **Editmaske**, um ein neues Feature zu bearbeiten.

.. note::
   Der Parameter ``tooloption`` funktioniert **nur**, wenn die Karte mit dem  
   *WebGIS 6 Desktop Layout* geöffnet wurde.  
   Ist dies nicht der Fall, muss der Nutzer **manuell auf "Neues Objekt" klicken**.


Sichtbarkeit/Darstellungsvarianten
==================================

Um beim Aufruf eine bestimmte **Darstellungsvariante** anzugeben, kann eine Liste von Varianten übergeben werden.  
Diese werden dann in der angegebenen Reihenfolge **automatisch aktiviert**.

**Hinweise zur Funktionsweise:**

- Im **CMS** hat jede Darstellungsvariante eine eigene **URL**.
- Im **Viewer** können diese Varianten jedoch als **Buttons**, **Checkboxen** oder in **Dropdowns** gruppiert sein.
- **Einzelne Varianten** können nur übergeben werden, wenn sie **nicht** in einer Gruppe sind.
- Befindet sich die Variante in einer Gruppe, kann **nur die gesamte Gruppe** als Parameter übergeben werden.
- Die interne **URL einer Gruppe** hat immer das Format:  
  ``dvg_[Gruppenname in Kleinbuchstaben mit Unterstrichen statt Leerzeichen]``.
- Falls der interne Name einer Gruppe oder Variante unbekannt ist, kann er mit den **Entwicklungstools des Browsers** ermittelt werden (**F12**).  
  Jedes Element in den **Darstellungsvarianten im TOC** hat ein Attribut **„data-dvid“**, dessen Wert die zu übergebene ID ist.

.. image:: img/image3.png

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``presentation``, ``darstellungsvariante``
     - String
     - Name der Darstellungsvariante oder Gruppe.  
       Beide Parameter sind möglich und haben die gleiche Funktion.

**Beispiel:**

Ein Aufruf mit mehreren Darstellungsvarianten:

.. code-block::

   &presentation=dvg_strom-naturbestand/dv_ssg_nb_geb,dvg_kataster

Sichtbarkeit von einzelnen Layern
=================================

Ist das Sichtbarschalten über **Darstellungsvarianten** nicht möglich, können auch **einzelne Layer** direkt **sichtbar** oder **unsichtbar** geschaltet werden. Die Namen der Layer (inklusive Gruppe) werden dabei als Parameter übergeben.

**Hinweise zur Funktionsweise:**

- Befindet sich der **Layer in einer Gruppe**, muss der **komplette Pfad** mit **Backslash** (``\``) als Trennzeichen übergeben werden.
- Mehrere Layer können durch **Beistrich** getrennt werden.

**Beispiel:**  

.. image:: img/image4.png

Daraus ergibt sich der Layername:

.. code-block::

   Verwaltungsdaten\Bezirke

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``showlayers``, ``sichtbar``
     - String
     - Schaltet die angegebenen **Layer sichtbar**.  
       **Beispiel:**  

       .. code-block::

          showlayers=Verwaltungsdaten\Bezirke,Verwaltungsdaten\Landesgrenze
   * - ``hidelayers``, ``unsichtbar``
     - String
     - Schaltet die angegebenen **Layer unsichtbar**.  
       **Beispiel:**  

       .. code-block::

          hidelayers=Verwaltungsdaten\Bezirke,Verwaltungsdaten\Landesgrenze

.. note::
   Das gezielte Ein- und Ausblenden einzelner Layer sollte **nur in Ausnahmefällen** verwendet werden.  

   **Mögliche Probleme**

   - Layernamen und Gruppen können sich im Laufe der Zeit ändern, wodurch **Aufruflinks unbrauchbar** werden.  
   - Es wird nicht geprüft, zu welchem Dienst ein Layer gehört. Falls es mehrere Layer mit **dem gleichen Namen** in verschiedenen Diensten gibt, kann dies **zu Darstellungsfehlern führen**.

Sichtbarkeit von Hintergrunddiensten
====================================

Hintergrunddienste (**Basemaps**) können über den Parameter ``basemap`` aktiviert werden. Es können mehrere Dienste durch **Beistrich getrennt** übergeben werden:  

- Der **erste Dienst** wird als **Hintergrund-Basemap** verwendet.  
- Alle **weiteren Dienste** sind **Overlay-Basemaps**.

**Beispiele:**

Ein einzelner Basemap-Dienst:

.. code-block::

   basemap=orhto_tiles_gray@my_cms

Ein Basemap-Dienst mit zusätzlichem **Overlay-Dienst**:

.. code-block::

   basemap=ortho_tiles_gray@my_cms,streets_tiles_default@my_cms

Snapshots
=========

Falls im **MapBuilder** für eine Karte mehrere *Snapshots* definiert wurden, kann ein bestimmter **Snapshot** über den Parameter ``snapshot`` geladen werden. Die Karte wird dann mit der für den Snapshot **eingestellten Sichtbarkeit und dem gespeicherten Ausschnitt** geöffnet.

**Beispiel:**

.. code-block::

   snapshot=snapshot-name

Dienste hinzufügen
==================

Beim Aufruf einer Karte können zusätzliche **Dienste** übergeben werden. Dazu kann der Parameter ``append-services`` oder ``gdiservices`` genutzt werden. Die angegebenen Dienste werden in **der Reihenfolge eingefügt**, in der sie übergeben wurden. 

- **Neue Dienste** werden in der Karte hinzugefügt.  
- **Bereits vorhandene Dienste** werden ignoriert.  
- **Der zuletzt eingefügte Dienst** überdeckt alle vorherigen Dienste.

**Verfügbare Parameter:**

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - **Parameter**
     - Datentyp
     - **Beschreibung**
   * - ``append-services``, ``gdiservices``
     - String
     - Eine mit Beistrich getrennte Liste von **Dienst-IDs**. 

       **Beispiel:**  

       .. code-block::

          append-services=service1,service2,service1@cms1

Allgemeine (originäre) URL-Parameter
==========================================

Neben den spezifischen URL-Parametern können auch **allgemeine Parameter** übergeben werden. Diese werden als **originäre Aufrufparameter** behandelt und bei jedem Request in der Viewer-Session an den Server übermittelt. Dort können sie entsprechend verarbeitet werden.

.. note::
   Ein **allgemeiner Parameter** ist jeder Parameter, der nicht einem der definierten Schlüsselwörter entspricht  
   (z. B. ``query``, ``abfragethema`` usw.).

**Anwendungsbeispiel:**

Eine Karte soll mit einer **Projekt-ID** aufgerufen werden, damit nur die dazugehörigen Objekte angezeigt werden. Dies kann durch einen **gesperrten Filter** realisiert werden.

**Aufruf:**

.. code-block::

   http://...?...&project_id=4711...

Der gesperrte (**locked**) Filter kann dann auf diesen Parameter zugreifen:

.. code-block::

   PROJECT_ID='[url-parameter:project_id]'

Hier wird über den Prefix ``url-parameter:`` der Wert aus der URL als Filterkriterium gesetzt. Dies funktioniert **nur für gesperrte Filter**.

**Automatische Übernahme der Projekt-ID beim Editieren**

Damit die **Projekt-ID** automatisch in ein Feld übernommen wird, kann im CMS beim **Edit-Feld** folgende Konfiguration genutzt werden:

- **AutoValue** auf ``custom`` setzen.
- Als Wert für ``custom`` den URL-Parameter referenzieren:

.. code-block::

   url-parameter:project_id

Für **spezifische Aktionen** kann der Prefix erweitert werden:

.. code-block::

   oninsert:url-parameter:project_id
   onupdate:url-parameter:project_id
