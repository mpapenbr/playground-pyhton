import asyncio
import time
from os import environ

from autobahn.asyncio.wamp import ApplicationRunner
from autobahn.asyncio.wamp import ApplicationSession


class BaseSession(ApplicationSession):
    """
    base class for handling basic connection setup    
    """
    def onConnect(self):
        self.log.info("Client connected: {klass}", klass=ApplicationSession)
        if 'user' in self.config.extra and len(self.config.extra['user'].strip()) > 0:
            self.join(self.config.realm, authid=self.config.extra['user'], authmethods=["ticket"])
        else:
            self.join(self.config.realm)

    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received {challenge}", authmethod=challenge.method, challenge=challenge)
        # print(f"sending {self.config.extra['password']}")
        return self.config.extra['password']

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


