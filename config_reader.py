from BrainBucket.utils.json_file_reader import JsonFileReader
from BrainBucket.utils.ini_file_reader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    # AN my code starts
    def get_email(self, section_name):
        return self.reader.get_email(section_name)

    def get_password(self, section_name):
        return self.reader.get_password(section_name)
    # AN my code ends