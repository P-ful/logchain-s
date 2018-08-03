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
        with open("/conf/settings.json", "r") as json_data:
            self._settings = json.load(json_data)

    def get(self, key):
        return self._settings[key]

    def all(self):
        return self._settings

    def get_storage_type(self):
        return self._settings["storage_type"]

    def get_root_path(self):
        return self._settings["root_path"]

    def get_ftp_address(self):
        return self._settings["ftp_address"]

    def get_ftp_port(self):
        return self._settings["ftp_port"]

    def get_ftp_account(self):
        return self._settings["ftp_account"]

    def get_ftp_password(self):
        return self._settings["ftp_password"]
