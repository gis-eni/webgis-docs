Url Parameter
=============

Optional zum normalen Aufruf können noch Parameter übergeben werden:

.. code-block::

    https://{Host}/{Portal-Applikation}/{Aortal-Seite}/{Kategorie}/{Kartenname}?param1=1&param2=2


Kartenausschnitt und Marker
---------------------------

**Parameter:**

*   ``bbox``

    Gibt eine Bounding-Box an, auf die Kartenansicht automatisch zoomt. Die Syntax lautet hier: [x-min],[y-min],[x-max],[y-max] bzw. bei geographischen Koordinaten [lng-min],[lat-min],[lng-max],[lat-max] wobei „lng“ für den geographischen Längegrad und „lat“ für den geographischen Beitengrad stehen. Die Werte werden mit Beistrich getrennt. Als Kommazeichen für die einzelnen Werte wird ein „.“ vorausgesetzt.

    Beispiel: ``&bbox=14.6,47.3,15.2,48.1`` 

*   ``center``

    Gibt das Zentrum an, auf das nach dem Start in der Kartenansicht gesprungen wird. Die Syntax lautet hier: [x],[y] bzw. [lng],[lat]

    Die Werte werden mit Beistrich getrennt. Als Kommazeichen für die einzelnen Werte wird ein „.“ vorausgesetzt.

    Beispiel: ``&center=14.6,47.3``   

    Wird kein Maßstab angeben (Parameter scale), zoomt die Ansicht auf einem Maßstab 1:1000 

*   ``srs``

    Der Viewer setzt voraus, dass die Koordinaten für ``bbox`` und ``center`` als geographische Koordinaten in WGS 84 übergeben werden. Ist dies nicht der Fall muss das Koordinatensystem über diesen Parameter spezifiziert werden. Übergeben wird hier der EPSG-Code des Koordinatensystems ohne dem „EPSG:“ Literal, also als Integer Zahl.

    Beispiel (GK-M34): ``&srs=31256``

*   ``scale``

    Gibt den Maßstab an, auf dem in der Kartenansicht gezoomt wird. Der Parameter wird nur berücksichtigt, wenn auch die Parameter ``center`` oder ``marker`` übergeben werden.


*   ``marker``

    Soll ein Punkt in der Karte mittels Marker dargestellt werden, kann der Marker über diesen Parameter definiert werden. Hier wird als Syntax ein Javascript Objekt mit entsprechenden Eigenschaften übergeben.

    Beispiel (mind): ``&marker={lng:14.7,lat:47.2}``

    Das Objekt wurd durch geschwungen Klammern abgegrenzt. Die einzelnen Eigenschaften des Objekts werden mittels Beistrich voneinander getrennt. Die Zuweisung einer Eigenschaft folgt mit folgender Syntax: [Eigenschaft]:[Wert] also beispielsweise lng:14.2 
    
    Enspricht der Wert einem String muss dieser in einfachen Hochkommata angeführt werden:

    Text:‘Popup Text‘

    Eine Beschreibung der einzelnen Werte folgt unten.

    Wenn nicht über die Parameter center oder bbox anders definiert, zoomt die Kartenansicht auf den Marker. Der Maßstab kann dafür über den Parameter scale übergeben werden.  

Marker übergeben
^^^^^^^^^^^^^^^^

Wie oben schon beschrieben kann über den Parameter ``marker`` ein Marker beim Aufruf in eine Karte übergeben werden. Die Übergabe Syntax ist dabei immer die Darstellung des Markers als Javascript Objekt (siehe oben). Folgende Tabelle führt alle möglichen Eigenschaften dieses Objekts an. Double-Werte sind immer Zahlen mit einen „.“ (Punkt) als Komma Separator. Integer Zahlen dürfen nur aus Zahlen bestehen. Strings müssen mit Hochkommata versehen werden. Die fett gedruckten Eigenschaften müssen angeführt werden:


*   ``lng``

    *   *Double*

    *   Der geographische Längengrad, an dem der Marker eingefügt werden soll

*   ``lat``

    *   *Double*

    *   Der geographische Breitengrad, an dem der Marker eingefügt werden soll

