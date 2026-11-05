.. _cms-mcp:

KI-Agenten (MCP)
================

.. versionadded:: 9.26.4104

Das WebGIS CMS bietet einen Endpunkt nach dem **Model Context Protocol** (MCP). Darüber können KI-Agenten (z. B. GitHub Copilot in VS Code, Claude, ...) ein CMS lesen und dem Administrator Fragen zur Konfiguration beantworten, ohne dass er sich durch den Baum klicken muss.

Beispiele für Fragen an einen Agenten:

- *In welchen Karten wird der Layer Grundstücke verwendet?*
- *Welche Felder hat der Layer Gebäude? Welche davon sind noch nicht in der Abfrage enthalten?*
- *Lege für den Layer Grundstücke eine Abfrage mit den Feldern KG, GNR und Fläche an.*

Bei einem CMS mit Git-Versionierung kann der Agent das CMS auch **ändern** (siehe :ref:`cms-mcp-write`). Weitere Beispiele stehen unter :ref:`cms-mcp-prompts`.

.. note::

    Ohne Git-Versionierung ist nur **lesender** Zugriff möglich.

Voraussetzungen
---------------

- MCP ist in der ``_config/mcp.config`` für das CMS freigegeben (siehe :ref:`cms-config-mcp-config`).
- Der MCP-Endpunkt ist in der ``cms.config`` für das CMS aktiviert (siehe :ref:`cms-config-mcp`).
- Der Zugang zum CMS ist gesichert (``_config/application-security.config``), da jeder Zugriff einem Benutzer zugeordnet wird.

Zugriffstoken erstellen
-----------------------

Ein Agent meldet sich nicht über das Login-Formular an, sondern mit einem persönlichen **Zugriffstoken**:

1. Im CMS links in der Seitenleiste auf **AI Agents (MCP)** klicken. Die Seite ``/{cms-id}/mcp-tokens`` öffnet sich in einem neuen Tab.
2. Eine Bezeichnung (z. B. *VS Code Laptop*), die Gültigkeit (7, 30 oder 90 Tage) und - bei Git-Versionierung - die Berechtigung wählen und auf **Token erstellen** klicken:

   - **Lesen**: der Agent kann das CMS nur lesen.
   - **Lesen & Schreiben**: der Agent kann zusätzlich Knoten ändern, Git-Befehle ausführen und Branch-Deploys erstellen (siehe :ref:`cms-mcp-write`). Nur bei Git-Versionierung möglich und wenn Schreiben in der ``_config/mcp.config`` freigegeben ist (``"tools": ["read", "write", ...]``). Sonst wird keine Berechtigung angeboten.

3. Den angezeigten Token bzw. die fertige Client-Konfiguration mit diesem Token kopieren (siehe unten). Der Token wird **nur einmal** angezeigt und am Server nur als Hash gespeichert.
Ein Token gilt nur für dieses CMS und für den Benutzer, der ihn erstellt hat. Unter **Meine Tokens** werden Ablaufdatum und letzte Verwendung angezeigt. Nicht mehr benötigte Tokens sollten dort **widerrufen** werden.

MCP-Client konfigurieren
------------------------

Auf derselben Seite werden die URL des Endpunkts und eine Beispiel-Konfiguration angezeigt, z. B. für VS Code (``.vscode/mcp.json``):

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

``<token>`` wird durch den erstellten Token ersetzt. Direkt nach dem Erstellen eines Tokens wird diese Konfiguration bereits mit dem neuen Token angezeigt und kann übernommen werden.

.. _cms-mcp-multiple-cms:

Mehrere CMS
~~~~~~~~~~~

Pro CMS gibt es einen eigenen Endpunkt ``/{cms-id}/mcp``, und ein Token gilt immer nur für ein CMS. Sollen mehrere CMS über einen Agenten erreichbar sein, wird **pro CMS ein Token erstellt** und **pro CMS ein Eintrag** in der Client-Konfiguration angelegt:

