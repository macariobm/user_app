from datetime import date
from app.models.user_entity import User
from app.models.new_user_dto import NewUserDTO


class UserRepository():
    def __init__(self, db_conn = []):
        self.db = db_conn

    