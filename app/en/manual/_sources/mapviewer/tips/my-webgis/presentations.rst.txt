My Presentation Variants
===========================

Since the topic tree becomes increasingly extensive and confusing due to the large number
of data layers, *presentation variants* were introduced. These are intended to replace the
topic tree and provide the most important map presentations at the push of a button.
Since this concept has also become increasingly extensive due to the complexity and number of different application requirements,
**My Presentation Variants** was developed.

With this, the user has the option to reuse the current configuration of the data layers under a
descriptive name, again and again. Creating **user-defined presentation variants**
is done per map. Any number of *presentation variants* can be created.
If additional services were loaded into the map for a presentation variant, these are also
loaded again in the future when the user applies the *presentation variant*. This method replaces
saving projects in this regard.

.. note::
   An advantage over saving projects here is that any number of
   **user-defined presentation variants** can be created in a map, instead of having to open a
   new project each time.

.. note::
   For standard activities, it is recommended to always open WebGIS with the same map and
   create recurring *presentations* there.


Advantages:

* Several **user-defined presentation variants** can be created per map and accessed directly
* If the presentation variants switch on (map) services that are not in the map at startup, these are automatically added as needed.

Limitations:

* No long-term guarantee can be given for **user-defined presentations** either,
  that they will continue to work the same way if the (map) services need to be changed in the background.
  However, it is far easier to recreate a single presentation variant than to recreate entire projects.
