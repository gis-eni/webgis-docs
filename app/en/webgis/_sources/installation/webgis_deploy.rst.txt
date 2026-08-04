.. _deploy:

Installation with webgis.deploy
=================================

The installation is done using the command-line tool webgis.deploy. This tool handles the following tasks:

- Fresh installation of webgis-portal, webgis-api and webgis-cms
- Management of deploy profiles (e.g. local, test, staging, production)
- Distribution of configuration changes (e.g. api.config, cms.config, portal.config)
- Distribution of styling changes (default.css, portal.css)

Preparation
------------

The deployment tool as well as other packages can be downloaded under *Releases* from the GitHub repository https://github.com/e-netze/webgis/releases.

An installation of the .NET App Runtime 9.0.x is required.

Microsoft offers two main runtime variants for running .NET applications:

1. **.NET Runtime (without IIS support):**
   This version contains only the runtime environment needed to run .NET applications as standalone processes – for example as a Windows service or in containers. It is suitable for scenarios where IIS is not used.

2. **.NET Hosting Bundle (with IIS support):**
   This variant additionally contains the ASP.NET Core Module for integration with Internet Information Services (IIS). This allows ASP.NET Core applications to be deployed directly via IIS. This version is best suited for use in Windows server environments with IIS.

.. raw:: html

   <p><a href="https://dotnet.microsoft.com/en-us/download/dotnet/9.0" target="_blank">Download .NET 8.0 Runtime</a></p>


**Windows:**

On Windows, the program can for example be copied to ``C:\deploy\webgis``.
After that, the EXE file can simply be run.

**Linux:**

Coming Soon ...

.. note::

   The description below is based on a Windows system. On Linux, the installation
   should work similarly by calling the *deploy tool*.

Deploying a New Version
-------------------------------------------

The first time you start the program, a profile must first be created.
The profile can, for example, be ``test``, ``staging`` or ``production`` and essentially
corresponds to a WebGIS instance. Since we
only want to test *WebGIS* locally in the first step, a profile with the name ``local``
is a good choice to start with:


.. code-block:: text
   :emphasize-lines: 1,5

    C:\deploy\webgis\> .\webgis.deploy.exe

    ******************************************
    *                                        *
    *      WebGIS.Deploy Tool 7.25.701      *
    *                                        *
    ******************************************
    Work-Directory: C:\deploy\webgis
    Directory C:\deploy\webgis\_deploy_repository exists: True
    Try Write security keys: C:\deploy\webgis\_deploy_repository\keys.config
    succeeded
    Choose a profile or create a new by enter an unique name, eg. production, staging, test
    Input profile index [0]: local

In the next step, the program offers to download the current release from *GitHub*,
if it is not already available.

.. code-block:: text

   Do you want to download latetest version from GitHub? Y/N [Y]

If this is not possible, the latest release can also be downloaded manually.
To do this, the ZIP files must be placed in the ``download`` directory.

In the example, that would be here: ``C:\deploy\webgis\download``

.. code-block:: text

    C:\deploy\webgis\>
    .
    ├── download
    │   └── webgis-win64-7.25.701.zip
    └── webgis.deploy.exe

If ZIP files are present in the ``download`` directory, the different versions are displayed:

.. code-block:: text

    Choose a version
    0 ... 7.25.701
    Input version index [0]:

The newest version gets the index ``0``.

.. note::

   All values entered via ``webgis.deploy`` do not need to be entered again on
   subsequent calls. Instead, these values are shown with an index number. You then
   only need to enter the corresponding number, or it is enough to simply press
   ``ENTER`` if the desired index is the
   suggested value, e.g. ``Input version index [0]`` => ``ENTER`` => version with
   index ``0``.

The deployment tool now asks once more whether the selected version should actually be deployed with the profile:

.. code-block:: text

    Deploy version 7.25.701 to profile local
    Do you want to continue? Y/N [Y]

When a profile (here ``local``) is published for the first time, a few more
values must be specified. If you want to use the default value, it is enough to confirm the question
with ``ENTER``.

