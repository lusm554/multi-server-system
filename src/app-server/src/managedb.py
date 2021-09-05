import psycopg2
from os import path

class ManageDB:
    def __init__(self, conn):
        self.conn = conn
        self.__sql_dir__ = path.join(path.dirname(path.abspath(__file__)), 'sql')

    def setupDatabase(self):
        try:
            cur = self.conn.cursor()
            cur.execute(open(path.join(self.__sql_dir__, 'setup_db.sql'), 'r').read())
            print('The database is built.')
        except Exception as e:
            raise e
        finally:
            self.conn.close()

    def createTables(self):
        try:
            cur = self.conn.cursor()
            cur.execute(open(path.join(self.__sql_dir__, 'create_tables.sql'), 'r').read())
            self.conn.commit()
            print('The tables created.')
        except Exception as e:
            raise e
    
