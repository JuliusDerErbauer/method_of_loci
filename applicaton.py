import os

from controller import Controller
from database import Database
from settings import Settings
from view.view import View


class Application:
    def __init__(self):
        database_describtor = {
            "host": "localhost",
            "port": 5432,
            "database": "methodofloci",
            "user": "loki",
            "password": "loki",

        }
        self.controller = Controller()
        self.view = View()
        self.database = Database(database_describtor)
        self.settings = Settings()
        self.controller.set_settings(self.settings)
        self.controller.set_view(self.view)
        self.controller.set_database(self.database)

    def start(self):
        self.settings.load()
        self.controller.start()

    def stop(self):
        self.settings.save()


if __name__ == "__main__":
    a = Application()
    a.start()
    a.stop()
