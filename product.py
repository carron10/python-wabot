class product:
    def __init__(self,id,name,desc=None):
        self.id=id
        self.name=name
        self.desc=desc
    def get_id(self):
        #to return the id of this cart;
        return self.id
    def get_name(self):
        #to return the name of this product
        return self.name
    def get_desc(self):
        return self.desc