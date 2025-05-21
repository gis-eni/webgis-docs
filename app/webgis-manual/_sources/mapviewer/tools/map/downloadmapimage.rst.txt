Kartenbild herunterladen
========================

Mit diesem Werkzeug kann das aktuelle Kartenbild als JPG oder PNG Format heruntergeladen werden.
Das Kartenbild wird im Gegensatz zum *Drucken* nicht in ein Drucklayout eingebettet. Dafür besteht die Möglichkeit
zusätzlich zum Kartenbild ein *WorldFile* für dieses Bild zu erzeugen. Damit kann das Kartenbild in
GI Anwendungen (ArcGIS, QGIS, ...) geladen werden und wird dadurch an der korrekten geographischen Position 
eingefügt. Man spricht hier auch von einem georeferenziertem Bild.

Der Werkzeugdialog bietet folgende Möglichkeiten:

.. image:: img/downloadimage1.PNG

In den Eingabefeldern kann die *BoundingBox* (Ausdehnung) und die Größe des Bildes in Pixel angegeben werden.
Die Ausdehnung muss in Koordinaten in der Kartenprojektion angeführt werden.

Das Werkzeug bietet über die beiden *Buttons* folgende Optionen:

* **Aktuellen Kartenausschnitt übernehmen**: *BoundingBox* und *Größe* werden aus der aktuellen Ansicht übernommen. Ändert man den Ausschnitt, ändern sich auch die Werte für die geographische Ausdehnung und Größe.
* **Rechteck aufziehen**: Damit kann ein Fenster in der Karte aufgezogen werden. Geographische Ausdehnung und Größe werden daraus übernommen.

.. note::
   Ist das Werkzeug **Rechteck aufziehen** ausgewählt, kann der Kartenausschnitt nicht verschoben werden, weil bei 
   gedrückter Maustaste ein Rechteck aufgezogen wird. Möchte man den Kartenausschnitt verschieben, muss wieder zum
   Werkzeug **Aktuellen Kartenausschnitt übernehmen** gewechselt werden.

Neben geographischer Ausdehnung und Bildgröße können noch folgende Auswahlen getroffen werden:

* **Auflösung (DPI):** Hier kann die Qualität der Ausgabe bestimmt werden. Ein Wert von *96 DPI* entspricht dabei der Auflösung, die auch auf dem Bildschirm dargestellt wird.

.. note::
   Wählt man hier einen Wert größer als *96 DPI* wird das Bild größer als die oben angeführte Bildgröße in Pixel.
   Diese Größe bezieht sich auf 96 DPI. Ein größeres Bild benötigt natürlich auch mehr Speicherplatz. Trotzdem macht 
   es manchmal Sinn, hier eine höhere Auflösung zu wählen, wenn das Kartenbild beispielsweise in ein Dokument
   eingefügt wird, das später ausgedruckt wird. Auf einem Ausdruck wirkt ein Bild mit höherer Auflösung *schärfer*.

* **Bildformat:** Als Bildformat kann entweder JPG (Jpeg) oder PNG angegeben werden. JPG Dateien haben den Vorteil, dass sie in der Regel weniger Speicherplatz benötigen, wenn sich im Kartenbild Luftbilder befinden. Für Karten ohne Luftbilder liefern allerdings oft PNG Dateien schärfere und kleinere Ergebnisse.

* **Georeferenzieren:** Hier kann gewählt werden, ob zusätzlich zum Bild auch noch ein *WorldFile* angelegt werden sollte. Wählt man diese Option, ist das Ergebnis eine ZIP Datei, die sowohl Bilddatei (jpg, png) als auch das *WorldFile* (jgw, pgw) enthält. Ansonsten wird direkt die Bilddatei heruntergeladen.

.. note::
   Ein *WorldFile* ist eine Textdatei in der die Koordinaten der oberen linken Ecke des Kartenbildes sowie die
   Größe eine Pixels in X- und Y-Richtung stehen. Die Koordinaten beziehen sich auf das Kartenkoordinatensystem.

.. note::
   Das Kartenkoordinatensystem ist im Viewer am Desktop links unten ersichtlich (EPSG):

   .. image:: img/downloadimage2.png
   
   Fügt man ein georeferenziertes Kartenbild in eine GI Software ein, fragt diese in der Regel nach dem
   räumlichen Bezugsystem. Dabei muss das Kartenkoordinatensystem mit dem hier angezeigtem EPSG Code angegeben werden.


Mit ``Kartenbild herunterladen`` kann das Kartenbild anhand der Einstellungen heruntergeladen werden. 