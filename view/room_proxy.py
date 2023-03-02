from view.view_proxy import ViewProxy


class RoomProxy(ViewProxy):
    def __init__(self, database, room_id):
        self.database = database
        self.room_id = room_id
        object = self.database.get_room(self.room_id)
        self.name = object["name"][0]

    def list_objects(self, view):
        objects = []
        ids = self.database.get_object_ids(self.room_id)
        for id in ids["id"]:
            object = str(self.database.get_object(id)["name"][0])
            objects.append(object)
        view.show_elements(objects)

    def create_object(self, view):
        name = view.request_input("Enter name of the object: ")
        topic = view.request_input("Enter suptopic of the object: ")
        self.database.create_object(self.room_id, name, topic)

    def show(self, view):
        print(f"Welcome to {self.name}")
        while True:
            options = ["List objects", "Create new object", "Exit"]
            chosen_option = view.get_chosen_option(options)
            if chosen_option == "List objects":
                self.list_objects(view)
            elif chosen_option == "Create new object":
                self.create_object(view)
            elif chosen_option == "Exit":
                break
