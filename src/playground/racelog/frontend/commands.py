"""commands for accessing public available data from"""
from autobahn.asyncio.wamp import ApplicationRunner
import click


from playground.racelog.caller import CallEndpoint
from playground.racelog.frontend.list_events import ListEvents




@click.command("events")
@click.pass_obj
def list(obj):
    """list stored events"""
    obj['endpoint'] = "racelog.public.get_events"
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(ListEvents)




    