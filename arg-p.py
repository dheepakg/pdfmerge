import argparse

my_parser = argparse.ArgumentParser(description="This is arg-parser")

my_parser.add_argument("Path", metavar="path", type=str, help="the path to list")

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path


print("The imput args is ", input_path)
