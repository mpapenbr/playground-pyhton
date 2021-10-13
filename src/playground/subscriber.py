import time
import datetime
import asyncio
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class Subscriber(ApplicationSession):
    """
    An application component that subscribes and receives events, and
    stop after having received 5 events.
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


