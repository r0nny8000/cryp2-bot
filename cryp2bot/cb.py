"""This is the cryp2bot module."""

import click
import cryp2bot.kraken.marketdata as marketdata


@click.group()
def cli():
    """add a group of commands to the command line interface."""
    pass # This is a no-op

@cli.command()
@click.argument('pair', required=True)
def ticker(pair):
    """Get the ticker information for a given pair."""
    if pair is None or pair.strip() == "":
        click.echo(click.style("The pair argument is required.", fg="red"))
        return
    
    data = marketdata.ticker(pair)


    if data is None:
        click.echo(click.style("Failed to retrieve ticker information.", fg="red"))
        return
    
    print(data)

if __name__ == "__main__":
    cli()  # Call the main function

# Generated by Copilot
