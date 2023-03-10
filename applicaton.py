from os import path, chdir

from controller import Controller
from database import Database
from settings import Settings
from view.view import View


class Application:
    def __init__(self):
        self.controller = Controller()
        self.view = View()
        self.database = Database()
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
    chdir(path.dirname(path.abspath(__file__)))
    a = Application()
    a.start()
    a.stop()
