from mylib.filetools import find_files
import pathlib

def test_find_files():
    """Test the find_files function."""
    directory = pathlib.Path(__file__).parent
    pattern = "*.py"
    ignore_patterns = ["__pycache__", "test_"]
    paths = list(find_files(directory, pattern, ignore_patterns))
    assert len(paths) == 1
    assert paths[0].name == "hello.py"