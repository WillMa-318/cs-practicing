from flask import Flask, render_template
from User import User 
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/user')
def user_log():
    users = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            user = User(fname = row[0], lname = row[1], email = row[2], username = row[3])
            users.append(user)
    
    return render_template('users.jinja', users = users)

@app.route('/register')
def register():
    return render_template('register.jinja')


@app.route('/login')
def login():
    return render_template('login.jinja')


if __name__ == "__main__":
    app.run()