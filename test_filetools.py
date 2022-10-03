from mylib.filetools import find_files, find_pattern_in_file
import pathlib


def test_find_files():
    """Test the find_files function."""
    directory = pathlib.Path(__file__).parent
    pattern = "*.py"
    ignore_patterns = ["__pycache__", "test_"]
    paths = list(find_files(directory, pattern, ignore_patterns))
    assert len(paths) == 1
    assert paths[0].name == "hello.py"


def test_find_pattern_in_file():
    """Test the find_pattern_in_file function."""
    mylib_filetools = pathlib.Path(__file__).parent / "mylib/filetools.py"
    pattern = "import pathlib"
    results = find_pattern_in_file(mylib_filetools, pattern)
    assert len(results) == 1
