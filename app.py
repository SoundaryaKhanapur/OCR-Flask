import os

from flask import Flask, render_template, request

from ocr_core import ocr_core


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'Send file in a Post method with key as file and filename with following file extensions :[png, jpg, jpeg, gif]'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename

        if file and allowed_file(file.filename):
            #file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))

            # call the OCR function on it
            extracted_text = ocr_core(file)

            # extract the text and display it
            return extracted_text
        
    elif request.method == 'GET':
        return 'Send file in a Post method with key as file and filename with following file extensions :[png, jpg, jpeg, gif]' 

if __name__ == '__main__':
    app.run()
