from app.models.user_entity import User
from app.models.new_user_dto import NewUserDto
from sqlite3 import Connection, Row


class UserRepository():
    def __init__(self, db_conn: Connection):
        self.db = db_conn

    def create_user(self, user: NewUserDto) -> User:
        sql = """
        INSERT INTO users (name, location)
        VALUES (:name, :location)
        """
        self.db.row_factory = Row
        cursor = self.db.cursor()
        cursor.execute(sql, {'name': user.name, 'location': user.location})
        user_id = cursor.lastrowid
        self.db.commit()
        created_user = self.get_user(user_id=user_id)
        return created_user

    def delete_user(self, id: int):
        sql = """
        DELETE FROM users WHERE id=:id
        """
        self.db.row_factory = Row
        cursor = self.db.cursor()
        cursor.execute(sql, {'id': id})
        id = cursor.lastrowid
        self.db.commit()
        if id == 0:
            raise KeyError(f'ID {id} not found')
        
        return 'User deleted from database'
    

    def get_user(self, user_id: int) -> User:
        sql = """
        SELECT * FROM users WHERE id=:id
        """
        self.db.row_factory = Row
        cursor = self.db.cursor()
        cursor.execute(sql, {'id': user_id})
        row = cursor.fetchone()

        return User(id=row['id'], name=row['name'], location=row['location'])

    def update_user(self, user: User) -> User:
        sql = """
        UPDATE users
        SET name=:name, location=:location
        WHERE id=:id
        """

        cursor = self.db.cursor()
        cursor.execute(sql, {'id': user.id, 'name': user.name, 'location': user.location })
        self.db.commit()

        user = self.get_user(user_id=user.id)
        return user
    
    def get_users(self):
        sql = """
        SELECT * from users
        """

        cursor = self.db.cursor()
        cursor.execute(sql)

        res = cursor.fetchall()
        return res
