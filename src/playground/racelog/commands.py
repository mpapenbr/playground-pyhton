import click

from .frontend import commands as frontend_commands
from .provider import commands as provider_commands
from .provider.register import commands as provider_register_commands


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

@racelog.group("public")
@click.pass_obj
def racelog_public(obj):
    """get public available data"""
    
    

racelog_provider_group.add_command(provider_commands.list)
racelog_provider_group.add_command(provider_commands.remove)

racelog_provider_reg_group.add_command(provider_register_commands.sampleA)
racelog_provider_reg_group.add_command(provider_register_commands.sampleB)

racelog_public.add_command(frontend_commands.list)