from flask import Blueprint, request



user_bp=Blueprint('user', url_prefix='/user')

user_bp.route('/', methods=['GET'])