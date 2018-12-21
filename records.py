class Records(object):
    """This class manages the individual user
    records by storing them in a CSV file"""

    def __init__(self, file_name="user_records.csv"):
        self.file_name = file_name

    def write_to_file(self, file_name):
        with open(self.file_name, 'a') as file_object:
            file_object.write("placeholder user data")
