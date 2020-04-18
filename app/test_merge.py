import sys
# from sys import stderr

import pytest
# from importlib_metadata import version

# from pyparsing import __version__

import merge
from _version import __version__


def test_read_2_variables():
    parser = merge.read_files()
    two_files = vars(parser.parse_args(["file one", "file two"]))
    assert len(two_files) == 2


def check_version():
    with pytest.raises(SystemExit):
        parser = merge.read_files()
        args = parser.parse_args(["--version"])
    assert True


def test_version_check(capsys):
    result = check_version()
    out, err = capsys.readouterr()
    # print("Output is ", out)
    # print("Error is ", err)
    ver_list = out.split(" ")
    # print(ver_list[-1])
    assert ver_list[-1] == __version__ + "\n"


if __name__ == "__main__":
    pass
