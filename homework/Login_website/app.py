from flask import Flask, render_template, request, redirect, url_for, session
import csv
from black_jeck import Card, Game, Deck, Player, load, check_c, clear_c
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    print(session.get('user'))
    return render_template('index.jinja', user = session.get('user'))

@app.route('/user')
def user():
    return render_template('user.jinja')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    will = Player('will')
    new_game = Game(will)
    if (request.method == 'POST'):
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User(fname, lname, username, email, password)
        user.save_db('users.csv')

        print('lalal')
        new_game.turn()

    return render_template('register.jinja', user = will)

@app.route('/login')
def login():
    return render_template('login.jinja')

@app.route('/play', methods = ['GET', 'POST'])
def blackjeck():
    name = 'will'
    check = True
    user = load(name)
    if check_c(load(name)) > 21:
        check = False

    if (request.method == 'POST' and check == True):
        new_game = Game(Player(name))
        new_game.turn()
        print(load(name))

        if check_c(load(name)) > 21:
            check = False

        if check == True:
            return render_template('play.jinja', user = user)
        
        if check == False:
            clear_c(name)
            return render_template('play.jinja', user = user, notice = '')
        
    return render_template('play.jinja', user = user, notice = '')


if __name__ == "__main__":
    app.run()