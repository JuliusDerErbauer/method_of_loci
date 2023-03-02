from view.view_proxy import ViewProxy


class SpaceProxy(ViewProxy):

    def __init__(self, database, space_id):
        self.database = database
        self.space_id = space_id
        object = self.database.get_space(self.space_id)
        self.name = object["name"][0]
        self.topic = object["topic"][0]
        self.is_real_space = object["is_real_space"][0]

    def show(self):
        pass

    def create(self):
        pass
