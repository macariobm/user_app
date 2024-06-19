from flask import Blueprint, request
from app.controllers.user_controller import UserController
from app.services.user_service import UserService


user_bp=Blueprint('user', __name__, url_prefix='/user', template_folder='templates')

user_list = []

user_bp.route('/', methods=['GET'])(UserController(request, UserService).get_user)
user_bp.route('/create', methods=['POST'])(UserController(request, UserService).create_user)
user_bp.route('<id>', methods=['DELETE'])(UserController(request, UserService).delete_user)
user_bp.route('/<id>', methods=['POST'])(UserController(request, UserService).update_user)
user_bp.route('/<name>', methods=['POST'])(UserController(request, UserService).update_user)