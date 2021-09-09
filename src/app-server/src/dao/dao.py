from src.db import conn

class DAO(object):
    def __init__(self, table):
        self.table = table

    def __is_exist__(self, field, value):
        cur = conn.cursor()
        query = 'select exists (                   \
                    select 1 from {} where {} = %s \
                )'
        cur.execute(query.format(self.table, field), (value,))
        data = cur.fetchone()[0]
        cur.close()
        return data

    def __perform_db_req__(self, query, args=(), **kw):
        try:
            cur = conn.cursor()
            cur.execute(query, args)
            conn.commit()
            data = cur.fetchone()
            if kw and kw['with_description']:
                data = {
                    'content': data,
                    'desc': cur.description
                }
            cur.close()
            return data
        except Exception as e:
            if not str(e) == 'no results to fetch':
                print(e)
