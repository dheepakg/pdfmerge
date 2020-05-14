import io
from PyPDF2 import PdfFileMerger, PdfFileReader

output_file = "../data/out.pdf"


def file_merge(file_dict):
    merger = PdfFileMerger()
    for _, fileName in file_dict.items():
        merger.append(PdfFileReader(fileName, "rb"))
    merger.write(output_file)
    return output_file

def file_merge_mutiple(request):
    merger = PdfFileMerger()
    for file in request.files.getlist('file'):
        merger.append(PdfFileReader('../temp/'+file.filename, "rb"))
    merger.write(output_file)
    return output_file

if __name__ == "__main__":
    test_files = {
        "file1": "../data/File_One.pdf",
        "file2": "../data/File_Two.pdf",
    }

    print(file_merge(test_files))
