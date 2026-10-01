Expressions (Ausdrücke)
=======================

Mit *Expressions* können Werte aus den Feldern eines Geo-Objekts berechnet oder zu Texten
zusammengesetzt werden, zum Beispiel ``[AREA]m2`` oder
``concat("Fläche: ", round([AREA], 2), " m2")``.

.. contents:: Inhalt dieser Seite
   :local:
   :depth: 2

Wo können Expressions verwendet werden?
---------------------------------------

AutoValues
^^^^^^^^^^

Bei :doc:`AutoValues <../apps/cms/editing/fields_autovalues>` kennzeichnet ein führendes ``=`` einen
Ausdruck. Das ist notwendig, um Ausdrücke von *benannten* AutoValues wie ``create_login``,
``shape_area`` oder ``change_datetime_utc`` zu unterscheiden.

.. code-block:: text

   create_login

ist ein benannter AutoValue.

.. code-block:: text

   =Objekt [NAME]

ist ein Legacy-Template.

.. code-block:: text

   =concat([FIRSTNAME], " ", [LASTNAME])

ist eine Structured Expression.

Das führende ``=`` gehört nur zur AutoValue-Konfiguration. Es wird entfernt, bevor der Inhalt als
Legacy-Template oder Structured Expression klassifiziert wird.

Tabellenspalten vom Typ ``TableFieldExpression``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tabellenspalten vom Typ ``TableFieldExpression`` (siehe :doc:`../apps/cms/queries/index`) sind
grundsätzlich Ausdrücke. Ein führendes ``=`` ist daher **nicht** notwendig. Es hat hier auch keine
besondere Bedeutung und wird nicht entfernt.

.. code-block:: text

   Objekt [NAME]

ist ein Legacy-Template.

.. code-block:: text

   concat([FIRSTNAME], " ", [LASTNAME])

ist eine Structured Expression.

Structured Expression oder Legacy-Ausdruck?
-------------------------------------------

Die Auswahl erfolgt **automatisch**:

* Eindeutig strukturierte Syntax wird mit dem neuen, typisierten Expression-Parser ausgewertet
  (*Structured Expression*).
* Text-Templates und bestehende ``$...``-Funktionen verbleiben im *Legacy*-Pfad.

.. important::

   Ein einmal als Structured Expression erkannter Ausdruck fällt bei einem Syntax- oder
   Auswertungsfehler **nicht** still auf Legacy zurück. Stattdessen wird ein Fehler mit Position
   gemeldet.

Wann wird eine Structured Expression erkannt?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Funktionsaufrufe**

.. code-block:: text

   concat([FIRSTNAME], " ", [LASTNAME])
   round([AREA], 2)
   if([STATUS] == "A", "Aktiv", "Inaktiv")
   coalesce([NAME], "Unbekannt")

Auch ein unbekannter Funktionsname wird als Structured Expression klassifiziert:

.. code-block:: text

   unknown([VALUE])

Dieser Ausdruck erzeugt den Fehler *Unknown function* und fällt nicht auf Legacy zurück.

**Feldreferenz mit Operator**

.. code-block:: text

   [COUNT] + 1
   [AREA] / 10000
   [STATUS] == "A"
   [VALUE] >= 10 && [ACTIVE] == true

Ein einzelnes Feld ohne Operator bleibt dagegen Legacy:

.. code-block:: text

   [NAME]

**Literale**

.. code-block:: text

   42
   12.5
   -10
   "Text"
   true
   false
   null

**Klammer- und Unary-Ausdrücke**

.. code-block:: text

   (1 + 2) * 3
   ![ACTIVE]

