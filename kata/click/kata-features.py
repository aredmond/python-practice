## Features
"""
1. Create a command with colored output. (use clicks built in color output)
2. Create a command that uses click.confirm() to confirm before execution.
3. Create a command that counts to 100 in 5 seconds and displays a progress bar as it counts.
4. Explore the documentation and implement one interesting feature.
"""
import click
import time

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

# 1.
@cli.command('color') 
def color_output():
    click.secho('Hello World!', fg='green')
    click.secho('Some more text', bg='blue', fg='white')
    click.secho('ATTENTION', blink=True, bold=True)

# 2.
@cli.command('conf') 
def confirm_test():
    click.confirm("Are you sure you want to execute this command?", abort=True)
    click.echo("You did not abort!")

# 3.
@cli.command('progress') 
def progress_test():
    one_to_one_hundred = list(range(1, 101))
    with click.progressbar(one_to_one_hundred, label='Count to 100 in 5 secs.') as bar:
        for tick in bar:
            time.sleep(.05)
    

# 4. click.pause()
@cli.command('pause')
def pause_test():
    click.echo('Testing Pause feature, pausing until key is pressed.')
    click.pause()
    click.echo('Pause Complete')

# 4. yes option
def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()

@cli.command('yestest')
@click.option('--yes', is_flag=True, callback=abort_if_false,
              expose_value=False,
              prompt='Are you sure you want to test this command?')
def yes_test():
    click.echo('The yes is tested!')

@cli.command('yestest-simple')
@click.confirmation_option(prompt='Are you sure you want to test this command?')
def yes_test_simple():
    click.echo('The yes is tested with less code!')

if __name__ == '__main__':
    cli()

