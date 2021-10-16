import asyncio
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner
from autobahn.asyncio.wamp import ApplicationSession

from playground.basesession import BaseSession


class CallEndpoint(BaseSession):
    """
    sends 'some caller value' to the endpoint
    """
   
    async def onJoin(self, details):
        print(details)
        print(self.config.extra)
        # self.log.info(f"onJoin {details}")

        
        try:
            x = await self.call(self.config.extra['endpoint'], "some caller value")
            print(x)
        except Exception as e:
            print(f"Got exception {e}. Aborting")             
        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


