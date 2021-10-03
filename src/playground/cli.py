"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mplayground` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``playground.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``playground.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import sys

import certifi
import click
import urllib3

from playground import __version__
from playground.greeter.greeter import Greeter
from playground.subtwo.bar import Bar


@click.command()


@click.option('--url', help='url to fetch')
@click.version_option(__version__)
def main(url):
    """This is a dummy module which will be adapted to certain test purposes. """
    if (url != None):
        click.echo(url)
        http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
        # http = urllib3.PoolManager()
        resp = http.request('GET', url )
        print(resp.status)