Übersicht
^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 55 45

   * - Konfiguration
     - Auswertung
   * - ``[NAME]``
     - Legacy
   * - ``Objekt [NAME]``
     - Legacy
   * - ``[FIRSTNAME] [LASTNAME]``
     - Legacy
   * - ``Object-ID [ID]``
     - Legacy
   * - ``$round2([AREA])``
     - Legacy
   * - ``Fläche: $round2([AREA]) m2``
     - Legacy
   * - ``Fläche: round([AREA], 2) m2``
     - Legacy; ``round`` wird **nicht** ausgeführt
   * - ``[COUNT] + 1``
     - Structured
   * - ``[AREA] / 10000``
     - Structured
   * - ``[STATUS] == "A"``
     - Structured
   * - ``round([AREA], 2)``
     - Structured
   * - ``concat("Fläche: ", round([AREA], 2), " m2")``
     - Structured
   * - ``if([STATUS] == "A", "Aktiv", "Inaktiv")``
     - Structured
   * - ``"Text"``
     - Structured
   * - ``42``
     - Structured
   * - ``(1 + 2) * 3``
     - Structured

Structured Expressions
----------------------

Structured Expressions sind typisiert und unterstützen:

* Feldreferenzen
* String-, Zahlen-, Boolean- und ``null``-Literale
* Rechenoperatoren
* Vergleiche
* logische Operatoren
* Bedingungen
* String-Funktionen
* Null-/Leerwertfunktionen
* numerische Funktionen
* Datumsfunktionen
* GIS-/Geometriefunktionen (bei AutoValues und Tabellen)

Feldreferenzen
^^^^^^^^^^^^^^

Felder werden in eckigen Klammern angegeben:

.. code-block:: text

   [NAME]
   [AREA]
   [STATUS]

* Ein **fehlendes** Feld ergibt ``null``.
* Ein **vorhandenes** Feld mit leerem Inhalt ergibt einen **leeren String** und nicht ``null``.

Literale
^^^^^^^^

**Strings** werden in doppelten Anführungszeichen angegeben:

.. code-block:: text

   "Text"
   "Aktiv"
   "Fläche: "

Unterstützte Escape-Sequenzen:

.. list-table::
   :widths: 20 80

   * - ``\"``
     - Anführungszeichen
   * - ``\\``
     - Backslash
   * - ``\n``
     - Zeilenumbruch
   * - ``\r``
     - Wagenrücklauf
   * - ``\t``
     - Tabulator

**Zahlen** werden invariant mit Dezimalpunkt geschrieben:

.. code-block:: text

   42
   12.5
   -10

**Boolean-Werte:** ``true``, ``false``

**Nullwert:** ``null``

Operatoren
^^^^^^^^^^

**Arithmetik:** ``+  -  *  /  %``

.. code-block:: text

   [COUNT] + 1
   [AREA] / 10000
   ([WIDTH] * [HEIGHT]) / 2

.. note::

   ``+`` dient ausschließlich der numerischen Addition. Strings werden mit ``concat(...)``
   verbunden. ``"Text" + "Text"`` ist daher ungültig.

**Vergleiche:** ``==  !=  <  <=  >  >=``

.. code-block:: text

   [STATUS] == "A"
   [AREA] >= 1000
   [MISSING] == null

**Logische Operatoren:** ``&&  ||  !``

.. code-block:: text

   [STATUS] == "A" && [AREA] > 1000
   [TYPE] == "A" || [TYPE] == "B"
   ![ACTIVE]

``&&`` und ``||`` werden *lazy* ausgewertet. Ein nicht benötigter rechter Zweig wird nicht
berechnet.

Bedingungen
^^^^^^^^^^^

.. code-block:: text

   if(condition, trueValue, falseValue)

Beispiel:

.. code-block:: text

   if([STATUS] == "A", "Aktiv", "Inaktiv")

``if(...)`` wird ebenfalls *lazy* ausgewertet. Nur der tatsächlich ausgewählte Ergebniszweig wird
berechnet.

String-Funktionen
^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - Funktion
     - Beschreibung
   * - ``concat(...)``
     - Verbindet beliebig viele Werte zu einem Text
   * - ``upper(value)``
     - Großbuchstaben
   * - ``lower(value)``
     - Kleinbuchstaben
   * - ``trim(value)``
     - Entfernt Leerzeichen am Anfang und Ende
   * - ``substring(value, start)``
     - Teilstring ab Position ``start`` (0-basiert, das erste Zeichen hat Index ``0``)
   * - ``substring(value, start, length)``
     - Teilstring mit der angegebenen Länge
   * - ``replace(value, oldValue, newValue)``
     - Ersetzt Textteile
   * - ``length(value)``
     - Länge des Textes

