from merge import pdfMerge

if __name__ == "__main__":
    obj = pdfMerge()
    parser = obj.read_files()
    if parser:
        file_dict = vars(parser.parse_args())
        if obj.check_pdf_or_not(file_dict):
            print("Valid PDF files")
