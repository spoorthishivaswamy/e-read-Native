from flask import Flask,render_template,request
import PyPDF2 
from utils import *
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload",methods=["POST"])
def upload():
    try:
        files = request.files["infile"]
        tgt_lang = request.form['tgtlang']
        files.save(files.filename)
        fname = files.filename
        pdfObj = open(fname, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfObj) 
        pageObj = pdfReader.getPage(0) 
        result = call_translate(pageObj.extractText(),tgt_lang)
        pdfObj.close() 
        return render_template("view.html",result = result)
    except Exception as e:
        print(e)
        return "Error"

if __name__ == "__main__":
    app.run()