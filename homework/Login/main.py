import login
import dashboard
import register
import csv

class user:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def __str__(self):
        return 'username: ' + self.name + ' password: ' + self.password 
    
    def __repr__(self):
        return 'username: ' + self.name + ' password: ' + self.password 
    
    def check_user(self):
        check = []
        
        with open('data.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                check.append(row)
        
        for item in check:
            if item[0] == self.name and item[1] == self.password:
                return True
        return False

    def log(self):
        check = []
        
        with open('data.csv', newline='') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                check.append(row)
        
        for item in check:
            if item[0] == self.name:
                return True
            else:
                return False

    def push(self):
        with open('data.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow([self.name, self.password])
    
    def change_pass(self, new):
        with open('data.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            for row in csv_writer:
                if row[0] == self.name:
                    row[1] = new
    
    def see_all(self):
        list_all = []
        with open('Students.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                list_all.append(row)
        return list_all

def main():
    print '-----------------------------'
    print 'Welcome'
    print '-----------------------------'
    first = input('Do you want to register: ')
    if first == 'yes' or 'Yes':
        register.main()
    second = input('Do you want to login:')
    if second == 'yes' or 'Yes':
        login.main()

if __name__ == "__main__":
    main()
