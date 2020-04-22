from src.merge import pdfMerge
from src._version import __version__


"""Arrange  Act  Assert """

from pathlib import Path
import pytest


def check_version():
    obj3 = pdfMerge()
    with pytest.raises(SystemExit):
        parser = obj3.read_args()
        args = parser.parse_args(["--version"])


def test_version_check(capsys):
    result = check_version()
    out, err = capsys.readouterr()
    ver_list = out.split(" ")
    assert ver_list[-1] == __version__ + "\n"


def test_read_2_variables():
    """To test 2 variables are passed or not"""
    obj2 = pdfMerge()
    parser = obj2.read_args()
    two_files = vars(parser.parse_args(["file one", "file two"]))
    assert len(two_files) == 2


def read_1_variables():
    """To test 2 variables are passed or not"""
    obj1 = pdfMerge()

    with pytest.raises(SystemExit):
        parser = obj1.read_args()
        one_file = vars(parser.parse_args(["file one"]))


def test_read_1_variables(capsys):
    """To test 1 variable are passed or not"""
    read_1_variables()
    out, err = capsys.readouterr()
    if out in "the following arguments are required: Key in second file":
        assert True


obj4 = pdfMerge()
parser = obj4.read_args()
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
    return check_pdf_or_not_output


def test_2_pdfs():
    method_pdf = check_pdf(two_valid_pdf_files)
    assert method_pdf == True


def test_2_non_pdfs():
    method_pdf = check_pdf(two_invalid_pdf_files)
    assert method_pdf == False


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
