#build a function that searches the file system for a pattern and ignores patterns
#that are in a list of ignore patterns
#use pathlib.Path.glob() to search the file system

import pathlib
import sys

def find_files(directory, pattern, ignore_patterns=[]):
    """Find files in the file system that match the pattern.
    Ignore files that match any of the ignore_patterns.
    """
    directory = pathlib.Path(directory)
    for path in directory.glob(pattern):
        for ignore_pattern in ignore_patterns:
            if ignore_pattern in str(path):
                break
        else:
            yield path

