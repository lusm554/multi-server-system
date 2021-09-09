from datetime import datetime, timezone
from src.db import conn
from .dao import DAO

class FilesDAO(DAO):
    def __init__(self):
        self.table = 'chunks'
        super(FilesDAO, self).__init__(self.table)

    def isChunkExist(self, id):
        return self.__is_exist__('chunk_id', id)

    def createObject(self, user_id, object_type, parent_object_id, name):
        created_at = updated_at = datetime.now(timezone.utc)
        query = 'insert into objects (                                 \
                    user_id,                                           \
                    object_type,                                       \
                    parent_object_id,                                  \
                    name,                                              \
                    created_at,                                        \
                    updated_at                                         \
                )                                                      \
                values (%s, %s, %s, %s, %s::timestamp, %s::timestamp); \
                '
        data = (user_id, object_type, parent_object_id, name, created_at, updated_at)
        return self.__perform_db_req__(query, data)

    def getChunk(self, object_id, url):
        query = 'select * from chunks               \
                 where object_id = %s and url = %s  \
                '
        return self.__perform_db_req__(query, (object_id, url))

    def getObject(self, user_id, name):
        query = 'select * from objects              \
                 where                              \
                    user_id = %s and name = %s and  \
                    parent_object_id is null        \
                '
        data = self.__perform_db_req__(query, (user_id, name), with_description=True)
        colnames = [desc[0] for desc in data['desc']]
        return {key: val for key, val in zip(colnames, data['content'])}

    def createChunk(self, object_id, url):
        created_at = updated_at = datetime.now(timezone.utc)
        query = 'insert into chunks (    \
                    object_id,           \
                    url,                 \
                    created_at,          \
                    updated_at           \
                 )                       \
                values (%s, %s, %s, %s); \
                '
        self.__perform_db_req__(query, (object_id, url, created_at, updated_at))
        return self.getChunk(object_id, url)
