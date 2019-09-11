===============================
DataKit data.world plugin
===============================


Commands to manage project integration with data.world.


* Free software: ISC license


Features
========

* Create a project (dataset) on data.world
* Push data files from a local directory to a data.world project


Setup instructions
==================

Assuming you have DataKit_ installed, run the following to install the
`datakit-dworld` plugin::

  $ pip install -e 'git+https://github.com/associatedpress/datakit-dworld.git#egg=datakit-dworld'

Create a configuration file at ``~/.datakit/plugins/datakit-dworld/config.json``
to tell the plugin about your data.world account. It should look like this::

    {
      "username": "USERNAME",
      "api_token": "API_TOKEN"
    }

Replace ``USERNAME`` with the username you will use on data.world to publish
datasets.

`Log in to data.world`_ as that same user, and go to your `Advanced settings`_
page. You'll see two long tokens under the "API Token" section. Copy the one
labeled "Admin", and paste that into your configuration file in place of
``API_TOKEN``.


How to use
==========

When in a datakit project, you'll have two new commands:

  * ``datakit dworld create``, which creates a new project (dataset) on
    data.world. This requires a ``--slug`` option to help set the project's
    URL. For example, if your username is ``example-human``, then running
    ``datakit dworld create --slug example-dataset`` will create an empty
    dataset at ``https://data.world/example-human/example-dataset``.

  * ``datakit dworld push``, which uploads data files (CSV, etc.) from your
    project to data.world. This defaults to uploading any files in your
    project's ``data/public`` directory, but you can specify a different
    directory with ``--source-dir``.


Credits
========

This plugin was created with Cookiecutter_ and the `associatedpress/cookiecutter-datakit-plugin`_
project template (a modified version of the most excellent `audreyr/cookiecutter-pypackage`_).

.. _`Advanced settings`: https://data.world/settings/advanced
.. _DataKit: http://datakit.ap.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Log in to data.world`: https://data.world/login
.. _`associatedpress/cookiecutter-datakit-plugin`: https://github.com/associatedpress/cookiecutter-datakit-plugin
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
