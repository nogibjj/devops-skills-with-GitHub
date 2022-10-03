#!/usr/bin/env python

import click
from mylib.research import get_wiki_pages, get_wiki_summary, get_wiki_keywords


# build a click group
@click.group()
def cli():
    """A command line interface for wikipedia research."""


@cli.command("search")
@click.argument("search_term")
def search(search_term):
    """Search wikipedia for a term.

    Example:
        ./wikiResearch.py search "python"
    """

    pages = get_wiki_pages(search_term)
    for page in pages:
        # use click colors to highlight the search term
        click.secho(page, fg="green")


# pylint: disable=redefined-outer-name
@cli.command("summary")
@click.argument("page")
def summary(page):
    """Get the summary of a page.

    Example:
        ./wikiResearch.py summary "Python"
    """
    # use click colors to highlight the page
    # count the number of characters in the summary
    # use click colors to highlight the number of characters
    page = click.style(page, fg="green")
    summary = get_wiki_summary(page)
    click.secho(
        f"Wikipedia Page Summary: [{page}] has {len(summary)} characters. in summary",
        fg="green",
    )
    click.echo(summary)


# pylint: disable=redefined-outer-name
@cli.command("keywords")
@click.argument("page")
def keywords(page):
    """Get the top 10 keywords of a page.

    Example:
        ./wikiResearch.py keywords "Python"
    """

    page = click.style(page, fg="green")
    keywords = get_wiki_keywords(page)
    # print the top 10 keywords line by line without the score and in a different color
    click.secho(f"Top 10 Keywords for Wikipedia Page: [{page}]", fg="yellow")
    for keyword in keywords:
        # use click colors to highlight the keyword
        click.secho(keyword, fg="green")


# call click
if __name__ == "__main__":

    cli()