``start`` und ``length`` müssen nichtnegative Ganzzahlen sein. Liegt ``start`` außerhalb des Strings oder reicht
``start + length`` über das Stringende hinaus, wird ein Ausdrucksfehler erzeugt.

.. code-block:: text

   substring("abcdef", 0, 3)  ->  "abc"
   substring("abcdef", 2, 3)  ->  "cde"
   substring("abcdef", 2)     ->  "cdef"

Weitere Beispiele:

.. code-block:: text

   concat([FIRSTNAME], " ", [LASTNAME])
   upper([NAME])
   lower([CODE])
   trim([DESCRIPTION])
   substring([CODE], 0, 3)
   replace([NAME], "-", " ")
   length([NAME])

Null- und Leerwertfunktionen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Funktion
     - Beschreibung
   * - ``coalesce(...)``
     - Liefert den ersten Wert, der nicht ``null`` ist. Ein leerer String wird **nicht**
       übersprungen.
   * - ``is_null(value)``
     - Prüft ausschließlich auf ``null``
   * - ``is_empty(value)``
     - ``true`` bei ``null`` oder einem leeren String
   * - ``null_if_empty(value)``
     - Wandelt einen leeren String in ``null`` um

Beispiele:

.. code-block:: text

   coalesce([DISPLAY_NAME], [NAME], "Unbekannt")
   is_null([MISSING])
   is_empty([DESCRIPTION])

Da ``coalesce`` leere Strings nicht überspringt, wird es oft mit ``null_if_empty`` kombiniert:

.. code-block:: text

   coalesce(null_if_empty([DISPLAY_NAME]), [NAME], "Unbekannt")

Numerische Funktionen
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   round(value)
   round(value, digits)
   abs(value)
   min(...)
   max(...)

Beispiele:

.. code-block:: text

   round([AREA], 2)
   round([AREA] / 10000, 2)
   abs([DIFFERENCE])
   min([VALUE1], [VALUE2], 0)
   max([VALUE1], [VALUE2], 100)

Datumsfunktionen
^^^^^^^^^^^^^^^^

.. code-block:: text

   format_date(value, format)
   year(value)
   month(value)
   day(value)

Beispiele:

.. code-block:: text

   format_date([CREATED], "yyyy-MM-dd")
   year([CREATED])
   month([CREATED])
   day([CREATED])

Datumswerte werden zuerst als ISO-8601 interpretiert. Als Kompatibilitätsfallback wird die aktuelle
Kultur verwendet.

GIS-/Geometriefunktionen
^^^^^^^^^^^^^^^^^^^^^^^^

Diese Funktionen stehen bei AutoValues und bei Tabellenspalten vom Typ ``TableFieldExpression`` zur Verfügung:

.. code-block:: text

   shape_len()               shape_len(SRefId)
   shape_area()              shape_area(SRefId)
   shape_perimeter()         shape_perimeter(SRefId)
   shape_centroid_x()        shape_centroid_x(SRefId)
   shape_centroid_y()        shape_centroid_y(SRefId)

* Ohne Argument wird im Koordinatensystem der Feature-Geometrie gerechnet.
* Mit einer ``SRefId`` (EPSG-Code) wird eine **transformierte Kopie** der Geometrie verwendet. Die
  ursprüngliche Feature-Geometrie wird nicht verändert.

.. important::

   Der EPSG-Code sollte **immer angegeben** werden:

   * **AutoValues:** Ohne Angabe wird in der Regel das Koordinatensystem der Ziel-Featureklasse verwendet.
     Das ist aber nicht gesichert.
   * **Tabellen:** Die Geometrie wird für verschiedene Anwendungsfälle in andere Koordinatensysteme
     transformiert und liegt hier in der Regel in WGS84 vor. Der EPSG-Code muss daher zwingend
     angegeben werden, sonst sind Längen und Flächen nicht in der erwarteten Einheit.

