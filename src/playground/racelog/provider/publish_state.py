import asyncio
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner
from autobahn.asyncio.wamp import ApplicationSession

from playground.basesession import BaseSession


class PublishState(BaseSession):
    """
    fake publish a state
    """
    def onJoin(self, details):
        try:
            self.publish(self.config.extra['endpoint'], "fakePublish")            
        except Exception as e:
            print(f"Got exception {e}. Aborting")             
        self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


