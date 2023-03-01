from view.view_proxy import ViewProxy


class StartProxy(ViewProxy):
    def __init__(self, settings, database):
        self.settings = settings
        self.database = database

    def list_places(self, view):
        spaces = []
        ids = self.database.get_space_ids()
        for id in ids:
            spaces.append(self.database.get_space(id)["name"])
        view.show_elements(spaces)

    def create_space(self, view):
        name = view.request_input("Enter name of the place: ")
        topic = view.request_input("Enter topic of the place: ")
        is_real_place = view.get_boolean_input("Is this a real place?")
        self.database.create_space(name, topic, is_real_place)

    def show(self, view):
        name = self.settings.get_setting("name")
        if name is None:
            name = view.request_input("Enter your name: ")
            self.settings.set_setting("name", name)
        print(f"Welcome {name} to the memory trainer what do you want to do?")
        while True:
            options = ["List places", "Create new place", "Exit"]
            chosen_option = view.get_chosen_option(options)
            if chosen_option == "List places":
                self.list_places(view)
            elif chosen_option == "Create new place":
                self.create_space(view)
            elif chosen_option == "Exit":
                break

