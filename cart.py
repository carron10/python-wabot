from flask import Flask, redirect, url_for, request, render_template, make_response

class cart:
    def __init__(self, user,products):
        self.user = user
        self.products = products.copy()
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

    def send(self,product_list):
        self.user.set_last_msg_sent("cart")
        tmp=list()
        total=0
        for p in self.products:
            k=list()
            k.append(product_list.product_list[int(p)])
            k.append(self.products[p])
            total+=(int(k[0].price)*int(k[1]))
            tmp.append(k)
            pass
        template = render_template(
            "cart_view.xml", products=tmp,total=total)
        response = make_response(template)
        response.headers['Content-Type'] = 'application/xml'
        return response

    def checkout(self):
        # tries to check if the user added products in cart then if yes, it goes to checkout
        self.user.set_last_msg_sent("checkout")
        return "Calling checkout"

    def add(self, msg,prdts,users):
        self.user.set_last_msg_sent("add")
        tmp=self.products.copy()
        data = msg.get_body().split()
        if len(data[1:]) == 0:
            return "Sorry you didn't specify the product to add in cart. pliz use *add n* to add the product with id *n* in your cart."
        for i in data[1:]:
            try:
                id = int(i)
                if(prdts.exist(id)):
                    if (id in tmp.keys()):
                        tmp[id]=tmp[id]+1
                    else:
                        tmp[id]=1
                else:
                    return "*The product you added in cart is Not found*"
            except ValueError:
                d = i.split("*")
                if len(d) == 2:
                    try:
                        k = int(d[0])
                        v = int(d[1])
                        if(prdts.exist(k)):
                            if (k in tmp.keys()):
                                tmp[k]=v
                            else:
                                tmp[k]=v
                        else:
                            return "*The product you added in cart is Not found*"
                    except ValueError:
                        return f"Error found on *{i}*, when trying to add products in cart"
                else:
                    return f"Error found on *{i}*, when trying to add products in cart"
        self.products=tmp.copy()
        users.save()
        return "Products success added to cart , To view cart send *cart*"
    
    def get_data(self):
        return self.products
        