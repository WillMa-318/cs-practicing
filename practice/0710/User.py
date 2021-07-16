class User:
    def __init__(self, fname='', lname='', email='', username='', password=''):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.password = password
    
    def __str__(self):
        return '{}: {} {}'.format(self.username, self.fname, self.lname)
    
    def __repr__(self):
        return '{}: {} {}'.format(self.username, self.fname, self.lname)