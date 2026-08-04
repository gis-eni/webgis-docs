Configuration of DataLinq.API and DataLinq.CodeApi
==================================================

The configuration of **DataLinq.API** and **DataLinq.CodeAPI** is done via two files:

1. **datalinq.api.json** - management of clients, file storage path, etc.
2. **datalinq.config** - defines global constants and code instances

The configuration files enable flexible adaptation of the application to
various deployment scenarios.

===============

`datalinq.api.json`
-------------------

This file is located in the directory:
**DataLinq.Api/_config/datalinq.api.json**

It contains central settings for security, paths, and clients.

Example:

.. code-block:: json

  {
    "DataLinq.Api": {
      "StoragePath": "{path_to_storage}",
      "Razor": {
        "Engine": "default"  // default or legacy (old engine)
      },
      "Crypto": {
        "SecureStringEncryptionLevel": "",  // optional
        "DefaultPasswort": "{a-secure-password}",  // optional
        "SaltBytes": "{8byte-base64-encoded}"  //optional
      },
      "ImageRequestWhiteList": [
        "https://upload.wikimedia.org/",
        "https://raw.githubusercontent.com/"
      ],
      "SelectEngines": {
        "TextFileEngine": {
          "AllowedExtensions": [
            ".txt",
            ".csv"
          ],
          "AllowedPaths": [
            "C:\\DataLinq\\Data\\" // or /etc/datalinq/data on linux
          ]
        }
      }
    },
    "DataLinq.CodeApi": {
      "InitializeSandboxOnStartup": true,
      "ClientEndpoints": [
        "http://localhost"
      ],
      "Clients": [
        {
          "Id": "1",
          "Name": "datalinq",
          "Password": "datalinq",
          "EndPointParameters": "*,_*"
        }
      ]
    },
    "AiService": {
      "UseAzure": false,
      "AzureOpenAi": {
        "DeploymentName": "",
        "Endpoint": "",
        "ApiKey": ""
      },
      "OpenAi": {
        "ModelId": "",
        "ApiKey": "",
        "ServiceUrl": ""
      }
    },
    "Agent": {
      "DataLinqQueryAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqQueryPrompt.txt",
      "DataLinqCodeAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqCodePrompt.txt",
      "DataLinqEndpointAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqEndpointPrompt.txt",
      "DataLinqGeneralAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/DataLinqGeneralPrompt.txt",
      "UserHistorySummarizerAgent": "../../nuget/E.Datalinq.Web/Services/Agents/Prompts/UserHistorySummarizerPrompt.txt"
    },
    "TokenCache": {
      "StorageType": "file",
      "RedisConnectionString": "localhost:6379",
      "FilePath": "C:\\temp\\datalinq\\Tokens\\",
      "DefaultTTL": "00:05:00",
      "DefaultMaxUsage": null,
      "EnableBackgroundCleanup": false,
      "CleanupIntervalMinutes": "24:00:00"
    },
    "VersionControl": {
      "UseVersionControl": false,
      "LocalRepositoryPath": "C:\\temp\\datalinq\\repo",
      "RemoteUrl": "http://localhost:3000/admin/datalinq-repo.git",
      "DefaultBranch": "main",
      "CredentialType": "Token",
      "Username": "",
      "Password": "",
      "PersonalAccessToken": "",
      "DefaultAuthorName": "DataLinq Bot",
      "DefaultAuthorEmail": "bot@datalinq.com",
      "AutoCreateRepository": true
    }
  }

Explanation of the configuration:

DataLinq.Api
++++++++++++

- **StoragePath**
  Defines the root directory in the file system for endpoints, queries, and views.

- **Razor**
  - **Engine** - Sets the Razor rendering engine (``default``, ``legacy``).

- **Crypto**
  - **SecureStringEncryptionLevel** - Sets the encryption level for stored connection data and queries.

    - **None**: - sensitive data is stored unencrypted in storage

    - **DefaultStaticEncryption**: - (default) data is encrypted in storage with a fixed password

    - **RandomSaltedPasswordEncryption**: - data is encrypted with a password and salt defined here.
      If this value is chosen, the two values **DefaultPasswort** and **SaltBytes** must be specified.

  - **DefaultPasswort** - Default password for the encryption (for RandomSaltedPasswordEncryption).
  - **SaltBytes** - Base64-encoded salt values for additional security (for RandomSaltedPasswordEncryption).

- **ImageRequestWhiteList** *(optional)*
  List of allowed URL prefixes from which external images may be loaded.
  If this section is not specified, no external image sources are allowed.

- **SelectEngines**
  DataLinq offers different **engines** for accessing data:

   - Databases
   - Other DataLinq.API instances
   - Plain text: here the data is entered directly as text in the **DataLinq.Code** application
   - Text files: files located on the **DataLinq.API** server or reachable from there
   - Within applications that implement the **DataLinq.API**, e.g. *WebGIS.API*, further
     **engines** can be offered, e.g. GeoJSON, ...

  Some **engines** need special settings, which can be specified here.
  The settings listed above are the default values and also apply if nothing is specified
  under the file system section.

  - **TextFileEngine** - Here you must specify which directories and file extensions
    may be accessed with the **TextFileEngine**.

DataLinq.CodeApi
++++++++++++++++

If this section is not specified, the **DataLinq.CodeApi** is not offered
on this instance.

.. note::

   This makes sense, for example, for **DataLinq** instances that are offered
   via the internet. Via these instances, only **DataLinq** reports can be published,
   but not modified.

   Editing of the **storage** via the **DataLinq.CodeApi** should always only be done via
   connections that do not run over the internet (e.g. intranet only!)

