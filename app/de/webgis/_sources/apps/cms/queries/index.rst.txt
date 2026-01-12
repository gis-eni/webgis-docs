Abfragen
========

.. note::
   Dieser Abschnitt kann nicht für *dynamische Dienste* (siehe vorheriges Kapitel) angewendet werden. Ist bei den Eigenschaften des Dienstes im CMS unter ``Dynamische Abfragen`` ein Wert ungleich ``None`` eingestellt, steht dieser Abschnitt im CMS nicht zur Verfügung.

Neben der kartographischen Darstellung von *Geo-Objekten* in einer Karte bieten manche Kartendienste die Möglichkeit, *Geo-Objekte* zu suchen oder abzufragen. Dazu muss im CMS beim jeweiligen Dienst in den Abschnitt ``Abfragen`` gewechselt werden:

.. image:: img/queries1.png

Dort kann über den Button ``Neue Abfrage`` eine neue Abfrage für diesen Dienst erstellt werden. In folgendem Dialog muss zuerst das Thema aus dem Dienst ausgewählt werden, das abgefragt werden soll:

.. image:: img/queries2.png

Unter ``Tabelle`` kann ausgewählt werden, welche Felder für dieses Thema in der Ergebnistabelle beim Erstellen importiert werden sollen:

* **Nichts importieren:** Bei der Erstellung der Abfrage wird nichts importiert. Die gewünschten Felder werden zu einem späteren Zeitpunkt festgelegt.

* **Felder dynamisch - (*) importieren:** Es wird für die Tabelle ein Feld mit dem "Feldnamen" ``*`` angelegt. Das bedeutet, dass alle Felder in der Tabelle angezeigt werden.  
  Das Auslesen der vorhandenen Felder erfolgt hier immer zur Laufzeit im *Kartenviewer*. Ändert sich das Datenmodell hinter dem Layer, werden die Änderungen automatisch im Kartenviewer angepasst.

* **Einzelne Felder importieren:** Alle Felder, die zum Zeitpunkt der Erstellung der Abfrage vorhanden sind, werden für die Tabelle übernommen. Spätere Änderungen im Datenmodell müssen nachträglich manuell nachgezogen werden. Diese Option kann für ein schnelles Erstellen von Abfragen hilfreich sein. Die importierten Felder können nach Wunsch im nächsten Schritt im CMS bearbeitet (Feldtyp, Reihenfolge, Bezeichnung) und ergänzt werden.

.. note::
   Nicht alle Diensttypen liefern über die *Capabilities* Auskunft über die Feldnamen der Themen. Für diese Diensttypen (z.B. WMS) kann die letzte Option auch entfallen.

Unter ``Allgemeine Eigenschaften`` müssen noch ein Name und ein eindeutiger ``URL (Name)`` für den Dienst vergeben werden.  
Der ``URL (Name)`` kann verwendet werden, um über einen parametrierten Aufruf der Karte eine Suche zu übergeben (``...&query=adressen&...``).  
Danach kann die Abfrage mit ``Übernehmen`` erstellt werden. Die Abfrage sollte jetzt in der Liste erscheinen.

Unter der Abfrage findet man folgende Punkte:

.. image:: img/queries3.png

* **[Abfragethema] (Eigenschaften):** Eigenschaften der Abfrage.

* **Abfragethema:** Das Thema des Dienstes, der abgefragt wird.

* **Exportierbare/Benutzerdefinierte Formate:** Hier können spezielle Regeln definiert werden, aus denen Textdateien auf Basis der Abfrageergebnisse erstellt werden. Diese können dann vom Anwender über den Kartenviewer heruntergeladen werden. Wird hier nichts definiert, steht trotzdem ein Export der Daten als CSV zur Verfügung.

* **Suchfelder:** Sollten Daten nicht nur abgefragt werden, sondern sollte der Anwender auch die Möglichkeit haben, innerhalb bestimmter Felder zu suchen, können diese Felder hier definiert werden.

