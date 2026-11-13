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

An installation of the .NET App Runtime 10.0.x is required.

Microsoft offers two main runtime variants for running .NET applications:

1. **.NET Runtime (without IIS support):**
   This version contains only the runtime environment needed to run .NET applications as standalone processes – for example as a Windows service or in containers. It is suitable for scenarios where IIS is not used.

2. **.NET Hosting Bundle (with IIS support):**
   This variant additionally contains the ASP.NET Core Module for integration with Internet Information Services (IIS). This allows ASP.NET Core applications to be deployed directly via IIS. This version is best suited for use in Windows server environments with IIS.

.. raw:: html

   <p><a href="https://dotnet.microsoft.com/en-us/download/dotnet/10.0" target="_blank">Download .NET 10.0 Runtime</a></p>

The *deploy tool* is a single file (``webgis.deploy.exe`` on Windows, ``webgis.deploy`` on Linux)
and uses the installed .NET runtime.

**Windows:**

On Windows, the program can for example be copied to ``C:\deploy\webgis``.
After that, the EXE file can simply be run.

**Linux:**

On Linux, the program can for example be copied to ``/opt/deploy/webgis``.
After that, the file must be made executable and can be started:

.. code-block:: bash

    chmod +x webgis.deploy
    ./webgis.deploy

.. note::

   The description below is based on a Windows system. On Linux, the installation
   should work similarly by calling the *deploy tool*.

.. _deploy-console-ui:

Usage
-----

.. versionchanged:: 9.26.4502
   The *deploy tool* has a new console interface with selection lists, progress bars, colors and symbols.

* **Selection lists** (profile, version): Select with the arrow keys ``↑`` / ``↓`` and confirm with ``ENTER``.
* **Multiple selection** (components): Toggle individual entries with ``SPACE`` and confirm with ``ENTER``.
* **Yes/no questions**: Enter ``y`` or ``n``. ``ENTER`` accepts the suggested value in parentheses.
* **Inputs**: The suggested value is shown in parentheses and is accepted with ``ENTER``.

The output is divided into sections (*Download*, *Repository*, *Deploy*, *Configure*).
For each step, only one line with ``✔`` and the number of files is shown. Details such as individual
files and paths are only shown with the ``--verbose`` parameter (see :ref:`deploy-automate`).

.. note::

   To display colors and symbols correctly, a modern terminal should be used
   (e.g. *Windows Terminal*). If the output is redirected (e.g. to a file), the program
   asks no questions and outputs no colors.

Deploying a New Version
-------------------------------------------

The first time you start the program, a profile must first be created.
The profile can, for example, be ``test``, ``staging`` or ``production`` and essentially
corresponds to a WebGIS instance. Since we
only want to test *WebGIS* locally in the first step, a profile with the name ``local``
is a good choice to start with:


.. code-block:: text
   :emphasize-lines: 1,10

    C:\deploy\webgis\> .\webgis.deploy.exe

    ╔════════════════════════════════════╗
    ║    WebGIS.Deploy Tool 9.26.4502    ║
    ╚════════════════════════════════════╝
    Work-Directory: C:\deploy\webgis

    Choose a profile:

    > <new...>

    Enter a name for the new profile (eg. production, staging, test): local

On the first start, there is only the ``<new...>`` entry. It creates a new profile.
On subsequent calls, the existing profiles are shown in the list.

In the next step, the program offers to download the current release from *GitHub*.

.. code-block:: text

   Do you want to download the latest version from GitHub? [y/n] (y): y

   ── Download ───────────────────────────────────────────────
   ✔ Download webgis-win64-9.26.4502.zip (95 MB)

A progress bar is shown during the download. If the current version already exists in the
``download`` directory, it is not downloaded again.

If this is not possible, the latest release can also be downloaded manually.
To do this, the ZIP files must be placed in the ``download`` directory.

In the example, that would be here: ``C:\deploy\webgis\download``

