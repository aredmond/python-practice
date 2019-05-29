## Commands and Groups
"""
[commands and groups](https://click.palletsprojects.com/en/7.x/commands/)

1. Create a cli app with one group and one command.
2. Add a second command
3. Add help instructions to the second command
"""

# 1.
import click

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()  # @cli, not @click!
def sync():
    click.echo('Syncing')

# 2. 3.
@cli.command()
def test():
    """This is the helo for my test command""" # 3.
    click.echo('Testing')

if __name__ == '__main__':
    cli()