* **Tabelle:** Hier werden die einzelnen Spalten angeführt, die in der Ergebnistabelle angezeigt werden. Neben einfachen Werte-Spalten können auch Spalten mit *Expressions* und *Hotlinks* (setzen sich aus den Werten einer oder mehrerer Spalten zusammen) angelegt werden.

* **TOC-Thema für diese Abfrage:** Hier können optional Themen aus diesem oder einem anderen Dienst abgegeben werden, auf die sich die Abfrage bezieht. Stellt der Anwender beim Abfragen ``sichtbare Themen`` ein, wird diese Abfrage mit in den Abfrageprozess einbezogen, wenn sich das Abfragethema oder eines der hier angeführten Themen im sichtbaren Kartenbereich befindet.


Allgemeine Abfrage Eigenschaften
================================

Unter den allgemeinen Eigenschaften einer Abfrage lassen sich folgende Optionen einstellen:

.. image:: img/queries4.png

Da eine Beschreibung der einzelnen Eigenschaften über das ``?`` im Dialog abrufbar ist, wird hier nicht auf alle Details eingegangen.

``Allgemein``

* **Minimaler Maßstab:** Nach einer Suche wechselt der Kartenviewer-Ausschnitt zum Suchergebnis. Handelt es sich hier nur um einen einzelnen Punkt, kann hier ein Maßstab angegeben werden, auf den gezoomt werden sollte.

``Erweiterte Eigenschaften``

* **Distinct:**
  Gibt es Objekte mit identischer Geometrie (z.B. gleicher Punkt) und sind ebenso die in der Abfrage abgeholten Attributwerte identisch, wird ein Objekt in der Ergebnisliste nur einmal angezeigt. Die Daten werden zuerst von der WebGIS-Applikation vom Karten/Feature-Dienst abgeholt und daraus das Distinct berechnet (serverseitig).  
  Ein Anwendungsbeispiel könnten Kundenbestellungen sein, die alle an die gleiche Adresse geliefert werden. Sollte in der Ergebnistabelle beispielsweise nur der Kundenname und die Adresse angezeigt werden, würden hier für jede Bestellung identische Punkte übereinander als Marker dargestellt werden. Mit ``Distinct`` würden diese identischen Punkte nur noch als einfacher Marker erscheinen.

* **Union:**
  Ergebnismarker, die in der Karte am gleichen Ort liegen (identischer Punkt), werden zu einem Objekt zusammengefasst. Der Marker enthält in der Tabellenansicht alle betroffenen 'Records'.  
  Hier kann das gleiche Anwendungsbeispiel wie bei ``Distinct`` herangezogen werden. Nimmt man in der Tabelle auch die Bestellnummer mit, können die einzelnen Punkte nicht mehr über ``Distinct`` zusammengefasst werden, weil sich die Bestellnummer bei den einzelnen Punkten unterscheiden wird (Kunde:Bestellungen = 1:n). Damit nicht am selben Ort mehrere Marker in der Karte dargestellt werden müssen, können Marker mit dem gleichen Einfügepunkt zusammengefasst werden. Klickt der Anwender auf einen dieser Marker, werden als Ergebnis alle betroffenen Bestellungen angezeigt. Für jeden *Record* (Bestellung) wird nur die erste Spalte angezeigt. Der Anwender kann durch Klick auf das erste Attribut den *Record* aufklappen und sieht dadurch alle Werte.

.. note::
   Kartendienste geben während einer Abfrage immer nur eine maximale Anzahl von Geo-Objekten zurück (z.B. ArcGIS Server Dienste liefern standardmäßig maximal 1000 Ergebnisse zurück). Wird die Option ``Union`` für eine Abfrage gewählt und die maximale Anzahl von abfragbaren Geo-Objekten überschritten, liefert WebGIS eine Meldung zurück, dass die Abfrage nicht möglich ist. Der Grund ist, dass ansonsten eine nicht vorhandene Vollständigkeit der Daten verschleiert werden würde.  
   Können nicht alle Geo-Objekte abgefragt werden, würde ein Punkt zwar angezeigt werden, es wäre jedoch nicht gewährleistet, dass die angezeigten *Records* unter diesem Marker vollständig sind. Daher wird in diesem Fall gar kein Ergebnis mit einem Hinweis angezeigt, damit unvollständige Daten nicht fälschlicherweise als vollständig interpretiert werden.

