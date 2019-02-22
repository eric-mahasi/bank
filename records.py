import csv


class Record(object):
    """This class stores and accesses stored user account information from a
    csv
    file.
    """
# TODO increase security by encrypting file
# TODO improve security by encrypting passwords

    def __init__(self):
        self.file_name = "records.csv"

    def write_to_file(self, account_dict):
        """Stores user account information to a file.

        Args:
            account_dict: A dictionary containing some of the user account
            details.
        """
        with open(self.file_name, mode='a') as record_file:
            fieldnames = ['name', 'id', 'pin', 'balance']
            record_writer = csv.DictWriter(record_file, fieldnames=fieldnames)
            record_writer.writerow(account_dict)

    def read_from_file(self):
        with open(self.file_name) as record_file:
            record_reader = csv.reader(record_file, delimiter=',')
            for row in record_reader:
                pass
