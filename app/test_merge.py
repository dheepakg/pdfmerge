"""Arrange  Act  Assert """

import sys
from operator import contains
from optparse import Values
from os.path import split
from pathlib import Path


import pytest

from _version import __version__

# import merge
from merge import pdfMerge

# from sys import stderr


# from importlib_metadata import version

# from pyparsing import __version__


obj = pdfMerge()


def check_version():
    obj3 = pdfMerge()
    with pytest.raises(SystemExit):
        parser = obj3.read_files()
        args = parser.parse_args(["--version"])


def test_version_check(capsys):
    result = check_version()
    out, err = capsys.readouterr()
    # print("Output is ", out)
    # print("Error is ", err)
    ver_list = out.split(" ")
    # print(ver_list[-1])
    assert ver_list[-1] == __version__ + "\n"


def test_read_2_variables():
    """To test 2 variables are passed or not"""
    obj2 = pdfMerge()
    parser = obj2.read_files()
    two_files = vars(parser.parse_args(["file one", "file two"]))
    assert len(two_files) == 2


def read_1_variables():
    """To test 2 variables are passed or not"""
    obj1 = pdfMerge()

    with pytest.raises(SystemExit):
        parser = obj1.read_files()
        one_file = vars(parser.parse_args(["file one"]))


def test_read_1_variables(capsys):
    """To test 1 variable are passed or not"""
    read_1_variables()
    out, err = capsys.readouterr()
    if out in "the following arguments are required: Key in second file":
        assert True


obj4 = pdfMerge()
parser = obj4.read_files()
two_valid_pdf_files = vars(
    parser.parse_args(
        [
            "/Users/deegee/Desktop/WorkArea/GitHub/pdfmerge/data/File_One.pdf",
            "/Users/deegee/Desktop/WorkArea/GitHub/pdfmerge/data/File_Two.pdf",
        ]
    )
)


two_invalid_pdf_files = vars(
    parser.parse_args(
        [
            "/Users/deegee/Desktop/WorkArea/GitHub/pdfmerge/data/File_One.txt",
            "/Users/deegee/Desktop/WorkArea/GitHub/pdfmerge/data/File_Two.pdf",
        ]
    )
)


def check_pdf(two_files_dict):

    check_pdf_or_not_output = obj4.check_pdf_or_not(two_files_dict)
    test_pdf_flag = True
    for element in two_files_dict.values():
        file_name = element.split("//")[-1]
        file_ext = file_name.split(".")[-1]
        if file_ext.upper() != "PDF":
            test_pdf_flag = False
            break
    return (test_pdf_flag, check_pdf_or_not_output)


def test_2_pdfs():
    test_pdf, method_pdf = check_pdf(two_valid_pdf_files)
    assert test_pdf == method_pdf


def test_2_non_pdfs():
    test_pdf, method_pdf = check_pdf(two_invalid_pdf_files)
    assert test_pdf == method_pdf


def check_pdf_files_exists(two_files_dict):

    file_exist_or_not_output = obj4.file_exist_or_not(two_files_dict)
    test_file_exist_flag = True
    for element in two_files_dict.values():
        given_file = Path(element)
        if not given_file.is_file():
            test_file_exist_flag = False
            break
    return (test_file_exist_flag, file_exist_or_not_output)


def test_pdf_file_exists_in_file_system():
    test_file, method_file = check_pdf_files_exists(two_valid_pdf_files)
    assert test_file == method_file


def test_pdf_file_not_exists_in_file_system():
    test_file, method_file = check_pdf_files_exists(two_invalid_pdf_files)
    assert test_file == method_file


if __name__ == "__main__":
    pass
