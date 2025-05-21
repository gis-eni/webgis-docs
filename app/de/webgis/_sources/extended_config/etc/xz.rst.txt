===================================
Werkzeug ``XZ (Koordinaten/Höhen)``
===================================

.. note::

  In früheren **WebGIS 4.0**-Installationen befand sich im **API-App-Verzeichnis** der 
  Ordner ``system/proj``, in dem Projektionen definiert wurden. Diese Konfiguration wurde 
  nun in das Verzeichnis ``etc/coordinates/proj`` verschoben.

Zusätzlich zu diesem ``proj``-Ordner kann im Verzeichnis ``etc/coordinates`` nun optional 
eine Datei ``h.xml`` erstellt werden. In dieser Datei wird festgelegt, welche **Höhenwerte** 
zusätzlich zu den Koordinaten ermittelt werden.  

Die Struktur von ``h.xml`` entspricht der Konfigurationsdatei des Höhenabfragetools 
(``etc/heightabovedatum``).