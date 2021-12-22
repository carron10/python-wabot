import os
import logging
from flask import Flask, redirect, url_for, request, render_template, make_response
from users import users
from message import message
from user import user
from cart import cart

account_sid = "AC7dfb1e683991fbc0c74dce6a58230862"
auth_token = "cc79eedc5c00cfd89fc960aa25db257e"
app = Flask(__name__)
users = users()
logging.basicConfig(filename="/opt/pybot.log",level=logging.DEBUG,format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
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

def send_msg(body):
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>%s</Body></Message></Response>"%(body)
@app.route('/bot/test', methods=['POST'])
def bot():
        global user,cart,users
        msg=message(request.form)
        send=""
        if msg.get_frm() in users.get_users().keys():
                send="testing...."
        else:
                cart=cart(msg.get_frm())
                users.get_users()[msg.get_frm()]=user(msg.get_frm(),cart,msg)
                send="Thank you for sending your message"
        user=users.get_users()[msg.get_frm()]
        user.set_prv_msg(msg)
        user.set_last_msg_sent(send)
        return send_msg(send)
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=443,ssl_context=('cert.pem', 'key.pem'))