Suchfelder 
----------

Suchfelder können für eine Abfrage optional parametriert werden. Enthält eine Abfrage keine Suchfelder, 
kann das Thema *nur* abgefragt werden (z.B. mit dem Identify-Werkzeug).
Werden Suchfelder definiert, scheint die Abfrage im *Karten Viewer* zusätzlich unter Detailsuche auf.

.. note::
   Nicht alle Dienst-Typen unterstützen das Suchen innerhalb eines Themas, z.B. WMS.

Zum Anlegen eines Suchfeldes muss in den Bereich ``Suchfelder`` gewechselt und auf ``Suchbegriff hinzufügen``
geklickt werden.

Im Dialog muss zuerst das Feld ausgewählt werden, in dem gesucht werden soll. 
Unter ``Abfrage Methode`` kann eingestellt werden, wie im entsprechenden Feld gesucht werden soll.
Mit ``Exact`` muss der Anwender beispielsweise den Suchbegriff exakt so eingaben, wie er in der 
Datenbank angeführt wird (Sinnvoll bei Ids, Zahlen). Meistens ist es anwenderfreundlicher,
wenn automatisch mit *Wildcards* gesucht wird. Mit ``EndingWildcard`` wird automatisch nach dem 
eingegeben Suchbegriff ein Wildcard (* oder %) angehängt. So werden alle Geo-Objekte gefunden,
bei denen das entsprechende Attribut mit dem eingegeben Suchbegriff beginnt. In der Auswahlliste 
werden noch weitere Optionen angeführt, die beispielsweise alle Leerzeichen durch *Wildcards* 
ersetzt (``SpacesToWildcard``, ``SpacesToWildcardWithEndingWildcard``, ...)

.. note::
   Damit die Suche performant ausgeführt wird, sollte darauf geachtet werden, das die Suchfelder 
   in der Datenbank entsprechend indiziert sind.

Abschließen muss noch ein Name angeben werden, der in der Suchmaske für dieses Feld angezeigt 
wird. Unter ``Url`` sollte eine für diese Abfrage eindeutige Ids für des Feld angeführt werden.
Ruft man den *Karten Viewer* auf, können so Parameter in der Url mitgegeben werden, die schon 
beim Start eine Abfrage ausführen. Die entsprechenden Parameter für die Suchfelder entsprechen 
dem hier eingetragenen (``...&query=adressen&adresse=hauptplatz...``). 

Schließt man den Dialog mit ``Übernehmen`` sollte der Suchbegriff in der Liste erscheinen.
Dort können die Eigenschaften auch noch nachträglich bearbeitet und die Reihenfolge der 
Suchbegriffe geändert werden. Über die Eigenschaften können auch noch weiter Eigenschaften wie 
Auswahlliste, Whitelists, usw. parametriert werden.