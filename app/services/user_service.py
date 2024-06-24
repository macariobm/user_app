from app.models.user_entity import User
from app.models.new_user_dto import NewUserDto
from app.database.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, new_user: NewUserDto) -> User:
        return self.user_repository.create_user(new_user)

    def update_user(self, user: User) -> User:
        return self.user_repository.update_user(user)
    
    def delete_user(self, id) -> User:
        user = self.user_repository.delete_user(id)
        return user


    def get_user(self, id) -> User:
        user = self.user_repository.get_user(id)
        return user
    
    def get_users(self):
        return self.user_repository.get_users()
