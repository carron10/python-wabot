import os
from twilio.rest import Client
from flask import Flask, redirect, url_for, request
from users import users
from message import message
from user import user
import logging

account_sid  ="AC7dfb1e683991fbc0c74dce6a58230862"
auth_token ="cc79eedc5c00cfd89fc960aa25db257e"

client = Client(account_sid, auth_token)
users=users()

def send_msg(to,frm,body):
        message = client.messages.create(body=body,from_=frm,to=to)
        print(message.sid)
        
app = Flask(__name__)
logging.basicConfig(filename='/opt/pybot.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 
@app.route('/')
def index():
        
        return "Helo your app is running"
@app.route('/bot/test/',methods=['POST'])
def bot():
        msg=message(request.form)
        app.logger.info('Info level log')
        app.logger.warning('Warning level log')
        send=""
        if msg.get_frm() in users:
                user=users.get_users()[msg.get_frm()]
                send_msg(msg.get_frm(),request.form['To'],"Testing messages")
        else:
                users.get_users()[msg.get_frm()]=user(msg.get_frm(),cart(),msg)
                send="Thank you for sending your message"
                send_msg(msg.get_frm(),request.form['To'],send)
                
        user=users.get_users()[msg.get_frm()]
        user.set_last_msg_sent(send)
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=443,ssl_context=('cert.pem', 'key.pem'))
