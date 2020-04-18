import argparse


def read_files():
    """
    Reads files from CLI
    """
    try:
        input_args = argparse.ArgumentParser(
            description="Reads pdf files (mandatory). Also, optional args"
        )
        input_args.add_argument("--version", action="version", version="%(prog)s 1.0")
        input_args.add_argument("File1", metavar="Key in first file", action="store")
        input_args.add_argument("File2", metavar="Key in second file", action="store")

        my_namespace = input_args.parse_args()
        return my_namespace
    except:
        return False


if __name__ == "__main__":
    arguments = read_files()
    print(arguments.File1)
    print(arguments.File2)
