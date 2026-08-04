File ``appsettings.json``
==============================

The ``appsettings.json`` file contains the configuration settings for the web application.
It is located in the application's root directory and is loaded when the application starts.
The settings in this file relate less to WebGIS-specific functionality
and more to general application parameters, such as logging at the ASP.NET Core level,
localization/culture, etc.

The file is structured in JSON format and contains various sections
that define different configuration parameters.
Below are some of the most important sections and their functions:

.. code:: json

  {
    "Logging": {
      "LogLevel": {
        "Default": "Information",  /* default: Warning */
        "Microsoft": "Warning",
        "Microsoft.Hosting.Lifetime": "Information"
      }
    },
    "Localization": {
        "DefaultCulture": "de-AT"
    }
  }

- **Logging**: This section defines the settings for the application's logging at the ASP.NET Core level,
  including the log levels and the log output targets.

- **Localization**: This defines the localization settings for the application,
  including the default culture used by the application.

  Normally the application starts in the operating system's culture,
  but an explicit culture can be defined here that then applies to the entire application.
  This can be used, for example, to determine how dates and times are formatted.

  .. note::

     All WebGIS web applications have an endpoint ``/instance/_culture``, through which the current culture
     of the application can be queried.
     This endpoint returns the current culture used by the application,
     and can be helpful for verifying that the application is using the expected culture:

     .. code:: http

        GET /instance/_culture HTTP/1.1

     .. code:: json

        {
          "culture": "de-AT",
          "cultureDisplayName": "German (Austria)",
          "cultureEnglishName": "German (Austria)",
          "cultureUI": "de-AT",
          "currentTimeString": "10.03.2026 07:42:40"
        }

     In this example, the response shows that the current culture of the application
     is "de-AT" (German - Austria),
     and also returns the current time in the corresponding format.