*   ``x``

    *   *Double*
    
    *   Falls die Übergabe der Koordinaten nicht in geographischen Koordinaten erfolgt, können hier die X,Y Koordinaten und die Koordinatensystem (als EPGS-Wert) übergeben werden. Werden diese Werte angeführt, sind lng und lat keine Pflichtfelder mehr.

*   ``y``

    *   *Double*

    *   Falls die Übergabe der Koordinaten nicht in geographischen Koordinaten erfolgt, können hier die X,Y Koordinaten und die Koordinatensystem (als EPGS-Wert) übergeben werden. Werden diese Werte angeführt, sind lng und lat keine Pflichtfelder mehr.

*   ``srs``

    *   *Integer*

    *   Falls die Übergabe der Koordinaten nicht in geographischen Koordinaten erfolgt, können hier die X,Y Koordinaten und die Koordinatensystem (als EPGS-Wert) übergeben werden. Werden diese Werte angeführt, sind lng und lat keine Pflichtfelder mehr.

*   ``icon``

    *   *String*

    *   (zZ nicht benutzt, es wird immer der Standardmarker gesetzt)

*   ``text``

    *   *Integer*

    *   Soll der Marker Information in Form von Text besitzen, kann dies über diesen Parameter erfolgen. Der Text wird dann als Popup Text beim Klick auf den Marker angezeigt.

        Innerhalb des des Textes können auch Links auf Bilder angeführt werden. Bilder werden mit einem „img:“ als Prefix gekennzeichnet, also Beispielsweise img:http://…../bild.jpg


*   ``openPopup``

    *   *Boolean*

    *   true/false

        Wird ein Text übergeben, kann hier angeführt werden, ob der Popup Text automatisch dargestellt wird oder erst durch einen Klick auf den Marker durch den Anwender.

            





**Beispiele:** 

Ein Marker mit dem Text „Hallo Welt“

.. code-block::

    &marker={lng:14.7,lat:47.2,text:‘Hallo Welt‘}

Ein Marker mit projezierten Koordinaten:

.. code-block::

    &marker={x:-68014.6,y:215601.4,srs:31256}

Ein Marker mit Text und eingeschlossem Bild. Wird nach dem Öffnen des Viewers automatisch angezeigt (``openPopup=true``). Die Zeilenumbrüche dienen hier nur der Veranschaulichung:

.. code-block::

    &marker={ 
    lng:15.4,
    lat:47.09,
    openPopup:true,
    text:
    ‘Das ist ein Bild img:https://upload.wikimedia.org/wikipedia/de/6/68/Nandu_gesamtes_Bild.jpg mit Subtext‘
    }

.. image:: img/image2.png



Abfragen
--------

An den Viewer kann beim Aufruf eine Abfrage mit Werten übergeben werden. Diese Abfrage ist dann automatisch im Viewer als aktuelles Abfrage/Identifythema aktiv. Wenn optional noch Werte übergeben werden, wird diese Abfrage ausgeführt und auf die Ergebnisse gezoomt. Ergebnisse werden im der Karte selektiert und mit Markern markiert.

*   query, abfragethema

    Beide Parameter sind möglich, die Funktionsweise ist gleich. Übergeben wird die Abfrage-Url, wie sie im CMS festgelegt wurde.

    Beispiel: ``&query=gemeinden``   

*   Abragewerte: name, plz, str, hnr, …

    Die Abfragewerte heißen so, wie sie im CMS definiert wurden


Sichtbarkeit/Darstellungsvarianten
----------------------------------

