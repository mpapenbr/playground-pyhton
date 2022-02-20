"""commands for register dummy events"""
import asyncio
import click
from autobahn.asyncio.wamp import ApplicationRunner

from playground.basesession import BaseSession



class SendExtrData(BaseSession):
    """
    sends data to an endpoint
    """
    async def onJoin(self, details):
        try:
            x = await self.call(self.config.extra['endpoint'], self.config.extra['event_key'], self.config.extra['rpc_data'])
            print(x)
        except Exception as e:
            print(f"Got exception {e}. Aborting")             
        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


@click.command("pit")
@click.pass_obj
@click.argument("eventKey")
def extraPit(obj,eventkey):
    """send extra data for event"""
    # obj['endpoint'] = "racelog.dataprovider.register_provider"
    obj['event_key'] = eventkey
    obj['rpc_data'] = {
        "track": {"trackId":12, "pit": {"entry": 1, "exit": 2}}
        }
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(SendExtrData)
