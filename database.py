from json import load

from sqlalchemy import create_engine, text
from pandas import DataFrame

from view.space_proxy import SpaceProxy

SQL_QUERYS = {
    "create_space": "INSERT INTO space (name, topic, is_real_space) VALUES ('{name}', '{topic}', {is_real_space});",
    "space_ids": "SELECT id FROM space ORDER BY id;",
    "space": "SELECT * FROM space WHERE space.id = {space_id};",
    "create_room": "INSERT INTO room (name, space_id) VALUES ('{name}', {space_id});",
    "room_ids": "SELECT id FROM room WHERE room.space_id = {space_id} ORDER BY id;",
    "room": "SELECT * FROM room WHERE room.id = {room_id};",
    "create_object": "INSERT INTO object (name, story, subtopic, room_id) VALUES ('{name}', '{story}', '{subtopic}', '{room_id}');",
    "object_ids": "SELECT id FROM object WHERE object.room_id = {room_id} ORDER BY id;",
    "object": "SELECT * FROM object WHERE object.id = {object_id};",
}

CONNECTION_STING = "postgresql://{host}:{port}/{database}?user={user}&password={password}"


class Database:
    def __init__(self):
        self.standart_path = 'dicts/settings.json'
        self.database_describtor = {}
        with open(self.standart_path, 'r') as f:
            self.database_describtor = load(f)

        self.engine = create_engine(CONNECTION_STING.format(**self.database_describtor))

    # SPACE METHODS
    def get_space_ids(self):
        sql = text(SQL_QUERYS["space_ids"])
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def get_space(self, space_id):
        sql = text(SQL_QUERYS["space"].format(space_id=space_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def create_space(self, name, topic, is_real_space):
        query = text(SQL_QUERYS["create_space"].format(name=name, topic=topic, is_real_space=is_real_space))

        with self.engine.connect() as connection:
            connection.execute(query)
            connection.commit()

    # ROOM METHODS
    def get_room_ids(self, space_id):
        sql = text(SQL_QUERYS["room_ids"].format(space_id=space_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def get_room(self, room_id):
        sql = text(SQL_QUERYS["room"].format(room_id=room_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def create_room(self, name, space_id):
        sql = text(SQL_QUERYS["create_room"].format(name=name, space_id=space_id))
        with self.engine.connect() as connection:
            connection.execute(sql)
            connection.commit()

    # OBJECT METHODS
    def get_object_ids(self, room_id):
        sql = text(SQL_QUERYS["object_ids"].format(room_id=room_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def get_object(self, object_id):
        sql = text(SQL_QUERYS["object"].format(object_id=object_id))
        with self.engine.connect() as connection:
            return DataFrame(connection.execute(sql).fetchall())

    def create_object(self, name, story, subtopic, room_id):
        sql = text(SQL_QUERYS["create_object"].format(name=name, story=story, subtopic=subtopic, room_id=room_id))
        with self.engine.connect() as connection:
            connection.execute(sql)
            connection.commit()

    def update_object(self, object_id, name, story, subtopic):
        sql = text("UPDATE object SET name = '{name}', story = '{story}', subtopic = '{subtopic}' WHERE id = {object_id};".format(
            name=name, story=story, subtopic=subtopic, object_id=object_id))
        with self.engine.connect() as connection:
            connection.execute(sql)
            connection.commit()

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
