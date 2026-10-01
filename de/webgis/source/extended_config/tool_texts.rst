======================
Werkzeugtexte anpassen
======================

Alle Texte der Werkzeuge (Bezeichnungen, Beschreibungen, Hinweise, Fehlermeldungen, Eingabe-Tipps, ...)
sind mehrsprachig und in Sprachdateien (Markdown) abgelegt. Im Installationspaket gibt es dafür je Sprache
ein Verzeichnis (``l10n/de``, ``l10n/en``, ...) und darin **eine Datei pro Werkzeug**,
z. B. ``Tools.Coordinates.md``.

Diese Dateien im Installationspaket sollten **nicht geändert** werden, da sie bei einem Update wieder
überschrieben werden. Angepasste Texte werden stattdessen im ``etc``-Verzeichnis abgelegt.

Vorgehensweise
==============

1. Im Verzeichnis ``etc`` den Ordner ``api/l10n`` anlegen.
2. Darin für jede betroffene Sprache einen Unterordner anlegen (``de``, ``en``, ...).
3. Die Datei des Werkzeugs aus dem Installationspaket dorthin kopieren,
   z. B. ``etc/api/l10n/de/Tools.Coordinates.md``.
4. In der kopierten Datei **nur die Einträge belassen, die tatsächlich geändert werden sollen**.
   Alle anderen Einträge werden gelöscht.
5. Den Anwendungspool (ApplicationPool) neu starten.

.. code:: text

  etc/
  └── api/
      └── l10n/
          ├── de/
          │   └── Tools.Coordinates.md
          └── en/
              └── Tools.Coordinates.md

.. important::

  Die Texte werden **nur beim Start der Anwendung** eingelesen. Nach Änderungen muss daher der
  **ApplicationPool neu gestartet** werden.

Wie die Anwendung die Texte lädt
--------------------------------

1. Zuerst werden alle Markdown-Dateien aus dem Installationspaket gelesen.
2. Danach werden die Dateien in ``etc/api/l10n`` gesucht. Die dort enthaltenen Werte
   **überschreiben** die bereits gelesenen Werte.

Einträge, die in der angepassten Datei nicht vorkommen, behalten daher den Standardwert aus dem Installationspaket.
Bei einem Update werden so neue oder geänderte Standardtexte übernommen, ohne dass die eigenen Anpassungen verloren gehen.

Aufbau der Dateien
==================

Die Dateien sind in **Markdown** aufgebaut. Die **Überschriften** definieren dabei die Id eines Textes,
gefolgt von einem Doppelpunkt. Dahinter steht die Übersetzung. Bei längeren Texten steht der Text nicht
in der Überschriftenzeile, sondern darunter als **Body**.

.. code:: text

  # name: Koordinaten / Höhe

  Koordinaten und Höhenwerte abfragen

  # container: Abfragen

  # enter-coordinates: Koordinaten eingeben

  # upload:
  ## label1:

  Hier können Koordinaten hochgeladen werden. ...

  ## exception-too-many-points: Es dürfen maximal {0} Koordinatenzeilen hochgeladen werden

.. important::

  Ob ein Text **direkt in der Überschriftenzeile** oder **im Body** steht, kann nicht frei gewählt werden,
  sondern wird von der Anwendung vorgegeben. In der Regel stehen einfache Übersetzungen (Bezeichnungen)
  in der Zeile, längere Beschreibungen im Body. Am besten wird die Form aus dem Installationspaket beibehalten.

Hierarchie
----------

Die **Hierarchie der Überschriften** (``#``, ``##``, ``###``, ...) muss eingehalten werden. Sie bildet den
Pfad der Id, über den die Anwendung auf den Text zugreift. Das gilt auch, wenn in der angepassten Datei nur
ein einzelner Eintrag steht: die übergeordneten Überschriften müssen mit angegeben werden.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Id
     - Position in der Datei
   * - ``upload.label1``
     - Body-Text unter ``# upload:`` / ``## label1:``
   * - ``upload.sketch.label1``
     - Text hinter ``# upload:`` / ``## sketch:`` / ``### label1:``

Ids dürfen daher nicht umbenannt und Ebenen nicht verschoben werden, nur die Texte selbst.

Platzhalter wie ``{0}`` müssen erhalten bleiben. Sie werden von der Anwendung durch Werte ersetzt.

Bei Werkzeugen gibt es die Einträge ``# name:`` (Anzeigename des Werkzeugs) und ``# container:``
(Anzeigename des Containers, in dem das Werkzeug aufgelistet wird).

Beispiel: Koordinatenwerkzeug
=============================

Datei ``etc/api/l10n/de/Tools.Coordinates.md``. Geändert werden ein Paragraph (Body) unter
``upload`` / ``label1``, eine einfache Bezeichnung (``tip-label``) und der Eingabe-Tipp (``tip``).
Alle anderen Texte bleiben unverändert und stehen deshalb nicht in der Datei:

.. code:: text

  # upload:

  ## label1:

  Es können Koordinaten hochgeladen werden. Die Koordinaten müssen als CSV Dateien
  vorliegen mit einem Strichpunkt als Trennzeichen. Die Spalten der CSV Datei sollten
  Punktname/nummer, Rechtswert und Hochwert entsprechen. Die erste Zeile wird als Tabellenüberschrift
  interpretiert.

  # tip-label: Tipp für die Eingabe

  # tip:

  md:Grundsätzlich gibt es projizierte Koordinaten (GK-M34, Web Mercator, ...) und geographische Koordinaten (WGS 84, GPS).
  Bei der Eingabe sollte daher immer zuerst das Koordinatensystem ausgewählt werden.

  **GK-M34**
  Rechtswert: -67772,43
  Hochwert: 215837,13

Das Präfix ``md:`` am Beginn des Textes kennzeichnet den Inhalt als Markdown.
Der Eingabe-Tipp wurde früher über die Datei ``tip.txt`` im ``etc``-Verzeichnis konfiguriert.
Diese Datei wird nicht mehr verwendet.
