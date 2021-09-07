from src.db import conn
from datetime import datetime, timezone
from .dao import DAO

class SessionsDAO(DAO):
    def __init__(self):
        self.table = 'sessions'
        super(SessionsDAO, self).__init__(self.table)
    
    def isTokenExist(self, token):
        return self.__is_exist__('token', token)

    def add(self, user_id, duration, token):
        created_at = datetime.now(timezone.utc)
        query = 'insert into sessions (user_id, created_at, duration, token)    \
                 values (%s, %s::timestamp, %s, %s)                             \
                 on conflict (user_id) do update                                \
                 set                                                            \
                    (created_at, token) = (EXCLUDED.created_at, EXCLUDED.token) \
                 '
        return self.__perform_db_req__(query, (user_id, created_at, duration, token))

    def remove(self, token):
        query = 'delete from sessions \
                 where                \
                    token = %s        \
                '
        return self.__perform_db_req__(query, (token,))

