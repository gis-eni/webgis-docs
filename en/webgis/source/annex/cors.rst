.. _annex-cors:

CORS and the HMAC endpoint
==========================

If a WebGIS API application is embedded not in the portal itself but on a **third-party site** (a different server),
that site must be allowed in the ``portal.config`` if **logged-in users** access it (see :ref:`below <annex-cors-when>`). This chapter explains why this is necessary and how to configure it.

.. contents:: Contents of this page
   :local:
   :depth: 2

Background: same-origin policy and CORS
---------------------------------------

By default, a browser only allows JavaScript code to read responses from its **own origin**.
An *origin* consists of scheme, host and port, e.g. ``https://example.com`` (``https://example.com:8443`` and ``http://example.com`` are different origins).
This is called the *same-origin policy*.

If a page on ``https://example.com`` is nevertheless to read responses from another server (e.g. ``https://webgisserver.com``),
that server must explicitly allow this via *CORS* (*Cross-Origin Resource Sharing*).
To do so, the server returns the HTTP header ``Access-Control-Allow-Origin`` containing the allowed origin.
If this header is missing or the origin does not match, the browser discards the response and the call fails.

What is the HMAC endpoint for?
------------------------------

The portal provides the endpoint ``https://webgisserver.com/portal/hmac``.
It is used to fetch credentials (keys) for accessing the API on behalf of the **currently logged-in user**.
A WebGIS API application calls this endpoint to identify itself to the API as that user.

The problem: for such a call the browser automatically sends the user's portal login (cookie).
Without protection, **any web page** could call the ``hmac`` request in the background and retrieve the keys for the visitor:

1. A logged-in user visits a malicious page ``https://evil.example``.
2. Its JavaScript calls ``https://webgisserver.com/portal/hmac``.
3. Without CORS protection the page could read the response and would thus have access to the API on behalf of the user.

With the CORS policy, the portal only answers the ``hmac`` request with a matching ``Access-Control-Allow-Origin`` header
if the calling origin has been explicitly allowed. For all other pages the browser refuses to expose the response.

.. _annex-cors-when:

When is ``/hmac`` needed?
-------------------------

Calling ``/hmac`` from a third-party site is **only** necessary when **logged-in users** access an API application.
How the user obtains a cookie (or a comparable login to the portal) on the third-party site is **not handled by WebGIS**.

For **anonymous applications** it is better to assign a **client ID**:

* The client ID always refers to an **HTTP referer** that can be set on the API client
  (see :doc:`../apps/api/clients_anlegen`).
* If an API key or client ID is present, ``/hmac`` is usually **not** called.
  The user automatically inherits the rights of the client.
* In this case no entry in ``add-cors-origins-for-hmac`` is needed for the third-party site.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Use case
     - Recommended approach
   * - Anonymous application on a third-party site
     - API client with client ID and HTTP referer; no ``/hmac``, no CORS entry
   * - Logged-in users on a third-party site
     - ``/hmac`` on the portal; add the third-party site to ``add-cors-origins-for-hmac``

Configuration
-------------

The allowed origins are specified in the file ``_config/portal.config`` using the key ``add-cors-origins-for-hmac``
as a **comma-separated list** (description of the key: :doc:`../config/portal/index`, section ``Advanced Security``):

.. code-block:: xml

   <add key="add-cors-origins-for-hmac" value="https://localhost,https://example.com" />

Rules:

* List **all servers** on which a WebGIS API application is embedded.
* Each entry consists of scheme, host and, if necessary, port, **without a path and without a trailing slash**
  (``https://example.com`` or ``https://example.com:8443``).
* Scheme and port must match exactly: ``https://example.com`` allows neither ``http://example.com`` nor ``https://www.example.com``.
* Separate entries with commas, without spaces.
* Pages served from the same server as the portal (same origin) do not need an entry.
* After changing the ``portal.config`` the portal application must be restarted.

Example
-------

The portal runs at ``https://webgisserver.com/portal``.
A municipality operates its own website ``https://gemeinde.example.org/karte.html`` which embeds a WebGIS API application.
Development is additionally done locally (``https://localhost``).
The ``portal.config`` then looks like this:

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <configuration>
     <appSettings>
       <!-- ... other settings ... -->

       <!-- Allowed origins (CORS) for the HMAC endpoint -->
       <add key="add-cors-origins-for-hmac"
            value="https://gemeinde.example.org,https://localhost" />
     </appSettings>
   </configuration>

Result:

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Calling page
     - Result
   * - ``https://gemeinde.example.org/karte.html``
     - allowed (origin ``https://gemeinde.example.org`` is listed)
   * - ``https://localhost``
     - allowed
   * - ``http://gemeinde.example.org``
     - **blocked** (different scheme)
   * - ``https://www.gemeinde.example.org``
     - **blocked** (different host)
   * - ``https://evil.example``
     - **blocked** (not listed)

Troubleshooting
---------------

If an origin is not listed, the embedded application does not work as expected (e.g. no login to the API).
The browser developer tools (F12, console or network tab) then show a message similar to:

.. code-block:: text

   Access to fetch at 'https://webgisserver.com/portal/hmac' from origin
   'https://gemeinde.example.org' has been blocked by CORS policy: No
   'Access-Control-Allow-Origin' header is present on the requested resource.

In this case, add the origin named in the message (here ``https://gemeinde.example.org``) to ``add-cors-origins-for-hmac``.

Wildcard ``~``
--------------

The value ``~`` is a wildcard and allows **all** sites:

.. code-block:: xml

   <add key="add-cors-origins-for-hmac" value="~" />

.. danger::

   The wildcard completely removes the protection described above. It should only be used in exceptional cases for testing
   and **never in a production environment**.