.. code-block:: text

    C:\deploy\webgis\>
    .
    ├── download
    │   └── webgis-win64-9.26.4502.zip
    └── webgis.deploy.exe

If ZIP files are present in the ``download`` directory, the different versions are displayed:

.. code-block:: text

    Choose a version:

    > 9.26.4502
      9.26.4301

The newest version is at the top and is preselected.

.. note::

   All values entered via ``webgis.deploy`` do not need to be entered again on
   subsequent calls. Existing profiles are shown in the selection list
   and can be selected with the arrow keys.

The deployment tool shows a summary and asks once more whether the selected version should actually be deployed with the profile:

.. code-block:: text

    ╭──────────┬───────────╮
    │ Profile  │ local     │
    │ Version  │ 9.26.4502 │
    │ Platform │ win64     │
    ╰──────────┴───────────╯
    Do you want to continue? [y/n] (y):

When a profile (here ``local``) is published for the first time, a few more
values must be specified. If you want to use the default value (in parentheses), it is enough to confirm the question
with ``ENTER``.

.. code-block:: text

    Company (my-company): foo
    Target installation path (C:\apps\webgis):
    Repsitory path (C:\apps\webgis/local/webgis-repository):
    Api online url (http://localhost:5001):
    Api internal url (http://localhost:5001):
    Portal online url (http://localhost:5002):
    Portal internal url (http://localhost:5002):

.. todo:

    Insert the missing examples here

* **Target path of the installation:** The path where WebGIS should be installed.
  Under this directory, the deployment tool creates an additional folder with the profile name
  and the version. Here, the app would be
  installed under ``C:\apps\webgis\local\9.26.4502``.

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
All components are preselected. Individual components can be deselected with ``SPACE``.
For the first installation, you can simply confirm with ``ENTER`` here.

.. code-block:: text

  Select the components to deploy:

  > [X] WebGIS API
    [X] WebGIS Portal
    [X] WebGIS CMS

  (Press <space> to toggle a choice and <enter> to accept)

.. note::

   If you want to offer WebGIS on the internet, you generally need *WebGIS API* and *WebGIS Portal*.
   The *WebGIS CMS* is only needed for configuration by an administrator and should not be
   publicly accessible. Ideally, the *WebGIS CMS* is installed only *locally* or on the *intranet*
   for a *test instance*. Administration is done there by the administrator. The configuration is then
   distributed from this instance to all other instances.

The deployment process then starts:


.. code-block:: text

    ── Repository ─────────────────────────────────────────────
    ✔ Create repository (webgis-api) (71 files)
    ✔ Create repository (webgis-portal)
    ✔ Create repository (webgis-cms) (167 files)

    ── Deploy WebGIS 9.26.4502 ────────────────────────────────
    ✔ WebGIS API (6,659 files)
    ✔ WebGIS Portal (951 files)
    ✔ WebGIS CMS (1,670 files)
    ✔ WebGIS Scripts (4 files)
    ✔ WebGIS Requirements (4 files)
    ✔ Root files (2 files)

    ── Configure ──────────────────────────────────────────────
    ✔ Security keys
    ✔ Overrides webgis-api (2 files)
      webgis-api
      └── _config
          ├── api.config
          └── application-security.config
    ✔ Overrides webgis-portal (2 files)
      webgis-portal
      └── _config
          ├── application-security.config
          └── portal.config
    ✔ Overrides webgis-cms (4 files)
      webgis-cms
      └── _config
          ├── application-security.config
          ├── cms.config
          ├── datalinq.config
          └── settings.config
    ✔ Custom CSS (0 files)

    ╭─ ✔ WebGIS 9.26.4502 deployed ──────────────────────────╮
    │                                                        │
    │  Profile       local                                   │
    │  Components    API, Portal, CMS                        │
    │  Installation  C:\apps\webgis\local\9.26.4502          │
    │  Repository    C:\apps\webgis/local/webgis-repository  │
    │  Duration      1:28 min                                │
    │                                                        │
    ╰────────────────────────────────────────────────────────╯

    Press ENTER to quit...

A progress bar is shown for each step while extracting.
Both *webgis-portal*, *webgis-api* and *webgis-cms* are deployed. After unpacking the ZIP files,
user-specific files from the directory ``_deploy_repository\profiles\{profile}\webgis-[api|cms|portal]\override``
are copied into the respective application directory.
This overwrites the configuration from the installation package with the configuration from the
current profile.

.. _deploy-override-tree:

Below each *Overrides* line, a tree shows which files were copied. The paths are
relative to the respective application directory (``webgis-api``, ``webgis-portal``, ``webgis-cms``),
i.e. as the files were placed in the target.

.. versionadded:: 9.26.4502

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
directory. Then run ``webgis.deploy.exe`` again, select the existing profile and the version
and you will get the following output:

.. code-block:: text

    ╭──────────┬───────────╮
    │ Profile  │ local     │
    │ Version  │ 9.26.4502 │
    │ Platform │ win64     │
    ╰──────────┴───────────╯
    Do you want to continue? [y/n] (y): y
    Company: foo
    Target installation path: C:\apps\webgis
    Repsitory path: C:\apps\webgis/local/webgis-repository
    Api online url: http://localhost:5001
    Api internal url: http://localhost:5001
    Portal online url: http://localhost:5002
    Portal internal url: http://localhost:5002

    ── Deploy WebGIS 9.26.4502 ────────────────────────────────
    ⚠ Version already deployed, files are not extracted again

    ── Configure ──────────────────────────────────────────────
    ✔ Security keys
    ✔ Overrides webgis-api (2 files)
      webgis-api
      └── _config
          ├── api.config
          └── application-security.config
    ...
    ✔ Custom CSS (0 files)

    ╭─ ✔ WebGIS 9.26.4502 deployed ──────────────────────────╮
    │  ...                                                   │
    ╰────────────────────────────────────────────────────────╯

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


.. _deploy-automate:

Automating Updates
---------------------

To automate updates, ``webgis.deploy`` can be called with parameters.
The parameter ``--help`` shows which parameters are possible:

.. code-block:: text

  .\webgis.deploy.exe --help

  usage: webgis.deploy [options]

  Options:
  -h, --help                Show this help message and exit
  -p, --profile             Choose a profile (runs without further questions)
  -d, --download-latest     Download latest version
  -v, --version             Choose a version, --version latest ... latest version
  --cms, --deploy-cms       Deploy WebGIS CMS
  --portal, --deploy-portal Deploy WebGIS Portal
  --api, --deploy-api       Deploy WebGIS API
  --portable                Only list/use portable (self-contained) ZIPs, skip GitHub download
  --non-interactive         Never prompt (also automatic if input/output is redirected)
  --no-color                Disable colors and ANSI sequences
  --verbose                 Show detailed output (files, paths, ...)

  Examples:
    webgis.deploy -p production -v latest --download-latest --deploy-cms --deploy-portal --deploy-api

If a profile is specified with ``-p``, the confirmation and the component selection are skipped. Only the
components specified via ``--api``, ``--portal`` or ``--cms`` are deployed.
For a call completely without questions (e.g. in scripts), additionally specify ``--non-interactive``.

.. versionadded:: 9.26.4502
   The parameters ``--non-interactive``, ``--no-color`` and ``--verbose``.

* ``--non-interactive``: The program asks no questions. If a required value (e.g. profile or
  version) is missing, the program aborts with an error. For profile values that are not set yet,
  the default values are used. This mode is used automatically if input or output
  is redirected (e.g. in scripts or CI pipelines).
* ``--no-color``: No colors and control characters in the output, e.g. for log files.
* ``--verbose``: Additionally outputs details, e.g. individual copied files and paths.

.. versionchanged:: 9.26.4502
   In non-interactive mode (``--non-interactive`` or redirected input/output), the latest version
   is only downloaded from *GitHub* if ``-d`` / ``--download-latest`` is specified.

The return value (*exit code*) is ``0`` if the deployment was successful and ``1`` on an error.
