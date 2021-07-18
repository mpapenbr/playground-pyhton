========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/playground-python/badge/?style=flat
    :target: https://playground-python.readthedocs.io/
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/mpapenbr/playground-python.svg?branch=main
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/mpapenbr/playground-python

.. |requires| image:: https://requires.io/github/mpapenbr/playground-python/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/mpapenbr/playground-python/requirements/?branch=main

.. |version| image:: https://img.shields.io/pypi/v/playground.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/playground

.. |wheel| image:: https://img.shields.io/pypi/wheel/playground.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/playground

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/playground.svg
    :alt: Supported versions
    :target: https://pypi.org/project/playground

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/playground.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/playground

.. |commits-since| image:: https://img.shields.io/github/commits-since/mpapenbr/playground-python/v0.1.1.svg
    :alt: Commits since latest release
    :target: https://github.com/mpapenbr/playground-python/compare/v0.1.1...main



.. end-badges


Playground for python stuff

* Free software: MIT license

Installation
============

::

    pip install playground

You can also install the in-development version with::

    pip install https://github.com/mpapenbr/playground-python/archive/main.zip


Documentation
=============


https://playground-python.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