Um beim Aufruf schon eine bestimmte Darstellung anzugeben, kann hier eine Liste von Darstellungsvarianten angeführt werden. Diese werden dann in der angeführten Reihenfolge „automatisch angeklickt“. 
Im CMS hat jede Darstellungsvariante beim Dienst eine Url. Im Viewers können diese Darstellungsvarianten allerdings wieder zu Buttons und Checkboxes gruppiert sein, 
oder sich in Dropdowns befinden. Darum funktioniert die Übergabe der Url einer Darstellungsvariante nur, wenn diese in keiner Gruppe ist. Wenn sich die Darstellungsvariante in einer Gruppe befindet, 
kann nur die komplette Gruppe als Parameter übergeben werden. Die interne Url für eine Gruppe ist immer dvg_[Name der Gruppe in Kleinbuchstaben, Leerzeichen werden Underscore, …). 
Wenn man sich nicht sicher ist, wie der interne Name einer Gruppe oder einer Darstellungsvariante unterhalb eines Dropdowns oder einer Gruppe ist, kann dies über die Entwicklungstools des Browsers feststellen (F12).
Jedes Element, auf das man in Darstellungsvarianten TOC klicken kann hat ein Attribut mit dem Namen „data-dvid“. Der Wert dieses Attributes entspricht der Id, die man über einen parametrierten Aufruf übergeben kann:

.. image:: img/image3.png

*   presentation, darstellungsvariante

    Beide Parameter sind möglich, die Funktionsweise ist gleich.

    Beispiel: ``&presentation=dvg_strom-naturbestand/dv_ssg_nb_geb,dvg_kataster``

Sichtbarkeit von einzelnen Layern
---------------------------------

Ist das Sichtbarschalten nicht über Darstellungsvariaten möglich, können auch einzelne Layer sichtbar bzw. unsichtbar geschalten werden. Hierzu werden die Namen (inklusive Gruppe) über einen Parameter übergeben.
Befindet sich der Layer in einer Gruppe, muss der komplette Pfad mit *Backslash* als Trennzeichen in der Url übergeben werden.

.. image:: img/image4.png

würde somit folgenden Layernamen ergeben ``Verwaltungsdaten\Bezirke``

Mehrere Layer können mit Beistrich getrennt abgeführt werden.

*   showlayers, sichtbar
    
    Beide Parameter sind möglich, die Funktionsweise ist gleich. Die hier angeführten Layer wurden zusätzlich sichtbar geschalten.

*   hidelayers, unsichtbar
    
    Beide Parameter sind möglich, die Funktionsweise ist gleich. Die hier angeführten Layer wurden unsichtbar geschalten.


Beispiele:

``showlayers=Verwaltungsdaten\Bezirke,Verwaltungsdaten\Landesgrenze``
``hidelayers=Verwaltungsdaten\Bezirke,Verwaltungsdaten\Landesgrenze``

.. note::
   Das Schalten einzelner Layer sollte wenn möglich vermieden und nur in Ausnahmefällen verwendet werden. Layernamen und Gruppen können sich im Laufe der Zeit für einen Dienst ändern, was die verwendeten Aufruflinks unbrauchbar macht.
   Ebenso wird nicht unterschieden, in welchem Dienst sich ein Layer mit dem Namen befinden muss. Gibt es hier Doppeldeutigkeiten, kann das zu Fehlern in der Darstellung führen.

Sichtbarkeit von Hintergrunddiensten
------------------------------------

Hintergrunddienste (Basemaps) können über den Parameter ``basemap`` eingeschalten werden. Es können mit Beistrich getrennt mehrere Dienste (ids) angegeben werden, wobei der erste Dienst Hintergrund Basemaps und alle weiteren *Oberlayer* Basemaps sein müsssen.

Beispiele:

``basemap=orhto_tiles_gray@my_cms``

oder mit zusätzlichem Basemap *Overlay* Dienst:

``basemap=ortho_tiles_gray@my_cms,streets_tiles_default@my_cms``

Dienste hinzufügen
------------------

Beim Aufruf einer Karten können noch zusätzliche Dienste übergeben werden. Dazu muss über den Parameter ``append-services`` oder ``gdiservices`` eine mit Bestrich getrennt Liste von Dienst Ids übergeben werden.
Die angeführten Dienste werden in der Reihenfolge in die Karte eingefügt, wie sie übergeben werden. Neue Dienste werden werden einer Karte grundsätzlich ganz eingefügt. Der am letzten eingefügte Dienst überdeckt alle bereits eingefügten Dienst.
Befindet sich ein Dienst bereits in der Karte, wird dieser ignoriert.

*  ``append-services`` gleichbedeutend mit ``gdiservices``
   z.B.: ``append-services=service1,service2,service1@cms1``