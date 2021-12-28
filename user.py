
class user:
    def __init__(self,id,cart=None,name=None,prv=None):
        self.prvmsg=prv
        self.id=id
        self.cart=cart
        self.lastmsg=None
        self.name=name
    def get_prv_msg(self):
        #to return the message previously sent by the user
        return self.prvmsg
    def set_prv_msg(self,prv):
        self.prvmsg=prv
        #to return the message previously sent by the user
    def get_name(self):
        #To return the user name(if added).
        return self.name
    def set_name(self,name):
        #To return the user name(if added).
        self.name=name
        return
    def set_last_msg_sent(self,msg):
        self.lastmsg=msg;
        return
    def get_last_msg_sent(self):
        #To return the last message that the bot has sent to this user
        return self.lastmsg
    def get_reg_date(self):
        #To get the date in which this user started to dm the bot |registered
        return 
    def get_cart(self):
        #To return the cart corresponding to this user
        return self.cart
    
    def set_cart(self,cart):
        #To return the cart corresponding to this user
        self.cart=cart
        return  
    def get_id(self):
        #To return the id of this user.. Normal the id is the phone number for this user
        return self.id
    def __str__(self):
        return '{"name":"%s","id":"%s","cart":"%s"}'%(self.name,self.id,self.cart)
    def get_data(self):
        data=dict()
        data["name"]=self.name
        data['id']=self.id
        data['cart']=self.cart.get_data()
        return data
    