.. code-block:: json

    {
      "servers": {
        "webgis-cms-kataster": {
          "type": "http",
          "url": "https://my-server/webgis-cms/kataster/mcp",
          "headers": { "Authorization": "Bearer <token-kataster>" }
        },
        "webgis-cms-leitungen": {
          "type": "http",
          "url": "https://my-server/webgis-cms/leitungen/mcp",
          "headers": { "Authorization": "Bearer <token-leitungen>" }
        }
      }
    }

Die Werkzeuge stehen dem Agenten dann für jedes CMS getrennt zur Verfügung. Jeder Endpunkt meldet dem Agenten, zu welchem CMS er gehört (Name, CMS-Id, Git-Versionierung und Berechtigung des Tokens). Damit der Agent das richtige CMS verwendet, sollte das CMS im Prompt genannt werden, z. B. *"Welche Abfragen gibt es im CMS Kataster für den Dienst Grundstücke?"*.

Aufgaben über mehrere CMS hinweg sind ebenfalls möglich, z. B. *"Vergleiche den Dienst Grundstücke im CMS Kataster mit dem im CMS Leitungen"*. Der Agent liest dabei aus dem einen und - mit einem Token **Lesen & Schreiben** - schreibt in das andere CMS. Jede Änderung erfolgt im Arbeitszweig des jeweiligen CMS.

Funktionen
----------

Der Agent erhält folgende Werkzeuge (Tools) zum Lesen:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Beschreibung**
   * - ``get_cms_info``
     - Name des CMS und - bei Git-Versionierung - der aktuelle Arbeitszweig.
   * - ``list_children``
     - Listet die Knoten unter einem Pfad im CMS-Baum (wie in der Baumansicht).
   * - ``get_node``
     - Liefert die Eigenschaften eines Knotens (Dienst, Layer, Abfrage, Editierthema, Karte, ...).
   * - ``describe_node_type``
     - Beschreibt die Eigenschaften eines Knotentyps mit Erklärung und erlaubten Werten.
   * - ``search_nodes``
     - Sucht Knoten nach einem Begriff (wie die Suche im CMS).
   * - ``find_references``
     - Findet die Stellen, an denen ein Knoten verwendet (verlinkt) wird.
   * - ``get_warnings``
     - Liefert die Warnungen des CMS.
   * - ``get_layer_fields``
     - Liest die Felder eines Layers direkt vom Dienst (ArcGIS Server, WFS).

.. _cms-mcp-write:

Änderungen durch den Agenten
----------------------------

Mit einem Token mit der Berechtigung **Lesen & Schreiben** kann der Agent das CMS ändern. Damit jede Änderung nachvollziehbar und rückgängig zu machen ist, gelten folgende Regeln:

- Änderungen sind nur bei einem CMS mit Git-Versionierung möglich (siehe :doc:`git`).
- Die Werkzeuge zum Ändern und die schreibenden Git-Werkzeuge werden nur angeboten, wenn in der ``_config/mcp.config`` die Gruppe ``write`` freigegeben ist, die Werkzeuge für den Branch-Deploy nur mit der Gruppe ``deploy`` (siehe :ref:`cms-config-mcp-config`). Die lesenden Git-Werkzeuge (``get_git_status``, ``list_branches``, ``get_changes``, ``get_file_diff``, ``get_history``) stehen auch mit einem Token mit der Berechtigung **Lesen** zur Verfügung.
- Der Agent arbeitet im **Arbeitsbereich des Token-Besitzers**. Änderungen des Agenten sind sofort in der CMS-Oberfläche sichtbar und können dort geprüft und korrigiert werden.
- Änderungen sind **nur in einem Arbeitszweig** möglich, nie direkt im Standard-Branch (z. B. ``main``). Der Agent legt dazu einen Arbeitszweig an oder wechselt in einen bestehenden.
- **In main übernehmen**, Arbeitszweige löschen und das Deploy des veröffentlichten Stands sind über den Agenten **nicht** möglich. Diese Schritte bleiben dem Administrator in der CMS-Oberfläche vorbehalten.
- Löschende Werkzeuge (``delete_node``, ``discard``, ``remove_branch_deploy``) sind als *destruktiv* gekennzeichnet. Der Agent soll vorher nachfragen; der MCP-Client zeigt in der Regel ebenfalls eine Bestätigung an.
- Zugangsdaten von Diensten können nur als Secret-Platzhalter (``{{secret-...}}``) gesetzt werden, nie im Klartext.

