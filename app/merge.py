import argparse
from _version import __version__


class pdfMerge:
    def read_files(self):
        """
        Reads files from CLI
        """
        try:
            input_args = argparse.ArgumentParser(
                description="Reads pdf files (mandatory). Also, optional args"
            )

            input_args.add_argument(
                "-v", "--version", action="version", version="%(prog)s " + __version__
            )

            input_args.add_argument(
                "File1", metavar="Key in first file", action="store"
            )
            input_args.add_argument(
                "File2", metavar="Key in second file", action="store"
            )

            return input_args
        except:
            return False

    def check_pdf_or_not(self):
        pass


if __name__ == "__main__":
    parser = read_files()
    a = parser.parse_args()
    b = vars(parser.parse_args())
    print(a)
    print(b)
