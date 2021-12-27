from flask import Flask, redirect, url_for, request, render_template, make_response


class cart:
    def __init__(self, user):
        self.user = user
        self.products = dict()

    def get_produts(self):
        # to return product id as a list
        return self.products

    def add_product(self, product):
        # To add a product here
        self.products[product.get_id()] = product

    def get_product(self, id):
        # To return the product with given id
        return self.products[id]

    def remove_product(self, id):
        # to remove the product from cart
        self.products.remove(id)

    def get_id(self):
        # to return the id of this cart
        return self.id

    def send(self):
        
        self.user.set_last_msg_sent("cart")
        template = render_template(
            "cart_view.xml", products=self.products.values())
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response

    def checkout(self):
        # tries to check if the user added products in cart then if yes, it goes to checkout
        self.user.set_last_msg_sent("checkout")
        return "Calling checkout"

    def add(self, msg):
        self.user.set_last_msg_sent("add")
        data = msg.get_body().split()
        if len(data[1:]) == 0:
            return "Sorry you didn't specify the product to add in cart. pliz use *add n* to add the product with id *n* in your cart."
        for i in data[1:]:
            try:
                id = int(i)
            except ValueError:
                d = i.split("*")
                if len(d) == 2:
                    try:
                        k = int(d[0])
                        v = int(d[1])
                    except ValueError:
                        return f"Error found on *{i}*, when trying to add products in cart"
                else:
                    return f"Error found on *{i}*, when trying to add products in cart"
        return f"Calling add--------------{data[1:]}"
