from view.start_proxy import StartProxy


class Controller:

    def __init__(self):
        self.view = None
        self.database = None
        self.settings = None

    def set_database(self, database):
        self.database = database

    def set_settings(self, settings):
        self.settings = settings

    def set_view(self, view):
        self.view = view

    def start(self):
        start_proxy = StartProxy(self.settings, self.database)
        start_proxy.show(self.view)
