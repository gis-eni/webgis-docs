.. _css-portal:

``portal.css`` – Logo und Navbar (Portal)
==========================================

Die Datei ``portal.css`` ist ausschließlich für das *WebGIS Portal* relevant und ergänzt die
:doc:`default-css`. Sie wird hauptsächlich verwendet, um ein **Unternehmenslogo in der
Navigationsleiste** einzubinden.

.. note::

    Die für alle WebGIS-Anwendung Navbar und Logos über die ``site.css`` angepasst werden können,
    siehe :doc:`site-css`, ist die Verwendung der ``portal.css`` mittlerweile fast obsolet und 
    nur noch aus gründen der Abwärtskompatibilität vorhanden. Einziger Anwendungsfall ist die Anpassung des Logos 
    in der Navigationsleiste einer bestimmten Portal Seite (also wenn mehrere Portal Seiten existieren,
    die ein unterschiedliches Logo benötigen).
    Hier greift dann die ``portal.css`` auf Portal-Ebene und überschreibt die ``site.css`` auf globaler Ebene.
    
Ablageort
---------

.. code-block:: none

    portal/
    └── wwwroot/
        └── content/
            └── companies/
                 └── <company>/
                    ├── portal.css
                    └── img/
                        └── logo.png    ← Logo-Bild (optional hier ablegen)

``<company>`` entspricht dem Wert des ``company``-Schlüssels aus der ``portal.config``.

.. note::

    Das Verzeichnis ``/<company>/`` wird bei einem Update **nicht** überschrieben.
    Alle Anpassungen darin bleiben erhalten.

Ist in der ```portal.config`` folgender Key gesetzt, kann eine Karten Author den Inhalt der ``default.css``
auf dem Portal direkt eingeben, ohne dass die Datei physisch im Repository abgelegt werden muss:

.. code-block:: xml

     <add key="portal-custom-content-rootpath" value="..../webgis-repository/portal-page-content" />

Logo in der Navbar einbinden
-----------------------------

Das Logo in der Navigationsleiste des Portals kann über den CSS-Selektor
``.webgis-portal-navbar-logo`` ersetzt werden:

.. code-block:: css
    
    .navbar-brand {
        background-image: url('../img/logo.png');
        background-size: 28px;
    }

Das Logo-Bild wird am besten im selben Unternehmensverzeichnis abgelegt, z. B. unter
``wwwroot/custom/<company>/img/logo.png``. Der relative Pfad ``../img/logo.png`` bezieht
sich dabei auf den Speicherort der ``portal.css``.
