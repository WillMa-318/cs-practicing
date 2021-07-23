from blackjack import Card, Game, return_sum
from user import User
from app import user
from flask_sqlalchemy import SQLAlchemy

class check:
    def __init__ (self, a, b = 0):
        self.a = a
        self.b = b

def main():
    username = 'malin'
    print (user.query.filter_by(username = username))
    print (user.query.all())
    
if __name__ == "__main__":
    main()