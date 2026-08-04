Security Measures for the WebGIS Portal
==========================================

Password Security Tips
----------------------------

A secure password is the first step in protecting the *WebGIS Portal*. Here are some tips on how to create a strong password:

Default passwords such as ``admin123`` or ``webgisauthor`` are **particularly vulnerable to brute-force attacks**. A brute-force attack is a method in which automated programs try millions of passwords until the correct one is found. The shorter and simpler the password, the faster it can be cracked.

Example:

- A password like ``admin123`` can be cracked with common hardware **in a few seconds**.
- A secure password with **at least 12 characters, uppercase and lowercase letters, numbers, and special characters**, on the other hand, requires **years or even centuries** to be cracked by brute force.

.. tip::

    **Strong, individual passwords** should be chosen for the **author account** and the **admin account in the API**. A good password strategy includes:

    - **At least 12 characters** (16+ is better).
    - **Uppercase and lowercase letters, numbers, and special characters**.
    - **No relation to real names, birth dates, or dictionary words**.
    - **Each account should have its own, unique password**.
    - If possible: **enable two-factor authentication (2FA)**.

To generate and securely store passwords, using a **password manager** is recommended.

More on password security and brute-force attacks:
`OWASP Authentication Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>`_

Use HTTPS Even on the Intranet
--------------------------------

Many people believe that an intranet is automatically secure because it is not directly reachable from the internet. But that is a misconception! There are risks even within a corporate network:

- **Employee devices can be infected** (e.g. via phishing or malware) and thereby spy on sensitive data.
- **Data is transmitted unencrypted** if HTTPS is not used. This means that passwords, session information, and personal data could be read by attackers or malware.
- **Internal attacks are possible**: people with access to the network could intentionally or accidentally intercept or manipulate data.
- **Future browser versions block unencrypted connections**, which can cause problems in the long run.

For this reason, the *WebGIS Portal* should always be operated over **HTTPS**, even if it is only used internally. More information on the importance of HTTPS and possible attacks can be found in the OWASP documentation:

`Transport Layer Security Cheat Sheet <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html>`_

Further Recommended Security Measures
---------------------------------------

In addition to HTTPS and changing default passwords, there are further important measures to secure the application:

- **Restrict access to the administration interface**
  If possible, only a **specific group of people or only devices from the internal network** should have access to the administration.

- **Use the browser's security mechanisms**
  Security features such as ``Strict-Transport-Security (HSTS)`` and ``Content-Security-Policy (CSP)`` should be enabled to prevent attacks via malicious code.

- **Perform regular updates**
  Outdated software can contain security vulnerabilities. It is important to regularly update the *WebGIS Portal* as well as all servers, databases, and third-party components used.

- **Monitor suspicious activity**
  The system should log who logged in and when. If someone logs in with incorrect passwords or accesses the administration unusually often, this could be an indication of an attack. In this case, administrators should be notified.

Further Information for Interested Readers
----------------------------------------------

There is a wide range of **possible attack scenarios** that also affect intranet applications. These include:

- **Man-in-the-middle attacks (MITM)**, in which an attacker reads network traffic.
- **Session hijacking**, in which a user's session is stolen to impersonate them.
- **Cross-site scripting (XSS)**, in which malicious code is injected into the system.

More on these attack techniques and how to protect against them can be found in the OWASP documentation:
`OWASP Top 10 Security Risks <https://owasp.org/www-project-top-ten/>`_

By implementing these measures, the *WebGIS Portal* is optimally protected and remains secure and reliable – whether on the intranet or publicly on the internet.
