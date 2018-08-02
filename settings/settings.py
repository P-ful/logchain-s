import json

class Settings:
    # Here will be the instance stored.
    __instance = None

    _settings = {}

    @staticmethod
    def get_instance():
        if Settings.__instance == None:
            Settings()
            Settings.__instance.load_settings()
        return Settings.__instance 

    def __init__(self):
        if Settings.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self

    def load_settings(self):
        with open("settings.json", "r") as json_data:
            self._settings = json.load(json_data)

    def get(self, key):
        return self._settings[key]

    def all(self):
        return self._settings

    def foo(self):
        return self._foo
    
    def get_storage_type(self)
        return self._settings["storage_type"]

    @property
    def network_interface_name(self):
        return self._settings["network_interface_name"]
