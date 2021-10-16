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
from autobahn.asyncio.wamp import ApplicationRunner
from click.decorators import pass_context

from playground import __version__
from playground.caller import CallEndpoint
from playground.greeter.greeter import Greeter
from playground.publish import Publisher
from playground.register import RegisterEndpoint
from playground.subscriber import Subscriber
from playground.subtwo.bar import Bar


@click.group()
@click.option('--url', help='url to fetch')
@click.version_option(__version__)
def main(url):
    """This is a dummy module which will be adapted to certain test purposes. """
    if (url is not None):
        click.echo(url)
        http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
        # http = urllib3.PoolManager()
        resp = http.request('GET', url)
        print(resp.status)


@main.command()
@pass_context
@click.option("--url", help="url of the crossbar server", default="ws://host.docker.internal:8090/ws")
@click.option("--realm", help="realm", default="demo", show_default=True)
@click.option("--topic", help="Subscribe to this topic", default="demo.sampletopic", show_default=True)
@click.option("--user", help="username")
@click.option("--password", help="password")
def subscribe(ctx, url, realm, topic, user, password):
    extra = {'topic':topic}
    if user is not None:
        extra['user'] = user
    if password is not None:
        extra['password'] = password
    runner = ApplicationRunner(url, realm, extra=extra)
    runner.run(Subscriber)


@main.command()
@pass_context
@click.option("--url", help="url of the crossbar server", default="ws://host.docker.internal:8090/ws")
@click.option("--realm", help="realm", default="demo", show_default=True)
@click.option("--topic", help="Subscribe to this topic", default="demo.sampletopic", show_default=True)
@click.option("--user", help="username")
@click.option("--password", help="password")
def publish(ctx, url, realm, topic, user, password):
    extra = {'topic':topic}
    if user is not None:
        extra['user'] = user
    if password is not None:
        extra['password'] = password
    runner = ApplicationRunner(url, realm, extra=extra)
    runner.run(Publisher)

@main.command()
@pass_context
@click.option("--url", help="url of the crossbar server", default="ws://host.docker.internal:8090/ws")
@click.option("--realm", help="realm", default="demo", show_default=True)
@click.option("--endpoint", help="name of the endpoint", default="demo.rpc.endpoint", show_default=True)
@click.option("--user", help="username")
@click.option("--password", help="password")
def register(ctx, url, realm, endpoint, user, password):
    extra = {'endpoint':endpoint}
    if user is not None:
        extra['user'] = user
    if password is not None:
        extra['password'] = password
    runner = ApplicationRunner(url, realm, extra=extra)
    runner.run(RegisterEndpoint)

@main.command()
@pass_context
@click.option("--url", help="url of the crossbar server", default="ws://host.docker.internal:8090/ws")
@click.option("--realm", help="realm", default="demo", show_default=True)
@click.option("--endpoint", help="name of the endpoint", default="demo.rpc.endpoint", show_default=True)
@click.option("--user", help="username")
@click.option("--password", help="password")
def call(ctx, url, realm, endpoint, user, password):
    extra = {'endpoint':endpoint}
    if user is not None:
        extra['user'] = user
    if password is not None:
        extra['password'] = password
    runner = ApplicationRunner(url, realm, extra=extra)
    runner.run(CallEndpoint)
