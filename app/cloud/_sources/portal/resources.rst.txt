WebGIS Cloud Resourcen (Übersicht)
==================================

Unter *WebGIS Cloud Resourcen* können Software Komponenten verstanden werden, die für den Betrieb von *WebGIS*
benötigt werden. Welche *WebGIS Cloud Resourcen* für eine Anwendung notwendig, hängt von der Komplexität 
der Anforderungen ab:

1. Einfache Karte auf eigener Infrastruktur (Homepage), optional mit POIs ohne zusätzlicher Nutzung von eigenen Geodaten

2. Bereitstellen von Karten in *gehostetem* Karten Viewer auf einer *Karten Portalseite* in der WebGIS Cloud

3. Berechtigen von *gehosten* Karten für definierte Anwendergruppen
     
4. Einbinden von selbst *gehosteten* Kartendiensten (WMS, WMTS, AGS) zur Anzeige, zum Abfragen und zum Bearbeiten der Geo-Daten
   
5. Hosten von Kartendiensten


ad 1)
Für diese Anwendung ist ein **API Client** für die WebGIS Api anzulegen. Dieser kann von einer angegeben 
Internetseite auf die *Javascript* API von *WebGIS Cloud* zugreifen. Erfolgt der Zugriff nur auf freie Kartendienste (Basemaps) und 
Adresssuche (Österreich), kann diese Resource mit der *"Free" Subscription* erfolgen.

ad 2)
Für diese Anwendung muss als *Resource* eine **Map Portal Page** angelegt werden. In dieser können dann über die
*MapBuilder* Anwendung Karten angelegt werden.

ad 3)
Sollten nur definierte Anwendergruppen auf die Karten eine *Map Portal Page* zugreifen ist als *Resource* eine
*Map Portal Login Domain* anzulegen. Unter dieser *Domain* können wieder beliebige Logins angelegt werden,
mit denen sich Anwender auf der *Map Portal Page* anmelden können. Alle Logins für diese Domain erhalten als 
Endung den Domainnamen mit vorangestelltem ``@`` Zeichen. Ein Domain Login kann somit die Form einer E-Mail 
Adresse haben, wobei der Domainname die Endung der E-Mail Adresse ist.
Neben *Map Portal Pages* lassen sich mit einer *Domain* auch **(WebGIS) CMS Accounts** berechtigen (siehe 4).

ad 4)
Zum Einbinden von eigenen Kartendiensten (WMS, WMTS, AGS) ist als *Resource* ein **(WebGIS) CMS Account** anzulegen.
Über diesen wird definiert, welche Dienste für WebGIS Karten zur Verfügung stehen. Im **(WebGIS) CMS Account**
kann zusätzlich genau definiert werden:

* Welche Themen vom Anwender sichtbar bzw. unsichtbar geschalten werden können
* Welche Themen Abgefragt werden können
* Welche Themen bearbeitet werden können
* Darstellungsfilter
* etc.

Müssen die Dienste nur für einen definierten Anwenderkreis zugänglich sein, ist hier als *Resource* ebenfalls ein
**Map Portal Login Domain** notwendig.

ad 5)
Steht kein eigener Kartenserver zu bereitstellen der eigenen Geodaten zur Verfügung, können über die 
**WebGIS Cloud** Dienste gehostet werden. Diese können dann in beliebige GIS-Anwendungen bzw. über einen 
**(WebIGS) CMS Account** in die **WebGIS Cloud** eingebunden werden, sowohl für gehostete Karten als
auch für **WebGIS API Client** Karten auf der eigenen Infrastruktur. 


  