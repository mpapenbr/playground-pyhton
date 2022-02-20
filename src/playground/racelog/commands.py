import click

from playground.racelog.admin.event.commands import delete as admin_delete_event

from .frontend import commands as frontend_commands
from .provider import commands as provider_commands
from .provider.register import commands as provider_register_commands
from .provider.extra import commands as provider_extra_commands


@click.group("racelog")
@click.pass_context
@click.option("--url", help="url of the crossbar server",envvar="RACELOG_URL", default="ws://host.docker.internal:8091/ws", show_default=True)
@click.option("--realm", help="realm", default="racelog", envvar="RACELOG_REALM", show_default=True)
@click.option("--user", help="username", envvar="RACELOG_USER")
@click.option("--password", help="password", envvar="RACELOG_PASSWORD")
def racelog(ctx,url,realm,user,password):
    """send specific test commands to racelog"""
    ctx.ensure_object(dict)
    ctx.obj['url'] = url
    ctx.obj['realm'] = realm
    ctx.obj['user'] = user
    ctx.obj['password'] = password
    

@racelog.group("provider")
@click.pass_obj
def racelog_provider_group(obj):
    """samples for registering"""
    
@racelog_provider_group.group("register")
@click.pass_obj
def racelog_provider_reg_group(obj):
    """samples for registering"""
    obj['endpoint'] = "racelog.dataprovider.register_provider"

@racelog_provider_group.group("extra")
@click.pass_obj
def racelog_provider_extra_group(obj):
    """samples for extra data"""
    obj['endpoint'] = "racelog.dataprovider.store_event_extra_data"


@racelog.group("admin")
@click.pass_obj
def racelog_admin_group(obj):
    """container for admin commands"""

@racelog_admin_group.group("event")
@click.pass_obj
def racelog_admin_event_group(obj):
    """event related admin commands"""
    
    

@racelog.group("public")
@click.pass_obj
def racelog_public(obj):
    """get public available data"""
    
    

racelog_provider_group.add_command(provider_commands.list)
racelog_provider_group.add_command(provider_commands.remove)
racelog_provider_group.add_command(provider_commands.publish)

racelog_provider_reg_group.add_command(provider_register_commands.sampleA)
racelog_provider_reg_group.add_command(provider_register_commands.sampleB)
racelog_provider_reg_group.add_command(provider_register_commands.sampleB)

racelog_provider_extra_group.add_command(provider_extra_commands.extraPit)

racelog_public.add_command(frontend_commands.list)
racelog_public.add_command(frontend_commands.eventinfo)

racelog_admin_event_group.add_command(admin_delete_event)