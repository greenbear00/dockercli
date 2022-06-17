import click
import sys

import docker

from dockercli import VERSION
from dockercli.docker_exec import *


def print_version(ctx, parm, value):
	if not value or ctx.resilient_parsing:
		return
	click.echo(f'Version {VERSION}')
	ctx.exit()


@click.option('-v', '--version', help="Show version of this program.", is_flag=True, callback=print_version,
			  expose_value=False, is_eager=True)
@click.group()
def cli():
	pass


@cli.command(help='ls is no additional options.')
def ls():
	# click.echo('ls...')
	docker_client = docker.from_env()
	check_running_docker(client=docker_client)


# @click.option('-v', '--verbose', is_flag=True, help="Will print verbose messages.")
@cli.command(help="required cname and cmd options")
@click.option('-cname', '--contain_container_name', default='', help='Enter a word that matches the name of the '
																	 'currently running Docker container. (ex: '
																	 'worker)')
@click.option('-cmd', '--docker_cmd', default='', help='Enter the command to be applied to the Docker container.')
@click.option('-u', '--user', default='', help='Enter the user username to execute command. default(root), '
												  '(ex: test_user)')
def exec(contain_container_name, docker_cmd, user):
	# print(f"... contain_container_name: {contain_container_name}")
	# print(f"... cmd : {docker_cmd}")
	if contain_container_name and docker_cmd:
		docker_client = docker.from_env()
		docker_exec(client=docker_client, contain_container_name=contain_container_name, cmd=docker_cmd, user=user)
		# sys.exit()
	else:
		click.echo(f"Required cname and cmd options!")
		click.echo(f"ex) exec -cname worker -cmd 'ls -l'")
		click.echo(f"ex) exec -cname worker -u root -cmd 'ls -l'")
		click.echo(f"ex) exec --contain_container_name worker --docker_cmd 'ls -l'")
		click.echo(f"ex) exec --contain_container_name worker --user test_user --docker_cmd 'ls -l'")
		sys.exit()


cli.add_command(ls)
cli.add_command(exec)


def main():
	cli()


if __name__ == "__main__":
	main()
