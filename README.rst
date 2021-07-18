========
Overview
========


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
