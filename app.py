
from flask import redirect, request, Flask, render_template, send_file
import pyqrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    # ppl should be able to put msg to generate qrcode
    return render_template("index.html")


@app.route("/generated-qr", methods=['GET', 'POST'])
def genrator():
    buffer = BytesIO()
    received_url = request.form.get('qrtext')
    if (received_url==''):
        return render_template('generate-qr.html', msg="Please add text to generate the QR!")
    
    qr_code = pyqrcode.create(received_url)
    qr_code.png(buffer, scale=30)
    buffer.seek(0)
    response = send_file(buffer, mimetype='image/png')
    res=b64encode(buffer.getvalue())
    res = res.decode('utf8')
    return render_template('generator.html', res=res)



@app.route("/download")
def download_file():
    path = "./static/images/generated-qr.png"
    return send_file(path, as_attachment=True)


@app.route('/show', methods=['GET', 'POST'])
def show():
    return render_template("show.html")
    
    
@app.route('/generate-qr', methods=['GET', 'POST'])
def generate_qr():
    return render_template('generate-qr.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)