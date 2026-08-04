Installation in Docker
======================

Registry
--------

Images for the WebGIS applications are available on GitHub:

https://github.com/orgs/e-netze/packages?ecosystem=container

* webgis-cms
* webgis-api
* webgis-portal

Pull Images
-----------

.. note::

    The version number here, for example 7.25.4002, may need to be adjusted to the desired version.

Images can be downloaded with the following commands:

.. code:: bash

   docker pull ghcr.io/e-netze/webgis-cms:7.25.4002
   docker pull ghcr.io/e-netze/webgis-api:7.25.4002
   docker pull ghcr.io/e-netze/webgis-portal:7.25.4002


Locally, the images can then be tagged as ``latest``:

.. code:: bash

   docker tag ghcr.io/e-netze/webgis-cms:7.25.4002 webgis-cms:latest
   docker tag ghcr.io/e-netze/webgis-api:7.25.4002 webgis-api:latest
   docker tag ghcr.io/e-netze/webgis-portal:7.25.4002 webgis-portal:latest

Starting the containers
-----------------------

For running WebGIS in Docker, ``docker-compose`` is recommended.
An example configuration can be found in the directory
``publish/linux-x64/docker`` in the repository https://github.com/e-netze/webgis/tree/main/publish/linux-x64/docker.

The configuration can be adapted to your own needs.
It can be started with the following command:

.. code:: bash

   docker-compose up -d

The WebGIS applications are then available at the following URLs:

* CMS: http://localhost:5003
* API: http://localhost:5001
* Portal: http://localhost:5002

.. note::

    This requires the images to be available locally with the ``latest`` tag.

Stopping the containers
------------------------

The containers can be stopped with the following command:

.. code:: bash

   docker-compose down

Configuration
--------------

The application-specific ``_config`` directories are mapped to separate volumes.
The configuration files can be adjusted there.
The configuration files are located in the ``_config`` directory of each application.

The ``webgis-repository`` directory is also mapped to its own volume.
All three applications should share this directory.

Environment variables in ``docker-compose.yml``
or in ``.env``, ``api.env``, ``portal.env``, ``cms.env`` can also be adjusted.

For example, to change the culture of the applications, the environment variable
``Localization__DefaultCulture`` can be adjusted.

.. note::

    All WebGIS web applications have an endpoint ``/instance/_culture`` that can be used to query the current culture
    of the application,
    and thus also whether the change of the environment variable was successful.

.. code::

   # api.env

   # Example: setting the default culture to English (US)
   # overriding the default culture from appsettings.json

   Localization__DefaultCulture=en-US



