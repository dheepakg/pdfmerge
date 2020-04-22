import _version as v
from validate_files import fileValidation
from pdf_merge import file_merge

obj = fileValidation()
parser = obj.read_args()
file_dict = vars(parser.parse_args())

if obj.check_pdf_or_not(file_dict) and obj.file_exist_or_not(file_dict):
    file_merge(file_dict)
    print("File merged")
else:
    print("Something's not right with pdf files")
