"""commands for register dummy events"""
import click
from autobahn.asyncio.wamp import ApplicationRunner
from click.core import Group

from playground.racelog.caller import CallEndpoint
from playground.racelog.provider.list_provider import ListProviders


@click.command("list")
@click.pass_obj
def list(obj):
    """list providers"""
    obj['endpoint'] = "racelog.public.list_providers"
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(ListProviders)

@click.command("remove")
@click.argument("eventKey")
@click.pass_obj
def remove(obj,eventkey):
    """remove provider"""
    obj['endpoint'] = "racelog.dataprovider.remove_provider"
    obj['rpc_data'] = eventkey
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(CallEndpoint)



    