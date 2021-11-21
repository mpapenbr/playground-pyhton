"""commands for register dummy events"""
import click
from autobahn.asyncio.wamp import ApplicationRunner

from playground.racelog.caller import CallEndpoint


@click.command("delete")
@click.argument("eventId", type=click.INT)
@click.pass_obj
def delete(obj,eventid):
    """delete event including data.
    The event is referenced by its internal database id.
    """
    obj['endpoint'] = "racelog.admin.event.delete"
    obj['rpc_data'] = eventid
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(CallEndpoint)

