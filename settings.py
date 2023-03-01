from json import load, dump


class Settings:
    def __init__(self):
        self.standart_path = 'dicts/settings.json'
        self.settings = {"name": None}

    def get_setting(self, setting):
        return self.settings[setting]

    def set_setting(self, setting, value):
        self.settings[setting] = value

    def load(self):
        with open(self.standart_path, 'r') as f:
            self.settings = load(f)

    def save(self):
        with open(self.standart_path, 'w') as f:
            dump(self.settings, f, indent=4, sort_keys=True)
