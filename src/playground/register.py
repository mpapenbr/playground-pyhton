import asyncio
import datetime
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner

from playground.basesession import BaseSession


class RegisterEndpoint(BaseSession):
    """
    returns the input data along with a prefixed timestamp
    """

    

    async def onJoin(self, details):
        print(details)
        print(self.config.extra)
        # self.log.info(f"onJoin {details}")
        def time_service(data:any):
            return f"{datetime.datetime.now().isoformat()}: {data}"
        
        try:
            await self.register(time_service, self.config.extra['endpoint'])
        except Exception as e:
            print(f"Got exception {e}. Aborting")
            self.leave()

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


