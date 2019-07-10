.. {{cookiecutter.github_repository_name}} documentation master file, created by
   sphinx-quickstart on Sun Jun 16 17:55:07 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: links.inc

Welcome to {{cookiecutter.github_repository_name}} documentation!
=================================================================

.. image:: https://api.travis-ci.org/alainivars/{{cookiecutter.github_repository_name}}.svg?branch=master
    :target: http://travis-ci.org/alainivars/{{cookiecutter.github_repository_name}}
    :alt: Build status

.. image:: https://coveralls.io/repos/github/alainivars/{{cookiecutter.github_repository_name}}/badge.svg?branch=master
    :target: https://coveralls.io/github/alainivars/{{cookiecutter.github_repository_name}}?branch=master
    :alt: Test coverage status

.. image:: https://requires.io/github/alainivars/{{cookiecutter.github_repository_name}}/requirements.svg?branch=master
    :target: https://requires.io/github/alainivars/{{cookiecutter.github_repository_name}}/requirements/?branch=master
    :alt: Requirements Status

.. image:: https://img.shields.io/pypi/dm/{{cookiecutter.github_repository_name}}.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.github_repository_name}}/
   :alt: pypi download

.. image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.github_repository_name}}.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.github_repository_name}}/
   :alt: python supported

.. image:: https://img.shields.io/pypi/l/{{cookiecutter.github_repository_name}}.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.github_repository_name}}/
   :alt: licence

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.github_repository_name}}.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.github_repository_name}}
   :alt: PyPi version

.. image:: https://landscape.io/github/alainivars/{{cookiecutter.github_repository_name}}/master/landscape.svg?style=flat
   :target: https://landscape.io/github/alainivars/{{cookiecutter.github_repository_name}}/master
   :alt: Code Health

.. image:: https://readthedocs.org/projects/{{cookiecutter.github_repository_name}}/badge/?version=latest
   :target: https://readthedocs.org/projects/{{cookiecutter.github_repository_name}}/?badge=latest
   :alt: Documentation status

.. image:: https://pypip.in/wheel/{{cookiecutter.github_repository_name}}/badge.svg
   :target: https://pypi.python.org/pypi/{{cookiecutter.github_repository_name}}/
   :alt: PyPi wheel

What is Drf-microservice
------------------------
{{cookiecutter.github_repository_name}} is a ready-to-use API skeleton:
    - `Cookiescutter-drf-microservice`_ generated it,
And you:
    - add your unittest and endpoints,
And it will help you to:
    - generate the documentation with Coreapi,
    - test it with Tox,
    - package it Docker,
    - deploy it (TODO with) Terraform or Ansible

Something disturb you in the code? Don't hesitate to open an issue and contribute.

Online documentation is here on `Readthedoc`_
Online source code available on `Github`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   functionalities
   devops_tools
   interact_with_api
   testing
   security_check
   docker
   aws

   releases_notes 

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
