import csv


class User:
    def __init__ (self, username, password, fname, lname, money = 2000):
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.money = money
    
    def save_user(self):
        user = [self.username, self.password, self.fname, self.lname, self.money]
        with open ('users.csv', 'a', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow(user)
    
    def user_list(self):
        return [self.username, self.password, self.fname, self.lname, self.money]
            
    @staticmethod
    def get_info(name):
        check = []
        with open('users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for line in csv_reader:
                check.append(line)
        for each in check:
            if (len(each) != 0):
                if each[0] == name:
                    return User(each[0], each[1], each[2], each[3])

        return None

    @staticmethod
    def get_money(name):
        check = []
        with open('users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for line in csv_reader:
                check.append(line)
        for each in check:
            if (len(each) != 0):
                if each[0] == name:
                    return each[4]

        return None

    @staticmethod
    def change_money(name, value):
        check = []
        test = True
        with open('users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for line in csv_reader:
                check.append(line)

        for each in check:
            if (len(each) != 0):
                if each[0] == name:
                    money = (int)(each[4])
                    if (money+value) < 0:
                        test = False
                    else:
                        money += value
                        each[4] = money
        
        with open('users.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            for line in check:
                csv_writer.writerow(line)

        return test

            
                