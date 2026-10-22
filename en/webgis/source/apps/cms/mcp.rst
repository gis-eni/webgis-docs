.. _cms-mcp:

AI Agents (MCP)
===============

.. versionadded:: 9.26.4104

The WebGIS CMS provides an endpoint based on the **Model Context Protocol** (MCP). Through it, AI agents (e.g. GitHub Copilot in VS Code, Claude, ...) can read a CMS and answer an administrator's questions about the configuration, without the administrator having to click through the tree.

Examples of questions to an agent:

- *Which queries exist for the service Cadastre and which fields are shown in the result?*
- *In which maps is the layer Parcels used?*
- *Which services have warnings?*
- *Which fields does the layer Buildings have? Which of them are not yet included in the query?*

For a CMS with Git versioning, the agent can also **change** the CMS (see :ref:`cms-mcp-write`), e.g.:

- *Create a query for the layer Parcels with the fields KG, GNR and Area.*
- *Set MaxFeatures to 500 for all queries of the service Cadastre.*
- *Deploy my working branch to the Test deployment so I can test it in WebGIS.*

.. note::

    Without Git versioning, only **read** access is possible.

Prerequisites
-------------

- The MCP endpoint is enabled for the CMS in the ``cms.config`` (see :ref:`cms-config-mcp`).
- Access to the CMS is secured (``_config/application-security.config``), because every access is assigned to a user.

Creating an access token
------------------------

An agent does not log in via the login form but with a personal **access token**:

1. In the CMS, click **AI Agents (MCP)** in the left sidebar. The page ``/{cms-id}/mcp-tokens`` opens in a new tab.
2. Choose a label (e.g. *VS Code Laptop*), the validity (7, 30 or 90 days) and - with Git versioning - the permission, and click **Create token**:

   - **Read**: the agent can only read the CMS.
   - **Read & write**: the agent can additionally change nodes, run Git commands and create branch deploys (see :ref:`cms-mcp-write`). Only possible with Git versioning.

3. Copy the displayed token. It is shown **only once** and stored on the server only as a hash.

A token is only valid for this CMS and for the user who created it. Under **My tokens**, the expiry date and the last use are shown. Tokens that are no longer needed should be **revoked** there.

Configuring the MCP client
--------------------------

The same page shows the URL of the endpoint and a sample configuration, e.g. for VS Code (``.vscode/mcp.json``):

.. code-block:: json

    {
      "servers": {
        "webgis-cms-webgis-custom": {
          "type": "http",
          "url": "https://my-server/webgis-cms/webgis-custom/mcp",
          "headers": { "Authorization": "Bearer <token>" }
        }
      }
    }

Replace ``<token>`` with the created token. Each CMS has its own endpoint.

Functions
---------

The agent gets the following tools for reading:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Description**
   * - ``get_cms_info``
     - Name of the CMS and - with Git versioning - the current working branch.
   * - ``list_children``
     - Lists the nodes below a path in the CMS tree (as in the tree view).
   * - ``get_node``
     - Returns the properties of a node (service, layer, query, editing theme, map, ...).
   * - ``describe_node_type``
     - Describes the properties of a node type with explanations and allowed values.
   * - ``search_nodes``
     - Searches nodes by a term (like the search in the CMS).
   * - ``find_references``
     - Finds the places where a node is used (linked).
   * - ``get_warnings``
     - Returns the warnings of the CMS.
   * - ``get_layer_fields``
     - Reads the fields of a layer directly from the service (ArcGIS Server, WFS).

.. _cms-mcp-write:

Changes by the agent
--------------------

With a token with the permission **Read & write**, the agent can change the CMS. To keep every change traceable and reversible, the following rules apply:

