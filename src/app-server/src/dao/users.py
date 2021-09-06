from datetime import datetime, timezone
from src.db import conn

def __is_exist__(table, row, val):
    cur = conn.cursor()
    query = 'select exists (           \
        select 1 from {} where {} = %s \
    )'
    cur.execute(query.format(table, row), (val,))
    isexist = cur.fetchone()[0]
    cur.close()
    return isexist


class UsersDAO:
    def isUserExist(name):
        return __is_exist__('users', 'username', name)


    def add(username, password):
        created_at = updated_at = datetime.now(timezone.utc)
        cur = conn.cursor()
        query = 'insert into users (username, password, created_at, updated_at) \
                values (%s, %s, %s::timestamp, %s::timestamp);'
        cur.execute(query, (username, password, created_at, updated_at))
        conn.commit()
        '''
        cur.execute('select * from users where username = %s', (username,))
        return cur.fetchone()
        '''
        

    def get(username):
        cur = conn.cursor()
        query = 'select           \
                    username,     \
                    created_at,   \
                    last_login_at \
                 from             \
                    users         \
                 where            \
                    username = %s \
                '
        cur.execute(query, (username,))
        data = cur.fetchone()
        if data is None:
            return False
        return {key: val for key, val in zip(['username', 'created_at', 'last_login_at'], data)}
        
