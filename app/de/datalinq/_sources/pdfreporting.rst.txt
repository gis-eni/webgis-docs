PDF Reporting in DataLinq
=========================

Mit dem **PDF Reporting** in **DataLinq** können wiederverwendbare **Report-Templates** erstellt werden, die parametrisiert aufgerufen und als PDF gerendert werden.
Typische Anwendungsfälle sind unter anderem:

- Rechnungen
- Briefe
- Infoblätter
- projektspezifische Auswertungen

Funktionsumfang
===============

PDF-Templates können beim Aufruf mit Parametern befüllt werden. Dadurch lassen sich Inhalte dynamisch je Datensatz, Benutzerkontext oder Prozessschritt erzeugen.

Optional können Reports zusätzlich über Benutzereingaben ergänzt werden, beispielsweise über Eingabefelder für:

- Name
- Datum
- weitere fachliche Parameter

Die erzeugten PDF-Dokumente stehen direkt im Browser zum Download bereit.
Der Download kann entweder:

- aus der View des PDF-Templates selbst erfolgen, oder
- aus einer anderen View über Helper ausgelöst werden.

Erstellung von PDF-Templates
============================

Die Erstellung erfolgt wie bei anderen DataLinq-Views im **DataLinq Code Editor**.
Dabei können folgende Technologien kombiniert werden:

- HTML
- CSS
- JavaScript
- Razor
- spezielle **@PDF-Helper** für das PDF Reporting

So lassen sich Layout, Datenbindung und Ausgabeformat flexibel steuern, von einfachen Standarddokumenten bis hin zu komplexen, dynamischen Berichten.

Aktivierung des PDF Reporting Modes
===================================

Um ein PDF-Template zu erstellen, wird zuerst eine neue View angelegt.
Anschließend kann in den Einstellungen der View unter **PDF Reporting mode** die gewünschte Betriebsart aktiviert werden.

.. image:: img/pdf_reporting_settings.png
	:alt: Einstellungen für PDF Reporting mode
	:align: center

Im Bereich **PDF Reporting mode** stehen drei Checkboxen zur Verfügung:

1. **View report mode**

	Aktiviert den PDF-Report-Modus für die aktuelle View. Die View wird damit als PDF-Report behandelt.

2. **Browser Compatibility Notice**

	Zeigt Benutzern beim Aufruf einen Hinweis an, dass für ein optimales Rendering ein aktueller Browser verwendet werden soll.
	Der Hinweis muss vom Benutzer bestätigt werden.

3. **Report editing mode**

	Aktiviert den Bearbeitungsmodus für Reports. Damit können Administratoren zusätzlich zum DataLinq-Markup-Code Elemente per Drag and Drop positionieren.
	Detaillierte Informationen dazu folgen in einem weiteren Kapitel.

Erstellung eines PDF-Templates
==============================

Um einen Report mit einer oder mehreren Seiten zu erstellen, werden die vorgefertigten **@PDF-Helper** verwendet.

Zusätzliche Unterstützung zur Anwendung der Helper finden Sie in:

- der DataLinq-Hilfe
- der DataLinq-Sandbox

Ein einfacher Report mit genau einer Seite und ohne weitere Zusatzfunktionen kann wie folgt erstellt werden:

.. code-block:: text

	@PDF.BeginReport()

	    @PDF.NewPage()

	        <h1>Simple Report</h1>

	    @PDF.EndPage()

	@PDF.EndReport()

In diesem Beispiel wird zunächst ein Report gestartet und anschließend eine Seite mit einer Überschrift eingefügt.

.. image:: img/simple_report.png
	:alt: Einfacher PDF-Report mit einer Seite
	:align: center

Erklaerung der @PDF-Helper-Funktionen
======================================

@PDF.BeginReport()
------------------

Der Helper ``@PDF.BeginReport()`` markiert den Beginn eines Reports.

Folgende Parameter stehen zur Verfuegung:

- ``pageNumberOptions``:
	Einstellungen fuer die automatische Seitennummerierung.
	Damit kann festgelegt werden:

	- ob Seitennummern verwendet werden,
	- die Position (links, mittig, rechts),
	- die Art der Darstellung (z. B. ``1`` oder ``1/X``),
	- wie viele Seiten zu Beginn uebersprungen werden sollen (z. B. fuer ein Deckblatt).

	Beispiel:

	.. code-block:: csharp

		 pageNumberOptions: new Dictionary<string, object>() {
				 {"UsePageNumbers", true},
				 {"Position", 1},
				 {"Type", 0},
				 {"SkipPages", 0}
		 }

