import qrcode
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    img = qrcode.make('https://www.instagram.com/sweet_aroma_pr/')
    img.save('qrcode.png')
    return send_file('qrcode.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(port=5000)
