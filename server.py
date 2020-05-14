from flask import Flask,render_template,request
import PyPDF2 
app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload",methods=["POST"])
def upload():
    files = request.files["infile"]
    files.save(files.filename)
    fname = files.filename
    pdfObj = open(fname, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObj) 
    print(pdfReader.numPages) 
    pageObj = pdfReader.getPage(0) 
    print(pageObj.extractText()) 
    pdfObj.close() 
    return "ok"

if __name__ == "__main__":
    app.run()