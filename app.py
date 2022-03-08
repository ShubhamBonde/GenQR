
import time
from flask import redirect, request, Flask, render_template, send_file
import urllib.parse as uparse
import pyqrcode as qr
import png

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    # ppl should be able to put msg to generate qrcode
    return render_template("index.html")


@app.route("/generated-qr", methods=['GET', 'POST'])
def genrator():
    print("method is post now")
    parsed_string = uparse.unquote(request.form.get('qrtext'))
    qrstring = qr.create(parsed_string)
    qrstring.png('./static/images/generated-qr.png', scale=50)
    return render_template('generator.html', url=parsed_string)


@app.route("/download")
def download_file():
    path = "D:\WEB_DEV\Qr code site\static\images\generated-qr.png"
    return send_file(path, as_attachment=True)


@app.route('/show', methods=['GET', 'POST'])
def show():
    return render_template("show.html")
    
    


if __name__ == "__main__":
    app.run(debug=True)