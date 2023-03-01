from view.view_proxy import ViewProxy


class SpaceProxy(ViewProxy):
    def __init__(self, model):
        self.model = model

    def show(self):
        print self.model

    def create(self):
        pass
