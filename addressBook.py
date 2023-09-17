import pandas as pd
COLUMNS = ['Name', 'IdNumber', 'UserName']


class AddressBook:
    def __init__(self, limit=1000):
        """
        The constructor imports the users' db to a DataFrame
        """
        self.book = pd.read_csv('address_book.csv', nrows=limit)

    def __str__(self):
        return str(self.book)

    def _update_book(self):
        """
        This method saves the book to the csv file.
        :return:
        """
        self.book.to_csv('address_book.csv', index=False)

    def register(self, name: str, id_number: int, username: str):
        """
        This method register a new user by adding it to the book and update the csv.
        :param name: name of new user
        :param id_number: id number of the new user. Can't already exist
        :param username: desired username. Can't already exist
        :return: 0 for successful registration
                 1 for id already registered
                 2 for username is taken.
        """
        if id_number in self.book['IdNumber'].values:
            print('ID already in system.')  # reset password?
            return 1
        if username in self.book['UserName'].values:
            print('UserName already exists. Choose a different one.')
            return 2
        new_user = pd.DataFrame([[name, id_number, username]], columns=COLUMNS)
        self.book = pd.concat([self.book, new_user], ignore_index=True)
        self._update_book()
        return 0

    def unregister(self, name: str, id_number: int, username: str):
        """
        implement it one day
        :param name:
        :param id_number:
        :param username:
        :return:
        """
        pass