.. code-block:: text

    Company [my-company]: foo
    Target installation path [C:\apps\webgis]:
    Repsitory path [C:\apps\webgis/local/webgis-repository]:
    Api online url [http://localhost:5001]:
    Api internal url [http://localhost:5001]:
    Portal online url [http://localhost:5002]:
    Portal internal url [http://localhost:5002]:

.. todo:

    Insert the missing examples here

* **Target path of the installation:** The path where WebGIS should be installed.
  Under this directory, the deployment tool creates an additional folder with the profile name
  and the version. Here, the app would be
  installed under ``C:\apps\webgis\local\7.25.701``.

* **Repository path:** Various files required for the software to work are stored in the repository path,
  for example the CMS tree, print layouts, etc.
  The repository folder is normally created in the directory
  of the profile (here: ``C:\apps\webgis\local``). Since the folder is not located in the *version*
  folder, it can be reused directly by a newly installed version. It is important
  that different profiles use their own repository directory.

* **WebGIS API Online URL:** A URL under which the *webgis-api* will be accessible,
  e.g. https://my-server.com/webgis-api.
  If you want to test the ``local`` profile and only run the programs locally, this is usually
  done via http://localhost:5001. If WebGIS is operated as an application in IIS, you must enter here
  the URL under which the WebGIS API is reachable via the browser.

* **WebGIS API Internal URL:** *WebGIS API* and *WebGIS Portal* must be able to communicate with each other.
  For this, a URL must be specified here under which the *WebGIS Portal* application can access the API directly.
  This should happen without requiring authentication. The simplest way here is also,
  even in a production environment, to specify a ``localhost`` path, e.g. http://localhost/webgis-api or,
  for the ``local`` profile, the suggested value http://localhost:5001

* **WebGIS Portal Online URL:** Here you must enter the URL under which the *WebGIS Portal* is called,
  e.g. https://my-server.com/webgis-api.
  For the ``local`` profile, the suggested value http://localhost:5002 can again be used.

* **WebGIS Portal Internal URL:** As above for the *WebGIS API*, a URL must be specified here
  with which the *WebGIS API* application can directly access the *WebGIS Portal* application, e.g.
  http://localhost/webgis-api. For the ``local`` profile, the suggested value can be used.

.. note::

  The values set here are stored in the ``_deploy_repository\profiles\{profil}\deploy-model.json``
  file and can also be changed there afterwards.

In the last step, it must also be specified which components of WebGIS should be installed.
In theory, all components (*WebGIS API*, *WebGIS Portal* and *WebGIS CMS*) can be installed separately.
For the first installation, you can answer all options with YES [Y] here.

.. code-block:: text

  Do you want to deploy WebGIS API? Y/N [Y]
  Do you want to deploy WebGIS Portal? Y/N [Y]
  Do you want to deploy WebGIS CMS? Y/N [Y]

.. note::

   If you want to offer WebGIS on the internet, you generally need *WebGIS API* and *WebGIS Portal*.
   The *WebGIS CMS* is only needed for configuration by an administrator and should not be
   publicly accessible. Ideally, the *WebGIS CMS* is installed only *locally* or on the *intranet*
   for a *test instance*. Administration is done there by the administrator. The configuration is then
   distributed from this instance to all other instances.

The deployment process then starts:


.. code-block:: text

    ************************************************************************************************************************

    Create a new webgis repositiry C:\apps\webgis/local/webgis-repository

    ************************************************************************************************************************

    ...succeeded 71 items created
    ...succeeded 0 items created
    ...succeeded 167 items created

    Deploy version 7.25.701
    Deploy WebGIS API:
    ...succeeded 6659 items created
    Deploy WebGIS Portal:
    ...succeeded 951 items created
    Deploy WebGIS CMS:
    ...succeeded 1670 items created
    Deploy WebGIS Scripts:
    ...succeeded 4 items created
    Deploy WebGIS Scripts:
    ...succeeded 4 items created
    Copy root files
    ...succeeded 2 items created
    Append keys.config
    Overrides
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\api.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\application-security.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\portal.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\cms.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\datalinq.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\settings.config
    ...succeeded 4 items created/overridden
    Create Custom CSS
    Build default.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\default.css not exits
    Build portal.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\portal.css not exits


    ########################################################################################################################

    Deploy succeeded

    ########################################################################################################################

    Press ENTER to quit...

Both *webgis-portal*, *webgis-api* and *webgis-cms* are deployed. After unpacking the ZIP files,
user-specific files from the directory ``_deploy_repository\profiles\{profile}\webgis-[api|cms|portal]\override``
are copied into the respective application directory.
This overwrites the configuration from the installation package with the configuration from the
current profile.

.. note::

   Any files can be copied into the *override* directories that should additionally
   be copied into or overwrite files in the application directories, e.g. logos, etc.
   Configuration files should never be changed directly in the application directory,
   but always for the respective application in the
   ``_deploy_repository\profiles\{profile}\webgis-[api|cms|portal]\override`` directory.
   This ensures that changes
   to the configuration are copied again the next time a profile is updated.

Changing the Current Configuration
------------------------------------

If you make changes to the configuration (e.g. ``api.config``), this is done in the *override*
directory. Then run ``webgis.deploy.exe`` again and you will get the following message:

.. code-block:: text

    ******************************************
    *                                        *
    *      WebGIS.Deploy Tool 7.25.701      *
    *                                        *
    ******************************************
    Work-Directory: C:\deploy\webgis
    Choose a profile or create a new by enter an unique name, eg. production, staging, test
    0 ... local
    Input profile index [0]:

    Do you want to download latetest version from GitHub? Y/N [Y]
    Download not implementet! Comming soon. Please download laytest Versions manually...

    Choose a version
    0 ... 7.25.701
    Input version index [0]:

    Deploy version 7.25.701 to profile local
    Do you want to continue? Y/N [Y]
    Company: foo
    Target installation path: C:\apps\webgis
    Repsitory path: C:\apps\webgis/local/webgis-repository
    Api online url: http://localhost:5001
    Api internal url: http://localhost:5001
    Portal online url: http://localhost:5002
    Portal internal url: http://localhost:5002

    Deploy version 7.25.701


    ***********************************************************************************************************************************************************************************

    Warning: version already deployed

    ***********************************************************************************************************************************************************************************

    Append keys.config
    Overrides
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\api.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-api\override\_config\application-security.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-portal\override\_config\portal.config
    ...succeeded 2 items created/overridden
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\application-security.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\cms.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\datalinq.config
    Copy C:\deploy\webgis\_deploy_repository\profiles\local\webgis-cms\override\_config\settings.config
    ...succeeded 4 items created/overridden
    Create Custom CSS
    Build default.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\default.css not exits
    Build portal.css css overrides...
    Canceld: C:\deploy\webgis\_deploy_repository\profiles\local\css-modify\portal.css not exits


    ###################################################################################################################################################################################

    Deploy succeeded

    ###################################################################################################################################################################################

    Press ENTER to quit...


The warning appears that this version has already been deployed. No data is copied from the ZIP files.
Only the *overrides* and changes to the styles ``default.css`` and
``portal.css`` are applied.

Styling the Applications
--------------------------

Two *CSS files* are mainly responsible for styling the applications:

* ``default.css`` is located in the ``webgis-api/wwwroot/content/...`` directory. All styles for
  the WebGIS map viewer are defined here.

* ``portal.css`` is located in the ``webgis-portal/wwwroot/content/...`` directory. The styles for
  the portal pages (landing page with the map collections) are defined here.

.. note::

  These files should never be changed directly. Since WebGIS is continuously developed further, these
  files change with every version. If you overwrite these files yourself, things can be lost
  and new features may not be accessible.

  If you want to change styles, this should always be done using the methods shown here.

To adjust styles (e.g. colors), the ``webgis.deploy`` tool creates a folder ``css-modify`` under
``_deploy_repository\profiles\{profile}``. Below that, there are further subfolders and files for each
of the two *CSS files*:

.. code-block:: text

    C:\deploy\webgis\_deploy_repository\profiles\{profile}>
    .
    ├── css-modify
        └── default.css
        |   └── modify.json
        |   └── append.css
        └── portal.css
        |   └── modify.json
        |   └── append.css
        └── site.css
            └── modify.json
            └── append.css

* **modify.json** is a file in which styles can be changed by simple text replacement.
  Such replacements are especially well suited for changing the CI (Corporate Identity) colors:

  .. code-block:: json

    {
      "mode": "shrink",
      "modifiers": [
        {
          "pattern": "#82C828",  // --webgis-brand-primary (CI Color)
          "replace": "#ccc"
        }
        /*,{
          "pattern": "#ccc",  // optional additional color codes
          "replace": "#aaa"
        }*/
      ]
    }

 Here, a ``pattern`` (current CI colors of WebGIS) is each replaced by another value ``replace``.
 With ``mode=shrink`` it is specified that the newly created file only includes the necessary properties
 of the changed styles (recommended).

* **append.css** This is a *CSS file* with which any style classes from the
  original files can be overridden, for example other ``root:`` variables:

.. code-block:: css

    // site.css
    :root {
        --webgis-brand-primary: #ccc;
        --webgis-brand-primary-light: #eee;
        --webgis-brand-primary-light-text-color: #333;
        --webgis-brand-logo: url(https://my-server.com/webgis-repository/content/companies/foo/img/logo.png);
    }

    // default.css
    .webgis-container, body {
        --webgis-brand-primary: #ccc;
        /* ... */
    }

If changes are made to these files, the ``webgis.deploy`` tool can be applied again to an
existing *WebGIS instance*. The updated *CSS files* are then distributed to the correct
location.

A more detailed description of the individual *CSS files* and their scope, variables, etc. can be found in the :doc:`../config/css-styling/index` documentation.

.. note::

  The original *CSS files* are never overwritten. Instead, additional *CSS files* are
  created that are always loaded in the browser at a later point in time than the original.
  The styles are therefore *only* overridden. It is therefore important to only list, even in **append.css**, those
  properties of the desired classes that should actually be changed!

.. note::

  The ``default.css`` is responsible for adjusting the styles (colors) of the viewer and portal pages.

.. note::

  Changes to the ``site.css`` affect the default values for all WebGIS applications. This is mainly
  about adjusting the CI colors for login and admin pages.


Automating Updates
---------------------

To automate updates, ``webgis.deploy`` can be called with parameters.
The parameter ``--help`` shows which parameters are possible:

.. code-block:: text

  .\webgis.deploy.exe --help
   ******************************************
   *                                        *
   *      WebGIS.Deploy Tool 7.25.1001      *
   *                                        *
   ******************************************
   Work-Directory: C:\deploy\webgis
   usage: webgis.deploy [options]

   Options:
     -h,       --help            Show this help message and exit
     -p,       --profile         Choose a profile
     -d,       --download-latest Download latest version
     -v,       --version         Choose a version, --version latest ... latest version
     -cms,     --deploy-cms      Deploy WebGis CMS
     -portal,  --deploy-portal   Deploy WebGIS Portal
     -api,     --deploy-api      Deploy WebGIS API

   Examples:
     webgis.deploy -p production -v latest --download-latest --deploy-cms --deploy-portal --deploy-api
