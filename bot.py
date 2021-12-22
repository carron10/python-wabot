import os
from twilio.rest import Client
from flask import Flask, redirect, url_for, request, render_template, make_response
from users import users
from message import message
from user import user
from cart import cart
import logging

account_sid = "AC7dfb1e683991fbc0c74dce6a58230862"
auth_token = "cc79eedc5c00cfd89fc960aa25db257e"

client = Client(account_sid, auth_token)
users = users()

def reply(**data):
        template=render_template(data['file'],data=data)
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response


def send_msg(to, frm, body):
        message = client.messages.create(body=body, from_=frm, to=to)
        print(message.sid)


app = Flask(__name__)
logging.basicConfig( filename="/opt/pybot.log",level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')



#@app.route('/')
#def index():
#        return reply(file="welcome.xml")

@app.route('/bot/test/', methods=['POST'])
def bot():
        
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>Hello</Body></Message></Response>"
        
        
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
   app.run(host='0.0.0.0',port=80)
   #ssl_context=('/opt/cert.pem', '/opt/key.pem'

