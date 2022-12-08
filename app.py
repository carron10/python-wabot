# Commands
# home -> To go back home
# cart -> To view products in cart
# add n[n1,n2....] -> To add products in cart e.g add 123 124 244 will add products for each id 123,124 and 244 respectively
# add n*2[n*0,n...] -> to add  same product many times in cart. e.g add 120*2  will add two products of the same id 120
# checkout -> To buy products added in cart
# order-> To view the oders made by the user!!

import logging
from flask import Flask, request, render_template,make_response
from message import message

app = Flask(__name__)

def send_mmsg(body, url):
    # To return a message with an image(provided url of the img) attached on it
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>%s</Body><Media>%s</Media></Message></Response>" % (body, url)

def send_msg(body):
    # To return a message
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>%s</Body></Message></Response>" % (body)

    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bot/test',methods=['POST'])
def bot():
    
    msg = message(request.form).as_str()
    print(msg)
    return send_msg(msg)
     
if __name__ == '__main__':
    app.run(host='0.0.0.0',)