.. note:: 
   Um den oben beschriebenen Effekt abzumildern, kann unter "Maximale Anzahl" ein größerer Wert angegeben werden. Auch wenn der zugrundeliegende Dienst nur maximal 1000 Objekte zurückliefert, kann durch Mehrfachabfragen im Hintergrund versucht werden, alle Geo-Objekte abzuholen. Der Wert sollte allerdings auch nicht zu groß sein, da es sonst zu einer höheren Serverlast kommen kann.

.. note:: 
   Eine weitere Möglichkeit, den Effekt abzufangen, ist das Einstellen der Option ``Layer Zoomgrenzen anwenden``. Die Abfrage kann dann nur mehr durchgeführt werden, wenn der Anwender in der Karte innerhalb der Maßstabsgrenzen des Abfragethemas ist. Die Zoomgrenzen werden dabei im Kartendienst definiert. Dieser Wert ist auch sinnvoll, wenn diese Abfrage als *dynamischer Inhalt* über den MapBuilder oder über eine *Dynamische Content Marker*-Darstellungsvariante eingebunden wird.


Suchfelder
==========

Suchfelder können für eine Abfrage optional parametriert werden. Enthält eine Abfrage keine Suchfelder, 
kann das Thema *nur* abgefragt werden (z.B. mit dem Identify-Werkzeug).  
Werden Suchfelder definiert, erscheint die Abfrage im *Karten Viewer* zusätzlich unter "Detailsuche".

.. note:: 
   Nicht alle Dienst-Typen unterstützen das Suchen innerhalb eines Themas, z.B. WMS.

Zum Anlegen eines Suchfeldes muss in den Bereich ``Suchfelder`` gewechselt und auf ``Suchbegriff hinzufügen`` 
geklickt werden.

Im Dialog muss zuerst das Feld ausgewählt werden, in dem gesucht werden soll.  
Unter ``Abfragemethode`` kann eingestellt werden, wie im entsprechenden Feld gesucht werden soll.  
Mit ``Exact`` muss der Anwender beispielsweise den Suchbegriff exakt so eingeben, wie er in der 
Datenbank angeführt wird (sinnvoll bei IDs, Zahlen). Meistens ist es anwenderfreundlicher, 
wenn automatisch mit *Wildcards* gesucht wird. Mit ``EndingWildcard`` wird automatisch nach dem 
eingegebenen Suchbegriff ein Wildcard (* oder %) angehängt. So werden alle Geo-Objekte gefunden, 
bei denen das entsprechende Attribut mit dem eingegebenen Suchbegriff beginnt. In der Auswahlliste 
werden noch weitere Optionen angezeigt, die beispielsweise alle Leerzeichen durch *Wildcards* 
ersetzen (``SpacesToWildcard``, ``SpacesToWildcardWithEndingWildcard``, ...).

.. note:: 
   Damit die Suche performant ausgeführt wird, sollte darauf geachtet werden, dass die Suchfelder 
   in der Datenbank entsprechend indiziert sind.

Abschließend muss noch ein Name angegeben werden, der in der Suchmaske für dieses Feld angezeigt 
wird. Unter ``Url`` sollte eine für diese Abfrage eindeutige ID für das Feld eingetragen werden.  
Ruft man den *Karten Viewer* auf, können so Parameter in der URL mitgegeben werden, die schon 
beim Start eine Abfrage ausführen. Die entsprechenden Parameter für die Suchfelder entsprechen 
dem hier eingetragenen (``...&query=adressen&adresse=hauptplatz...``).

