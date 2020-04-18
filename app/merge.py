import argparse
from _version import __version__
from pathlib import Path


class pdfMerge:
    def read_files(self):
        """
        Reads files from CLI
        """

        input_args = argparse.ArgumentParser(
            description="Reads pdf files (mandatory). Also, optional args"
        )

        input_args.add_argument(
            "-v", "--version", action="version", version="%(prog)s " + __version__
        )

        input_args.add_argument("File1", metavar="Key in first file", action="store")
        input_args.add_argument("File2", metavar="Key in second file", action="store")

        return input_args

    def check_pdf_or_not(self, files_dict):
        print("files ", files_dict.values())
        pdf_flag = True
        for element in files_dict.values():
            file_name = element.split("//")[-1]
            file_ext = file_name.split(".")[-1]
            if file_ext.upper() != "PDF":
                pdf_flag = False
                break
        return pdf_flag

    def file_exist_or_not(self, files_dict):
        print("files ", files_dict)
        file_exist = True
        for element in files_dict.values():
            given_file = Path(element)
            if not given_file.is_file():
                file_exist = False
                break

        return file_exist
