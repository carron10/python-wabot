import os
from flask import Flask, redirect, url_for, request, render_template, make_response
account_sid = "AC7dfb1e683991fbc0c74dce6a58230862"
auth_token = "cc79eedc5c00cfd89fc960aa25db257e"
app = Flask(__name__)
@app.route('/')
def index():
        return render_template("index.html")

@app.route('/about')
def about():
        return render_template("about.html")
@app.route('/contact')
def contact():
        return render_template("contact.html")
@app.route('/products')
def products():
        return render_template("products.html")
@app.route('/bot/test', methods=['POST'])
def bot():
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>Hello</Body></Message></Response>"
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=443,ssl_context=('cert.pem', 'key.pem'))