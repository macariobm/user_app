from . import User
from . import NewUserDTO


class UserService:
    def __init__(self):
        pass

    def create_user(self, new_user: NewUserDTO) -> User:
        user = self.create_user(new_user)
        #add  database operations
        return user

    def update_user(self, id):
        return #alter user name
    
    def delete_user(self, id):
        return #database deletion


    def get_user(self, id):
        return #select * from User WHERE id=':id'

        
    def get_all_users(self):
        return #all the database