from sqlalchemy import create_engine, text
from pandas import DataFrame

from view.space_proxy import SpaceProxy

SQL_QUERYS = {
    "create_space": "INSERT INTO space (name, topic, is_real_space) VALUES ('{name}', '{topic}', {is_real_space});",
    "space_ids": "SELECT id FROM space;",
    "space": "SELECT * FROM space WHERE space.id = {space_id};",
    "create_room": "INSERT INTO room (name, description, space_id) VALUES ('{name}', '{description}', {space_id});",
    "room_ids": "SELECT id FROM room WHERE room.space_id = {space_id};",
    "room": "SELECT * FROM room WHERE room.id = {room_id};",
    "create_object": "INSERT INTO object (name, description, room_id) VALUES ('{name}', '{description}', {room_id});",
    "object_ids": "SELECT id FROM object WHERE object.room_id = {room_id};",
    "object": "SELECT * FROM object WHERE object.id = {object_id};",
}

CONNECTION_STING = "postgresql://{host}:{port}/{database}?user={user}&password={password}"


class Database:
    def __init__(self, database_describtor):
        self.engine = create_engine(CONNECTION_STING.format(**database_describtor))

    # SPACE METHODS
    def get_space_ids(self):
        sql = text(SQL_QUERYS["space_ids"])
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def get_space_proxy(self, space_id):
        return SpaceProxy()

    def get_space(self, space_id):
        sql = text(SQL_QUERYS["space"].format(space_id=space_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def create_space(self, name, topic, is_real_space):
        query = text(SQL_QUERYS["create_space"].format(name=name, topic=topic, is_real_space=is_real_space))

        with self.engine.connect() as connection:
            connection.execute(query)

    # ROOM METHODS
    def get_room_ids(self, space_id):
        sql = text(SQL_QUERYS["room_ids"].format(space_id=space_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def get_room(self, room_id):
        sql = text(SQL_QUERYS["room"].format(room_id=room_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def create_room(self, name, description, space_id):
        sql = text(SQL_QUERYS["create_room"].format(name=name, description=description, space_id=space_id))
        with self.engine.connect() as connection:
            connection.execute(sql)

    # OBJECT METHODS
    def get_object_ids(self, room_id):
        sql = text(SQL_QUERYS["object_ids"].format(room_id=room_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def get_object(self, object_id):
        sql = text(SQL_QUERYS["object"].format(object_id=object_id))
        with self.engine.connect() as connection:
            return connection.execute(sql).fetchall()

    def create_object(self, name, description, room_id):
        sql = text(SQL_QUERYS["create_object"].format(name=name, description=description, room_id=room_id))
        with self.engine.connect() as connection:
            connection.execute(sql)

    def get_learn_object(self):
        sql = text("SELECT * FROM object WHERE next_learn_time < NOW() ORDER BY next_learn_time ASC LIMIT 1;")
        with self.engine.connect() as connection:
            data = connection.execute(sql).fetchall()
            connection.commit()
            return DataFrame(data)

    def know_object(self, object_id):
        sql = text("UPDATE object SET learning_status_id = learning_status_id + 1,"
                   " next_learn_time = NOW() + "
                   "(SELECT lenght from learning_status as l where l.learning_status_id = object.learning_status_id) "
                   "WHERE object.id = {object_id};".format(object_id=object_id))
        with self.engine.connect() as connection:
            connection.execute(sql)
            connection.commit()
