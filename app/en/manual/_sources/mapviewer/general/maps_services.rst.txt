Maps and Services
==================

The map viewer displays the maps provided by the map author. A map usually combines topics for specific use cases.

Similar geodata is grouped into topics (*layers*), which can be shown and queried individually. Individual topic groups are in turn grouped into map services.

For a map, this results in the following hierarchy for geodata:


* **Topics:** (layers) group geo-objects of the same type together. One possible topic is, for example, *Parcels*, which consists of several geo-objects of the type parcel.
  Each has its own typical cartographic presentation (legend). Certain topics can be queried by clicking (the *Identify* tool) or offer a search option via attribute data.


* **(Map) services:** several layers can be combined into a service. For example, a service *Cadastre* could combine the topics parcels, usage sections, and usage symbols.


* **Maps:** a map, as shown in the map viewer, combines several services. For example, a map *Base* could combine background services for the town plan and aerial imagery, political boundaries, addresses, and the cadastre as services.


A map service can appear in different maps. In particular, the background services (town plan and aerial imagery) make sense in almost every map. In the map viewer, there is also the option
for the user to add any services to an existing map for the current session, via a ``Add services`` button.
