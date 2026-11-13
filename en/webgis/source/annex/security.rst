.. _annex-security:

Security Measures for the WebGIS Portal
=======================================

This chapter is intended for **administrators and operators**. It describes which protection mechanisms *WebGIS* has built in,
which keys in ``api.config``, ``portal.config`` and ``settings.config`` (CMS) adjust them, and which settings are recommended for an
installation on the **internet** or in an **intranet**.
Instructions for the first steps after the installation (changing default passwords, disabling self-registration and login) can be found under
:doc:`Security Measures (Hardening) </config/hardening/index>`.

At the end of the chapter, the table :ref:`annex-security-keys` gives an overview of **all** security-relevant keys with
risk level and recommendation.

.. _annex-security-principles:

Basic principles
----------------

- **Strong, individual passwords.** Default passwords such as ``admin123`` or ``webgisauthor`` are particularly vulnerable
  to brute-force attacks, in which programs automatically try millions of passwords. A password like
  ``admin123`` is cracked within seconds, whereas a password of at least 12 characters (better 16+) made of upper and lower case letters,
  digits and special characters, unrelated to names or dictionary words, takes years. Every account should have its own
  password; a **password manager** helps to generate and store them. Where possible, two-factor authentication should be used
  (see :ref:`annex-security-mfa`).
  More on this: `OWASP Authentication Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>`_
- **HTTPS in the intranet, too.** An intranet is not secure by default: employee devices can be infected,
  passwords and session information can be read or manipulated in the network, and modern browsers increasingly block
  unencrypted connections. The *WebGIS Portal* should therefore always be operated via **HTTPS**.
  More on this: `Transport Layer Security Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>`_
- **Restrict the administration.** Access to the administration interfaces (CMS, subscriber login of the API)
  should be limited to a specific group of people or to the internal network. In public
  instances the login should be disabled completely (see :ref:`annex-security-subscriber-login`).
- **Use browser protection mechanisms.** Security headers such as ``Strict-Transport-Security (HSTS)`` and
  ``Content-Security-Policy (CSP)`` are enabled on the web server or reverse proxy.
- **Update regularly.** Both *WebGIS* and servers, databases and third-party components.
- **Monitor logins.** Who logged in and when is logged. Frequent failed logins or
  unusual access to the administration can indicate an attack.
- **Know the attack scenarios.** Intranet applications, too, are affected by man-in-the-middle attacks, session hijacking or
  cross-site scripting (XSS). More on this: `OWASP Top 10 Security Risks <https://owasp.org/www-project-top-ten/>`_

.. note::

   The following sections describe the behavior with **default values**. Most protection mechanisms are active by
   default. Settings that weaken a protection are marked as **compatibility opt-out**
   in the table :ref:`annex-security-keys`.

.. _annex-security-subscriber-login:

Subscriber login and subscriber database
----------------------------------------

Map authors and administrators (*subscribers*) log in via ``/Subscribers/Login`` of the WebGIS API.
Subscribers are stored in a **subscriber database** (SQL database or file system), which is specified with the same value
``subscriber-db-connectionstring`` in ``api.config`` and ``portal.config``
(:ref:`api.config <api-config-subscriber-db>`, :ref:`portal.config <portal-config-subscriber-db>`).
Access to the database or directory should be limited to what is necessary (dedicated
database user with minimal rights, file system permissions only for the application user).

Passwords are hashed with **PBKDF2-SHA256**; older hashes are converted automatically at the next successful login.
Login error messages are kept generic and protected against guessing user names;
logins are logged.

Two keys control whether the subscriber login is available at all (without an entry, both are ``false``):

- ``allow-subscriber-login`` (:ref:`api.config <api-config-subscriber-registration>`,
  :ref:`portal.config <portal-config-advanced-security>`): If the value is ``false``, no login is possible. In
  **internet instances** it should be ``false`` in **both** files, so that no configuration from outside is possible even with a copied
  configuration. The configuration is then done in an internal instance that shares the storage.
- ``allow-register-new-subscribers`` (:ref:`api.config <api-config-subscriber-registration>`): Allows the
  self-registration of new subscribers. It may only be ``true`` **during the installation** to create the first
  administrator, and **never on the internet**. Further accounts are created by the administrator afterwards.

