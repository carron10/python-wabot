import os
from twilio.rest import Client
from flask import Flask, redirect, url_for, request
from users import users
from message import message
from user import user

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
print(os.getenv('TWILIO_AUTH_TOKEN'))
client = Client(account_sid, auth_token)
users=users()

def send_msg(to,frm,body):
        message = client.messages.create(body=body,from_=frm,to=to)
        print(message.sid)
        
app = Flask(__name__)
@app.route('/')
def index():
        return "Helo your app is running"
@app.route('/bot/test/',methods=['POST'])
def bot():
        msg=message(request.form)
        send=""
        if msg.get_frm in users:
                user=users.get_users()[msg.get_frm()]
        else:
                users.get_users()[msg.get_frm()]=user(msg.get_frm,cart(),msg)
                send="Thank you for sending your message"
                send_msg(msg.get_frm(),request.form['To'],send)
                
        user=users.get_users()[msg.get_frm()]
        user.set_last_msg_sent(send)
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080,ssl_context=('cert.pem', 'key.pem'))
