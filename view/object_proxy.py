class ObjectProxy:
    def __init__(self, database, object_id):
        self.database = database
        self.object_id = object_id
        object = self.database.get_object(self.object_id)
        self.name = object["name"][0]
        self.story = object["story"][0]
        self.subtopic = object["subtopic"][0]

    def change_object(self, view):
        name = self.name
        if (view.get_boolean_input("Do you want to change the name? Currently: " + name + "")):
            name = view.request_input("Enter name of the object: ")
        story = self.story
        if (view.get_boolean_input("Do you want to change the story? Currently: " + story + "")):
            story = view.request_input("Enter story of the object: ")
        subtopic = self.subtopic
        if (view.get_boolean_input("Do you want to change the subtopic? Currently: " + subtopic + "")):
            subtopic = view.request_input("Enter subtopic of the object: ")
        self.database.update_object(self.object_id, name, story, subtopic)

    def show(self, view):
        print(f"Welcome to {self.name}")
        print(f"Story: {self.story}")
        print(f"Subtopic: {self.subtopic}")
        while True:
            options = ["Change Object", "Exit"]
            chosen_option = view.get_chosen_option(options)
            if chosen_option == "Change Object":
                self.change_object(view)
            elif chosen_option == "Exit":
                break
