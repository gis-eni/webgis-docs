===========================
Tool ``Measure Distance``
===========================

For the **measure distance tool** to also be usable in **3D**, a file ``3d.xml`` must be created in the directory ``etc/measure``. The structure of this file corresponds to the configuration for the elevation query. However, there are some restrictions:

- Only **one** elevation query may be defined.
- The result must be a **numeric elevation value** (without text additions such as "müA").

Example configuration:

.. code-block:: xml

   <!-- Example for an ArcGIS Server Servie -->
   <xml>
        <heightabovedatum
            type="ags"
            srs="31256"
            name="DTM"
            server="my-server.com"
            service="https://my-server.com/../rest/.../servicename/MapServer"

            user="username" pwd="my-passw0rd" tokenExpiration="60"

            rastertheme="DGM"
            expression="{0:0.00}" />
   </xml>

.. code-block:: xml

   <!-- Example for an ArcGIS Server Mosaic services -->
   <xml>
        <heightabovedatum
            type="ags-mosaic"
            srs="31256"
            name="DTM"
            server="my-server.com"
            service="https://my-server.com/../rest/.../servicename/MapServer"

            user="username" pwd="my-passw0rd" tokenExpiration="60"

            rastertheme="DGM"
            expression="{0:0.00}" />
   </xml>

.. code-block:: xml

   <!-- Example for an ArcGIS Server ImageServer Service -->
   <xml>
      <heightabovedatum type="ags-imageserver"
                  srs="31255"

                  user="username" pwd="my-passw0rd" tokenExpiration="60"

                  server="my-server.com"
                  service="https://my-server.com/arcgis/rest/services/.../ImageServer"
                  rastertheme="0"
                  expression="+{0:.00} müA"
                  />
   </xml>

.. code-block:: xml

   <!-- Example for a IMS Service -->
   <xml>
      <heightabovedatum
           type="ims"
           srs="31256"
           name="DTM"
           server="my.server.com:8010"
           service="hoehenservice"
           rastertheme="hoeheDTM"
           expression="{0:0.00}" />
   </xml>

.. note::

   ``user`` and ``pwd`` are only required if the service is protected.
   For protected AGS services, it is also recommended to set the ``tokenExpiration`` parameter,
   to define the validity of the token. The value is specified in minutes.
   If a value that is too high is specified here, a token may not be retrievable
   (long-living tokens).
