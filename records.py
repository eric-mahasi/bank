import csv


class Record(object):
    """
    A class that stores and accesses stored user account data.

    ...

    Attributes
    ----------
    file_name : str
        Name of the file that stores user data. This file is currently
        in the root directory of the project.
    account_dict : dictionary
        The user data to be stored.

    Methods
    -------
    write_to_file(account_dict)
        Writes the data in the dictionary to the file.
    read_from_file
        Allows the data stored in the file to be accessed.

    """

    def __init__(self):
        self.file_name = "records.csv"

    def write_to_file(self, account_dict):
        """Writes user account information to the file.

        Parameters
        ----------
        account_dict : dictionary
            The user account information to be stored.
        """
        with open(self.file_name, mode='a', newline='') as record_file:
            fieldnames = ['name', 'id', 'pin', 'balance']
            record_writer = csv.DictWriter(record_file, fieldnames=fieldnames)
            record_writer.writerow(account_dict)

    def read_from_file(self):
        """Allows the data stored in the file to be accessed."""
        with open(self.file_name) as record_file:
            record_reader = csv.reader(record_file, delimiter=',')
            for row in record_reader:
                pass
