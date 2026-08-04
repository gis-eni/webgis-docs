Configuration of DataLinq.Code
==============================

The configuration of **DataLinq.Code** is done via the file:

1. **datalinq.code.json** – management of encryption and **DataLinq.CodeApi** instances.

The configuration file enables flexible adaptation of the application
to various deployment scenarios.

===============

`datalinq.code.json`
--------------------

This file is located at:
**datalinq.code/_config/datalinq.code.json**

Example:

.. code-block:: json

  {
    "DataLinq.Code": {
      "Crypto": {
        "DefaultPasswort": "",
        "SaltBytes": ""
      },
      "Instances": [
        {
          "Name": "Local",
          "Description": "A local datalinq instance for testing and development",
          "LoginUrl": "{url-datalinq-code-api}",
          "LogoutUrl": "{url-datalinq-code-api}",  // optional
          "CodeApiClientUrl": "{url-datalinq-code-api}"
        }
      ]
    }
  }

Explanation:

- **Crypto**
  These values are usually assigned randomly and are optional. If several
  instances of **DataLinq.Code** run behind a load balancer, fixed values should be
  specified here for all instances.

  - **DefaultPasswort** – default password for the encryption.
  - **SaltBytes** – base64-encoded salt values for additional security.

- **Instances**
  Defines **DataLinq.CodeApi** instances. With one **DataLinq.Code** instance,
  multiple **DataLinq.CodeApi** instances can be managed.

  - **Name** – name of the instance.
  - **Description** – description of the instance.
  - **LoginUrl** – URL for logging in. The user of *DataLinq.Code* must log in via the
    browser. Here, the URL to the *DataLinq.CodeApi* must be specified that is reachable
    via the browser.
  - **LogoutUrl** – URL for logging out (optional, usually the same as **LoginUrl**)
  - **CodeApiClientUrl** – URL to the *DataLinq.CodeApi* as it can be addressed by
    *DataLinq.Code*. Usually this URL is the same as **LoginUrl**. If the applications run
    in a **Docker** or **Kubernetes** environment, the URL through which the two containers
    can communicate with each other may need to be specified here.
