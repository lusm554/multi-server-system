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