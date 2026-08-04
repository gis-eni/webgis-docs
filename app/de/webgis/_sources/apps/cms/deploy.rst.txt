CMS Veröffentlichen
===================

Um zu überprüfen, wie die bisherige Parametrierung im Viewer aussieht, kann das CMS einmal veröffentlicht werden. Dazu klickt man in der Sidebar auf ``Deploy``:

.. image:: img/image132.png

Es erscheint ein Dialog mit einer Schaltfläche, in der noch einmal der Name und gegebenenfalls das Datum der letzten Veröffentlichung angeführt werden.

Ein Klick auf diese Schaltfläche startet den Erstellungsprozess:

.. image:: img/image133.png

Dieser Vorgang kann je nach Größe des CMS Baumes einige Momente dauern. Ist das Erstellen erfolgreich, wird am Ende die Meldung *Succeeded* ausgegeben und der Dialog kann mit ``X`` geschlossen werden. 

Treten beim Veröffentlichen Warnungen auf, etwa weil es Darstellungsvarianten gibt, die auf gelöschte Layer-Schaltungen verweisen, bricht der Vorgang ab:

.. image:: img/image35.png

Ein CMS mit einer Warnung kann nicht mehr veröffentlicht werden. Zum Lösen des Konfliktes gibt es zwei Möglichkeiten:

1.	Aufgrund der ausgegebenen Meldung das Problem suchen und den entsprechenden Verweis löschen (hier eine Darstellungsvariante).
2.	Die Warnung automatisch löschen.

Zu 2:
Nach der Ausgabe von Warnungen das Fenster schließen. Im Deploy-Dialog erscheint jetzt der Hinweis, dass es beim letzten Veröffentlichen Warnungen gegeben hat:

.. image:: img/image36.png

Klickt man auf die rote Schaltfläche, wird versucht, die Warnungen automatisch zu beheben, was so viel bedeutet, dass die entsprechenden Verweise gelöscht werden. 

**Achtung:** Diesen Vorgang sollte man nur durchführen, wenn das Löschen der z.B. Layer-Schaltung beabsichtigt war. Ansonsten werden vielleicht unabsichtlich Verweise gelöscht:

.. image:: img/image37.png

Nach diesem Vorgang ist die rote Schaltfläche im Deploy-Dialog verschwunden und das CMS kann neu Veröffentlicht werden.