# Commands
# home -> To go back home
# cart -> To view products in cart
# add n[n1,n2....] -> To add products in cart e.g add 123 124 244 will add products for each id 123,124 and 244 respectively
# add n*2[n*0,n...] -> to add  same product many times in cart. e.g add 120*2  will add two products of the same id 120 
# checkout -> To buy products added in cart
# order-> To view the oders made by the user!!

import logging
from flask import Flask,request
from users import users
from message import message
from user import user
from cart import cart
from data import data
from products import products
app = Flask(__name__)
users = users()
product_list=products()
logging.basicConfig(filename="/opt/pybot.log",level=logging.DEBUG,format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def index():
    # Home webpage
    return render_template("index.html")


def send_mmsg(body, url):
    # To return a message with an image(provided url of the img) attached on it
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>%s</Body><Media>%s</Media></Message></Response>" % (body, url)


def send_msg(body):
    # To return a message
    return "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>%s</Body></Message></Response>" % (body)


def order(u):
    # return details of the product with corresponding id
    u.set_last_msg_sent("order")
    return send_msg("Viewing ordering _____")

def show_products(u):
    # return all the products that the company is selling
    u.set_last_msg_sent("product_list")
    return product_list.send()


def home(u):
    # return home message
    u.set_last_msg_sent("home")
    return send_msg(data["home"].format(u.get_name()))

def handle(msg, u):
    # tries to map user message to the corresponding function
    if(msg.get_body() == "home"):
        return home(u)
    elif (msg.get_body() == "order"):
        return order(u)
    elif msg.get_body().startswith("add"):
        return send_msg(u.get_cart().add(msg))
    elif (msg.get_body() == "checkout"):
        return send_msg(u.get_cart().checkout())
    else:
        send = "Sorry %s invalid Value!!<br>" % (u.get_name())
        return send_msg(send+data["home_alt"])


@app.route('/bot/test', methods=['POST'])
def bot():
    global user, users
    ##This is the function that will be executed when they is a message sent from twillio
    
    print(request.form)
    msg = message(request.form)    #It represent the message that have been sent
    
    if msg.get_frm() in users.get_users().keys(): 
        #msg.get_frm() is a number that is used by the client. You know cellphone numbers Are unique
        #So in above statement we are checking if the user is already added in our users list or not..
        
        u = users.get_users()[msg.get_frm()]   #To get the user(becuase we know now the user exist in our list)
        
        #Below we are trying to find out the previous message that we have sent to the user, then try to transform the message to what we are expecting
        #For example consider if we have previously sent the home message, we are now expecting to get a number 1,2,3 
        
        if(u.get_last_msg_sent() == "welcome"): #if previous msg that we sent is a welcome message--then...
            u.set_name(msg.get_body())   
            return home(u)
        elif (u.get_last_msg_sent() == "home"): #if previous msg that we sent is a home message--then.. do below tasks.
            try:
                v = int(msg.get_body())
                if v == 1:
                    return show_products(u)
                elif v == 2:
                    return send_msg(u.get_cart().send())
                elif v == 3:
                    return order(u)
                else:
                    send = "Sorry %s invalid Value." % (u.get_name())
                    return send_msg(send+data["home_alt"])
            except ValueError:
                return handle(msg, u)
        elif (u.get_last_msg_sent() == "product_list"):
            try:
                v = int(msg.get_body())
                if(product_list.exist(v)):
                    return product_list.get(v).send()
                else:
                    return send_msg("Error no Product like that")
                
            except ValueError:
                return handle(msg, u)
        elif (u.get_last_msg_sent() == "product_view"):
            try:
                v = int(msg.get_body())
                if(product_list.exist(v)):
                     return product_list.get(v).send()
                else:
                    return send_msg("Error no Product like that")
            except ValueError:
                return handle(msg, u)
        elif ((u.get_last_msg_sent() == "cart") or(u.get_last_msg_sent() == "order")or (u.get_last_msg_sent() == "add")):
            return handle(msg, u)
        else:
            return home(u)
    else:
        users.get_users()[msg.get_frm()] = user(
            msg.get_frm(),None, msg)
        u = users.get_users()[msg.get_frm()]
        crt=cart(u)
        u.set_cart(crt)
        u.set_prv_msg(msg)
        u.set_last_msg_sent("welcome")
        return send_msg(data["welcome"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=443,
            ssl_context=('cert.pem', 'key.pem'))
