Editieren (Geo-Objekte Bearbeiten)
==================================

Neben dem Anzeigen von Geodaten können Daten auch erstellt oder bearbeitet werden. Im Kartenviewer gibt es dazu
ein eigenes Werkzeug (Bearbeiten, Editing) mit dem sowohl die Geometrie als auch die Sachdaten von Geo-Objekten
bearbeitet werden kann.

Voraussetzung ist ein (Karten-) Dienst, über den die Bearbeitung von Daten ermöglicht wird.
Kartendienste, die diese Voraussetzung erfüllen, sind beispielsweise ArcGIS Server FeatureServer Dienste.
Diese bieten die entsprechenden Methoden über eine REST Schnittstelle an. Dazu sind am ArcGIS Server bestimmte 
Einstellungen und Berechtigungen zu setzen, die in dieser Dokumentation nicht beschrieben werden. Hier wird davon 
ausgegangen, dass der gewählte Dienst alle notwendigen Voraussetzungen erfüllt.

.. note::
   Das Bearbeiten der Geodaten erfolgt ausschließlich über (Feature-) Dienste und nicht direkt in einer Datenbank.
   Da diverse Geodatenbanken oft mehr bieten als "flache" Tabellen, also oft auch komplexere Beziehungen
   und Versionierung, sollte schreibend immer über einen Dienst auf diese Datenbanken zugegriffen werden. 
   Der Dienst ist dann dafür verantwortlich, dass sämtliche Beziehungen beim Schreiben von Daten korrekt 
   behandelt werden. 

.. note::
   Wenn hier von ArcGIS Server Diensten gesprochen wird, sind eigentlich Dienste gemeint, die die 
   GeoServices REST Schnittstelle, die von ArcGIS Server eingeführt wurde, unterstützen. Diese (freie) Schnittstelle
   kann theoretisch auch von andern Kartenservern wie gView Server https://github.com/jugstalt/gview5 unterstützt werden.


Wenn man Editieren über einen ArcGIS Server Dienst über das CMS ermöglichen möchte, wird hier vorausgesetzt, 
dass der Anzeige- und Bearbeitungsdienst (MapServer/FeatureServer) identisch sind.

In diesem Tutorial wird von einem Dienst ausgegangen, der zur Planung von Stromleitungs-Projekten dienen sollte.
Im ArcGIS Server Dienst, befinden sich entsprechende Punkt-, Linien- und Flächenthemen. Die Beschreibung der Möglichkeiten
wird an einigen Ausgewählten Themen gezeigt.

.. toctree::
    :maxdepth: 2

    create_edittheme
    theme_properties
    fields
    fields_validation
    fields_autovalues
    fields_domains
    snapping 


    