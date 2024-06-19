from app.models.user_entity import User
from app.models.new_user_dto import NewUserDto


class UserService:
    def __init__(self):
        pass

    def create_user(self, new_user: NewUserDto) -> User:
        user = self.create_user(new_user)
        #add  database operations
        return user

    def update_user(self, user: User) -> User:
        return #alter user name
    
    def delete_user(self, user: User) -> User:
        return #database deletion


    def get_user(self, user: User) -> User:
        return #select * from User WHERE id=':id'
