from flask import Flask, redirect, url_for, request, render_template, make_response
class product:
    def __init__(self,id,name,url,price,desc=None):
        self.id=id
        self.name=name
        self.desc=desc
        self.url=url
        self.price=price
    def get_id(self):
        #to return the id of this cart;
        return self.id
    def get_name(self):
        #to return the name of this product
        return self.name
    def get_desc(self):
        return self.desc
    def get_url(self):
        return self.url
    def price(self):
        return self.price
    def send(self):
        #For sending a product
    
        template=render_template("product_view.xml",url=self.url,id=self.id,price=self.price,desc=self.desc,name=self.name)
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response