- **InitializeSandboxOnStartup** *(optional)*
  Specifies whether the code sandbox is already initialized when the instance starts
  (default: ``true``). With ``false``, the sandbox is only initialized on first use,
  which reduces startup time.

- **ClientEndpoints**
  Defines allowed client connections to the *DataLinq.Code API*.
  Here, the URL of the *DataLinq.Code* application is specified.

.. note::

  If nothing is specified here, any client (**DataLinq.Code** instance) can edit the
  data in the **storage**. It is therefore important to enter values here and
  list clients with secure passwords!

- **Clients**
  Defines users with credentials and permissions.

  - **Id** - Unique identifier of the client.
  - **Name** - Display name or user name of the client.
  - **Password** - Password for the client's login.
  - **EndPointParameters** - Restriction of the accessible endpoint parameters (e.g. ``*,_*``).

AiService *(optional)*
++++++++++++++++++++++

Configures the AI support (e.g. for query, code, and endpoint assistants).
This section is optional. The AI services are only enabled if either an
Azure OpenAI endpoint (**AzureOpenAi:Endpoint**) or an OpenAI service URL
(**OpenAi:ServiceUrl**) is specified. Without these values, the AI functions remain disabled.

- **UseAzure** - Specifies whether Azure OpenAI (``true``) or OpenAI (``false``) is used.

- **AzureOpenAi** - Settings for Azure OpenAI.

  - **DeploymentName** - Name of the deployed model (deployment).
  - **Endpoint** - URL of the Azure OpenAI endpoint.
  - **ApiKey** - Access key for the Azure OpenAI service.

- **OpenAi** - Settings for OpenAI (or compatible services).

  - **ModelId** - Identifier of the model to be used.
  - **ApiKey** - Access key for the OpenAI service.
  - **ServiceUrl** - URL of the OpenAI-compatible service.

.. note::

   **ApiKey** values should not be stored in plain text in the configuration file,
   but provided via *user secrets* or environment variables.

Agent *(optional)*
++++++++++++++++++

Defines the paths to the prompt files of the individual AI agents. This section is
only relevant in combination with a configured **AiService**.

- **DataLinqQueryAgent** - prompt file for the query assistant.
- **DataLinqCodeAgent** - prompt file for the code assistant.
- **DataLinqEndpointAgent** - prompt file for the endpoint assistant.
- **DataLinqGeneralAgent** - prompt file for the general assistant.
- **UserHistorySummarizerAgent** - prompt file for summarizing the history.

TokenCache *(optional)*
+++++++++++++++++++++++

Configures the caching of tokens. If this section is not specified,
the default values apply.

- **StorageType** - type of token storage: ``file`` (file system) or ``redis``.
- **RedisConnectionString** - connection string to the Redis server (only for ``redis``).
- **FilePath** - directory for storing tokens (only for ``file``).
- **DefaultTTL** - default lifetime of a token in the format ``hh:mm:ss``.
- **DefaultMaxUsage** - maximum number of uses per token (``null`` = unlimited).
- **EnableBackgroundCleanup** - enables periodic cleanup of expired tokens.
- **CleanupIntervalMinutes** - cleanup interval in the format ``hh:mm:ss``
  (only effective if **EnableBackgroundCleanup** is enabled).

VersionControl *(optional)*
+++++++++++++++++++++++++++

Configures the connection of the **storage** to a Git repository, in order to version changes to
endpoints, queries, and views. If this section is not specified, or
**UseVersionControl** is set to ``false``, versioning is disabled.

- **UseVersionControl** - enables (``true``) or disables (``false``) Git versioning.
- **LocalRepositoryPath** - local path of the Git repository.
  This path is also used as the **RepoPath** of the **storage**.
- **RemoteUrl** - URL of the remote repository (e.g. on Gitea, GitHub, or GitLab).
- **DefaultBranch** *(optional)* - default branch for commits (default: ``main``).

- **CredentialType** - type of authentication against the remote repository:

  - **None** - no authentication (e.g. for purely local repositories).
  - **Token** - (default) authentication via a *personal access token*.
  - **UsernamePassword** - authentication via user name and password.

- **Username** - user name (only for **UsernamePassword**).
- **Password** - password (only for **UsernamePassword**).
- **PersonalAccessToken** - access token (only for **Token**).

- **DefaultAuthorName** *(optional)* - name of the author for automatic commits
  (default: ``DataLinq Bot``).
- **DefaultAuthorEmail** *(optional)* - email of the author for automatic commits
  (default: ``bot@datalinq.com``).
- **AutoCreateRepository** *(optional)* - specifies whether a non-existent repository
  is automatically created (default: ``true``).

===============

`datalinq.config`
-----------------

This file is optional and is located at:
**datalinq.api/_config/datalinq.config**

It is used to define constants that are used in DataLinq views (Razor code):

.. code-block:: text

  @{  var env = Const.Environment;   }

  @if(env == "Production") {
     // ...
  }

Example:

.. code-block:: xml

  <?xml version="1.0" encoding="utf-8" ?>
    <configuration>
      <const>
        <add name="Environment" value="Test" />
        <!-- production, staging, test, development, ... -->
      </const>
  </configuration>

Explanation:

- **<const>** - constants can be defined here that are later used in the code.

These values can be read in the code in order to configure the application
according to the environment.

With these configuration files, **DataLinq** can be flexibly adapted to
different requirements.