Ein typischer Ablauf:

1. Der Agent legt einen Arbeitszweig an (``create_branch``).
2. Er ändert das CMS (Knoten anlegen, Eigenschaften setzen, verlinken, ...).
3. Er zeigt die Änderungen (``get_changes``, ``get_file_diff``), committet und pusht sie.
4. Optional deployt er den Arbeitszweig als Branch (``fast_deploy``), damit die Änderungen im WebGIS getestet werden können (siehe :ref:`cms-deploy-branch`).
5. Der Administrator prüft die Änderungen und übernimmt den Arbeitszweig in der CMS-Oberfläche in ``main``.

Werkzeuge zum Ändern:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Beschreibung**
   * - ``describe_create_form``
     - Liefert das Formular zum Anlegen eines neuen Knotens (wie der Dialog *Neu* im CMS), inklusive der Auswahllisten, die vom Dienst geladen werden.
   * - ``create_node``
     - Legt einen neuen Knoten an (Dienst, Abfrage, Editierthema, Karte, ...).
   * - ``set_properties``
     - Ändert Eigenschaften eines Knotens. Es werden nur die angegebenen Eigenschaften geändert.
   * - ``delete_node``
     - Löscht einen Knoten (destruktiv).
   * - ``reorder_children``
     - Ändert die Reihenfolge der Knoten unter einem Knoten (z. B. Tabellenspalten).
   * - ``list_link_targets``
     - Listet die Knoten, die verlinkt werden können.
   * - ``add_links``
     - Verlinkt Knoten (z. B. einen Dienst in eine Karte).

Git-Werkzeuge:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Beschreibung**
   * - ``get_git_status``
     - Aktueller Arbeitszweig, Änderungen, Commits vor/hinter dem Server.
   * - ``list_branches``
     - Listet die Arbeitszweige.
   * - ``create_branch``, ``checkout_branch``
     - Legt einen Arbeitszweig an bzw. wechselt in einen bestehenden.
   * - ``commit``, ``push``, ``pull``
     - Committet die Änderungen, überträgt sie zum Git-Server bzw. holt Änderungen vom Git-Server.
   * - ``merge_from_default``, ``abort_merge``
     - Übernimmt den aktuellen Stand von ``main`` in den Arbeitszweig bzw. bricht ein Zusammenführen ab.
   * - ``discard``
     - Verwirft nicht committete Änderungen eines Knotens oder aller Knoten (destruktiv).
   * - ``get_changes``, ``get_file_diff``, ``get_history``
     - Zeigt die geänderten Knoten, die Unterschiede einer Datei bzw. den Verlauf.

Werkzeuge für den Branch-Deploy:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - **Tool**
     - **Beschreibung**
   * - ``list_branch_deployments``
     - Listet die Deployments, die Branch-Deploys erlauben (``allowBranchDeploy``, siehe :doc:`../../config/cms/index`), und die dort deployten Branches.
   * - ``fast_deploy``
     - Deployt den aktuellen Stand des Arbeitsbereichs als Branch (Fast Deploy). Der Deploy läuft im Hintergrund; währenddessen sind keine Änderungen über den Agenten möglich.
   * - ``get_deploy_status``
     - Liefert Status und Ausgabe eines laufenden oder beendeten Deploys.
   * - ``remove_branch_deploy``
     - Entfernt den Branch-Deploy des eigenen aktuellen Arbeitszweiges (destruktiv). Branch-Deploys anderer Arbeitszweige können nur in der CMS-Oberfläche entfernt werden.

