from xml.dom import minidom
from product import product
from flask import Flask, redirect, url_for, request, render_template, make_response
from pathlib import Path
from database import database

class products:
    def __init__(self):
        self.product_list=dict()
        self.con=database().get_connection()
      
        cur=self.con.cursor()
        cur.execute('''
        select products from my_data where id=0
        ''')
        my_products=cur.fetchone()
        cur.close()
        file=minidom.parse(str(my_products))
        products=file.getElementsByTagName("product")
        for p in products:
            id=int(p.attributes['id'].value)
            name=p.attributes['name'].value
            desc=p.firstChild.data.strip()
            price=p.attributes['price'].value
            url=p.attributes['url'].value
            self.product_list[id]=product(id,name,url,price,desc)
           # print(f"\nProduct Name: {name}\nId:{id}\nDescription: {desc}\nUrl: {url}\n")
        
        #It accepts list of products. These are usual products that  are already in dabase
    def get_products(self):
        #To return all the products
        return self.product_list.values()
    def add_product(self):
        #to add the products in db
        return
    def remove_product(self,id):
        #to remove a product with given id from database 
        return
    def get(self,id):
        return self.product_list.get(id);
    def exist(self,id):
        #Checks weather the product with given id does exist 
        return id in self.product_list.keys()
    def send(self):
        template=render_template("products_view.xml",products=self.product_list.values())
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response