.. tip::

   In Tabellen sollten die Funktionen nicht verwendet werden, wenn die Datenbank bereits einen berechneten
   Wert (z. B. ``Shape.Length()`` bzw. ein Längen-/Flächenfeld) liefert. Dieser Wert sollte aus
   Performancegründen bevorzugt werden.

Beispiele:

.. code-block:: text

   =shape_area()
   =shape_area(31256)
   =round(shape_area(31256), 2)
   =shape_centroid_x(4326)
   =concat("Fläche: ", round(shape_area(31256), 2), " m2")

In einer Tabellenspalte (``TableFieldExpression``) entfällt das führende ``=``:

.. code-block:: text

   round(shape_area(31256), 2)
   concat("Länge: ", round(shape_len(31256), 1), " m")

Textausgaben in Structured Expressions
--------------------------------------

Eine Structured Expression muss **insgesamt** ein gültiger Ausdruck sein. Freier Text vor oder nach
einem Funktionsaufruf macht daraus nicht automatisch eine Structured Expression.

Diese Eingabe

.. code-block:: text

   Fläche: round([AREA], 2) m2

wird als **Legacy-Template** erkannt. Nur ``[AREA]`` wird ersetzt, ``round(...)`` wird nicht als
neue Funktion ausgeführt. Bei ``AREA = 123.456`` ist das Ergebnis ungefähr:

.. code-block:: text

   Fläche: round(123.456, 2) m2

Für eine berechnete Textausgabe muss ``concat(...)`` verwendet werden:

.. code-block:: text

   concat("Fläche: ", round([AREA], 2), " m2")

Bei AutoValues zusätzlich mit führendem ``=``:

.. code-block:: text

   =concat("Fläche: ", round([AREA], 2), " m2")

Das Ergebnis ist:

.. code-block:: text

   Fläche: 123.46 m2

Weitere Beispiele (Ausdrücke dürfen über mehrere Zeilen geschrieben werden):

.. code-block:: text

   concat("Name: ", upper([NAME]))

.. code-block:: text

   concat(
       "Status: ",
       if([STATUS] == "A", "Aktiv", "Inaktiv")
   )

.. code-block:: text

   concat(
       "Fläche: ",
       round([AREA] / 10000, 2),
       " ha"
   )

Legacy-Ausdrücke
----------------

Legacy-Ausdrücke bleiben aus Kompatibilitätsgründen vollständig unterstützt. Falls der konfigurierte
Ausdruck eine ``$...``-Funktion enthält, wird diese nach dem Ersetzen der Platzhalter ausgewertet.

.. important::

   ``$...``-Ausdrücke aus **Feature-Attributwerten** werden nicht ausgeführt. Nur Funktionen, die
   bereits im konfigurierten Ausdruck stehen, werden ausgewertet. Dadurch wird Expression-Injection
   über Attributdaten verhindert (siehe :ref:`expressions-security`).

Einfache Text-Templates
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   [NAME]
   [FIRSTNAME] [LASTNAME]
   Objekt [NAME]
   Object-ID [ID]
   Name: [NAME], Fläche: [AREA]

Beispiele:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Ausdruck
     - Ergebnis
   * - ``Objekt [NAME]``
     - ``Objekt Hauptstraße``
   * - ``[FIRSTNAME] [LASTNAME]``
     - ``Ada Lovelace``

Platzhalter und Formatierung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Syntax
     - Beschreibung
   * - ``[!FIELD]``
     - Pflichtfeld: Ist der Feldwert leer, ergibt der **gesamte** Legacy-Ausdruck einen leeren
       String (z. B. ``[!NAME]``)
   * - ``[~FIELD]``
     - Bleibt aus Gründen der Rückwärtskompatibilität erhalten
   * - ``[FIELD:format]``
     - Formatierter Wert, z. B. ``[AREA:0.00]``, ``[COUNT:0000]``
   * - ``[url-encode:FIELD]``
     - URL-Encoding (UTF-8)
   * - ``[url-encode-latin1:FIELD]``
     - URL-Encoding (Latin-1)

