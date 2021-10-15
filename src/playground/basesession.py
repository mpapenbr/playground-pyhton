import time
import asyncio
from os import environ
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner


class BaseSession(ApplicationSession):
    """
    base class for handling basic connection setup    
    """
    def onConnect(self):
        self.log.info("Client connected: {klass}", klass=ApplicationSession)
        if 'user' in self.config.extra:            
            self.join(self.config.realm, authid=self.config.extra['user'], authmethods=["ticket"])
        else:
            self.join(self.config.realm)

    def onChallenge(self, challenge):
        self.log.info("Challenge for method {authmethod} received {challenge}", authmethod=challenge.method, challenge=challenge)
        return self.config.extra['password']

    def onDisconnect(self):
        asyncio.get_event_loop().stop()


