from view.space_proxy import SpaceProxy
from view.view_proxy import ViewProxy


class StartProxy(ViewProxy):
    def __init__(self, settings, database):
        self.settings = settings
        self.database = database

    def list_places(self, view):
        spaces = []
        ids = self.database.get_space_ids()
        for id in ids["id"]:
            space = str(self.database.get_space(id)["name"][0])
            spaces.append(space)
        view.show_elements(spaces)

    def create_space(self, view):
        name = view.request_input("Enter name of the space: ")
        topic = view.request_input("Enter topic of the space: ")
        is_real_space = view.get_boolean_input("Is it a real space?")
        self.database.create_space(name, topic, is_real_space)

    def visit_space(self, view):
        spaces = []
        ids = self.database.get_space_ids()
        for id in ids["id"]:
            space = str(self.database.get_space(id)["name"][0])
            spaces.append(space)
        space = view.get_chosen_option(spaces)
        SpaceProxy(self.database, ids["id"][spaces.index(space)]).show(view)

    def learn(self, view):
        while True:
            object = self.database.get_learn_object()
            if len(object) == 0:
                view.show_message("There are no objects to learn")
                break
            view.show_message(object["name"][0])
            if (view.get_boolean_input("Did you know this object?")):
                self.database.know_object(object["id"][0])
            else:
                self.database.message("Thema: " + object["subtopic"][0])

    def show(self, view):
        name = self.settings.get_setting("name")
        if name is None:
            name = view.request_input("Enter your name: ")
            self.settings.set_setting("name", name)
        print(f"Welcome {name} to the memory trainer what do you want to do?")
        while True:
            options = ["Visit Place", "Create new place", "List places", "Learn", "Exit"]
            chosen_option = view.get_chosen_option(options)
            if chosen_option == "Visit Place":
                self.visit_space(view)
            elif chosen_option == "Create new place":
                self.create_space(view)
            elif chosen_option == "List places":
                self.list_places(view)
            elif chosen_option == "Learn":
                self.learn(view)
            elif chosen_option == "Exit":
                break

