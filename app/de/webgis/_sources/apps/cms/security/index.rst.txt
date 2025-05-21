=========================
Berechtigungen (Security)
=========================

Standardmäßig sind alle Knoten des CMS Baumes für jeden Anwender (der Karten mit Diensten aus diesem CMS sehen kann) sichtbar.
Darf ein Anwender beispielsweise eine Karte nutzen, kann er theoretisch alle anderen Dienste aus dem CMS über den ``Dienste hinzufügen`` 
Button im **Karten Viewer** in die Karte einbinden (sofern dieser Button in der Karte angeboten wird).

Ist dies nicht erwünscht, können im CMS einzelnen Knoten des CMS Baumes berechtigt werden. Ist ein Knoten für einen Benutzer nicht berechtigt,
sind für diesen weder der Knoten, noch die darunter liegenden Knoten sichtbar. Ist beispielsweise der Knoten eines Kartendienstes berechtigt, 
gelten diese Berechtigungen auch für alle Abfragen und Editthemen dieses Dienstes.

.. note:: 
   Die Berechtigungen eines Knotens, werden an alle darunter liegenden Knoten vererbt.

Natürlich ist es dadurch auch möglich, dass beispielsweise ein Dienst für alle Anwender sichtbar und abfragbar, das Editieren von Themen
aber nur einem eingeschränkten Benutzerkreise vorbehalten ist. Und auch dabei können wieder einzelne Editierthemen unterschiedlich berechtigt sein.

Knoten berechtigen
==================

Jeder Knoten im CMS kann berechtigt werden. Dazu muss beim entsprechenden Knoten in der Liste auf 
das *Berechtigungs-Symbol* geklickt werden:

.. image:: img/security1.png

Dadurch wird der **Knoten-Security** Dialog für diesen Knoten geöffnet. Standardmäßig wird hier für einen
*ungeschützten* Knoten folgendes dargestellt:

.. image:: img/security2.png

Grundsätzlich können einzelnen Benutzer oder Benutzergruppen (Rollen) berechtigt werden. 
Der Benutzer *Jeder* ist hier ein spezieller Benutzer, dem alle echten User entsprechen. Ist für einen Knoten der Benutzer *Jeder*
berechtigt, können diesen Knoten alle Anwender sehen.

Je nach Konfiguration der WebGIS Instanz stehen für Benutzer und Gruppen unterschiedliche *Schematas* zur Verfügung. Ein *Schema*
beschreibt hier die Methode, mit der die Authentifizierung vorgenommen wird. Bei Windows-Authentifizierung lauten die entsprechenden 
*Schematas* beispielsweise ``nt-user::`` und ``nt-group::``. 

Auf welche WebGIS Instanz sich die Anmeldungs-Schematas beziehen, ist im Dialog unter dem Abschnitt ``WebGIS`` ersichtlich:

.. image:: img/security3.png

Klickt man auf den ``Aktualisieren`` -Button werden die Auswahllisten für die *Schematas* entsprechend neu befüllt.

Möchte man beispielsweise eine Gruppe für einen Knoten berechtigen, muss zuerst das richtige *Schema* gewählt und dann der Gruppenname eingetragen werden.
Je nach *Schema* werden nach Eingabe einiger Zeichen Vorschläge angezeigt. Klickt man danach auf den *Plus*-Button wird diese Gruppe der Liste für
diesen Knoten hinzugefügt.

.. image:: img/security4.png

In dieser Ansicht wurde auch die Default-Berechtigung für *Jeder* entfernt (die Checkbox ist nicht angehakt). Mit dem *Löschen* Symbol wird eine Berechtigung wieder entfernt.
Es können nur Berechtigung entfernt werden, die auch für diesen Knoten dezidiert gesetzt wurden. Vererbte Berechtigungen können nur überstimmt werden (durch an- oder abhaken).

Ist eine Berechtigung von einem Übergeordneten geerbt, wird der Pfad dieses Knoten angezeigt, in dem die eigentliche Berechtigung gesetzt wurde:

.. image:: img/security5.png

Möchte man eine vererbte Berechtigung für den aktuellen Knoten wieder zurück nehmen, geschieht diese durch abhaken der entsprechenden Berechtigung. Dadurch wird die entsprechende 
Berechtigung für diesen Knoten neu gesetzt und die Vererbung wird überschrieben:

.. image:: img/security6.png

Da die Berechtigung hier für diesen Knoten neu gesetzt wurde, kann diese wieder mit den *Löschen*-Symbol entfernt werden. Danach würde wieder die geerbte Berechtigung angezeigt werden:

.. image:: img/security7.png

Anzeige des Berechtigungs-Button
================================

Um im CMS die Übersicht zu bewahren, welche Knoten berechtigt sind, wird der Berechtigungs-Button in unterschiedlichen Farben dargestellt:

.. image:: img/security8.png

Folgende Farben sind möglich:

* **Grün** (default Farbe - wie alle anderen Buttons): Für diesen Knoten gibt es keine Berechtigung. Der Knoten ist für *Jeden* sichtbar.

* **Rot**: Für diesen Knoten gibt es eine Berechtigung, die mindestens einen Benutzer für diesen Knoten ausgrenzt.

* **Gelb**: Für diesen Knoten wurden Berechtigungen definiert, die allerdings keine Benutzer beschränken. Dieser Knoten ist immer noch für alle Anwender sichtbar.

Beim letzten Punkt stellt sich vielleicht die Frage, warum ein Knoten "ohne" Einschränkung berechtigt werden sollte. Das macht beispielsweise bei einem 
übergeordneten Knoten wie ``Dienste`` Sinn. Dort könnte die Berechtigung etwa folgendermaßen aussehen:

.. image:: img/security9.png

