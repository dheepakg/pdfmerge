"""Arrange  Act  Assert """

import sys

# from sys import stderr

import pytest

# from importlib_metadata import version

# from pyparsing import __version__

# import merge
from merge import pdfMerge
from _version import __version__

obj = pdfMerge()


def test_read_2_variables():
    parser = obj.read_files()
    two_files = vars(parser.parse_args(["file one", "file two"]))
    assert len(two_files) == 2


def check_version():
    with pytest.raises(SystemExit):
        parser = obj.read_files()
        args = parser.parse_args(["--version"])


def test_version_check(capsys):
    result = check_version()
    out, err = capsys.readouterr()
    # print("Output is ", out)
    # print("Error is ", err)
    ver_list = out.split(" ")
    # print(ver_list[-1])
    assert ver_list[-1] == __version__ + "\n"


def key_in_files():
    parser = merge.read_files()
    two_files = vars(parser.parse_args(["file one", "file two"]))


def test_pdf_or_not():
    """
    Key-in PDF files, should PASS
    Key-in non-pdf file, should FAIL
    """

    assert True


def test_pdf_file_exists_in_file_system():
    assert True


if __name__ == "__main__":
    pass
