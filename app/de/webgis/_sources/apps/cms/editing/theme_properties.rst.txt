Editthema-Eigenschaften bearbeiten
==================================

Unter ``Eigenschaften`` lassen sich allgemeine Einstellungen für ein erstelltes Editthema festlegen:

.. image:: img/editing5.png

Die Eigenschaften werden in einem Dialog mit unterschiedlichen Kategorien dargestellt:

.. image:: img/editing8.png

Allgemein
---------

Hier wird festgelegt, ob ein Editthema im Bearbeiten-Werkzeug angezeigt werden soll. Damit das Thema 
im Kartenviewer verwendet werden kann, muss die Option ``Sichtbar`` aktiviert werden.  
Themen können jedoch auch über andere Methoden bearbeitet werden, z. B. über vorgefertigte App-Vorlagen für den 
*AppBuilder* (Collector), mit denen Daten erfasst werden können. Damit diese Werkzeuge das Editthema nutzen dürfen, 
muss die Option ``Über Edit-Server verfügbar`` gesetzt werden.

.. note:: 
   Aus Sicherheitsgründen sollten immer nur die notwendigen Optionen aktiviert werden. ``Edit-Server`` sollte nur dann 
   aktiviert werden, wenn tatsächlich ein Zugriff über eine App erfolgen soll. Falls ausschließlich über eine App 
   editiert wird, sollte ``Sichtbar`` nicht aktiviert werden, da diese Option sich auf den Kartenviewer bezieht.

Eine weitere wichtige Einstellung ist das ``räumliche Bezugssystem (EPSG-Code)``. Hier wird festgelegt, in welchem 
Koordinatensystem die Daten über den (AGS-) *FeatureServer* ausgetauscht werden. Es sollte das Koordinatensystem angegeben 
werden, in dem die Daten auch in der Datenbank gespeichert sind. Dies muss nicht mit dem Koordinatensystem der Karte 
übereinstimmen, in der die Daten editiert werden. Durch die Angabe des nativen Bezugssystems der Daten kann unnötiges 
Projizieren vermieden werden, was Rundungsungenauigkeiten reduzieren kann.

.. note::  
   Beim Bearbeiten sollte eine Projektion möglichst vermieden werden. Wenn beispielsweise nur Sachdaten geändert 
   und die Geometrie unverändert bleiben soll, könnte ein erneutes Speichern aufgrund von Ungenauigkeiten bei 
   der Projektion unerwünschte Änderungen verursachen.

Bezeichnung
-----------

Hier wird der Name des Editthemas angegeben und kann bei Bedarf geändert werden.

Rechte
------

.. image:: img/editing9.png

Für jedes Editthema kann über die *Rechte*-Einstellungen festgelegt werden, welche Aktionen erlaubt sind:

* **INSERT:** Neue Objekte dürfen angelegt werden.
* **UPDATE:** Bestehende Objekte dürfen bearbeitet werden.
* **DELETE:** Bestehende Objekte dürfen gelöscht werden.
* **Geometrie:** Neben den Sachdaten darf auch die Geometrie geändert werden. Dies kann nützlich sein, wenn 
  der Anwender nur Sachdaten bestehender Objekte bearbeiten darf, aber keine geometrischen Änderungen vornehmen soll.
* **Massenattributierung:** Ist diese Option aktiviert, kann der Anwender Sachdaten für alle ausgewählten Objekte gleichzeitig ändern.


Aktionen (Insert)
-----------------

.. image:: img/editing10.png

In diesem Bereich kann festgelegt werden, welche Möglichkeiten der Anwender hat, um ein erstelltes Geo-Objekt zu speichern.  
Standardmäßig besitzt ein Editthema in der Maske ``Neues Objekt erstellen`` im Kartenviewer neben der Attributeingabe  
folgende *Buttons*:

.. image:: img/editing11.png

Der Anwender kann auf ``Speichern`` klicken und danach entweder ein weiteres Objekt desselben Typs zeichnen oder die  
Eingabemaske verlassen. Nach erfolgreichem Speichern erscheint das Objekt in der Karte, und die  
Sachdaten-Eingabemaske wird auf den Standard zurückgesetzt. Für ein neues Objekt müssen alle Sachdaten erneut eingegeben  
werden – mit Ausnahme von *beständigen* (resistant) Feldern, die einmal gesetzt und beibehalten werden können.

Mit ``Speichern und Auswählen`` kann der Anwender das erstellte Objekt speichern und es anschließend direkt auswählen.  
Ohne diesen Button müsste das Objekt erst gespeichert und dann mit dem Abfrage-Werkzeug ausgewählt werden.  
Diese Aktion ist sinnvoll, wenn nach der Erstellung des Objekts beispielsweise eine Nachbarschaftsberechnung durchgeführt  
werden soll. Voraussetzung dafür ist, dass im Dienst eine Abfrage für dieses Thema existiert.