Schließt man den Dialog mit ``Übernehmen``, sollte der Suchbegriff in der Liste erscheinen.  
Dort können die Eigenschaften auch noch nachträglich bearbeitet und die Reihenfolge der 
Suchbegriffe geändert werden. Über die Eigenschaften können auch noch weitere Optionen wie 
Auswahllisten, Whitelists, usw. parametriert werden.


Auswahllisten
=============

Um die Eingabe von Suchbegriffen für den Anwender zu erleichtern, können Auswahllisten angeboten werden.  
Wenn der Anwender ein Zeichen in einem Suchfeld eingibt, wird im Hintergrund die Datenbank abgefragt und 
dem Anwender daraus Vorschläge angeboten.

Auswahllisten funktionieren auch kaskadierend: Bereits eingegebene Suchbegriffe können berücksichtigt werden.  
(Beispiel: Es werden nur Grundstücke einer KG angeboten, wenn bereits die KG-Nummer eingegeben wurde).

Gehen wir von einer Grundstückssuche aus, in der der Anwender eine KG-Nummer oder einen KG-Namen 
und eine Grundstücksnummer eingeben kann:

.. image:: 
    img/queries10.png

Die Datenbank-Felder zum Abfragen heißen im Beispiel:

* ``KG``: Eingabefeld ID - ``kg``
* ``KG_NAME``: Eingabefeld ID - ``kgname``
* ``GNR``: Eingabefeld ID - ``gnr``

Damit Auswahllisten funktionieren, muss das beim entsprechenden Suchfeld bei den Eigenschaften angegeben werden:

.. image:: 
    img/queries11.png

Über den Auswahllisten-Editor kann das entsprechende SQL-Statement definiert werden:

.. image:: 
    img/queries12.png

Unter *ConnectionString* kann die Verbindung zur Datenbank angegeben werden, die abgefragt werden soll.

.. note:: 
    Verwendet man als Server *ArcGIS Server* oder *gView* (über die GeoServices REST-Schnittstelle), muss
    keine direkte Verbindung zur Datenbank angegeben werden. Hier kann die Abfrage der Auswahllisten-Werte
    direkt über den *MapServer* erfolgen (empfohlen).  
    In diesem Fall gibt man als *ConnectionString* einfach das Kürzel ``#`` an.