- ``quality``:
	Gibt die Ausgabequalitaet fuer den Download an.
	Moegliche Werte sind: ``PdfQuality.Preview``, ``PdfQuality.Low``, ``PdfQuality.Medium``, ``PdfQuality.High``, ``PdfQuality.Best``.

- ``download_button``:
	``bool``-Wert, der steuert, ob in der Template-View direkt ein Download-Button fuer den Benutzer angezeigt wird.

- ``fileName``:
	Dateiname der heruntergeladenen PDF-Datei.
	Standardwert ist ``dataLinqPdfReport.pdf``.


Komplettes Beispiel:

    .. code-block:: csharp

        @DLH.BeginPdfReport(pageNumberOptions: new Dictionary<string, object>(){
                        {"UsePageNumbers", true},
                        {"Position", 3},
                        {"Type", 0},
                        {"SkipPages", 0}},
                    download_button:true,
                    fileName: $"Example_{@Guid.NewGuid().ToString()}",
                    quality: PdfQuality.Medium
        )

@PDF.NewPage()
--------------

Der Helper ``@PDF.NewPage()`` wird verwendet, um eine neue Seite zu beginnen.

Folgende Parameter stehen zur Verfuegung:

- ``pageTemplateOptions``:
	Kann verwendet werden, wenn eine Seite zusaetzlich zum eigenen Content auf ein bestehendes Template zugreifen soll.
	Ein typischer Anwendungsfall ist ein zentrales Corporate-Design-Template mit Kopf- und Fusszeile, das auf allen Seiten wiederverwendet wird.
	Dadurch muss der gemeinsame Rahmen nicht auf jeder Seite erneut definiert werden.

	Beispiel:

	.. code-block:: csharp

		 pageTemplateOptions: new Dictionary<string, object>() {
				 {"UsePageTemplate", true},
				 {"TemplateId", "datalinq-guide@pdf@pdf-template"}
		 }

	- ``UsePageTemplate`` (bool): Aktiviert die Verwendung eines Templates.
	- ``TemplateId``: DataLinq-ID der zu verwendenden Template-View.

	.. note::

	   Bei Templates (z. B. Kopf- und Fusszeilen) sollten die enthaltenen Elemente immer **absolut positioniert** werden.
	   Andernfalls koennen sich die Template-Elemente verschieben, sobald in der Seite zusaetzlicher Content eingefuegt wird.

	   Beispiel:

	   .. code-block:: html

	      <h1 style="position: absolute; top:150px; left:150px;"></h1>

.. image:: img/template_example.png
	:alt: Beispiel fuer die Verwendung eines PDF-Seitentemplates
	:align: center

- ``landscape``:
	``true`` dreht die Seite ins Querformat.
	Standard ist ``false`` (Hochformat/Portrait).

.. image:: img/landscape_example.png
	:alt: Beispiel fuer Landscape-Ausrichtung
	:align: center

- ``paperSize``:
	Legt die Seitengroesse ueber das ``PaperSize``-Enum fest.
	Standard ist ``A4``.
	Moeglich sind ``A1`` bis ``A6``.
	Die Papiergroessen koennen mit ``landscape`` kombiniert werden und innerhalb eines Reports gemischt eingesetzt werden.

.. image:: img/papersize_example.png
	:alt: Beispiel fuer verschiedene Papiergroessen
	:align: center

- ``dynamicTableOptions``:
	Wird verwendet, um Inhalte aus Tabellen und flachen Hierarchien automatisch auf mehrere Seiten aufzuteilen,
	wenn der Platz auf der aktuellen Seite aufgrund dynamischer Tabelleninhalte nicht ausreicht.

	Beispiel:

	.. code-block:: csharp

		 dynamicTableOptions: new Dictionary<string, object>() {
				 {"Dynamic", true},
				 {"DynamicUseTemplate", true},
				 {"DefaultMarginTop", 220},
				 {"DefaultMarginBottom", 110},
				 {"RepeatHeader", true}
		 }

	- ``Dynamic`` (bool): Aktiviert die dynamische Seitenteilung.
	- ``DynamicUseTemplate`` (bool): Legt fest, ob bei dynamisch erzeugten Seiten ebenfalls ein Template verwendet wird.
	- ``DefaultMarginTop`` (int): Standardabstand oben fuer neu erzeugte Seiten, z. B. fuer Kopfbereiche aus dem Template.
		Dieser Wert wirkt nur fuer zusaetzlich generierte Seiten.
		Falls auf der ersten Seite ein oberer Mindestabstand benoetigt wird, kann dies mit
		``<div style="height:XYZ px"></div>`` umgesetzt werden.
	- ``DefaultMarginBottom`` (int): Mindestabstand unten, z. B. fuer Fussbereiche; wirkt auch auf der ersten Seite.
	- ``RepeatHeader`` (bool, Standard ``true``): Wenn auf ``false`` gesetzt, wird bei gesplitteten Tabellen auf Folgeseiten die Tabellenkopfzeile nicht wiederholt.

