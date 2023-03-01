from view_proxy import ViewProxy

class RoomProxy(ViewProxy):
    def __init__(self, model):
        self.model = model

    def show(self):
        print self.model