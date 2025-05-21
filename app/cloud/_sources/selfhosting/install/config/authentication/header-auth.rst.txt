Headerbasierte Authentifizierung
================================

Bei dieser Methode werden der angemeldete Benutzername und die Rollen über
**HTTP Header Variablen** des Requests ausgelesen.

Diese Methode macht Sinn, wenn sich die Installation des *WebGIS Portals* hinter 
einem *Reverse Proxy* befindet. Dabei erfolgt die *Authentifizierung* und 
die *Autorisierung* der Zugriffe über den *Reverse Proxy*. Bei der Weiterleitung
werden vom *Reverse Proxy* jedem Request Header Variablen hinzugefügt, die 
Auskunft über den angemeldeten Benutzer enthalten. Das *WebGIS Portal* liest 
diese Header Variablen aus und verwendet sie zur *Autorisierung* von Karten 
und Kartendiensten.

.. note::
   Verwendet man diese Methode, darf das *WebGIS Portal* nur über den *Reverse
   Proxy* erreichbar sein! Ist das *WebGIS Portal* auch frei zugänglich, könnte 
   diese Methode von Angreifern ausgenutzt werden. 
   Das *WebGIS Portal* überprüft nicht, ob die Header Variablen erst vom *Reverse 
   Proxy* gesetzt wurden.

Die *headerbasierte Authentifizierung* wird über die ``portal.config``-Datei über
die *Section* ``header-authentication`` aktiviert:

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
    </section>

Beschreibung der Keys
---------------------

* ``use`` (default: false)
  
  Gibt an, dass die headerbasierte Authentifizierung angewendet wird.

* ``username-variable``
  
  Die Header Variable, in die der Benutzername übergeben wird .

* ``roles-variable`` 
  
  Die Header Variable, in der die Benutzerrollen übergeben werden.

* ``extract-role-parameters`` default: none 
  
  Rollenparameter sind spezielle Parameter, die einem Anwender zugeordnet werden können.
  Damit kann eine Rolle noch weiter eingeschränkt werden. Gibt man einer Anwendergruppe 
  beispielsweise die Rolle ``GEMEINDE`` kann über einen *Rollen Parameter* 
  gesteuert werden, um welche Gemeinde es sich handelt. Alle Anwender sehen dann die
  *Gemeinde* Anwendung aber über einen Filter später nur die entsprechende Gemeinde.

  *Reverse Proxy Systeme* können diese Parameter übergeben. Erfolgt dies über 
  ``roles-variable``, kann hier angegeben werden, wie das *Parsing* des Rollenwert
  erfolgt.

  Stellt man hier ``insideBrackets``, erwartet das Portal den Rollenparameter innerhalb 
  von Klammern nach der Rolle:

  ``role1(param1=1,param2=2);gemeinde(gemnr=123456)``

  => **Rollen:** ``role1``, ``gemeinde``
  => **Rollen Parameter:** ``param1=1``, ``param2=2``, ``gemnr=123456``

* ``role-separator`` (default ``,``)
  
  Enthält der Wert aus ``roles-variable`` mehrere Rollen, kann hier das 
  Trennzeichen angegeben werden.

* ``role-parameters-separator``  (default ``,``)
  
   Das Trennzeichen, das zum *Parsen* einzelner Rollenparameter verwendet werden sollte.
  
  ``(param1=1,param2=2,...)`` 

* ``user-prefix``, ``role-prefix``
  
  Verwendet man mehrere Authentifizierungsmethoden kann über Namensräume 
  (Prefixes) unterschieden werden, woher ein Nutzer kommt. Ansonsten kann es
  zu falschen Interpretationen von Berechtigungen kommen, wenn der gleiche 
  Name in unterschiedlichen Systemen vorkommt. 
  Der Namensraum (Prefix) wird mittels ``::`` vom ursprünglichen Namen getrennt.

  Beispiel: ``user-prefix = header-user``, ``username = maxmustermann``
  => ``header-user::maxmustermann``  

  Im CMS stellt man die entsprechende Berechtigung inklusive Namensraum ein 
  (``header-user::maxmustermann``).


