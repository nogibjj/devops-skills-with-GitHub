#!/usr/bin/env python

import click
from mylib.filetools import find_files, find_pattern_in_file


@click.group()
def cli():
    """A command line interface for the filetools module."""


@cli.command("search")
@click.argument("directory")
@click.argument("pattern")
@click.option("--ignore-patterns", default=[], multiple=True)
def search(directory, pattern, ignore_patterns):
    """Search for files in a directory that match a pattern.

    Example:
        ./fileToolsCli.py search . "*.py" --ignore-patterns __pycache__ --ignore-patterns test_
    """
    # create a count of files found
    count = 0
    # loop through the files found
    files = find_files(directory, pattern, ignore_patterns)
    for file in files:
        click.secho(f"{file}", fg="green")
        count += 1
    # print the number of files found using a click color
    click.secho(f"{count} files found", fg="yellow")


# build a command that searches a file for a pattern and prints the line number and line
@cli.command("find")
@click.argument("file")
@click.argument("pattern")
def find(file, pattern):
    """Find a pattern in a file.

    Example:
        ./fileToolsCli.py find ./mylib/filetools.py "import pathlib"
    """
    #count the number of times the pattern is found
    count = 0
    # loop through the results
    for i, line in find_pattern_in_file(file, pattern):
        count += 1
        # print the line number and line using a click color
        click.secho(f"{i}: {line}", fg="green")
    # print the number of times the pattern was found using a different click color
    click.secho(f"{count} matches found", fg="yellow")

if __name__ == "__main__":
    cli()
