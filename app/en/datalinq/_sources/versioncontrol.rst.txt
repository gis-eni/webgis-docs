
========================
DataLinq Version Control
========================

With **DataLinq Version Control**, the code of **views** and **queries** can be backed up to an external
version control system (Git), for example **Gitea**, **GitHub**, or comparable platforms.

Goals and Benefits
==================

Connecting to Git provides several important benefits:

- **Resilience**: relevant changes additionally exist outside the running DataLinq instance.
- **Traceability**: changes can be tracked in a structured way.
- **Transparency within the team**: every change can be documented with author and reason for the change.

When changes are made, commits with **name** and **change message** can be created in DataLinq.
This makes it clear later **who** changed something, **when** the change was made,
and **what purpose** the change served.

Recommendation for Operation
============================

For production environments, it is recommended to use an **internal Git repository**
and not a publicly accessible repository instance.

This way, content and change history remain within a controlled infrastructure.

Example in This Documentation
================================

In this documentation, the setup is shown as an example using a **local Gitea instance**.

The configuration is done in the API application under the **Configuration** section.
There, the credentials for the target repository must be entered,
for example **user name and password**, or alternatively an **access token**.

Creating a Repository
=============================

To use it with DataLinq, a repository must first be created in the desired Git system.

1. Log in to your own Git system.
2. Create a new repository.

.. image:: img/repo_new.png
	:alt: Create new repository
	:align: center

3. Enter the repository details.

	It is important here that the **branch name** and **repository name** match the values in the
	**DataLinq API Configuration**.

.. image:: img/repo_new_1.png
	:alt: Repository details and branch configuration
	:align: center

4. After creation, copy the repository URL and enter it in the DataLinq settings.
5. Afterwards, you can decide whether to initialize the repository locally yourself
	or let DataLinq handle the initialization.

.. image:: img/repo_new_2.png
	:alt: Empty repository after creation
	:align: center

Initialization in DataLinq (Snapshot)
======================================

After the repository configuration, additional buttons are shown on the DataLinq home page:

- **Init Snapshot**
- **Snapshot Status**

.. image:: img/snapshot_1.png
	:alt: New snapshot buttons on the DataLinq home page
	:align: center

Snapshot Status
---------------

Right after setup, **Snapshot Status** usually shows that nothing is up to date yet,
since no content has been transferred to version control yet.

.. image:: img/snapshot_2.png
	:alt: Snapshot Status shows content that is not up to date
	:align: center

Init Snapshot
-------------

**Init Snapshot** starts the initialization process.
DataLinq asks for confirmation beforehand.

.. warning::

	The init process should only be performed **once**, right at the beginning,
	since it merges all existing content into a shared **initial commit**.

.. image:: img/snapshot_3.png
	:alt: Confirmation dialog for Init Snapshot
	:align: center

After successful initialization, a success message is shown.

.. image:: img/snapshot_4.png
	:alt: Successful initialization of the snapshot
	:align: center

Status After Initialization
-------------------------------

Afterwards, **Snapshot Status** shows that all files are in sync with version control.

.. image:: img/snapshot_5.png
	:alt: Snapshot Status shows all files as up to date
	:align: center

Verification in the Git Repository
----------------------------------

The automatic initialization is also visible in the Git repository afterwards,
including the first initial commit and the transferred query and endpoint files.

.. image:: img/snapshot_6.png
	:alt: Initialized repository with first commit and DataLinq files
	:align: center

Files:

.. image:: img/snapshot_7.png
	:alt: Initialized repository with first commit and DataLinq files
	:align: center

Commit Workflow in the DataLinq Code Editor
===========================================

When a new query or view is created in the DataLinq Code Editor,
or an existing query/view is changed, the Git icon in the toolbar signals the status.

If the icon is **red**, local changes exist and the state is not yet synchronized.

.. image:: img/git_1.png
	:alt: Red Git icon shows unsynchronized changes
	:align: center

After clicking the Git icon, a commit can be created.
This records **name** and **message**.

.. image:: img/git_2.png
	:alt: Commit dialog with name and message
	:align: center

After a successful commit, a success message is shown.

.. image:: img/git_3.png
	:alt: Successful commit in the DataLinq Code Editor
	:align: center

Afterwards, the Git icon turns **green** and shows the synchronized status.

.. image:: img/git_4.png
	:alt: Green Git icon shows synchronized status
	:align: center

If further changes are made afterwards (for example, by another user),
the icon switches back to **red**.

.. image:: img/git_5.png
	:alt: Git icon turns red again after further changes
	:align: center

After another commit, the current state is synchronized again.

.. image:: img/git_6.png
	:alt: Another commit after new changes
	:align: center

The new commits, including commit messages, are then visible in the Git repository.

.. image:: img/git_7.png
	:alt: New commits and messages in the Git repository
	:align: center

The exact changes can be tracked.

.. image:: img/git_8.png
	:alt: New commits and messages in the Git repository