.. image:: img/dynamic_example.png
	:alt: Beispiel fuer automatisches Splitten auf mehrere Seiten
	:align: center

Hinweise zum Auto-Splitting
---------------------------

Beim Auto-Splitting werden Tabelleninhalte automatisch auf Folgeseiten verteilt, wenn der Platz auf einer Seite nicht ausreicht.

Wichtig fuer die Struktur:

- Tabellen, die automatisch gesplittet werden sollen, duerfen nicht in anderen Containern verschachtelt sein (zum Beispiel in einem ``div``).
- Diese Regel gilt auch fuer Tabellen, die ueber ``@DLH.IncludeView`` eingebunden werden.
- Beim Splitting werden ausschliesslich die Zeilen (Rows) einer Tabelle aufgeteilt.

Alle anderen HTML-Elemente werden als flache Hierarchie behandelt und nicht in Teilbereiche zerlegt.
Das bedeutet: Elemente wie ``div``, ``h1`` oder ``p`` werden immer als Ganzes betrachtet.
Wenn ein solches Element nicht mehr vollstaendig auf die aktuelle Seite passt, wird es als gesamter Block auf der naechsten Seite positioniert.

@PDF.EndPage()
--------------

Der Helper ``@PDF.EndPage()`` markiert das Ende einer PDF-Report-Seite.
Alles, was zwischen ``@PDF.NewPage()`` und ``@PDF.EndPage()`` definiert ist, wird auf dieser Seite gerendert.

Der Helper besitzt keine weiteren Parameter.

@PDF.EndReport()
----------------

Der Helper ``@PDF.EndReport()`` markiert das Ende des PDF-Reports.

Der Helper besitzt keine weiteren Parameter.

@PDF.NewDraggable() / @PDF.EndDraggable()
------------------------------------------

Die beiden Helper muessen immer in Kombination verwendet werden:

- ``@PDF.NewDraggable(...)`` oeffnet den verschiebbaren Bereich.
- ``@PDF.EndDraggable()`` schliesst den verschiebbaren Bereich.

Der Inhalt zwischen diesen beiden Helpern wird als zusammenhaengendes Element behandelt und kann per Drag and Drop verschoben werden,
wenn in den View-Einstellungen der **PDF Editing Mode** aktiviert ist.

Parameter von ``@PDF.NewDraggable(...)``:

- ``x``: X-Position des Elements.
- ``y``: Y-Position des Elements.

Hinweise zur Verwendung:

- Per Rechtsklick auf das verschiebbare Element werden die aktuellen ``x``- und ``y``-Werte in die Zwischenablage kopiert.
- Der Einsatz wird nur auf **fixen Seiten** empfohlen, also ohne Auto-Splitting.
	Bei dynamisch gesplitteten Seiten kann sich die Positionierung sonst unvorhersehbar verhalten.
- Auf einer PDF-Seite kann mit ``Strg+M`` ein Grid mit Mittellinien ein- und ausgeblendet werden.
- Wird waehrend des Verschiebens eines Elements ``Strg`` gedrueckt gehalten, kann auf die Mittellinien gesnappt werden.
- Sind die Mittellinien deaktiviert (``Strg+M``), koennen Elemente stattdessen an anderen Elementen einrasten (Snapping).

@PDF.PrintPdfButton(...)
------------------------

Der Helper ``@PDF.PrintPdfButton(string id, string buttonText = "Print", Dictionary<string, string> parameters = null)``
kann verwendet werden, um einen Report parametrisiert aus einer anderen View herunterzuladen.

Dabei wird ein Button erzeugt, der den Download direkt startet,
ohne dem Benutzer das eigentliche Template anzeigen zu muessen.

Parameter:

- ``id``: Eindeutige ID des Buttons.
- ``buttonText``: Beschriftung des Buttons (Standard: ``Print``).
- ``parameters``: Optionale Parameter als ``Dictionary<string, string>``, die beim Report-Aufruf mitgegeben werden.
