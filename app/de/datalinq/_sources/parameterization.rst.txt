==============
Parametrierung
==============

Der **Navigationsbaum** auf der linken Seite bildet die Struktur der **Endpoints, Queries und Views** ab.  
Durch einfaches Anklicken kann ein Element schnell ausgewählt und bearbeitet werden.

Endpunkt
========

Ein neuer **Endpoint** kann direkt in der **Sidebar** erstellt werden.  
Das oberste Eingabefeld ermöglicht die **Namensvergabe**, die durch **Enter** bestätigt wird.

.. image:: img/hello_world1.png
   :alt: Endpunkt erstellen
   :align: center

.. important::

   Die Namen von Endpunkten dürfen **nur Kleinbuchstaben, Zahlen und den Bindestrich (`-`)** enthalten.  
   Sonderzeichen sollten vermieden werden, da die Namen später Teil der **Aufruf-URL** sind.

Ein Klick auf einen **Endpoint** öffnet den **Eigenschaften-Dialog**, in dem folgende Einstellungen vorgenommen werden können:

Einstellungen
-------------

In der unteren Übersicht werden alle Sektionen des **Eigenschaften-Dialogs** mit den jeweiligen Feldern aufgelistet:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Feld
     - Beschreibung
   * - **General**
     - 
   * - ``EndPoint Id``
     - Eindeutiger Name des Endpoints für den URL-Aufruf
   * - ``Name``
     - Bezeichnung des Endpoints
   * - ``Description``
     - Optionale Beschreibung
   * - **Connection**
     -
   * - ``EndPoint Connection Type``
     - Folgende **Verbindungstypen** sind möglich:

       - Datenbank (Database)
       - API (REST-Schnittstelle)
       - GeoRss
       - GeoJson
       - DataLinq
       - PlainText
       - TextFile

   * - ``ConnectionString``
     - Je nach Verbindungstyp variiert die Konfiguration.

       - **Datenbank (Database)**: 

         Beispiel für eine ``SQL-Server`` Verbindung:

         .. code-block:: text

            SQL:Server=db123.firma.at\instanz;Database=ssg;User Id=user1;Password=pwd1;

       - **API (REST-Schnittstelle)**:
         
         Beispiel für eine ``WebGIS API REST`` Verbindung:

         .. code-block:: text

            service=http://server123.at/api5test;user=username;pwd=12345
       
       - **GeoRss**:
         
         .. code-block:: text

            service=https//some.georss.com;user=username;pwd=12345
       
       - **GeoJson**:
         
         Siehe **GeoRss**.
       
       - **DataLinq**:
         
         Ein anderer ``WebGIS DataLinq Dienst``, der ConnectionString ist die URL der Anwendung.
       
       - **PlainText**:
         
         Daten werden als **zeilenweise Texte** abgefragt, kann leer gelassen werden.
       
       - **TextFile**:
         
         Datenquellen sind lose Textdateien (`*.txt`, `*.log`, `*.csv`).
         
         .. code-block:: text

            C:\logs
         
         .. note::

            Hier wird das **Verzeichnis** angegeben, in welchem die Textdateien liegen. Es können mehrere Textdateien in einem Verzeichnis liegen, welche dann über die Abfrage angesprochen werden.

   * - **Security**
     - Berechtigungen für Nutzer und Rollen setzen (siehe **Berechtigungen**).
   * - **Info**
     -
   * - ``Created``
     - Erstelldatum des Endpoints
   * - **Styling**
     -
   * - ``Open EndPoint CSS Button``
     - Bearbeitung des CSS-Dokuments für alle zugehörigen **Views**
   * - **Scripting**
     - 
   * - ``Open EndPoint Javascript Button``
     - Bearbeitung des Script-Dokuments für alle zugehörigen **Views**
   * - **Delete**
     -
   * - ``Delete Button``
     - Löschen des Endpoints

Query (Abfragen)
================

Nach Auswahl eines **Endpoints** können für diesen **Abfragen** erstellt werden.  
Die Abfragen ermöglichen den Zugriff auf die zugehörigen **Datenbestände**.

Ein neuer **Query-Knoten** kann direkt in der **Sidebar** unterhalb des gewünschten Endpoints erstellt werden:

.. image:: img/hello_world3.png
   :alt: Abfrage erstellen
   :align: center

