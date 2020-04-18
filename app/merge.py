import argparse
from _version import __version__


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

    def check_pdf_or_not(self, files):
        print("files ", files.values())
        pdf_flag = True
        for element in files.values():
            file_name = element.split("//")[-1]
            file_ext = file_name.split(".")[-1]
            if file_ext.upper() != "PDF":
                pdf_flag = False
                break
        return pdf_flag

        # return file_validation_dict
