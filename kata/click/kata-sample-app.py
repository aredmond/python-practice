## Sample Project
"""
1. Create sample app using code from the link above.
"""

# 1.
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

## python kata-sample-app.py --help
## python kata-sample-app.py --count 3