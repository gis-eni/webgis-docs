.. _css-cms:

``cms.css`` – Styling der CMS-Oberfläche
=========================================

Über die Datei ``cms.css`` kann die Primärfarbe der *WebGIS CMS*-Oberfläche angepasst werden.

Ablageort
---------

Im Gegensatz zu ``default.css`` und ``portal.css`` wird die ``cms.css`` **nicht** im
``wwwroot``-Verzeichnis der Anwendung abgelegt, sondern im **Dateisystem**, in dem die
CMS-Bäume verwaltet werden.

Der ``path``-Wert eines ``cms-item``-Eintrags in der ``cms.config`` zeigt auf den Ordner des
jeweiligen CMS-Baums. Die ``cms.css`` muss **eine Ebene darüber** – also im **übergeordneten
Verzeichnis** dieses Ordners – abgelegt werden.

Beispiel: In der ``cms.config`` ist folgender Eintrag konfiguriert:

.. code-block:: json

    {
      "id": "webgis-release-default",
      "path": "C:\\apps\\webgis-repositoy\\cms\\param\\webgis-release-default",
      "scheme": "webgis"
    }

Dann wird die ``cms.css`` hier abgelegt:

.. code-block:: none

    C:\apps\webgis-repositoy\cms\param\
    ├── cms.css                        ← gilt für alle CMS-Bäume in diesem Verzeichnis
    └── webgis-release-default\        ← CMS-Baum-Ordner (path in cms.config)

.. important::

    Die Datei liegt **neben** dem Baum-Ordner, **nicht darin**.

Mehrere CMS-Bäume mit unterschiedlichem Styling
-------------------------------------------------

Wenn in einem Verzeichnis mehrere CMS-Bäume liegen und jeder eine andere Darstellung erhalten
soll, muss die Datei nach dem Schema ``cms.<baum-ordner-name>.css`` benannt werden:

.. code-block:: none

    C:\apps\webgis-repositoy\cms\param\
    ├── cms.webgis-release-default.css ← Styling nur für diesen Baum
    ├── cms.webgis-custom.css          ← Styling nur für diesen Baum
    ├── webgis-release-default\
    └── webgis-custom\

Eine unbenannte ``cms.css`` (ohne Baum-Namen) gilt als **Fallback** für alle Bäume im selben
Verzeichnis, die keine eigene benannte CSS-Datei haben.

Verfügbare CSS-Variablen
------------------------

Für das CMS stehen nur die **Brand-Variablen** zur Verfügung. Diese werden im Selektor
``:root { ... }`` definiert:

.. code-block:: css

    :root {
        /* Primärfarbe der CMS-Oberfläche */
        --webgis-brand-primary: #ff5a9a;

        /* Optional: helle Variante (wird sonst automatisch berechnet) */
        --webgis-brand-primary-light: #ffd5ff;
    }

.. list-table::
   :widths: 40 20 40
   :header-rows: 1

   * - Variable
     - Standardwert
     - Beschreibung
   * - ``--webgis-brand-primary``
     - ``#59c134``
     - Primärfarbe der CMS-Oberfläche.
   * - ``--webgis-brand-primary-light``
     - *(berechnet)*
     - Helle Variante der Primärfarbe. Wird automatisch aus ``--webgis-brand-primary``
       berechnet, wenn nicht explizit gesetzt.

