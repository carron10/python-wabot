from user import user
import json
from cart import cart
from pathlib import Path

class users:

       def __init__(self):
        self.users = dict()
        f = Path("/opt/py/")
        f.mkdir(parents=True, exist_ok=True)
        filename=f/"users.json"
   
        with open(filename, 'r') as openfile:
            json_object = json.load(openfile)
            openfile.close()
       
        for n in json_object:
               u=user(n['id'],None,n['name'])
               u.set_cart(cart(u,n['cart']))
               self.users[n['id']]=u
       
       def get_users(self):
          return self.users

       def add(self, user):
        # To add new user
        self.users[user.get_id] = user

       def remove(self, user):
        # to remove user
        self.users.remove(user.get_id())
        return

       def get_user_by_id(self, id):
        # To return a user with specified id
        return self.users[id]

       def get_user_by_name(self, name):
        # Try to search all there users with the name above and return a list
        u = list()
        for user in self.users.values:
            if(user.get_name() == name):
                u.append(user)
        return u
       def save(self):
              data=list()
              f = Path("/opt/py/")
              f.mkdir(parents=True, exist_ok=True)
              filename=f/"users.json"
              for u in self.users.values():
                     data.append(u.get_data())
                     
              with open(filename, "w") as outfile:
                     json.dump(data, outfile)

              
              