Klickt man auf die neue **Query**, erscheint im **Content-Bereich** ein **Editorfenster**, in dem die Abfrage formuliert werden kann.

Je nach **EndPoint Connection Type** unterscheidet sich die Möglichkeiten und die Syntax für die Abfrage.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - EndPoint Connection Type
     - Beispiel
   * - **Datenbank (SQL)**
     - Abfrage mit geseztem Filterwert

       - Mit Farbfilter: ``DATALINQ-URL-PFAD/select/endpoint@query?GebaeudeArt=Einfamilienhaus&Dachfarbe=rot``
       - Ohne Farbfilter: ``DATALINQ-URL-PFAD/select/endpoint@query?GebaeudeArt=Einfamilienhaus``

       SQL-Abfrage:

       .. code-block:: sql

          SELECT
              [NAME],
              [FARBE]
          FROM projekt_gebaeude
          WHERE gebaeudeart = @GebaeudeArt
          #if Dachfarbe
              AND FARBE = @Dachfarbe
          #endif
   * - **REST**
     - Auch hier können Urlparameter, welche mit der Query-URL mitübergeben wurden an die abzufragende REST API weitergeleitet werden.

       Beispiel: ``DATALINQ-URL-PFAD/select/endpoint@query?parameter1=wert1&parameter2=wert2``

       .. code-block:: text

          https://server123.at/api?p1=parameter1

          #if parameter2
              &p2 = @parameter2
          #endif

       Die zusammengesetzte URL der abzufragenden REST API wäre (falls ``parameter2`` gesetzt ist) ``https://server123.at/api?p1=parameter1&p2=parameter2``, ansonsten ``https://server123.at/api?p1=parameter1``

   * - **Textfiles (CSV)**
     - 
        .. hint::

           - Spalten in CSV Dateien müssen mit ``;`` getrennt werden.  
           - Falls eine Header-Zeile vorhanden ist, muss diese entfernt werden. Die einzelnen Spalten können mit `column1`, `column2`, `column3`, ... angesprochen werden.  

        .. warning::  

           Die Datei muss im **Verzeichnis** des Endpoints liegen. Dieses Verzeichnis wird im Verbindungstyp des Endpoints angegeben.  


        In der Abfrage können folgende Parameter definiert werden:  
        
        .. code-block:: text
           
           my-datafile.csv # Die Quelldatei, welche die Datensätze enthält
        
           maxlines=10     # Maximale Anzahl der Zeilen (optional)
           from=bottom     # Von unten lesen (optional)
           filter=xxx      # Filterbedingung (optional)

        Ein Filter kann verwendet werden, um nur die Datenzeilen zu extrahieren, welche den im Filter definierten Text enthalten (case-insensitive). Dies kann hilfreich sein, um große Datenmengen zu durchsuchen und nur relevante Informationen zu extrahieren.
        
        **Beispiel für eine URL mit Filter:**  
        
        In diesem Beispiel filtert die URL ``DATALINQ-URL-PFAD/select/dh-form@get?_pjson=true&GebaeudeArt=Einfamilienhaus`` nur die Datensätze, bei denen die jeweilige Zeile in der CSV Datei den Wert ``Einfamilienhaus`` enthält.
        
        Filter-Bedingung in der Abfrage:
        
        .. code-block:: text
        
           my-datafile.csv
        
           ...
        
           #if GebaeudeArt
              filter={{GebaeudeArt}}
           #endif 
        
        Dies stellt sicher, dass der Filter nur angewendet wird, wenn der Wert `GebaeudeArt` definiert ist. Andernfalls wird der Filter nicht angewendet, und alle Zeilen der Textdatei werden in die Abfrage einbezogen. 

Einstellungen
-------------