- Changes are only possible for a CMS with Git versioning (see :doc:`git`).
- The agent works in the **workspace of the token owner**. Changes made by the agent are immediately visible in the CMS user interface and can be reviewed and corrected there.
- Changes are **only possible in a working branch**, never directly in the default branch (e.g. ``main``). The agent creates a working branch or switches to an existing one.
- **Merging into main**, deleting working branches and deploying the published state are **not** possible through the agent. These steps are reserved for the administrator in the CMS user interface.
- Deleting tools (``delete_node``, ``discard``, ``remove_branch_deploy``) are marked as *destructive*. The agent should ask beforehand; the MCP client usually also asks for confirmation.
- Credentials of services can only be set as secret placeholders (``{{secret-...}}``), never in plain text.

A typical workflow:

1. The agent creates a working branch (``create_branch``).
2. It changes the CMS (create nodes, set properties, link, ...).
3. It shows the changes (``get_changes``, ``get_file_diff``), commits and pushes them.
4. Optionally it deploys the working branch as a branch (``fast_deploy``) so the changes can be tested in WebGIS (see :ref:`cms-deploy-branch`).
5. The administrator reviews the changes and merges the working branch into ``main`` in the CMS user interface.

Tools for changing:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Description**
   * - ``describe_create_form``
     - Returns the form for creating a new node (like the *New* dialog in the CMS), including the selection lists loaded from the service.
   * - ``create_node``
     - Creates a new node (service, query, editing theme, map, ...).
   * - ``set_properties``
     - Changes properties of a node. Only the given properties are changed.
   * - ``delete_node``
     - Deletes a node (destructive).
   * - ``reorder_children``
     - Changes the order of the nodes below a node (e.g. table columns).
   * - ``list_link_targets``
     - Lists the nodes that can be linked.
   * - ``add_links``
     - Links nodes (e.g. a service into a map).

Git tools:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Description**
   * - ``get_git_status``
     - Current working branch, changes, commits ahead of/behind the server.
   * - ``list_branches``
     - Lists the working branches.
   * - ``create_branch``, ``checkout_branch``
     - Creates a working branch or switches to an existing one.
   * - ``commit``, ``push``, ``pull``
     - Commits the changes, pushes them to the Git server or pulls changes from the Git server.
   * - ``merge_from_default``, ``abort_merge``
     - Merges the current state of ``main`` into the working branch or aborts a merge.
   * - ``discard``
     - Discards uncommitted changes of one node or of all nodes (destructive).
   * - ``get_changes``, ``get_file_diff``, ``get_history``
     - Shows the changed nodes, the differences of a file or the history.

Tools for branch deploys:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Description**
   * - ``list_branch_deployments``
     - Lists the deployments that allow branch deploys (``allowBranchDeploy``, see :doc:`../../config/cms/index`) and the branches deployed there.
   * - ``fast_deploy``
     - Deploys the current state of the workspace as a branch (fast deploy). The deploy runs in the background; meanwhile, no changes through the agent are possible.
   * - ``get_deploy_status``
     - Returns the status and output of a running or finished deploy.
   * - ``remove_branch_deploy``
     - Removes the branch deploy of the own current working branch (destructive). Branch deploys of other working branches can only be removed in the CMS user interface.

Security
--------

- The agent has the same permissions as the user who created the token and, with Git versioning, works in that user's workspace.
- **Secrets** (passwords, tokens, ...) are never returned to the agent in plain text but shown as ``********``.
- A token is valid for at most 90 days and can be revoked at any time.
- Where no changes are needed, a token with the permission **Read** should be used. If an agent works autonomously (e.g. in autopilot mode), it can also confirm destructive tools without asking - the safety net is then the working branch and the Git history.
- Content returned to the agent is processed by the AI model used. Therefore, only use a model or provider that is approved for the data of the CMS.

.. note::

    ``get_layer_fields`` always queries the service through the CMS. Secret placeholders (``{{secret-...}}``) in the service URL and credentials are replaced server-side with the values of a deployment's environment, as during deploy. By default ``discovery-deployment`` (see :ref:`cms-config-mcp`) or the first deployment is used, but the agent can specify another deployment (e.g. *"Read the fields from the Test deployment"*). The replaced values are never returned to the agent.
