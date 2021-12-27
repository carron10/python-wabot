from flask import Flask, redirect, url_for, request, render_template, make_response
import os
from twilio.rest import Client
from users import users
from message import message
from user import user
from cart import cart
import logging

account_sid = "AC7dfb1e683991fbc0c74dce6a58230862"
auth_token = "cc79eedc5c00cfd89fc960aa25db257e"

client = Client(account_sid, auth_token)
users = users()

app = Flask(__name__)
logging.basicConfig(filename="/opt/pybot.log",level=logging.DEBUG,format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
def reply(**data):
        template=render_template(data['file'],data=data)
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response

def send_msg(to, frm, body):
        message = client.messages.create(body=body, from_=frm, to=to)
        print(message.sid)


@app.route('/bot/test/', methods=['POST'])
def bot():
        global user,cart
        msg=message(request.form)
        send=""
        if msg.get_frm() in users.get_users().keys():
                send_msg(msg.get_frm(),request.form['To'],"Testing messages")
        else:
                
                cart=cart(msg.get_frm())
                users.get_users()[msg.get_frm()]=user(msg.get_frm(),cart,msg)
                send="Thank you for sending your message"
                send_msg(msg.get_frm(),request.form['To'],send)
                
        user=users.get_users()[msg.get_frm()]
        user.set_prv_msg(msg)
        user.set_last_msg_sent(send)
        
        
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

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=443,ssl_context=('cert.pem', 'key.pem'))
   #ssl_context=('/opt/cert.pem', '/opt/key.pem')

