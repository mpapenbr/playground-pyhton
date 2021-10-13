import time
import datetime
import asyncio
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class RegisterEndpoint(ApplicationSession):
    """
    An application component that subscribes and receives events, and
    stop after having received 5 events.
    """

    def onConnect(self):
        self.log.info("Client connected: {klass}", klass=ApplicationSession)
        if 'user' in self.config.extra:            
            self.join(self.config.realm, authid=self.config.extra['user'], authmethods=["ticket"])
        else:
            self.join(self.config.realm)

    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received ", authmethod=challenge.method)
        return self.config.extra['password']

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