Die beiden Standardbuttons ``Speichern`` und ``Speichern und Auswählen`` können über die Optionen in diesem Dialog  
deaktiviert werden.

Zusätzliche Speicheroptionen  
----------------------------

Für spezielle Anforderungen gibt es weitere optionale Buttons zum Speichern von Geo-Objekten.  
Über den Dialog können bis zu fünf zusätzliche Buttons definiert werden. Damit ein optionaler Button angezeigt wird,  
müssen eine *Speicheraktion* und ein *Text* für den Button angegeben werden.

Folgende *Aktionen* stehen zur Verfügung:

* **Speichern (Save):** Entspricht dem Standardbutton ``Speichern``, kann jedoch mit einem alternativen Text versehen werden.
* **Speichern und Auswählen:** Entspricht dem Standardbutton ``Speichern und Auswählen``.
* **Speichern und Attribute behalten:** Die Attributwerte in der Sachdatenmaske bleiben nach dem Speichern erhalten.  
  Der Anwender kann so direkt ein weiteres Geo-Objekt erstellen, ohne alle Werte erneut eingeben zu müssen.
* **Speichern und mit letztem Vertex weiterzeichnen:** Nach dem Speichern wird der letzte Punkt des erstellten  
  Objekts als Startpunkt für das nächste Objekt übernommen.
* **Speichern, mit letztem Vertex weiterzeichnen und Attribute behalten:** Eine Kombination aus den beiden vorherigen Aktionen.

Anwendungsbeispiel  
------------------

Ein kurzes Beispiel, in dem die unterschiedlichen Speicheraktionen sinnvoll eingesetzt werden können:

Für die Planung von Leitungsobjekten sollte der Künettenverlauf im Kartenviewer erfasst werden (Linien-Objekt).  
Anhand der Linienlänge können die geschätzten Kosten der Grabungen berechnet werden. Diese Kosten hängen  
wesentlich vom Untergrund (z. B. Wiese, Asphalt) ab, weshalb ein entsprechendes Attribut *Untergrund* ausgewählt  
werden kann.  

Ändert sich der Untergrund innerhalb eines längeren Leitungsprojekts, muss der Planer an den Übergangspunkten  
die Linie speichern und den neuen *Abschnitt* am letzten Punkt des vorherigen Abschnitts fortsetzen.  
Da es sich dabei um ein neues Geo-Objekt handelt, müssten im Standardfall alle Sachdaten (Planungsnummer, Variante,  
Zuständiger, usw.) erneut eingegeben werden.  

Optimierung mit automatisierter Speicherung  
-------------------------------------------

Eine erhebliche Erleichterung stellt die Aktion **„Speichern, mit letztem Vertex weiterzeichnen und Attribute behalten“** dar.  
Mit einem Klick auf einen speziell konfigurierten Button könnte so ein neuer Abschnitt begonnen werden, wobei  
sämtliche Attribute – mit Ausnahme des *Untergrunds* – übernommen werden.  

Konfiguration der Aktionen (Insert)  
-----------------------------------

Die *Aktionen (Insert)* können folgendermaßen parametriert werden:

.. image:: img/editing12.png

1. Die beiden Standardbuttons werden ausgeblendet.  
2. Die Standard-Speicheraktion wird als optionaler Button mit neuem Text *„Speichern ⇒ neue Künette“* hinzugefügt.  
3. Die erste optionale Aktion (1) ermöglicht das direkte Weiterzeichnen mit beibehaltenen Attributen (*„Speichern ⇒ neuer Abschnitt“*).  

Im Kartenviewer erscheinen die Buttons für dieses Editthema dann folgendermaßen:

.. image:: img/editing13.png

==================

Erweiterte Eigenschaften  
------------------------

.. image:: img/editing14.png  

Jedes Editthema erhält intern eine eindeutige ID zur Identifikation. Falls das Editthema nicht nur im  
Kartenviewer, sondern auch in externen Anwendungen (z. B. Apps wie *Collector*) verwendet wird, muss diese  
ID im entsprechenden JavaScript-Code hinterlegt werden.  

Da eine sprechende ID oft wünschenswert ist, kann der Wert hier manuell geändert werden.  

.. note::  
   Wird die ID manuell geändert, muss sichergestellt werden, dass sie innerhalb des CMS **eindeutig** bleibt.  
   Das System überprüft die Eindeutigkeit **nicht**, sodass dies in der Verantwortung des CMS-Autors liegt.  
   Zudem sollte die ID nachträglich nicht mehr geändert werden, da eine Änderung in **allen angebundenen Apps**  
   nachgezogen werden müsste. Falls eine sprechende ID gewünscht ist, sollte diese direkt nach dem Erstellen  
   des Editthemas festgelegt werden.