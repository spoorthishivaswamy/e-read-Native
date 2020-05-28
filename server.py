from flask import Flask,render_template,request,send_file
import PyPDF2,os
from utils import *
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    os.system("rm static/*.wav")
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
        print("Translated successfully")
        return render_template("view.html",filename = result[0]['filename'],text = result[0]['translations'][0]['text'])
    except Exception as e:
        print("Error while translating :"+str(e))
        return "Error"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)