Zu den Einstellungen für die jeweilige Abfrage gelangt man über einen Klick auf das **Zahnrad-Symbol** in der rechten unteren Ecke des Editorfensters.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Feld
     - Beschreibung
   * - **Link**
     - 
   * - ``Route``
     - URL-Route für die Abfrage (``endpoint_id@query_id``)
   * - **General**
     -
   * - ``Query Id``
     - Eindeutiger Name der Abfrage (wird in der URL verwendet) 
   * - ``Name``
     - Bezeichnung der Abfrage
   * - ``Description``
     - Optionale Beschreibung
   * - **Debug**
     -
   * - ``Test Url Parameters``
     - Hier können **Testparameter** für die Abfrage festgelegt und ausgeführt werden.
     
       .. image:: img/ad3_3.png
          :alt: Testparameter setzen
          :align: center
       
       .. hint::
       
          Die Testparameter sollten so gewählt werden, dass **Testabfragen jederzeit ausführbar** sind.
   * - **Security**
     - Berechtigungen für Nutzer und Rollen setzen (siehe **Berechtigungen**).
   * - **Domains**
     -
   * - ``Domains``
     - Query-Domains werden verwendet, um kodierte Werte in einer Tabelle durch verständliche Namen zu ersetzen, indem eine Lookup-Tabelle genutzt wird, die die kodierten Werte und deren Übersetzungen enthält.
       
       - ``Destination Field``: Bezeichnung der Spalte, die die kodierten Werte enthält.
       - ``Query Id``: Lookup-Tabelle, die kodierte Werte und deren Übersetzungen enthält.
       - ``Value Field``: Spaltenname in der Lookup-Tabelle, der die kodierten Werte enthält.
       - ``Name Field``: Spaltenname in der Lookup-Tabelle, der die Übersetzungen enthält.

       Siehe auch :ref:`Queries mit Domain-Übersetzung <Anchor57>`.
   * - **Info**
     -
   * - ``Created``
     - Erstelldatum der Abfrage
   * - **Delete**
     -
   * - ``Delete Button``
     - Löschen des Endpoints

Views (Ansichten)
=================

Zur **Darstellung** der Ergebnisse einer Abfrage können **eine oder mehrere Views** erstellt werden.

.. image:: img/hello_world7.png
   :alt: View erstellen
   :align: center

Views nutzen **HTML mit ASP.NET Razor Markup**.

.. image:: img/param_editor.png
   :alt: Razor Code Editor
   :align: center

Einstellungen
-------------

Zu den Einstellungen für die jeweilige Abfrage gelangt man über einen Klick auf das **Zahnrad-Symbol** in der rechten unteren Ecke des Editorfensters.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Feld
     - Beschreibung
   * - **Link**
     - 
   * - ``Route``
     - URL-Route für die View (``endpoint_id@query_id@view_id``)
   * - **General**
     -
   * - ``View Id``
     - Eindeutiger Name der View (wird in der URL verwendet) 
   * - ``Name``
     - Bezeichnung der View
   * - ``Description``
     - Optionale Beschreibung
   * - **Debug**
     -
   * - ``Test Url Parameters``
     - Hier können **Testparameter** für die Abfrage festgelegt und ausgeführt werden.
     
       .. image:: img/ad3_3.png
          :alt: Testparameter setzen
          :align: center
       
       .. hint::
       
          Die Testparameter sollten so gewählt werden, dass **Testabfragen jederzeit ausführbar** sind.
   * - **JS Libraries**
     - Hier können die derzeit verfügbaren JS-Bibliotheken für die View hinzugefügt werden.
   * - **Info**
     -
   * - ``Created``
     - Erstelldatum der View
   * - ``Changed``
     - Änderungsdatum der View
   * - **Delete**
     -
   * - ``Delete Button``
     - Löschen des Endpoints

Berechtigungen
==============

Für **Endpoints und Abfragen** können in den Einstellungen Berechtigungen gesetzt werden, welche hierarchisch vererbt werden.

.. note::

  Hierarchisch bedeutet: Wer auf einen **Endpoint keinen Zugriff** hat, kann auch dessen **Abfragen nicht ausführen**.

- Berechtigungen können für **einzelne Benutzer, Rollen oder Gruppen** gesetzt werden.
- **Token- und Portal-Authentifizierung** sind ebenfalls möglich.

Die Berechtigungsverwaltung erfolgt über das **„+“-Symbol** oder durch **Enter**.

.. warning::

  Hier können auch Wildcards mittels der Zeichenfolge `"*"` vergeben werden. Diese Zeichenfolge bedeutet einen **uneingeschränkten Zugriff für alle Benutzer**.

.. image:: img/param_berechtigung.png
   :alt: Berechtigungen setzen
   :align: center


Stile (CSS)
===========

CSS-Stile können **auf zwei Ebenen** definiert werden:

1. **Globale Styles für den gesamten Endpoint**.  
2. **Inline-Stile direkt in einer View** über `<style>`-Tags oder `style`-Attribute.