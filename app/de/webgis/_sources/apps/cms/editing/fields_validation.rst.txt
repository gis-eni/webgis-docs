Editierbare Felder: Validierung
===============================

.. image:: img/editing17.png

In diesem Abschnitt wird festgelegt, ob ein Feld vor dem Speichern eines Geo-Objektes auf bestimmte Kriterien überprüft werden soll.  
Wenn eines der Kriterien nicht erfüllt wird, erhält der Anwender eine Fehlermeldung, und das Objekt kann nicht gespeichert werden.

Folgende Kriterien sind möglich:

* **Erforderlich (required):** Ein Wert muss für dieses Feld eingegeben werden.
* **Minimale Länge:** Die Eingabe muss mindestens eine bestimmte Anzahl von Zeichen lang sein.
* **Regulärer Ausdruck:** Die Eingabe muss einem definierten regulären Ausdruck entsprechen.

Mit **regulären Ausdrücken** können auch komplexere Eingaben, wie z.B. eine gültige E-Mail-Adresse, überprüft werden.  
Wenn ein Fehler auftritt, erhält der Anwender eine Fehlermeldung. Sollte diese nicht der Standardfehlermeldung entsprechen,  
kann der Text unter ``Validierungsfehlermeldung`` angepasst werden.  
Bei der Verwendung von **regulären Ausdrücken** empfiehlt es sich, dem Anwender Beispiele für gültige Eingaben zu geben.

Clientseitige Validierung
-------------------------

Die Validierung erfolgt vor dem Speichern am Server und verhindert, dass falsche Eingaben in der Geo-Datenbank gespeichert werden.  
Eine bessere **User Experience** ergibt sich jedoch, wenn Eingaben bereits am Client (im Browser) während der Eingabe überprüft werden.  
Der Anwender sieht dann sofort, wenn eine Eingabe nicht dem gewünschten Ausdruck entspricht – und muss nicht erst auf "Speichern" klicken.

Um **clientseitige Validierung** zu aktivieren, muss die entsprechende Option aktiviert werden.