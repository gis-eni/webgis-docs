Datei ``appsettings.json``
==============================

Die Datei ``appsettings.json`` enthält die Konfigurationseinstellungen für die Web-Anwendung.
Sie befindet sich im Hauptverzeichnis der Anwendung und wird beim Starten der Anwendung geladen.
Die Einstellungen in dieser Datei beziehen sich weniger auf die WebGIS Spezifischen Funktionen, 
sondern eher auf allgemeine Anwendungsparameter, wie z.B. Logging aus ASP.NET Core Ebene, 
Localization/Culture, etc.

Die Datei ist im JSON-Format strukturiert und enthält verschiedene Abschnitte, 
die unterschiedliche Konfigurationsparameter definieren. 
Hier sind einige der wichtigsten Abschnitte und ihre Funktionen:

.. code:: json

  {
    "Logging": {
      "LogLevel": {
        "Default": "Information",  /* default: Warning */
        "Microsoft": "Warning",
        "Microsoft.Hosting.Lifetime": "Information"
      }
    },
    "Localization": {
        "DefaultCulture": "de-AT"
    }
  }

- **Logging**: Dieser Abschnitt definiert die Einstellungen für das Logging der Anwendung aus ASP.NET Core Ebene, 
  einschließlich der Log-Level und der Log-Ausgabeziele.

- **Localization**: Hier werden die Einstellungen für die Lokalisierung der Anwendung festgelegt,
  einschließlich der Standardkultur, die für die Anwendung verwendet wird.

  Normalerweise wird die Applikation im der Culture des Betriebssystems gestartet, 
  aber hier kann eine explizite Culture definiert werden, die dann für die gesamte Anwendung gilt.
  Damit kann beispielsweise bestimmt werden, wie Datums- und Zeitangaben formatiert werden.

  .. note::

     Alle WebGIS Web-Anwendungen haben einen Endpoint ``/instance/_culture``, über den die aktuelle Culture 
     der Anwendung abgefragt werden kann.
     Dieser Endpoint gibt die aktuelle Culture zurück, die von der Anwendung verwendet wird, 
     und kann nützlich sein, um sicherzustellen, dass die Anwendung die erwartete Culture verwendet:

     .. code:: http

        GET /instance/_culture HTTP/1.1
        
     .. code:: json

        {
          "culture": "de-AT",
          "cultureDisplayName": "Deutsch (Österreich)",
          "cultureEnglishName": "German (Austria)",
          "cultureUI": "de-AT",
          "currentTimeString": "10.03.2026 07:42:40"
        }

     In diesem Beispiel zeigt die Antwort, dass die aktuelle Culture der Anwendung 
     "de-AT" (Deutsch - Österreich) ist, 
     und gibt auch die aktuelle Zeit im entsprechenden Format zurück.



