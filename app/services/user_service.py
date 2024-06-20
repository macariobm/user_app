from app.models.user_entity import User
from app.models.new_user_dto import NewUserDto
from app.database.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, new_user: NewUserDto) -> User:
        user = self.user_repository.create_user(new_user)
        return user

    def update_user(self, user: User) -> User:
        return 
    
    def delete_user(self, del_user: User) -> User:
        user = self.user_repository.delete_user(del_user)
        return user


    def get_user(self, user_id: User) -> User:
        user = self.user_repository.get_user(user_id)
        return user
