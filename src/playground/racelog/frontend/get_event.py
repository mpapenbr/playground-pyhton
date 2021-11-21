import asyncio
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner
from autobahn.asyncio.wamp import ApplicationSession

from playground.basesession import BaseSession


class GetEventById(BaseSession):
    """
    get event by eventId
    """
    async def onJoin(self, details):
        try:
            x = await self.call(self.config.extra['endpoint'], self.config.extra['rpc_data'])
            print(x)
        except Exception as e:
            print(f"Got exception {e}. Aborting")             
        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


