import argparse

my_parser = argparse.ArgumentParser(description="This is arg-parser")

my_parser.add_argument(
    "Path", metavar="path variable", type=str, help="the path to list"
)

my_parser.add_argument(
    "--optional", metavar="optional variable", type=str, help="optional command"
)

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path


print("The imput args is ", input_path)
print("args are ", type(args), args)
print("args are ", args.Path)
print("args are ", args.optional)
