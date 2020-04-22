import _version as v
from merge import pdfMerge

obj = pdfMerge()
parser = obj.read_args()
file_dict = vars(parser.parse_args())

print(file_dict)
