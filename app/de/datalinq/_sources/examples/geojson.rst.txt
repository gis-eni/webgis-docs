GeoJson Einbinden
=================

In diesem Beispiel wird erklärt, wie man einen GeoJson Dienst einbindet und tabellarisch darstellt.
Über einem Filter wird eine Auswahlliste angeboten. Diese wird auch von einem GeoJson Dienst befüllt.

Der entsprechende Dienst ist ein *gView MapServer* Dienst mit Adressen. Über eine Query werden die Werte
abgeholt. Für die Auswahlliste werden ebenfalls eine Query aus dem Dienst mit zusätzlichem DISTINCT verwendet.

.. note::
    Das Beispiel kann auch 1:1 für einen ArcGIS Server MapServer Dienst umgesetzt werden. Hier ändert sich
    nur der Pfad im ConnectionString des *EndPoints*.

Endpunkt
--------

Zuerst muss ein *EndPoint* mit dem Namen ``geojson-gview`` angelegt werden. 
Der Typ für den *EndPoint* ist ``GeoJson``. Als ConnectionString gibt man 
die Url zur gView Server GeoServices REST Schnittstelle an:

.. code-block::

   https://localhost/gview/geoservices/rest/services

Abfragen
--------

Wir möchten aus einem Dienst (bspw. ``test/basis``) die Adressen abfragen. Dazu legt man unter dem *EndPoint*
eine *Query* ``adressen`` an.

Als Query gibt man den Url Pfad, unter der im ConnectionString des *EndPoints* angeführten Url an.
Im Falle von gView (oder AGS) ermittelt man diesen Url Pfad am einfachsten über die REST Oberfläche des 
MapServers. Dort kann man in der Regel für den Dienst eine Abfrage über eine Benutzer Oberfläche erstellen 
und ausführen. Die Url Pfad kann dann aus der Adresszeile des Browsers kopiert werden.

.. code-block::

   /test/postgis/MapServer/0/query?where=plz%3D{{plz}}&
                                  geometry=&geometryType=&inSR=&relationParam=&objectIds=&time=0&distance=0&
                                  units=&outFields=*&returnGeometry=true&maxAllowableOffset=0&
                                  geometryPrecision=0&outSR=&returnIdsOnly=false&returnCountOnly=false&
                                  returnExtentOnly=false&orderByFields=&outStatistics=&groupByFieldsForStatistics=&
                                  returnZ=false&returnM=false&returnDistinctValues=false&
                                  returnTrueCurves=false&resultOffset=0&resultRecordCount=0&
                                  datumTransformation=&rangeValues=&quantizationParameters=&parameterValues=&
                                  historicMoment=0&
                                  layerId=0&f=geojson

.. note::
    Eine gView bzw. AGS Abfrage benötigt viele Parameter. Darum wird empfohlen, den Link über die 
    UI des MapServer zu erstellen.

Im Beispiel wurde auch noch ein Platzhalter für eine Abfrage definiert: ``where=plz%3D{{plz}}``

.. note::
    Das ``=`` must mit ``%3D`` Url-Codiert werden.

.. note:: 
    Als Ausgabe Format der Abfrage muss ``geojson`` angegeben werden. Das Standard JSON Format von gView bzw. AGS
    ist nicht GeoJson! ``&f=geojson``

Ruft man die Query (https://localhost/datalinq/select/geojson-gview@adressen?plz=3100&_pjson=true) auf,
kommt beispielsweise folgendes Ergebnis:

.. code-block::

    [
        {
            "oid": null,
            "_location": {
                "Latitude": 48.1877734994291,
                "Longitude": 15.627903754497671,
                "BBox": null,
                "BBoxValid": false
            },
            "gid": 8285,
            "ortsname": "St. Pölten",
            "strassenname": "...",
            "adrcd": 6192061,
            "subcd": 1,
            "adresse": "... 1, 3100 St.Pölten",
            "hnr": "1",
            "plz": 3100,
            "pgnr": 30201,
            "pgname": "St. Pölten",
            "okznr": 3158,
            "kgnr": 19544,
            "kgname": "St. Pölten"
        },...
    ]

Im nächten Schritt bauen wir über die MapServer Oberfläche eine Abfrage, die ein DISTINCT über 
die Postleitzahlen (plz) durchführt und tragen den Url Pfad in eine neue DataLinq Abfrage
``adressen-distinct-plz`` ein:

.. code-block::

   /test/postgis/MapServer/0/query?where=1%3D1&
                                  geometry=&geometryType=&
                                  inSR=&relationParam=&objectIds=&time=0&distance=0&
                                  units=&outFields=plz&returnGeometry=false&
                                  maxAllowableOffset=0&geometryPrecision=0&outSR=&
                                  returnIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&
                                  orderByFields=&outStatistics=&groupByFieldsForStatistics=&
                                  returnZ=false&returnM=false&returnDistinctValues=true&returnTrueCurves=false&
                                  resultOffset=0&resultRecordCount=0&datumTransformation=&rangeValues=&
                                  quantizationParameters=&parameterValues=&historicMoment=0&
                                  layerId=0&f=geojson

Diese Abfrage erfordert keine Parameter und liefert bem Aufruf (https://localhost/datalinq/select/geojson-gview@adressen-distinct-plz?_pjson=true)
folgendes:

.. code-block::

    [
        {
            "oid": null,
            "plz": 1300
        },
        {
            "oid": null,
            "plz": 2723
        },
        {
            "oid": null,
            "plz": 3925
        },...
    ]

View
----

Unter Query ``adressen`` bauen wir jetzt ein View ``table``:

.. code-block::

    @DLH.Table(Model.Records, max: 100)

Dieser sollte beim Aufruf die ersten 100 Adressen anzeigen.

.. note::
    Wir haben in der Abfrage einen Filter mit Platzhalter ``{{plz}}`` angegeben. 
    Darum kann es sein, dass die Tabelle *leer* ist. Die Parameter muss jetzt auch an den *View*
    übergeben werden. Das kann zum Test auch über die Einstellungen des *Views* erfolgen:

    Unter ``Test Url Parameters`` kann ``plz=3100`` eingetragen werden.

In nächsten Schritt erweitern wir den *View* noch um einen Filter, um nach Postleitenzahlen zu filtern.
Der Filter sollte eine Auswahlliste an Postleitzahlen anführen, der über die DataLinq Abfrage ``adresse-distinct-plz``
befüllt wird:

.. code-block::

    @DLH.FilterView(label: "Filter123", 
                filterParameters: new Dictionary<string, object>{
                    {"plz", new { displayname="Postleitzahl", 
                                  source="geojson-gview@adressen-distinct-plz", 
                                  valueField="plz", 
                                  nameField="plz" }
                    }
                })

    @DLH.Table(Model.Records, max: 100)

Führt man den *View* aus, sollte die Tabelle über die Postleitzahl filtern können. 