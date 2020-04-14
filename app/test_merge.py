import pytest

import merge


def test_read_files():
    list_of_files = merge.read_files()
    assert len(list_of_files) == 2  # tests 2 files are passed
    # tests 2 files are pdfs
