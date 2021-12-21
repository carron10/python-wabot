from user import user
class users:
       
       def __init__(self):
               self.users=dict()
       def get_users(self):
              #to return ALL USERS
              print(self.users.values())
               return self.users.values()
       def add(self,user):
            #To add new user
              self.users[user.get_id()]=user
       def remove(self,user):
              #to remove user
              self.users.remove(user.get_id())
              return
       def get_user_by_id(self,id):
            #To return a user with specified id
              return self.users[id]
       def get_user_by_name(self,name):
            #Try to search all there users with the name above and return a list
              u=list()
              for user in self.users.values:
                     if(user.get_name()==name):
                           u.append(user)
              return u
       
