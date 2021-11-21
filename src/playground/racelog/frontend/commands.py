"""commands for accessing public available data from"""
import click
from autobahn.asyncio.wamp import ApplicationRunner

from playground.racelog.caller import CallEndpoint
from playground.racelog.frontend.get_event import GetEventById
from playground.racelog.frontend.list_events import ListEvents


@click.command("events")
@click.pass_obj
def list(obj):
    """list stored events"""
    obj['endpoint'] = "racelog.public.get_events"
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(ListEvents)

@click.command("eventinfo")
@click.argument("eventid", type=click.INT)
@click.pass_obj
def eventinfo(obj,eventid):
    """request data for event with id"""
    obj['endpoint'] = "racelog.public.get_event_info"
    obj['rpc_data'] = eventid
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(GetEventById)



    