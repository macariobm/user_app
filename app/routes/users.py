from flask import Blueprint, request
from app.controllers.user_controller import UserController
from app.services.user_service import UserService
from app.database.user_repository import UserRepository
from app.database.db import conn


user_bp=Blueprint('user', __name__, url_prefix='/user', template_folder='templates')

user_repo = UserRepository(db_conn=conn)
user_service = UserService(user_repo)

user_bp.route('/<int:id>', methods=['GET'])(UserController(request, user_service).get_user)
user_bp.route('/users', methods=['GET'])(UserController(request, user_service).get_users)
user_bp.route('/', methods=['POST'])(UserController(request, user_service).create_user)
user_bp.route('<int:id>', methods=['DELETE'])(UserController(request, user_service).delete_user)
user_bp.route('/<int:id>', methods=['PUT'])(UserController(request, user_service).update_user)
