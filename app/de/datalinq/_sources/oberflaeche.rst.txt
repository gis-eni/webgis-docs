DataLinq.Code Oberfläche
========================

Die Benutzeroberfläche von **DataLinq.Code** bietet eine intuitive und leistungsstarke Umgebung zur Verwaltung von Endpunkten, Abfragen und Ansichten. Nachfolgend werden die einzelnen Bereiche und Funktionen im Detail erläutert.

.. image:: img/oberfl.png
   :alt: DataLinq.Code Oberfläche
   :align: center

===============

Startseite
----------

Beim Start von **DataLinq.Code** erscheinen die folgenden Elemente:

.. image:: img/oberfl_start.png
   :alt: Startseite von DataLinq.Code
   :align: center

- **Verify All Views**  
  - Überprüft alle vorhandenen **Views** auf **Syntaxfehler** und sicherheitsrelevante Keywords.  
  - Dieser Schritt wird besonders nach Updates empfohlen, um Fehler frühzeitig zu erkennen.  

===============

Sidebar
-------

Die **Sidebar** ermöglicht eine effiziente Navigation und Suche nach **Endpoints, Queries und Views**.

.. image:: img/oberfl_sidebar1.png
   :alt: Sidebar mit Suchfunktion
   :align: center

- Über das **Suchfeld** können gezielt Einträge gefunden werden.  
- Mit dem **Pfeil-nach-oben-Button** kann der aufgeklappte Baum vollständig geschlossen werden.  

.. image:: img/oberfl_sidebar3.png
   :alt: Sidebar aufgeklappt
   :align: center

Ein aufgeklappter Baum sieht beispielsweise so aus:

.. image:: img/oberfl_sidebar2.png
   :alt: Beispiel für einen aufgeklappten Baum
   :align: center

- Die **Füllung der Dreiecke** zeigt an, ob weitere untergeordnete Elemente existieren.  
- Dies erleichtert insbesondere die Suche nach **Views**.

===============

Erstellen eines neuen Endpoints, einer Query oder einer View
------------------------------------------------------------

- Ist die entsprechende Ebene geöffnet, kann ein neuer **Endpoint, eine Query oder eine View** erstellt werden.  
- Nach der **Eingabe des Namens** öffnet sich der zugehörige Code-Editor oder die Einstellungen.  

===============

Löschen eines Endpoints, einer Query oder einer View
----------------------------------------------------

- Zum Löschen eines **Endpoints, einer Query oder einer View** muss diese zunächst **geöffnet** werden.  
- Anschließend kann das Element über die **Einstellungen unten** mittels `Delete` entfernt werden.  

===============

Bezeichnung eines Endpoints, einer Query oder einer View kopieren
-----------------------------------------------------------------

- Beim **Überfahren eines Elements mit der Maus** erscheint rechts ein **Copy-Symbol**.  
- Durch einen Klick wird die Bezeichnung in die **Zwischenablage** kopiert.  

===============

Tabs
----

Die Editor-Umgebung unterstützt **mehrere geöffnete Dateien** gleichzeitig.

.. image:: img/oberfl_tabs1.png
   :alt: Tab-Ansicht mit Indikatoren für Änderungen
   :align: center

- Ein **roter Ring** signalisiert ungespeicherte Änderungen im aktuellen Tab.  
- Falls viele Tabs geöffnet sind, kann über das **Dreieck rechts** eine kompakte Navigationsansicht geöffnet werden:

.. image:: img/oberfl_tabs3.png
   :alt: Tab-Navigation
   :align: center

- Dort können alle geöffneten Dateien übersichtlich verwaltet und geschlossen werden.  
- Vor dem **Schließen nicht gespeicherter Dateien** wird eine Bestätigung angefordert:

.. image:: img/oberfl_tabs4.png
   :alt: Bestätigung beim Schließen ungespeicherter Dateien
   :align: center

===============

Toolbar
-------

Die **Toolbar** enthält mehrere wichtige Funktionen:

.. image:: img/oberfl_toolbar1.png
   :alt: Toolbar mit Funktionen
   :align: center

- **Check syntax** → Überprüfung auf Syntaxfehler  
- **Save Document** → Aktuelles Dokument speichern (`Strg+S`)  
- **Save all Docs** → Alle offenen Dateien speichern (`Strg+Shift+S`)  
- **Simple Preview** → Vorschau im Pop-up (`F5`)  
- **Preview in tab** → Vorschau im neuen Tab (`Strg+F5`)  
- **Color scheme** → Aktivierung/Deaktivierung des **Dark Mode**  

**Hinweis:**  
Vor dem Speichern wird automatisch überprüft, ob **Fehler in einer View** vorhanden sind. Falls Probleme erkannt werden, erscheinen entsprechende **Fehlermeldungen im unteren Bereich** des Editors.

===============

Toolbar (Rechts oben)
----------------------

.. image:: img/oberfl_toolbar2.png
   :alt: Toolbar oben rechts
   :align: center

- **Ausloggen** → Beendet die aktuelle Sitzung  
- **DataLinqHelper** → Zeigt eine Beschreibung der **DataLinqHelper-Funktionen**  

===============

Editor
------

Der Editor ermöglicht das **Bearbeiten von Code und Einstellungen**.

- Mithilfe der beiden Buttons unten rechts kann zwischen **Code und Einstellungen** umgeschaltet werden.

.. image:: img/oberfl_content1.png
   :alt: Editor-Ansicht mit Code- und Einstellungsmodus
   :align: center

**Weitere Details zur Konfiguration der Einstellungen** finden sich im Kapitel **Parametrierung**.
