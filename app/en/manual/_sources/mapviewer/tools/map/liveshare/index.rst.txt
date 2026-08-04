Live Share (Sharing a Map *Live*)
=================================

With this tool, maps can be shared in real time (*live*).
This makes sense when all participants have a WebGIS map open at the same time and are communicating with each other via phone/chat.

There are two different user groups in LiveShare sessions:

* **Session owner:** The user who starts the LiveShare session. This person can distribute links and/or session IDs and thereby invite other users. Before a new user can join the session, the session owner can confirm or decline access. The session owner can also end the session. There is exactly one owner per session.

* **Session participant:** Session participants receive a link or a session ID from the session owner. This allows them to join a session. There can be any number of participants per session.

The following are shared:

* Map view
* Position marker (each participant can place a marker on the map that is visible to all others, e.g. their own position)
* Presentation/topic layers
* Drawings (Redlining): All participants can see/edit/add to the session owner's drawings.

.. note::
   If the *session owner* distributes a link to the session, all participants generally join the session with the same map. This also means that all owners (depending on permissions) see the same topic layers.
   For LiveShare, however, it is not necessary for all participants to join the same map. It can happen that not all participants have access to the session owner's map (for example, it might only be
   accessible via an intranet). Participants can still join any WebGIS map accessible to them (e.g. at https://maps.webgiscloud.com) and take part in the *Live Share session* there
   with the corresponding session ID. In this case, only the view, position marker, and drawings (redlining) can be shared (no topic layers).

.. note::
   LiveShare is not only usable by different participants. Sometimes it also makes sense to create a session just for your own use. If you work with multiple screens, for example, you can open
   a map viewer on each screen (possibly with different map layers). To ensure both map viewers always show the same view, a "local" LiveShare session can be used for this.


.. toctree::
   :maxdepth: 3

   procedure
