
class cart:
    def __init__(self,id):
        self.id=id
        self.products=dict()
    def get_produts(self):
        #to return product id as a list
        return self.products
    def add_product(self,product):
        #To add a product here
        self.products[product.get_id()]=product
    def get_product(self,id):
        #To return the product with given id
        return self.products[id]

    def remove_product(self,id):
        #to remove the product from cart
        self.products.remove(id)
    def get_id(self):
        #to return the id of this cart
        return self.id
