from src.pdf_merge import file_merge
from pathlib import Path
from src.validate_files import *

print("inside test pdf merge")

test_files = {
    "file1": "./data/File_One.pdf",
    "file2": "./data/File_Two.pdf",
}


def test_verify_file_generated():
    """
    Reads output from file_merge().
    Verifies whether output file is generated or not
    """
    output_file = file_merge(test_files)
    file_path = Path(output_file)
    assert file_path.is_file()