Beispiel für URL-Encoding:

.. code-block:: text

   https://example.com/?name=[url-encode:NAME]

Spatial-Platzhalter
^^^^^^^^^^^^^^^^^^^

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

Legacy-Dollar-Funktionen
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   $eval(...)
   $sin(...)   $cos(...)   $tan(...)
   $asin(...)  $acos(...)  $atan(...)

   $round0(...) ... $round5(...)
   $n0(...)     ... $n5(...)
   $n0_de(...)  ... $n5_de(...)

   $pi()

Beispiele:

.. code-block:: text

   $eval(1+2*3)
   $round2([AREA])
   Fläche: $round2([AREA]) m2
   [NAME]: $n2_de([VALUE])

Eine Beschreibung der einzelnen Funktionen (inklusive Hinweisen zur Verschachtelung) findet sich im
Kapitel :doc:`../apps/cms/queries/index`.

Beispiele
---------

AutoValues
^^^^^^^^^^

.. code-block:: text

   create_login                                              (benannter AutoValue)

   =Objekt [NAME]                                            (Legacy)
   =[FIRSTNAME] [LASTNAME]                                   (Legacy)

   =concat([FIRSTNAME], " ", [LASTNAME])                     (Structured)
   =round([AREA] / 10000, 2)                                 (Structured)
   =if([STATUS] == "A", "Aktiv", "Inaktiv")                  (Structured)
   =concat("Fläche: ", round(shape_area(31256), 2), " m2")   (Structured)

TableFieldExpression
^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   Objekt [NAME]                                             (Legacy)
   [FIRSTNAME] [LASTNAME]                                    (Legacy)
   Fläche: $round2([AREA]) m2                                (Legacy)

   concat([FIRSTNAME], " ", [LASTNAME])                      (Structured)
   round([AREA] / 10000, 2)                                  (Structured)
   if([STATUS] == "A", "Aktiv", "Inaktiv")                   (Structured)
   concat("Fläche: ", round([AREA], 2), " m2")               (Structured)

Fehlerverhalten
---------------

Structured Expressions liefern klare Fehler mit Quellposition, unter anderem bei:

* ungültiger Syntax
* unbekannter Funktion
* falscher Argumentanzahl
* falschem Datentyp
* Division durch null
* Modulo durch null
* ungültiger SRefId
* ungültigem Substring-Bereich

Beispiele für ungültige Structured Expressions:

.. code-block:: text

   round(
   unknown([VALUE])
   "Text" + "Text"
   [VALUE] / 0

Structured Expressions fallen bei Fehlern nicht still auf Legacy zurück.

.. _expressions-security:

Sicherheit
----------

Die konfigurierte Structured Expression wird einmal vor dem Rendern zu einem festen Syntaxbaum
kompiliert. Feature-Attributwerte werden anschließend nur als **typisierte Werte** eingesetzt. Sie
werden nicht erneut tokenisiert oder geparst.

Ein Attributwert wie

.. code-block:: text

   round(12.345, 2) || unknown()

bleibt deshalb normaler Text und kann keine zusätzliche Funktion oder Operation einschleusen.

Auch im Legacy-Pfad werden ``$...``-Funktionen nur ausgeführt, wenn sie bereits in der
konfigurierten Expression vorkommen. Aus Attributwerten stammende ``$round``, ``$eval`` oder
ähnliche Inhalte werden nicht ausgeführt.

Performance
-----------

Die feature-unabhängige Vorarbeit wird bei Tabellenspalten vom Typ ``TableFieldExpression`` nur
**einmal pro Tabellenfeld** ausgeführt:

* Auswahl zwischen Structured und Legacy
* Parsen und Kompilieren der Structured Expression
* Ermitteln der Legacy-Platzhalter
* Erkennen konfigurierter Legacy-Dollar-Funktionen

Beim Rendern der einzelnen Objekte wird danach der vorbereitete Syntaxbaum bzw. die gecachten
Legacy-Parameter verwendet. Parserwahl und Parsing werden dadurch nicht für jedes einzelne Objekt
wiederholt.
