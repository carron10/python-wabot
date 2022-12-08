# Commands
# home -> To go back home
# cart -> To view products in cart
# add n[n1,n2....] -> To add products in cart e.g add 123 124 244 will add products for each id 123,124 and 244 respectively
# add n*2[n*0,n...] -> to add  same product many times in cart. e.g add 120*2  will add two products of the same id 120
# checkout -> To buy products added in cart
# order-> To view the oders made by the user!!

import logging
from flask import Flask, request, render_template,make_response


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/bot/test',methods=['POST'])
def bot():
    print(request.form)
    msg = request.form
    return msg
     
if __name__ == '__main__':
    app.run(host='0.0.0.0',)
