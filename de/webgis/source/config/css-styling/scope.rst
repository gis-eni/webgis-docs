Geltungsbereich und Ebenen
============================

Die unterschiedlichen CSS Dateien können auf mehreren Ebenen angepasst werden, wobei eine höhere Ebene die Werte 
der darunterliegenden Ebene überschreibt.

``default.css``:
^^^^^^^^^^^^^^^^^^

Verwendet von: Portal, API
Geltungsbereich: Viewer, Portalseiten, API-Seiten

1. Mitgelieferte Standardwerte, die in der Datei ``default.css`` definiert sind. 
   Diese Datei soll nicht überschrieben werden.

2. Company Ebene: 
   Für eine **Company** (definiert in der ``portal.config``) wird über das deployment tool
   eine eigene ``default.css`` Datei in das Verzeichnis 
   ``api/wwwroot/content/styles/<company>/default.css`` kopiert. 

3. Portal Seiten Ebene:
   Für eine Portal Seite kann eine eigene ``default.css`` Datei in das Verzeichnis 
   ``portal/wwwroot/portals/<portal-id>/map-default.css`` kopiert werden.
   Alternativ kann die Datei auch in der Admin Oberfläche auf der entsprechenden 
   Portalseite bearbeitet werden (zB, wenn Anwendung als **Container** läuft).

``portal.css``:
^^^^^^^^^^^^^^^

Verwendet von: Portal
Geltungsbereich: Portalseiten (nicht Viewer!)

1. Mitgelieferte Standardwerte, die in der Datei ``portal.css`` definiert sind. 
   Diese Datei soll nicht überschrieben werden.

2. Company Ebene: 
   Für eine **Company** (definiert in der ``portal.config``) wird über das deployment tool
   eine eigene ``portal.css`` Datei in das Verzeichnis 
   ``portal/wwwroot/content/companies/<company>/portal.css`` kopiert.

3. Portal Seiten Ebene:
   Für eine Portal Seite kann eine eigene ``portal.css`` Datei in das Verzeichnis 
   ``portal/wwwroot/portals/<portal-id>/portal.css`` kopiert werden.
   Alternativ kann die Datei auch in der Admin Oberfläche auf der entsprechenden 
   Portalseite bearbeitet werden (zB, wenn Anwendung als **Container** läuft).

``site.css``:
^^^^^^^^^^^^^^

Verwendet von: Portal, API, CMS
Geltungsbereich: Portalseiten, Login-Seiten, Admin-Seiten (nicht Viewer!)

1. Mitgelieferte Standardwerte, die in der Datei ``site.css`` definiert sind. 
   Diese Datei soll nicht überschrieben werden.

2. Company Ebene: 
   Für eine **Company** (definiert in der ``portal.config``) wird über das deployment tool
   eine eigene ``site.overrides.css`` angelegt, die ebenfalls nicht überschrieben werden soll,
   das sie bei jedem deployment ersetzt wird. Änderungen in dieser Datei sollte außschließlich
   über das deployment tool erfolgen (modify-css)

   Alternativ können die entsprechenden Werte über Umgebungsvariablen gesetzt werden, wenn die Anwendung
   nicht mit dem ``deployment tool`` installiert wird, sondern über **Container Images**.

``cms.css``:
^^^^^^^^^^^^^^

Verwendet von: CMS
Geltungsbereich: CMS-Oberfläche

Überschreibt die Werte für die CMS Oberfläche (alle CMS Bäume).
Legt man eine Datei ``cms.{cms-id}.css`` an, werden die Werte nur für den entsprechenden 
CMS Baum überschrieben.

Die Datei wird immer ins selbe Verzeichnis kopiert, in der auch der CMS Baum liegt
(gleiche Ebene, nicht NICHT ins Baumverzeichnis selbst!).

Ist nur notwendig, wenn für spezielle CMS Bäume andere Farben als die Standardwerte benötigt werden.
Ansonsten reicht es aus die ``site.css`` anzupassen, da die CMS Oberfläche die Werte 
aus der ``site.css`` übernimmt.