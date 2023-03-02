from view.room_proxy import RoomProxy
from view.view_proxy import ViewProxy


class SpaceProxy(ViewProxy):

    def __init__(self, database, space_id):
        self.database = database
        self.space_id = space_id
        object = self.database.get_space(self.space_id)
        self.name = object["name"][0]
        self.topic = object["topic"][0]
        self.is_real_space = object["is_real_space"][0]

    def list_rooms(self, view):
        rooms = []
        ids = self.database.get_room_ids(self.space_id)
        for id in ids["id"]:
            room = str(self.database.get_room(id)["name"][0])
            rooms.append(room)
        view.show_elements(rooms)

    def create_room(self, view):
        name = view.request_input("Enter name of the room: ")
        topic = view.request_input("Enter topic of the room: ")
        self.database.create_room(self.space_id, name, topic)

    def visit_room(self, view):
        rooms = []
        ids = self.database.get_room_ids(self.space_id)
        for id in ids["id"]:
            room = str(self.database.get_room(id)["name"][0])
            rooms.append(room)
        room = view.get_chosen_option(rooms)
        RoomProxy(self.database, ids["id"][rooms.index(room)]).show(view)

    def show(self, view):
        print(f"Welcome to {self.name}")
        print(f"Topic: {self.topic}")
        print(f"Is real place: {self.is_real_space}")
        while True:
            options = ["Visit room", "Create new object", "List objects", "Exit"]
            chosen_option = view.get_chosen_option(options)
            if chosen_option == "Visit room":
                self.visit_room(view)
            elif chosen_option == "Create new room":
                self.create_room(view)
            elif chosen_option == "List rooms":
                self.list_rooms(view)
            elif chosen_option == "Exit":
                break

    def create(self):
        pass
