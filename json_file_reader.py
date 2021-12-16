import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    # AN my code starts
    def get_email(self, section_name=None):
        if 'email' not in self.data.keys():
            raise Exception("email option is not present in the config file")
        return self.data['email']

    def get_password(self, section_name=None):
        if 'password' not in self.data.keys():
            raise Exception("password option is not present in the config file")
    # AN code ends
