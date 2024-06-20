from datetime import date
from app.models.user_entity import User
from app.models.new_user_dto import NewUserDto


class UserRepository():
    def __init__(self, db_conn):
        self.db = db_conn

    def create_user(self, user: NewUserDto) -> User:
        sql = """
        INSERT INTO users (id, name, location)
        VALUES (:id, :name, :location)
        RETURNING id, name, location
        """

        cursor = self.db.cursor()
        cursor.execute(sql, {'id': user.id, 'name': user.name, 'location': user.location})
        self.db.commit()

        res = cursor.fetchone()
        created_user = User(id=res['id'], name=res['name'], locations=res['location'])
        cursor.close()
        return created_user

    def delete_user(self, user_id: int) -> User:
        sql = """
        DELETE * FROM users WHERE id=:id
        """

        cursor = self.db.cursor()
        cursor.execute(sql, {'id': user_id})
        self.db.commit()

        res = cursor.fetchone()
        deleted_user = User(id=res['id'], name=res['name'], location=res['location'])
        cursor.close()
        return deleted_user
    

    def get_user(self, user_id: int) -> User:
        sql = """
        SELECT * FROM users WHERE id=:id
        """

        cursor = self.db.cursor()
        cursor.execute(sql, {'id': user_id})
        self.db.commit()

        res = cursor.fetchone()
        cursor.close()
        user = User(id=res['id'], name=res['name'], location=res['location'])
        return user