Hier wird zusätzlich zu ``Jeder`` noch der Benutzer ``subscriber::map-author`` hinzugefügt. Dieser ist beispielsweise der Karten-Autor, dieser sollte natürlich auch alle
Dienste sehen. Da alle Dienste unter diesem Knoten angelegt werden, wird dieses Recht auf alle Dienst-Knoten vererbt.

Möchte man jetzt einen speziellen Dienst-Knoten für eine Benutzergruppe, etwa ``nt-group::gis-edit-users``, berechtigen, wäre die Einstellung für diesen 
Knoten folgendermaßen:

.. image:: img/security10.png

Der Benutzer ``Jeder`` wird dezidiert abgehakt. Dafür wird für diesen Knoten die Windows Gruppe ``gis-edit-users`` berechtigt. 
Obwohl der Karten Author ``subscriber::map-author`` nicht in der Windows Gruppe ist, kann er den Dienst trotzdem sehen, da dieses Recht vom übergeordneten Knoten 
geerbt wird.

**Rote** Berechtigungs-Buttons gibt es zusätzlich noch in einer etwas *blasseren* Darstellung:

.. image:: img/security11.png

Diese Einfärbung bedeutet, dass es für die Knoten zwar Einschränkung gibt (nicht für jeden sichtbar), allerdings alle einschränkenden Rechte geerbt wurden.

Knoten exklusiv berechtigen
===========================

Vorsetzung: Build >= 3.21.502

Knoten können auch *exklusiv* berechtigt werden. Das bedeutet, dass man einem Benutzer oder einer Gruppe die exklusiven Rechte für diesen Knoten erteilt.
Alle anderen Berechtigung verlieren damit für diesen Knoten seine Gültigkeit.

Exklusive Berechtigungen sind in der Entwicklungsphase oder im Wartungsfall sinnvoll, wenn Knoten noch nicht produktiv erreichbar sein sollten. Dazu gibt man beispielsweise 
nur dem Administrator die Exklusivrechte auf den Knoten. Erst wenn alles fertig ist, werden die Exklusivrechte wieder entfernt.

Der Vorteil bei exklusiven Berechtigungen ist, dass hier sehr wohl bereits die endgültigen *normalen* Rechte gesetzt werden können. Diese werden beim 
Veröffentlichen des CMS allerdings als "*ignoriert*" gekennzeichnet, solange es auf den Knoten mindesten ein exklusives Recht gibt.

Im Prinzip kann jede Berechtigung, egal ob Gruppe oder einzelner Benutzer, als *exklusive* gekennzeichnet werden. Dazu muss dem User beim Einfügen die Endung ``.@@EXCLUSIVE`` (Groß- Kleinschreibung egal)
hinten angefügt werden, also zum Beispiel ``subscriber::my_admin_user.@@EXCLUSIVE@@``.

.. note::
   Es ist egal, ob der User (z.B. ``subscriber::my_admin_user``) bereits eingefügt wurde. Die bestehenden Einstellungen werden dadurch nicht geändert. Für Wartungen kann dieser User jederzeit 
   eingebaut und später wieder entfernt werden, ohne die bestehenden Einstellungen zu verändern.

Fügt man ein exklusives Recht ein, werden alle anderen Berechtigungen für diesen Knoten transparent dargestellt und das exklusive Recht hervorgehoben: 

.. image:: img/exclusive1.png

Hat ein Konten ein exklusives Recht, wird das auch in der Liste über ein schwarzes Symbol angezeigt:

.. image:: img/exclusive2.png

Gibt es in einem CMS exklusive Rechte, werden die Berechtigungen beim Veröffentlichen des CMS entsprechenden angepasst.
Dabei wird in der *Ausgabe-Console* am Ende angezeigt, wie bestehende Berechtigungen modifiziert werden:

.. image:: img/exclusive3.png

Löscht man zu einem späteren Zeitpunkt die exklusiven Berechtigungen wieder, werden die bereits gesetzten Berechtigungen wieder an diesem Knoten angewendet:

.. image:: img/exclusive4.png

Instanzrollen
=============

Beim den Berechtigungen im CMS gibt es eine spezielle Rolle mit dem Prefix ``instance::``.
Diese Berechtigungen beziehen sich auf eine bestimmte WebGIS Instanz.

Ein Anwendungsfall wäre etwa ein exklusives Rechte für einen Knoten auf eine WebGIS-Testinstanz zu berechtigen.

.. image:: img/instance1.png

Dieser Knoten wäre dann für andere Instanzen (Produktivsystem) nicht sichtbar. Damit kann man gewährleisten, dass für den gesamte 
Zeitraum der Entwicklung von neuen Kartenanwendungen diese Änderungen nicht im Produktivsystem angezeigt werden, auch wenn das CMS 
zwischenzeitlich für diese Instanz veröffentlicht wird.

Welche Instanzrollen von einer WebGIS Instanz möglich sind, wird bei der Eingabe durch Autovervollständigung angezeigt. Dabei muss natürlich
die Url zur entsprechenden WebGIS Portalseite angeben und mit ``Aktualisieren`` bestätigt werden:

.. image:: img/instance2.png

Welche Instanzen möglich sind, hängt von Betreiber der WebGIS Instanz hab. Er hat die Möglichkeit, über die ``api.config`` Datei, beliebige 
Instanzrollen anzugeben:

.. code::

   <add key="instance-roles" value="webgis5-test,webgis5-ausfall"/>

.. note::
   Instanzrollen sollten vom Betreiber zum  Beginn festgelegt werden und nachträglich maximal ergänzt werden. Ansonsten könnten eventuell 
   bereits für die Instanz vergebenen CMS Berechtigungen nicht mehr funktionieren.