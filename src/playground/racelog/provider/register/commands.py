"""commands for register dummy events"""
import click
from autobahn.asyncio.wamp import ApplicationRunner

from playground.racelog.caller import CallEndpoint


@click.command("a")
@click.pass_obj
def sampleA(obj):
    """send register sample A"""
    # obj['endpoint'] = "racelog.dataprovider.register_provider"
    obj['rpc_data'] = {
        "eventKey": "1239",         
        "manifests": {"car":[], "state": [], "session":[], "other":[]},
        "trackInfo": {"trackId": 12, "sectors": [], "trackLength": 0, "trackDisplayName": "dummy","trackDisplayShortName": "dummyShort", "trackConfigName": "none" },
        "info": {
            "name": "SampleA",
            "trackId": 12,
            "sectors": [], "trackLength": 0, "trackDisplayName": "dummy","trackDisplayShortName": "dummyShort", "trackConfigName": "none"
            # no description by design
        }}
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
        "info": {
            "name": "SampleB",
            "description": "Description for SampleB",
        }}
    runner = ApplicationRunner(url=obj['url'], realm=obj['realm'], extra=obj)
    runner.run(CallEndpoint)    