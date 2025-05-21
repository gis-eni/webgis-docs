Preise
======

Über das WebGIS Cloud Portal können *Ressourcen* angelegt werden, die zum Bereitstellen von WebGIS Karten
verwendet werden können.

Die *Ressourcen* werden innerhalb von *Subscriptions* organisiert. Eine *Subscription* ist dabei eine Abrechnungseinheit. 
Zur Zeit werden zwei Arten von *Subscriptions* angeboten:

* **Free:** Diese *Subscription* wird automatisch bei der Registrierung angelegt. Innerhalb dieser *Subscription* können freie Ressourcen angelegt werden.

* **Credits:** Für diese *Subscription* können *Credits* erworben werden, mit denen beliebige Ressourcen angelegt und betrieben werden können.

Subscription "Free"
-------------------

Diese *Subscription* steht jedem registrierten Account zur Verfügung. Damit lassen sich ausschließlich *Api Clients* erstellen.
*Api Clients* können dazu verwendet werden, um Karten auf einer beliebigen Homepage einzubinden. 
Programmierkenntnisse sind von Vorteil aber nicht notwendig. Karten können im *MapBuilder* erstellt und daraus ein HTML/Javascript *Snippet*
erstellt werden. Dieses *Snippet* kann in eine bestehende Homepage integriert werden.

+------------------------+------------+--------------------+--------------------+----------------+
| Resource               | Max Anzahl | Einrichtungsgebühr | Pay per use        | Flatrate/Monat |
+------------------------+------------+--------------------+--------------------+----------------+
| Api Client             |      2     |  0                 | 0                  | 0              |
+------------------------+------------+--------------------+--------------------+----------------+

Über die API können theoretisch alle Werkzuge in eine Karte integriert werden, die auch im *Karten Viewer* (siehe unten)
zur Verfügung stehen. Einige Werkzuge verursachen allerdings Processor Last in der WebGIS Cloud (z.B. Koordinaten abfragen und umwandeln).
Diese Werkzeuge stehen in der "Free" *Subscription* nicht oder nur eingeschränkt zur Verfügung. 

Die integrierte *Adressen Suche* kann in der "Free" *Subscription* verwendet werden. Die Performance wird allerdings 
auf maximal eine Abfrage pro Sekunde gedrosselt.

.. note::
   Pro Account kann nur eine "Free" *Subscription* angelegt werden.


Subscription "Credits"
----------------------

Bei dieser *Subscription* gibt es keine Einschränkungen im Bezug auf Resources und Performance-Drosselung.

Folgende resource Typen stehen zur Verfügung:

* **Api Client:** siehe oben, es können jedoch alle Werkzeuge verwendet werden.

* **Map Portal Pages:** Sind Seiten auf denen Karten(-sammlungen) angeboten werden können. Diese Seite werden in der WebGIS Cloud 
  gehostet. Eine eingene Infrastruktur ist noch notwendig. Innerhalb einer *Map Portal Page* können beliebig viele 
  Karten angelegt werden.

* **(WebGIS) CMS Accounts:** Möchten sie ihre eigenen Karten Dienste (WMS, WMTS, ArcGIS Server) in Karten einbinden, muss in einem 
  **CMS Account** definiert werden, welche Dienste eingebunden werden können. Das **CMS** regelt auch, welche Themen- 
  Ebenen schaltbar oder abfragbar sind. Erlaubt der Kartendienst das Bearbeiten von Geo-Daten (ArcGIS Server FeatureService),
  kann über das **CMS** festgelegt werden, welche Themen im Karten Viewer bearbeitet werden können und welche Sachdaten
  eingegeben werden müssen.

* **Map Portal Login Domains:** Um **Map Portal Pages** und Dienste aus einem **CMS Account** zu berechtigen sind
  **Domains** notwendig. Innerhalb einer **Domain** können beliebige Benutzer (Logins) definiert werden, für die diese 
  Resources sichtbar sind. Die **Domain** kann als Gruppe von Anwendern verstanden werden, die die gleichen Dienste nutzen dürfen.

* **MapServer Service Containers:** Wenn sie zwar Geodaten haben, aber keinen Kartenserver betreiben möchten, kann
  mit dieser Resource ein *Container* angelegt werden, in dem Kartendienste gehostet werden können. 
  Der dahinter liegenden MapServer ist ein *gView Server*. Damit lassen sich Dienste im WMS oder GeoServices REST (ArcGIS Server) exportieren, die dann über einen
  **CMS Account** in den Karten Viewer eingebunden werden können. 


  In der folgenden Liste werden die Preise in der Einheit *Credits* angeführt. Die Credits können *hier* erworben werden.
  Für kommerzielle Projekte gilt die Umrechnung 1 Credit = 1 Euro.
  Für Forschung, Weiterbildung und Projekte im öffentlichen Interesse können spezielle Tarife festgelegt werden. 

+------------------------------+--------------------+--------------------+------------------+
| Resource                     | Einrichtungsgebühr | Pay per use        | Flatrate/Monat * |
+------------------------------+--------------------+--------------------+------------------+
| Api Client                   |  50                | Proc + Traffic     | 50               |
+------------------------------+--------------------+--------------------+------------------+
| Map Portal Pages             |  250               | Proc + Traffic     | 50/Karte **      |
+------------------------------+--------------------+--------------------+------------------+
| (WebGIS) CMS Accounts        |  250               | Proc + Traffic     | 50               |
+------------------------------+--------------------+--------------------+------------------+
| Map Portal Login Domains     |  500               | 0                  | 0                |
+------------------------------+--------------------+--------------------+------------------+
| MapServer Service Containers |  500               | Proc + Traffic     | 50/Service       |
+------------------------------+--------------------+--------------------+------------------+

Die Abrechnung kann nach der tatsächlichen Nutzung oder über eine Flatrate erfolgen. Bei der Nutzung wird 
zwischen **Prozessor Zeit** (Proc) und **Netzwerk Traffic** (ausgehend/download) unterschieden. 
Beide Werte werden sekundengenau für jeden Request verrechnet.
Die Tarife für die beiden Kenngrößen sind:

+--------------------------------------+----------------------------------------------+
| Prozessor Zeit                       | Datendurchsatz                               |
+--------------------------------------+----------------------------------------------+
| 0.6/Stunde = 0.00017/Sekunde         | 0.1 / GB                                     |
+--------------------------------------+----------------------------------------------+         

\*) Die Flatrate gilt für eine moderate Nutzung von maximal 50.000 Requests.

\*\*) Flatrates gelten bei *Map Portal Pages* pro Karte in Produktion. Bei Karten, die nur zu Testzwecken dienen, wird
die Flatrate nur zu 20% berechnet.



