Zeichnungen Verwalten
=====================

In diesem Abschnitt werden weitere Konzepte des Zeichnen (Redlining) Werkzeugs behandelt:

* Zeichnungen speichern

* Zeichnungen laden

* Zeichnungen teilen

* Zeichnungen hochladen

* Zeichnungen herunterladen

Zeichnung speichern
-------------------

.. note::
   Das Laden und Speichern von Zeichnungen ist nur für Intranet Anwendungen gedacht, bei denen die Anwender 
   über die Anmeldung des Firmennetzwerks bekannt sind. Für den anonymen Zugriff über das Internet gibt es 
   als Alternative das *Karte Speichern* Werkzeug, *Teilen* Werkzeug, bzw. *Download* und *Upload* von Zeichnungen.

Um eine Zeichnung später wieder verwenden zu können, kann sie mit diesem Werkzeug gespeichert werden.
Im Dialog muss für die Zeichnung ein eindeutiger Name vergeben werden. Gibt man einen Namen ein,
den man bereits verwendet hat, wird die *alte* Zeichnung automatisch überschrieben (ohne Nachfrage).

.. note::
   Die Zeichnung wird auf den Servern des Betreibers des Kartenviewers gespeichert. Es obliegt diesem,
   "alte" Zeichnungen von Zeit zu Zeit zu löschen, da mit dem Redlining Werkzeug eigentlich nur temporäre 
   Zeichnungen erstellt werden sollten (siehe Beschreibung "gute Anwendungsfälle für Redlining").

.. note::
   Sollten Zeichnungen langfristig gespeichert werden, empfiehlt es sich, diese mit dem unten angeführten 
   *Herunterladen* Werkzeug auf der eigenen Festplatte zu speichern.

Trotzdem bietet das *Zeichnung Speichern* Werkzeug gegenüber dem *Herunterladen* Vorteile:

* Der Zugriff kann von unterschiedlichen Geräten erfolgen. Ein Projekt kann am Desktop erstellt und später am Handy wieder geöffnet werden.

* Nur für den eigenen Benutzer sichtbar.

Zeichnung laden
---------------

Zeichnungen, die mit dem *Zeichnung speichern* Werkzeug am Server des Betreibers des Kartenviewers gespeichert 
wurden, können mit diesem Werkzeug wieder geladen werden.

Zeichnung teilen
----------------

Zeichnungen sind in der Regel nur für den Anwender sichtbar, der diese Anwendung erstellt hat. Mit diesem Werkzeug 
kann eine Zeichnung über einen Link mit anderen Anwendern geteilt werden.

.. note::
   Der Button ist *nur* ein Shortcut (Abkürzung) zum *Karte teilen* Werkzeug. Eine genaue
   Beschreibung erfolgt im Abschnitt *Karten Werkzeuge*. Beim Teilen werden über den Link nicht nur die Zeichnung,
   sondern alle anderen Einstellungen der Kartenansicht (dargestellte Themenebenen) geteilt.

Zeichnung herunterladen
-----------------------

Damit kann eine Zeichnung dauerhaft auf dem eigenen Rechner gespeichert werden. Je nach Format, kann diese Datei 
zu einem späteren Zeitpunkt wieder hochgeladen werden.

Folgende Formate stehen zur Verfügung:

**Redlining-Projekt (GeoJson):**

Die Zeichnung wird als Text Datei im Geo-Json Format heruntergeladen. Geo-Json ist ein Standard für
GeoDaten und die Geometrie der Zeichnung kann auch in anderen Programmen wiederverwendet werden. In den *Properties*
der einzelnen Elemente wird auch die Darstellung (Farben...) beschrieben, die allerdings nicht standardisiert ist und
nur vom Redlining Werkzeug beim späteren Hochladen wieder interpretiert werden kann.

Dieses Format eignet sich zum dauerhaften Speichern von Zeichnungen, da es auch die Möglichkeit des Hochladens 
gibt. Beim Hochladen werden wieder alle Einstellungen aus der Zeichnung (Farben, Beschreibungen, ...) übernommen.

**GPX:**

GPX ist ein Format, mit dem man *Tracks* (Wege) und *Waypoints* (Wegpunkte) auf Navigationsgeräte übertragen kann.
Die Zeichnungen sollten nur dann in diesem Format heruntergeladen werden, wenn das Ziel ein Navigationsgerät ist.
Die Dateien können zwar später wieder hochgeladen werden, es kommt aber eventuell zu Datenverlusten:

.. note::
   Beim Herunterladen im GPX Format werden nur Linien (werden zu *Tracks*) und Texte (werden zu *Waypoints*)
   berücksichtigt. Alle andern Geometrietypen werden ignoriert!
   Auch die Darstellung (Farben, ...) können in eine GPX Datei nicht übernommen werden.

**Esri Shapefile:**

*Esri Shapefiles* sind ein Standardformat für die Verarbeitung von Geo-Daten, da es quasi von jeder GI-Software
geladen werden kann. Um erstellte Projekte in beliebige GI-Systeme übernehmen zu können wird hier der
Download in diesem Format angeboten. 

.. note::
   Für *Esri Shapefiles* gibt es später keine Möglichkeit des Hochladens. Verwenden Sie dieses Format **nicht**
   zur Sicherung der Zeichnungen, sondern nur wenn es in zusätzliche GI-Systeme überführt werden soll.

Das Ergebnis beim **Esri Shapefile** Download ist eine ZIP Datei, in dem sich die *Shapefiles* befinden.
Für jeden Geometrietyp wird ein Shapefile angelegt (symbol, text, line, ...). Jedes *Shapefile* besteht wieder 
aus mindestens 3 Dateien. Zu den Sachdaten werden Informationen zur Darstellung (Farb-Codes) und die Beschreibung/Texte
der einzelnen Element übernommen.

Zeichnung hochladen
-------------------

Es können *GPX* und *GeoJson* (Redlining Projekte, die früher heruntergeladen wurden) Dateien hochgeladen werden.

.. note::
   Um welchen Dateityp es sich handelt, entscheidet der Viewer über die Dateiendung (\*.gpx, \*.json, ...).
   Auf die richtige Dateiendung ist dabei zu achten.

Bei *GPX* Dateien können auch Dateien hochgeladen werden, die nicht vorher mit dem *Zeichnen* Werkzeug 
heruntergeladen wurden. Mit dem Upload können auch *GPX* Dateien hochgeladen werden, die mit einem 
Navigationsgeräte erstellt wurden, um diese in der Karte zu visualisieren. Übernommen werden dabei 
*Tracks* und *Waypoints*.

