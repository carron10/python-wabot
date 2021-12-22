import os
from flask import Flask, redirect, url_for, request, render_template, make_response
account_sid = "AC7dfb1e683991fbc0c74dce6a58230862"
auth_token = "cc79eedc5c00cfd89fc960aa25db257e"
app = Flask(__name__)
@app.route('/bot/test', methods=['POST'],strict_slashes=False)
def bot():
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>Hello</Body></Message></Response>"
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=443,ssl_context=('cert.pem', 'key.pem'))
