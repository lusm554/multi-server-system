from datetime import datetime, timezone
from src.db import conn
from .dao import DAO

class UsersDAO(DAO):
    def __init__(self):
        self.table = 'users'
        super(UsersDAO, self).__init__(self.table)

    def isUserExist(self, name):
        return self.__is_exist__('username', name)

    def add(self, username, password):
        created_at = updated_at = datetime.now(timezone.utc)
        query = 'insert into users (username, password, created_at, updated_at) \
                 values (%s, %s, %s::timestamp, %s::timestamp);'
        self.__perform_db_req__(query, (username, password, created_at, updated_at))
        return self.getFullData(username)

    def get(self, username):
        query = 'select           \
                    username,     \
                    created_at,   \
                    last_login_at \
                 from             \
                    users         \
                 where            \
                    username = %s \
                '
        data = self.__perform_db_req__(query, (username,))
        if data is None:
            return False
        return {key: val for key, val in zip(['username', 'created_at', 'last_login_at'], data)}
    
    def getFullData(self, username):
        query = 'select * from users \
                 where               \
                    username = %s    \
                '
        data = self.__perform_db_req__(query, (username,), with_description=True)
        colnames = [desc[0] for desc in data['desc']]
        return {key: val for key, val in zip(colnames, data['content'])}