Unter *SqlStatement* wird jetzt der Ausdruck angegeben, der für die Suche verwendet wird. Bei einer Datenbank- 
Abfrage mit *ConnectionString* ist das in der Regel ein komplettes ``SELECT FROM WHERE``-Statement.  
Verwendet man den *MapServer* zur Abfrage (ConnectionString = ``#``), gibt man hier nur die ``WHERE``-Klausel an (ohne WHERE).

Als Platzhalter können die Namen der Suchbegriffe eingegeben werden (z.B. ``{{kg}}``, Wildcards nicht vergessen).

Für unser Beispiel könnten die *SqlStatements* wie folgt aussehen:

**KG**

.. code-block:: 

    KG like '{{kg}}%'

**KG Name**

.. code-block:: 

    KG_NAME like '{{kgname}}%'

**Grundstücksnummer**

.. code-block:: 

    GNR like '{{gnr}}%'

    #if kg
      AND KG='{{kg}}'
    #endif

    #if kgname
      AND KG='{{kgname}}'
    #endif

Hier wird die Abfrage noch weiter eingeschränkt, wenn bereits eine KG-Nummer oder ein KG-Name eingegeben wurde.  
Über die ``#if``-Direktiven kann hier erzwungen werden, dass der entsprechende Code-Teil nur ins Statement aufgenommen 
wird, wenn der Anwender für dieses Feld einen Wert eingegeben hat.

.. note:: 
    Hier im Beispiel wurden für alle drei Eingabefelder Auswahllisten definiert.  
    Das ist nicht zwingend erforderlich. Wenn es für die Aufgabe sinnvoll ist, kann auch 
    nur ein Eingabefeld Auswahllisten anbieten.


Tabelle
=======

Hier wird angeführt, welche Felder in der Ergebnisliste angezeigt werden. Damit die Abfrage 
funktioniert, müssen hier Werte eingetragen werden. Eine Ausnahme stellen hier WMS-Dienste dar, 
wo das Schema der Daten nicht über die *Capabilities* bekannt ist. Hier kann in der 
Regel keine Tabelle definiert werden.

Hat man beim Erstellen der Abfrage (siehe oben) unter Tabelle ``Felder dynamisch importieren`` 
ausgewählt, befindet sich unter ``Tabelle`` bereits eine *Spalte*:

.. image:: img/queries6.png

Hierbei handelt es sich um einen Sonderfall: Als Feld wird hier ``*`` angeführt, was 
bedeutet, dass die Felder automatisch zur Laufzeit bestimmt werden. Alle Attribute, die von 
einer Abfrage vom *Kartendienst* zurückgeliefert werden können, werden angezeigt.

.. note::
   Diese Option kann auch verwendet werden, wenn bei einem WMS-Dienst als ``GetFeatures Type`` 
   beispielsweise ``application/geojson`` oder ``txt/xml`` eingestellt wird. Dann werden auch 
   hier alle Felder in die Tabelle übernommen. Alternativ könnten hier auch die einzelnen 
   Felder manuell angelegt werden.

Möchte man mehr Kontrolle über die Tabelle haben, können hier Felder auch einzeln angegeben werden. 
Dazu kann der Button ``Mehrere Spalten hinzufügen`` und ``Spalte hinzufügen`` verwendet werden. 
Der erste Punkt funktioniert allerdings nur, wenn der zugrunde liegende Dienst auch Auskunft 
über das Datenschema der einzelnen Themen liefert (AGS, IMS, ...).

Wurden Spalten hinzugefügt, kann die Eigenschaften weiter bearbeitet werden:

.. image:: img/queries7.png

Der ``Spalten-Typ`` gibt an, was in der Tabellenspalte angezeigt wird. Der Standardwert ist 
hier ``Field``, was bedeutet, dass in der Spalte der Wert eines Attributs des Geo-Objektes angezeigt 
wird. Unter ``Definition / Quelle`` muss für diesen Typ ein Feld aus dem Abfragethema angeführt 
werden:

.. image:: img/queries8.png

Wählt man als ``Spalten-Typ`` beispielsweise ``Hotlink``, erscheint in der Tabelle ein *Hotlink*, über 
den der Anwender auf eine neue Seite weitergeleitet werden kann. Unter ``Definition / Quelle`` 
kann hier eine ``Hotlink-URL`` angegeben werden. In dieser URL können Felder aus dem 
entsprechenden Geo-Objekt als Platzhalter (in eckigen Klammern) angeführt werden:

.. image:: img/queries9.png

Unter ``Name / Bezeichnung des Hotlinks`` kann eingetragen werden, mit welchem Text der Hotlink in der 
Tabelle angezeigt wird.

``1:n`` gibt an, ob der Link für alle Zeilen einer Tabelle aufgerufen werden kann. Dabei kann auch ein 
Trennzeichen angegeben werden, mit dem die einzelnen Werte in der URL getrennt werden.

Weitere Spalten-Typen sind beispielsweise:

* **Expression:**  
  Hier kann ein *Ausdruck* bestehend aus (mehreren) Feldern und freiem Text angegeben werden.  
  Die Platzhalter für die Felder werden wieder in eckigen Klammern angegeben, z.B.: ``Fläche: [THE_AREA_FIELD]m²``.  
  Zusätzlich können bei Expression auch Funktionen zum Berechnen und Formatieren verwendet werden (siehe unten).

* **ImageExpression:**  
  Wie Hotlink, nur muss die Ziel-URL eine Bilddatei sein. Das Bild wird in der Ergebnistabelle 
  angezeigt. Die Größe kann eingestellt werden.

* **EmailAddress, PhoneNumber:**  
  Das Ergebnis wird als anklickbare E-Mail-Adresse oder Telefonnummer in der Tabelle dargestellt.

* **DateTime:**  
  Das Ergebnis wird als Datum dargestellt. Unter Definition kann dabei eingestellt 
  werden, wie das Datum formatiert werden soll.


Funktionen innerhalb von Expressions
------------------------------------

Bei Tabellenspalten vom Typ *Expression* können innerhalb des Ausdrucks neben den oben angeführten Platzhaltern für Felder in eckigen Klammern 
auch Funktionen eingefügt werden. Diese dienen für spezielle Berechnungen und Formatierungen des Feldes.

Funktionen beginnen immer mit ``$`` gefolgt vom Funktionsnamen. Das Argument wird der Funktion in Klammern übergeben, z.B. ``$eval(42*42)``, 
Attribute aus dem aktuellen Objekt werden der Funktion wieder als Platzhalter in eckigen Klammern übergeben, z.B. ``$eval([THE_AREA_FIELD]*42)``.

Folgende Funktionen stehen zur Verfügung:

* ``$eval()``: Berechnet einen mathematischen Ausdruck (Addition, Subtraktion, Multiplikation, Division), z.B. ``$eval(11+1)``, ``$eval([AREA]*[COST])``

* ``$sin()``, ``$cos()``, ``$tan()``, ``$asin()``, ``$acos()``, ``$atan()``: Winkelfunktionen. Die Berechnung und das Ergebnis beziehen sich immer auf das Bogenmaß. 
  Für Umrechnungen kann die Funktion ``$pi()`` verwendet werden, z.B. ``$sin(45.0*$pi()/180.0)``

* ``$round0()`` ... ``$round5()``: Rundet den übergebenen Wert. Die Zahl gibt die Nummer der Nachkommastellen an, z.B. ``$round0(100.123)``, ``$round2([AREA])``

* ``$n0()`` ... ``$n5()``: Wandelt eine Zahl ins *Standard Numeric Format* um. Dieses Format fügt beispielsweise Tausender-Punkte in eine Zahl ein (1000 => 1.000). 
  Die Zahl gibt die Nummer der Nachkommastellen an. Diese Funktion kann also auch als Alternative zu ``$round`` verwendet werden.

* ``$n0_de()`` ... ``$n5_de()``: Mit der Funktion ``$n()`` erfolgt die Darstellung in der aktuellen ``Culture`` des Servers. Ist die Sprache am Server Englisch, 
  werden die Ergebnisse eventuell nicht richtig formatiert (1000,123 => 1,000.123). Um das zu vermeiden, kann mit der ``$n0_de()`` die deutsche Darstellung erzwungen werden.

.. note::
   Die einzelnen Funktionen können auch verschachtelt werden:

   - ``$round2($eval([AREA]*[COST])) €``
   - ``$n2_de($eval([AREA]*[COST])) €``

.. note::
  ``$n0()`` bzw. ``$n0_de()`` sollte immer die äußerste Funktion sein. Verwendet man das Ergebnis zur Berechnung von weiteren Ergebnissen, 
  kann es zu Fehlern kommen, weil Berechnungsfunktionen mit Tausender-Punkten nicht umgehen können:

  - ``$eval($n0([AREA])*$n2([COST])) €`` => FALSCH
  - ``$eval($round0([AREA])*$round2([COST])) €`` => RICHTIG
  - ``$n2_de($eval($round0([AREA])*$round2([COST]))) €`` => RICHTIG

.. note::
  Macht man im Ausdruck einen syntaktischen Fehler (Parametrierfehler), wird das als Exception in der Ergebnisliste angezeigt (betrifft alle Zeilen in der Tabelle).

.. note::
  Entsteht ein Fehler bei der Rechnung des Wertes, weil in einem Feld ``COST`` beispielsweise kein gültiger Zahlenwert steht, ist das Ergebnis in der 
  Tabelle ``NaN`` (Not a Number). Das betrifft dann nur die entsprechenden Zeilen in der Tabelle.
