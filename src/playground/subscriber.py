import asyncio
import datetime
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner
from autobahn.asyncio.wamp import ApplicationSession

from playground.basesession import BaseSession


class Subscriber(BaseSession):
    """
    prints incoming data from connected topic to console
    """

    async def onJoin(self, details):
        print(details)
        print(self.config.extra)
        # self.log.info(f"onJoin {details}")
        def on_recv(data:any):
            print(f"{datetime.datetime.now().isoformat()}: {data}")
        
        try:
            await self.subscribe(on_recv, self.config.extra['topic'])
        except Exception as e:
            print(f"Got exception {e}. Aborting")
            self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