.. _cms-mcp-prompts:

Beispiel-Prompts
----------------

Die folgenden Prompts zeigen, was mit einem Agenten möglich ist. Sie können direkt verwendet oder an das eigene CMS angepasst werden.

**Lesen und Analysieren**

- *Gib mir einen Überblick über das CMS: welche Dienste, Karten und Editierthemen gibt es?*
- *Beschreibe die Abfrage Grundstücke: Suchfelder, Tabellenspalten und Hotlinks.*
- *Welche Felder hat der Layer Grundstücke laut ArcGIS Server? Welche davon fehlen in der Abfrage Grundstücke?*
- *Welche Warnungen hat das CMS und wie behebe ich sie?*

**Ändern**

- *Lege einen Arbeitszweig "abfrage-gebaeude" an.*
- *Lege für den Layer Gebäude eine Abfrage mit den Suchfeldern Adresse und Hausnummer an und zeige alle Felder außer OBJECTID in der Tabelle.*
- *Setze bei allen Abfragen des Dienstes Kataster MaxFeatures auf 500.*
- *Sortiere die Tabellenspalten der Abfrage Grundstücke alphabetisch.*
- *Lösche die Abfrage Test im Dienst Kataster. Prüfe vorher, wo sie verwendet wird.*

**Prüfen, Committen und Testen**

- *Zeige mir alle Änderungen seit dem letzten Commit.*
- *Committe die Änderungen mit einer passenden Nachricht und pushe sie.*
- *Übernimm den aktuellen Stand von main in meinen Arbeitszweig.*
- *Deploye meinen Arbeitszweig auf das Test-Deployment und zeige mir die Ausgabe.*

**Mehrere CMS** (siehe :ref:`cms-mcp-multiple-cms`)

- *Welche Dienste gibt es im CMS Kataster, aber nicht im CMS Leitungen?*
- *Vergleiche die Abfrage Grundstücke im CMS Kataster mit der im CMS Leitungen.*
- *Lege die Abfrage Grundstücke aus dem CMS Kataster auch im CMS Leitungen an.*

Sicherheit
----------

- Der Agent hat dieselben Rechte wie der Benutzer, der den Token erstellt hat, und arbeitet bei Git-Versionierung in dessen Arbeitsbereich.
- **Secrets** (Passwörter, Tokens, ...) werden dem Agenten nie im Klartext geliefert, sondern als ``********`` angezeigt.
- Ein Token ist maximal 90 Tage gültig und kann jederzeit widerrufen werden.
- Wo keine Änderungen nötig sind, sollte ein Token mit der Berechtigung **Lesen** verwendet werden. Arbeitet ein Agent selbstständig (z. B. im Autopilot-Modus), kann er auch destruktive Werkzeuge ohne Rückfrage bestätigen - Sicherheitsnetz sind dann der Arbeitszweig und die Git-Historie.
- Inhalte, die an den Agenten geliefert werden, verarbeitet das verwendete KI-Modell. Es sollte daher nur ein Modell bzw. Anbieter verwendet werden, der für die Daten des CMS freigegeben ist.

.. note::

    ``get_layer_fields`` fragt den Dienst immer über das CMS ab. Secret-Platzhalter (``{{secret-...}}``) in Dienst-URL und Zugangsdaten werden dabei serverseitig mit den Werten der Umgebung eines Deployments ersetzt, wie beim Deploy. Standardmäßig wird ``discovery-deployment`` (siehe :ref:`cms-config-mcp`) bzw. das erste Deployment verwendet, der Agent kann aber ein anderes Deployment angeben (z. B. *"Lies die Felder aus dem Test-Deployment"*). Die ersetzten Werte werden dem Agenten nie geliefert.
