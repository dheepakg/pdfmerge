import argparse
import sys

file_dict = {}
if len(sys.argv) < 3:
    raise('Not sufficient files')

file_dict[1] = sys.argv[1]
file_dict[2] = sys.argv[2]


print(sys.argv)
print(file_dict)

