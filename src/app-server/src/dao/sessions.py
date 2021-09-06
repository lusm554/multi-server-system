from src.db import conn
from datetime import datetime, timezone

def __is_exist__(table, row, val):
    cur = conn.cursor()
    query = 'select exists (           \
        select 1 from {} where {} = %s \
    )'
    cur.execute(query.format(table, row), (val,))
    isexist = cur.fetchone()[0]
    cur.close()
    return isexist

class SessionsDAO:
    def isSessionExist(id):
        return __is_exist__('sessions', 'user_id', id)

    def isTokenExist(token):
        return __is_exist__('sessions', 'token', token)

    def add(user_id, duration, token):
        created_at = datetime.now(timezone.utc)
        cur = conn.cursor()
        query = 'insert into sessions (user_id, created_at, duration, token)    \
                 values (%s, %s::timestamp, %s, %s)                             \
                 on conflict (user_id) do update                                \
                 set                                                            \
                    (created_at, token) = (EXCLUDED.created_at, EXCLUDED.token) \
                 '
        cur.execute(query, (user_id, created_at, duration, token))
        cur.close()
        conn.commit()

    def remove(token):
        cur = conn.cursor()
        query = 'delete from sessions \
                 where                \
                    token = %s        \
                '
        cur.execute(query, (token,))
        cur.close()
        conn.commit()

