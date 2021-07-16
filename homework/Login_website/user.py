
import csv
class User:
    def __init__(self, fname = '', lname = '', email = '', username = '', password = ''):
        self.fname = fname
        self.lname = lname 
        self.email = email
        self.username = username
        self.password = password

    def __str__(self):
        return '{}: {} {}'.format(self.username, self.fname, self.lname)
    def __repr__(self):
        return '{}: {} {}'.format(self.username, self.fname, self.lname)

    def save_db(self, db):
        with open(db, 'w+', newline = '') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.fname, self.lname, self.email, self.username, self.password])

    @staticmethod
    def get_user(username, db):
        with open(db) as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                if (row[2]==username):
                    return User(row[0], row[1], row[2], row[3], row[4])
                
        return False