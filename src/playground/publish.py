import asyncio
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner
from autobahn.asyncio.wamp import ApplicationSession

from playground.basesession import BaseSession


class Publisher(BaseSession):
    """
    sends the current time (x5) to a topic
    Sidenode: crossbar does not throw an exception is user is not allowed to publish on that topic. 
    Messages are just discarded on server
    """
    
    async def onJoin(self, details):
        print(details)
        print(self.config.extra)
        # self.log.info(f"onJoin {details}")

        for _ in range(0,5):
            try:
                x = self.publish(self.config.extra['topic'], time.time())
                print(x)
            except Exception as e:
                print(f"Got exception {e}. Aborting")             
        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


