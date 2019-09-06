===============================
Datakit data.world plugin
===============================


Commands to manage project integration with data.world.


* Free software: ISC license


Features
========

* Create a project (dataset) on data.world
* Push data files from a local directory to a data.world project

Installation
============

In order to use this plugin with a system-wide install of datakit_::

  $ pip install -e 'git+https://github.com/associatedpress/datakit-dworld.git#egg=datakit-dworld'


You'll need a config file at
  ``~/.datakit/plugins/datakit-dworld/config.json`` that looks like this::

    {
      "username": "USERNAME",
      "api_token": "API_TOKEN"
    }

  where ``USERNAME`` is the data.world username under which you want to handle
  data sets and ``API_TOKEN`` is the Admin token under your
  `Advanced settings`_ in data.world.


Usage
=====

* When in a datakit project, you'll have two new commands:

  * ``datakit dworld create``, which creates a new project (dataset) on
    data.world. Has a required ``--slug`` option to specify the slug used in
    the project's URLs.

  * ``datakit dworld push``, which uploads data files (CSV, etc.) from your
    project to data.world. Defaults to uploading any files in your project's
    ``data/public`` directory, but you can specify a different directory with
    ``--source-dir``.


Credits
========

This plugin was created with Cookiecutter_ and the `associatedpress/cookiecutter-datakit-plugin`_
project template (a modified version of the most excellent `audreyr/cookiecutter-pypackage`_).

.. _`Advanced settings`: https://data.world/settings/advanced
.. _datakit: http://datakit.ap.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`associatedpress/cookiecutter-datakit-plugin`: https://github.com/associatedpress/cookiecutter-datakit-plugin
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
