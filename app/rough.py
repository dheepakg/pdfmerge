import argparse

input_args = argparse.ArgumentParser(
    description="Reads pdf files (mandatory). Also, optional args"
)
input_args.add_argument("--version", action="version", version="%(prog)s 1.0")
input_args.add_argument("File1", metavar="Key in first file", action="store")
input_args.add_argument("File2", metavar="Key in second file", action="store")


# print(input_args.parse_args())
# print(input_args.parse_args(['-h']))
my_namespace = input_args.parse_args()

file_dict = {1:my_namespace.File1,2:my_namespace.File2}

print(file_dict)
