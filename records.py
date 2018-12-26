class Records(object):
    """This class handles all the operations pertaining to user records."""
# TODO increase security by encrypting file
# TODO improve security by encrypting passwords

    def __init__(self, file_name="user_records.csv"):
        self.file_name = file_name

    def write_to_file(self, file_name):
        with open(self.file_name, 'a') as file_object:
            file_object.write("placeholder user data")

    def read_from_file(self):
        pass
