"""commands for register dummy events"""
from autobahn.asyncio.wamp import ApplicationRunner
import click

from playground.racelog.caller import CallEndpoint

@click.command("a")
@click.pass_obj
def sampleA(obj):
    """send register sample A"""
    # obj['endpoint'] = "racelog.dataprovider.register_provider"
    obj['rpc_data'] = {
        "eventKey": "1239", 
        "manifests": {"car":[], "state": [], "session":[], "other":[]},
        "info": {}}
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(CallEndpoint)

@click.command("b")
@click.pass_obj
def sampleB(obj):
    """send register sample B"""
    # obj['endpoint'] = "racelog.dataprovider.register_provider"
    obj['rpc_data'] = {
        "eventKey": "333", 
        "manifests": {"car":[], "state": [], "session":[], "other":[]},
        "info": {}}
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(CallEndpoint)    