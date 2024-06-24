from flask import Request, jsonify
from app.services.user_service import UserService 
from app.models.new_user_dto import NewUserDto
from app.models.user_entity import User


class UserController():
    def __init__(self, request: Request, user_service: UserService):
        self.request = request
        self.service = user_service

    def create_user(self):
        new_user = NewUserDto(name=self.request.json['name'], location=self.request.json['location'])

        user = self.service.create_user(new_user)

        return jsonify([vars(user)]), 201
    

    def delete_user(self, id: int):
        self.service.delete_user(id)
        return '', 200
        
    
    def get_user(self, id: int):
        user = self.service.get_user(id)
        return jsonify([vars(user)]), 200
    
    def update_user(self, id):
        updated_user = self.service.update_user(User(id=id, name=self.request.json['name'], location=self.request.json['location']))

        return jsonify(vars(updated_user)), 200
    
    def get_users(self):
        return jsonify([vars(user) for user in self.service.get_users()])
    
