Parametrierung
==============

Der **Navigationsbaum** auf der linken Seite bildet die Struktur der **Endpoints, Queries und Views** ab.  
Durch einfaches Anklicken kann ein Element schnell ausgewählt und bearbeitet werden.

===============

Endpunkte
---------

Ein neuer **Endpoint** kann direkt in der **Sidebar** erstellt werden.  
Das oberste Eingabefeld ermöglicht die **Namensvergabe**, die durch **Enter** bestätigt wird.

.. image:: img/hello_world1.png
   :alt: Endpunkt erstellen
   :align: center

**Hinweis:**  
Die Namen von Endpunkten dürfen **nur Kleinbuchstaben, Zahlen und den Bindestrich (`-`)** enthalten.  
Sonderzeichen sollten vermieden werden, da die Namen später Teil der **Aufruf-URL** sind.

Ein Klick auf einen **Endpoint** öffnet den **Eigenschaften-Dialog**, in dem folgende Einstellungen vorgenommen werden können:

General
- **EndPoint Id** → Eindeutiger Name des Endpoints für den URL-Aufruf  
- **EndPoint Name** → Bezeichnung des Endpoints  
- **Description** → Optionale Beschreibung  

Connection
Je nach **Verbindungstyp** variiert die Konfiguration.

**Datenbank (Database)**
Beispiel für eine **SQL-Server-Verbindung**:

.. code-block:: text

   SQL:Server=db123.firma.at\instanz;Database=ssg;User Id=user1;Password=pwd1;

**API (REST-Schnittstelle)**
WebGIS API REST-Verbindung:

.. code-block:: text

   service=http://server123.at/api5test;user=username;pwd=12345

**GeoRss**
GeoRss-Dienst mit URL:

.. code-block:: text

   service=https//some.georss.com;user=username;pwd=12345

**GeoJson**
Ähnliche Vorgehensweise wie bei **GeoRss**.

**DataLinq**
Ein anderer **WebGIS DataLinq Dienst**, der ConnectionString ist die **URL der Anwendung**.

**PlainText**
Daten werden als **zeilenweise Texte** abgefragt. Kein ConnectionString erforderlich.

**TextFile**
Datenquelle sind **lose Textdateien** (`*.txt`, `*.log`, `*.csv`).  
Der ConnectionString definiert das **Verzeichnis**, z. B.:

.. code-block:: text

   C:\logs

Security
- **Berechtigungen für Nutzer und Rollen setzen** (siehe **Berechtigungen**).  

Info
- **Erstelldatum des Endpoints** wird hier angezeigt.

Styling
- **Open EndPoint CSS…** → Bearbeitung des CSS-Dokuments für alle zugehörigen **Views**.

Delete
- Löschen des Endpoints über die `Delete`-Funktion.

===============

Query (Abfragen)
----------------

Nach Auswahl eines **Endpoints** können für diesen **Abfragen** erstellt werden.  
Die Abfragen ermöglichen den Zugriff auf die zugehörigen **Datenbestände**.

Ein neuer **Query-Knoten** kann direkt in der **Sidebar** unterhalb des gewünschten Endpoints erstellt werden:

.. image:: img/hello_world3.png
   :alt: Abfrage erstellen
   :align: center

Klickt man auf die neue **Query**, erscheint im **Content-Bereich** ein **Editorfenster**, in dem die Abfrage formuliert werden kann.

Abfragearten
------------
Je nach **ConnectionType** unterscheidet sich die Syntax:

**Datenbank (SQL)**
Beispiel für eine SQL-Abfrage:

.. code-block:: sql

   SELECT
       [OBJECTID],
       [NAME]
   FROM projekt_gebaeude
   WHERE gebaeudeid = @GebaeudeId;

**REST-API (WebGIS, GeoJson, GeoRss)**
URL-Abfrage mit **Platzhaltern für Parameter**:

.. code-block:: text

   URL-PFAD/gebaeude?gebaeudeid={{GebaeudeId}}&...

**Dynamische Parameter (Optional)**  
SQL:

.. code-block:: sql

   SELECT
       [NAME],
       [FARBE]
   FROM projekt_gebaeude
   WHERE gebaeudeart = @GebaeudeArt
   #if dachfarbe
       AND FARBE = @dachfarbe
   #endif

**REST:**

.. code-block:: text

   URL-PFAD/gebaeude?gebaeudeart={{GebaeudeArt}}
   #if dachfarbe
       &farbe = @dachfarbe
   #endif

**Textfiles (bei Endpoint Typ TextFile)**
Beispiel für eine Datei-Abfrage:

.. code-block:: text

   my-log.csv

Optionale Parameter:

.. code-block:: text

   maxlines=10   # Maximale Anzahl der Zeilen
   from=bottom   # Von unten lesen

Falls ein **Filter** benötigt wird:

.. code-block:: text

   #if filter
       filter={{filter}}
   #endif

Test Parameter
- Hier können **Testparameter** für die Abfrage festgelegt und ausgeführt werden.

.. image:: img/ad3_3.png
   :alt: Testparameter setzen
   :align: center

**Hinweis:**  
Parameter sollten so gewählt werden, dass **Testabfragen jederzeit ausführbar** sind.

===============

Views (Ansichten)
-----------------

Zur **Darstellung** der Ergebnisse einer Abfrage können **eine oder mehrere Views** erstellt werden.

.. image:: img/hello_world7.png
   :alt: View erstellen
   :align: center

Ein Klick auf eine **View** öffnet den **Razor-Code**, der über das **Zahnrad-Symbol** zu den **Einstellungen** führt.

General
- **View Id** → Eindeutiger Name der View (wird in der URL verwendet)  
- **Name** → Bezeichnung der View  
- **Description** → Optionale Beschreibung  

Code (über Editor)
------------------
Views nutzen **HTML mit ASP.NET Razor Markup**.

.. image:: img/param_editor.png
   :alt: Razor Code Editor
   :align: center

===============

Berechtigung
------------

Für **Endpoints und Abfragen** können **Berechtigungen** gesetzt werden.  
Hierarchisch bedeutet: Wer auf einen **Endpoint keinen Zugriff** hat, kann auch dessen **Abfragen nicht ausführen**.

- Berechtigungen können für **einzelne Benutzer, Rollen oder Gruppen** gesetzt werden.
- **Token- und Portal-Authentifizierung** sind ebenfalls möglich.

Die Berechtigungsverwaltung erfolgt über das **„+“-Symbol** oder durch **Enter**.

- `"*"` → **Uneingeschränkter Zugriff für alle Benutzer**.

.. image:: img/param_berechtigung.png
   :alt: Berechtigungen setzen
   :align: center

===============

Stile (CSS)
-----------

CSS-Stile können **auf zwei Ebenen** definiert werden:

1. **Globale Styles für den gesamten Endpoint**.  
2. **Inline-Stile direkt in einer View** über `<style>`-Tags oder `style`-Attribute.