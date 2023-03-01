from database import DatabaseAdapter
from view_proxy import ViewProxy

class ObjectProxy(ViewProxy):
    def __init__(self, database):
        self.database: DatabaseAdapter = database

    def show(self):
        print(self.database.get_object())