For installations on the internet, if a login is required, the login via an identity provider
(OpenID Connect) is the recommended variant.

.. _annex-security-password:

Password rules
~~~~~~~~~~~~~~

When a password is created or changed, the following applies (:ref:`details <api-config-security-password-rules>`):

- Minimum length ``password-min-length`` (default ``12``).
- The password must not be in a built-in list of common passwords. Optionally, this list can be extended with
  ``password-blocklist-file`` (e.g. with lists of compromised passwords).
- User name, first name, last name and e-mail address must not be contained; trivial patterns
  (``aaaaaaaaaaaa``, ``123456789012``) are rejected.
- Optionally, a number of character classes can be required with ``password-required-character-classes`` (``0`` - ``4``).
  The default is ``0``: a sufficient length in combination with the blocklist is more effective than
  composition rules.
- The default password ``webgisauthor`` of the initial installation can no longer be set; whoever logs in with it
  has to change it immediately.

The rules only apply to new or changed passwords; existing passwords remain valid. Every subscriber can change their own
password on the **Account** page.

.. _annex-security-mfa:

Two-factor authentication (2FA/TOTP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subscribers can set up two-factor authentication with an authenticator app (TOTP) and
recovery codes on the **Account** page. The key ``mfa-required`` (:ref:`details <api-config-security-mfa>`) determines
who has to use it: ``none`` (default, optional), ``admins`` or ``all``. Affected subscribers are guided through the setup at their next
login. ``mfa-issuer`` determines the name shown in the authenticator app.

- **Internet:** at least ``admins``, better ``all``.
- **Intranet:** ``admins`` recommended.
- With an SQL database, the **Setup** page of the API has to be run once after the update (table
  ``webgis_api_subscriber_mfa``). As long as the table is missing, the login works **without** a second factor
  (even with ``mfa-required``); a warning is logged.
- *Basic Authentication* and *DataLinq* still use only user name and password.
- The MFA secrets are encrypted with the crypto key of the API. If it changes, the
  two-factor authentication of the subscribers has to be reset (administrators can do this).

.. _annex-security-captcha-lockout:

Captcha, lockout and IP throttling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The login is protected against brute-force attacks (:ref:`details <api-config-security-subscriber-login>`):

- **Captcha:** After ``login-captcha-after-failed-attempts`` failed attempts (default ``3``, per user name or
  client IP) a captcha has to be solved. Every captcha can be used once and is only valid for
  ``captcha-lifetime-minutes`` (default ``5``).
- **Lockout per user name:** After ``login-lockout-after-failed-attempts`` failed attempts (default ``10``, ``0`` = no
  lockout) the user name is temporarily locked. The duration increases according to ``login-lockout-minutes`` (default
  ``1,5,15``, the last value is repeated). The counter is reset after ``login-failed-attempts-reset-minutes``
  (default ``60``) without further failed attempts.
- **Throttling per client IP:** From ``login-ip-max-failed-attempts`` failed attempts (default ``30``, ``0`` = off) within
  ``login-ip-window-minutes`` (default ``15``), every login from this IP requires a captcha and is delayed. An IP is deliberately
  not blocked hard (shared addresses, e.g. behind NAT).
- **Multiple instances:** By default the counters are kept in the memory of the respective instance. With load balancing they can be shared
  via **Redis**: ``login-throttle-redis-connectionstring``.
- **Password cache:** Successful password verifications for *Basic Authentication* and *DataLinq* are kept in memory for
  ``password-verification-cache-seconds`` (default ``300``), because hashing is intentionally expensive.
  ``0`` disables the cache.

.. important::

   The IP throttling requires that the API sees the **real client IP**. Behind a reverse proxy, the
   *X-Forwarded* headers must therefore be configured correctly (see :ref:`annex-security-proxy`).

.. _annex-security-sessions:

Sessions and cookies
--------------------

The login cookie of the API is ``HttpOnly`` and ``SameSite=Lax``. It contains a security stamp, so that changing
the password or the two-factor authentication invalidates other sessions
(:ref:`details <api-config-security-subscriber-login>`):

- ``cookie-secure``: ``auto`` (default) sets the *Secure* flag for HTTPS requests (incl. ``X-Forwarded-Proto``); local
  installations via ``http://localhost`` keep working. ``always`` always sets it (only use with HTTPS), ``never``
  never. ``never`` is not acceptable on the internet.
- ``session-max-lifetime-minutes``: maximum duration of a login regardless of activity (default ``480``,
  ``0`` = unlimited, not recommended).
- ``session-idle-timeout-minutes``: logout after inactivity (default ``0`` = off). On the internet, e.g. 30 to 60 minutes.

.. _annex-security-redirects:

Redirects after login
---------------------

The redirect target of the subscriber login is validated before an access token is appended (protection against
*open redirect*). The host of ``portal-url`` is always allowed; all other targets are rejected with ``400 Bad Request``.
If the portal is reachable under a different host name, these hosts can be allowed with
``subscriber-login-allowed-redirect-hosts`` (:ref:`details <api-config-subscriber-registration>`). Only
**your own** hosts should be entered.

.. _annex-security-cors:

Portal CORS
-----------

The ``hmac`` endpoint of the portal delivers credentials for the API to the logged-in user. It may only be called by the browser from
allowed pages; otherwise a malicious page could request keys for its visitors in the background. All other pages of the portal
can by default only be called with login (cookies) from the portal and the API themselves
(:ref:`details <portal-config-advanced-security>`, in depth: :ref:`annex-cors`):

- ``add-cors-origins-for-hmac``: third-party pages that may call the ``hmac`` endpoint (value ``~`` = all pages, for testing only).
- ``add-cors-origins-for-default``: additional origins that may call the other portal pages with login.
  Normally no entry is necessary. Value ``~`` = all pages (for testing only, warning in the log file).
- ``cors-default-allow-any-origin-without-credentials``: default ``false``. With ``true``, foreign origins may read public
  portal pages **without** login.

The wildcard ``~`` must not be used in production environments.

.. _annex-security-dynamic-content:

Dynamic content (SSRF protection)
---------------------------------

The ``DynamicContentProxy`` loads content (GeoRSS, GeoJSON, API queries) on behalf of the viewer. So that it cannot be abused for attacks
on internal systems (*server-side request forgery*), the following applies
(:ref:`details <api-config-dynamic-content>`):

- Only ``http`` and ``https`` without user information are allowed. Targets that point to loopback, private, link-local
  (e.g. cloud metadata) or other non-public addresses are rejected. This also applies to every
  redirect. Certificates are validated.
- The proxy only loads **signed URLs**. The API signs the URLs when a map is loaded.
- ``allow-hosts``: host names or patterns that may also point to internal addresses. Default empty. Only enter concrete internal
  sources, no broad patterns.
- ``allow-unsigned``: default ``false``. ``true`` also allows unsigned URLs (only for maps that are not loaded via the
  API, e.g. MapBuilder HTML or ``custom.js``).
- ``timeout-seconds`` (default ``20``), ``max-response-bytes`` (default 50 MB) and ``max-redirects`` (default ``5``)
  limit the download.

The search terms of the selection lists (VisFilter lookups) are validated as well: ``term-whitelist`` in the ``lookup`` section
(:ref:`details <api-config-lookup>`) determines which characters are allowed.

.. _annex-security-tls:

Outbound TLS connections
------------------------

Server certificates of outbound HTTPS connections (map services, ArcGIS, WMS, etc.) are validated. Internal services with
self-signed certificates or certificates of an internal CA should be connected by installing the CA in the
**certificate store of the server**. Only if this is not possible, the validation can be turned off
(man-in-the-middle risk). The key is:

- ``allow-untrusted-server-certificates`` in the ``security`` section of ``api.config``
  (:ref:`details <api-config-security-untrusted-certificates>`) and of ``portal.config``
  (:ref:`details <portal-config-security>`),
- ``allow_untrusted_server_certificates`` in the ``settings.config`` of the CMS (:ref:`details <cms-config-settings-security>`).

The default is ``false`` in each case. In practice, ``true`` should only be used for legacy services in trusted networks.

For the portal, the following also applies: ``use-local-url-scheme`` (``portal.config``, :ref:`details <portal-config-security>`) may only be
``true`` in local or offline environments, because the key exchange is then done unencrypted via HTTP.

.. _annex-security-csrf:

CSRF protection
---------------

The forms of the subscriber management of the API (login, registration, account, two-factor authentication) and further
write endpoints are protected against *cross-site request forgery* by **anti-forgery tokens**.
The key ``disable-anti-forgery`` (``security`` section of ``api.config``, :ref:`details <api-config-security>`)
turns this check off (default ``false``). This only makes sense in special cases, e.g. if the API serves exclusively as
a backend for another application or if a reverse proxy prevents the check. Do not use on the internet.

.. _annex-security-endpoints:

Secured endpoints
-----------------

Maintenance endpoints such as ``cache/clear`` are reachable **without authentication** by default, so that maintenance (e.g. after a
CMS deployment) works. As soon as credentials are configured in the ``security`` section of ``api.config`` or ``portal.config``,
the endpoint is only reachable with valid credentials
(:ref:`api.config <api-config-security>`, :ref:`portal.config <portal-config-security>`):

- ``secure-endpoint-url-password``: password that is passed as the query parameter ``pwd``.
- ``secure-endpoint-basicauth-username`` and ``secure-endpoint-basicauth-password``: credentials for HTTP Basic Authentication.

In publicly accessible instances these keys must be set; in the intranet it is recommended.

.. _annex-security-proxy:

Reverse proxy and client IP
---------------------------

If the API runs behind a reverse proxy, it sees the IP address of the proxy instead of that of the client by default.
Among other things, this impairs the IP throttling of the login (:ref:`details <api-config-middleware>`):

- ``use-x-forwarded-headers`` (``middleware`` section): takes over the *X-Forwarded* headers (default ``false``). Only enable behind a
  reverse proxy.
- ``x-forwarded-known-proxies`` and ``x-forwarded-known-networks``: The headers are only accepted from these trusted proxies
  (IP addresses or networks in CIDR notation), by default only from ``localhost``. Only enter the proxies that are
  actually used, no broad networks.
- ``use-x-forwarded-headers-logging``: logs the headers (for troubleshooting only).

.. _annex-security-keys:

Overview of all security-relevant keys
--------------------------------------

**Categories**

- **Compatibility opt-out:** A protection is active by default and can be turned off or relaxed for reasons of backward compatibility.
  Enabling the exception weakens security and should only be done when needed and with knowledge of the
  risk.
- **Feature enablement:** A function is only available after it has been enabled. Enabling it enlarges the attack surface.
- **Fine-tuning:** Values used to adjust a protection mechanism (times, limits, credentials, lists).

**Risk levels** (impact of an insecure value or of enabling the exception; default values are chosen to be secure)

- **High:** An attack is directly possible or a protection mechanism is completely bypassed (e.g. takeover of
  accounts, access to internal systems, eavesdropping on or manipulation of traffic).
- **Medium:** The protection is noticeably weakened; an attack needs additional prerequisites.
- **Low:** Minor impact; defense in depth.
- **Info:** No direct impact on security; operational or informational key.

Keys are written as ``section:key`` if they are located in a *section* of the configuration file (e.g.
``security:cookie-secure``); the link leads to the description in the respective configuration documentation. The
recommendations apply to standard installations. Where not stated otherwise, the recommendation equals the default value.

.. list-table::
   :widths: 20 9 12 7 26 26
   :header-rows: 1

   * - **Key**
     - **File**
     - **Category**
     - **Risk**
     - **Recommendation internet**
     - **Recommendation intranet**
   * - :ref:`allow-subscriber-login <api-config-subscriber-registration>`
     - api.config
     - Feature enablement
     - High
     - ``false``
     - ``true`` only if map authors/administrators have to log in (without an entry: ``false``)
   * - :ref:`allow-subscriber-login <portal-config-advanced-security>`
     - portal.config
     - Feature enablement
     - High
     - ``false``
     - ``true`` only if map authors/administrators have to log in (without an entry: ``false``)
   * - :ref:`allow-register-new-subscribers <api-config-subscriber-registration>`
     - api.config
     - Feature enablement
     - High
     - ``false`` (never enable)
     - ``true`` only during the installation (create the first administrator), then ``false``
   * - :ref:`subscriber-db-connectionstring <api-config-subscriber-db>`
     - api.config
     - Fine-tuning
     - Info
     - Restrict access to the database or directory; identical value in api.config and portal.config
     - Same as internet
   * - :ref:`subscriber-db-connectionstring <portal-config-subscriber-db>`
     - portal.config
     - Fine-tuning
     - Info
     - As in api.config
     - As in api.config
   * - :ref:`subscriber-login-allowed-redirect-hosts <api-config-subscriber-registration>`
     - api.config
     - Fine-tuning
     - Medium
     - Leave empty or enter only your own hosts
     - Same as internet
   * - :ref:`security:cookie-secure <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Medium
     - ``auto`` (assuming a correct proxy configuration) or ``always``; never ``never``
     - ``auto``; ``always`` with end-to-end HTTPS
   * - :ref:`security:session-max-lifetime-minutes <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Medium
     - ``480`` or shorter; not ``0``
     - ``480``
   * - :ref:`security:session-idle-timeout-minutes <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - e.g. ``30`` to ``60``
     - Optional
   * - :ref:`security:password-min-length <api-config-security-password-rules>`
     - api.config
     - Fine-tuning
     - Medium
     - ``12`` or more
     - ``12`` or more
   * - :ref:`security:password-required-character-classes <api-config-security-password-rules>`
     - api.config
     - Fine-tuning
     - Low
     - ``0`` (length and blocklist are more effective)
     - ``0``
   * - :ref:`security:password-blocklist-file <api-config-security-password-rules>`
     - api.config
     - Fine-tuning
     - Low
     - Recommended: list of compromised passwords
     - Optional
   * - :ref:`security:login-captcha-after-failed-attempts <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Medium
     - ``3`` or fewer
     - ``3``
   * - :ref:`security:login-lockout-after-failed-attempts <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Medium
     - ``10`` or fewer; not ``0``
     - ``10``
   * - :ref:`security:login-lockout-minutes <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - ``1,5,15`` or longer
     - ``1,5,15``
   * - :ref:`security:login-failed-attempts-reset-minutes <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - ``60``
     - ``60``
   * - :ref:`security:login-ip-max-failed-attempts <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - ``30`` or fewer; not ``0``
     - ``30``
   * - :ref:`security:login-ip-window-minutes <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - ``15``
     - ``15``
   * - :ref:`security:login-throttle-redis-connectionstring <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - Set with multiple instances (load balancing)
     - Only with multiple instances
   * - :ref:`security:captcha-lifetime-minutes <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - ``5``
     - ``5``
   * - :ref:`security:password-verification-cache-seconds <api-config-security-subscriber-login>`
     - api.config
     - Fine-tuning
     - Low
     - ``300`` or less
     - ``300``
   * - :ref:`security:mfa-required <api-config-security-mfa>`
     - api.config
     - Fine-tuning
     - Medium
     - ``admins`` or ``all``
     - ``admins`` recommended; ``none`` possible
   * - :ref:`security:mfa-issuer <api-config-security-mfa>`
     - api.config
     - Fine-tuning
     - Info
     - Name in the authenticator app
     - Name in the authenticator app
   * - :ref:`security:allow-untrusted-server-certificates <api-config-security-untrusted-certificates>`
     - api.config
     - Compatibility opt-out
     - High
     - ``false``; install the internal CA in the certificate store of the server
     - ``false``; ``true`` only for legacy services in trusted networks
   * - :ref:`security:allow-untrusted-server-certificates <portal-config-security>`
     - portal.config
     - Compatibility opt-out
     - High
     - ``false``; install the internal CA in the certificate store of the server
     - ``false``; ``true`` only for legacy services in trusted networks
   * - :ref:`allow_untrusted_server_certificates <cms-config-settings-security>`
     - settings.config (CMS)
     - Compatibility opt-out
     - High
     - ``false``; install the internal CA in the certificate store of the server
     - ``false``; ``true`` only for legacy services in trusted networks
   * - :ref:`security:disable-anti-forgery <api-config-security>`
     - api.config
     - Compatibility opt-out
     - High
     - ``false``
     - ``false``; ``true`` only in special cases (backend for another application, reverse proxy)
   * - :ref:`security:secure-endpoint-url-password <api-config-security>`
     - api.config
     - Fine-tuning
     - Medium
     - Set (strong password)
     - Setting recommended
   * - :ref:`security:secure-endpoint-basicauth-username <api-config-security>`
     - api.config
     - Fine-tuning
     - Medium
     - Set (together with the password)
     - Setting recommended
   * - :ref:`security:secure-endpoint-basicauth-password <api-config-security>`
     - api.config
     - Fine-tuning
     - Medium
     - Set (strong password)
     - Setting recommended
   * - :ref:`security:secure-endpoint-url-password <portal-config-security>`
     - portal.config
     - Fine-tuning
     - Medium
     - Set (strong password)
     - Setting recommended
   * - :ref:`security:secure-endpoint-basicauth-username <portal-config-security>`
     - portal.config
     - Fine-tuning
     - Medium
     - Set (together with the password)
     - Setting recommended
   * - :ref:`security:secure-endpoint-basicauth-password <portal-config-security>`
     - portal.config
     - Fine-tuning
     - Medium
     - Set (strong password)
     - Setting recommended
   * - :ref:`use-local-url-scheme <portal-config-security>`
     - portal.config
     - Compatibility opt-out
     - High
     - ``false``
     - ``false`` (use HTTPS in the intranet, too); ``true`` only in offline/test environments
   * - :ref:`dynamic-content:allow-hosts <api-config-dynamic-content>`
     - api.config
     - Compatibility opt-out
     - High
     - Empty (public targets only)
     - Only concrete internal host names, no broad patterns
   * - :ref:`dynamic-content:allow-unsigned <api-config-dynamic-content>`
     - api.config
     - Compatibility opt-out
     - High
     - ``false``
     - ``false``; ``true`` only if unsigned maps (MapBuilder HTML, ``custom.js``) are absolutely required
   * - :ref:`dynamic-content:timeout-seconds <api-config-dynamic-content>`
     - api.config
     - Fine-tuning
     - Low
     - ``20`` or less
     - ``20``
   * - :ref:`dynamic-content:max-response-bytes <api-config-dynamic-content>`
     - api.config
     - Fine-tuning
     - Low
     - ``52428800`` (50 MB) or less
     - ``52428800``
   * - :ref:`dynamic-content:max-redirects <api-config-dynamic-content>`
     - api.config
     - Fine-tuning
     - Low
     - ``5`` or fewer
     - ``5``
   * - :ref:`lookup:term-whitelist <api-config-lookup>`
     - api.config
     - Fine-tuning
     - Medium
     - Default; only extend by characters that are actually needed
     - Default
   * - :ref:`add-cors-origins-for-hmac <portal-config-advanced-security>`
     - portal.config
     - Fine-tuning
     - High
     - Only required third-party pages; never ``~``
     - Only required third-party pages; never ``~``
   * - :ref:`add-cors-origins-for-default <portal-config-advanced-security>`
     - portal.config
     - Fine-tuning
     - High
     - Empty; never ``~``
     - Empty; never ``~``
   * - :ref:`cors-default-allow-any-origin-without-credentials <portal-config-advanced-security>`
     - portal.config
     - Compatibility opt-out
     - Low
     - ``false``
     - ``false``
   * - :ref:`middleware:use-x-forwarded-headers <api-config-middleware>`
     - api.config
     - Fine-tuning
     - Medium
     - ``true`` only behind a reverse proxy
     - ``true`` only behind a reverse proxy
   * - :ref:`middleware:x-forwarded-known-proxies <api-config-middleware>`
     - api.config
     - Fine-tuning
     - Medium
     - Only the proxies actually used
     - Only the proxies actually used
   * - :ref:`middleware:x-forwarded-known-networks <api-config-middleware>`
     - api.config
     - Fine-tuning
     - Medium
     - Only the networks of the proxies used (CIDR), no broad networks
     - Only the networks of the proxies used (CIDR), no broad networks
   * - :ref:`middleware:use-x-forwarded-headers-logging <api-config-middleware>`
     - api.config
     - Fine-tuning
     - Info
     - ``false`` (for troubleshooting only)
     - ``false`` (for troubleshooting only)
