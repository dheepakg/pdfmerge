import os
from flask import Flask, render_template, request
from validate_files import fileValidation
from pdf_merge import file_merge, file_merge_mutiple

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'html', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = '../temp'

#Below command to convert py to exe file
#--> pyinstaller --onefile api_gateway.py

# For Page start up with index.html
@app.route('/')
def startup():
    return render_template("index.html")

#Merge PDF with parameter(File names) as JSON String
@app.route('/mergeFile', methods=['POST'])
def mergeFile():
    file_dict = request.get_json()
    obj = fileValidation()
    if obj.check_pdf_or_not(file_dict) and obj.file_exist_or_not(file_dict):
        file_merge(file_dict)
        print("File merged")
    else:
        print("Something's not right with pdf files")
            
    return "Files are merged !"

#Merge PDF with parameter as Multipart file
@app.route('/handle_form', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for file in request.files.getlist('file'):
            if file.filename == '':
                return 'No selected file'
            if allowed_file(file.filename):
                #Creating Temp files for merging
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        print("File created")
        #Calling merging logic with file list
        file_merge_mutiple(request)
        print("File Merged")
        filelist = [ f for f in os.listdir(app.config['UPLOAD_FOLDER'])]
        for f in filelist:
            #Deleteing Temp files once merge is completed
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))
        return render_template("success.html")

#Validate File Type
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)