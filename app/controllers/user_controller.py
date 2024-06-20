from flask import Request
from app.services.user_service import UserService 
from app.models.new_user_dto import NewUserDto


class UserController():
    def __init__(self, request: Request, user_service: UserService):
        self.request = request
        self.service = user_service

    def create_user(self, new_user: NewUserDto):
        new_user = NewUserDto(name=self.request.json['name'])

        user = self.service.create_user(new_user)

        return[vars(user)], 201
    

    def delete_user(self):
        user = self.service.delete_user(id=self.request.json['id'])
        return [vars(user)], 200
    
    def get_user(self):
        user = self.service.get_user(id=self.request.json['id'])
        return[vars(user)], 201
    
    def update_user(self):
        new_user = UserService(location=self.request.json['location'], name=self.request.json['name'])
        
        user = self.service.update_user(new_user)

        return[vars(user)], 201


