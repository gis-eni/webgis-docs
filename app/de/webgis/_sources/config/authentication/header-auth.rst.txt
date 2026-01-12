================================
Headerbasierte Authentifizierung
================================

Bei dieser Methode werden der angemeldete Benutzername und die Rollen über **HTTP-Header-Variablen** des Requests ausgelesen.

Diese Methode eignet sich insbesondere, wenn das *WebGIS Portal* hinter einem *Reverse Proxy* betrieben wird. In diesem Fall übernimmt der *Reverse Proxy* die **Authentifizierung** und **Autorisierung** der Zugriffe. Beim Weiterleiten der Anfragen fügt er spezifische HTTP-Header hinzu, die Informationen über den angemeldeten Benutzer enthalten. Das *WebGIS Portal* liest diese Header-Variablen aus und verwendet sie zur **Zugriffssteuerung** für Karten und Kartendienste.

.. danger::
   Wird diese Methode verwendet, darf das *WebGIS Portal* **nur** über den *Reverse Proxy* erreichbar sein! Ist das Portal direkt zugänglich, besteht die Gefahr, dass Angreifer diese Methode missbrauchen. Das *WebGIS Portal* überprüft nicht, ob die Header-Variablen tatsächlich vom *Reverse Proxy* gesetzt wurden.

Die **headerbasierte Authentifizierung** wird über die Sektion ``header-authentication`` in der ``portal.config``-Datei aktiviert:

.. code-block:: xml

   <section name="header-authentication">
      <add key="use" value="true" />  <!-- default false -->
      <add key="username-variable" value="X-username" />
      <add key="roles-variable" value="X-roles" />

      <add key="extract-role-parameters" value="none" /> <!-- none, insideBrackets -->

      <add key="role-separator" value=";" />  <!-- default: , -->
      <add key="role-parameters-separator" value="," />  <!-- default: , -->

      <add key="user-prefix" value="header-user" />
      <add key="role-prefix" value="header-role" />

      <!-- Optional: -->
      <add key="extended-role-parameters-from-headers-prefix" value="X-AUTH-" />
      <add key="extended-role-parameters-from-headers" value="roleparam1,roleparam2" />
   </section>

Beschreibung der Konfigurationswerte
====================================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribut
     - Beschreibung
   * - ``use`` (default: ``false``)
     - Aktiviert die headerbasierte Authentifizierung.
   * - ``username-variable``
     - Definiert den **Header-Namen**, der den Benutzernamen enthält.
   * - ``roles-variable``
     - Definiert den **Header-Namen**, in dem die Benutzerrollen übergeben werden.
   * - ``extract-role-parameters`` (default: ``none``)
     - Rollenparameter ermöglichen eine **zusätzliche Einschränkung** von Rollen.  
       Wird beispielsweise einer Anwendergruppe die Rolle ``GEMEINDE`` zugewiesen, kann ein *Rollenparameter* bestimmen, auf welche Gemeinde sich die Berechtigung bezieht.  
       *Reverse Proxy*-Systeme können diese Parameter über die ``roles-variable`` übergeben.  
       - ``none`` → Keine Extraktion von Rollenparametern.  
       - ``insideBrackets`` → Rollenparameter werden innerhalb von Klammern nach der Rolle erwartet.  

       Beispiel für ``insideBrackets``:  
       ``role1(param1=1,param2=2);gemeinde(gemnr=123456)``  
       → **Rollen:** ``role1``, ``gemeinde``  
       → **Rollenparameter:** ``param1=1``, ``param2=2``, ``gemnr=123456``
   * - ``role-separator`` (default: ``,``)
     - Trennzeichen zwischen mehreren Rollen im ``roles-variable``-Header.
   * - ``role-parameters-separator`` (default: ``,``)
     - Trennzeichen für einzelne Rollenparameter beim *Parsing*.  
       Beispiel: ``(param1=1,param2=2,...)``
   * - ``user-prefix``, ``role-prefix``
     - Definiert Namensräume für Benutzer und Rollen, um Mehrdeutigkeiten bei mehreren Authentifizierungsmethoden zu vermeiden. Der Präfix wird mit ``::`` vom Benutzernamen getrennt.  

       Beispiel:  
       ``user-prefix = header-user``, Benutzername = ``maxmustermann``  
       → ``header-user::maxmustermann``  

       In der CMS-Berechtigungsverwaltung wird der vollständige Name inklusive Präfix 
       verwendet (``header-user::maxmustermann``).

   * - ``extended-role-parameters-from-headers-prefix``, ``extended-role-parameters-from-headers``
     - Diese beiden Parameter ermöglichen die Definition von **zusätzlichen Rollenparametern**, 
       die aus den HTTP-Headern extrahiert werden.  
       Der Präfix wird vor den Parameternamen gesetzt, um sie eindeutig zu kennzeichnen.  
        
       → Die Header ``X-AUTH-roleparam1`` und ``X-AUTH-roleparam2`` für das Beispiel von oben 
       werden als Rollenparameter extrahiert: Zusätzliche Rollenparameter könnten 
       dann ``roleparam1=wert1`` und ``roleparam2=wert2`` sein.
       
       
       
       
