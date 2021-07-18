from flask import Flask, render_template, request, redirect, url_for, session
import csv
from user import User
from blackjack import Card, Game, return_sum

app = Flask(__name__)
app.secret_key = 'AOASndoasinOINoiosaaSFai'

@app.route('/')
def index():

    return render_template('index.jinja')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form.get('sending'):
        uname = request.form.get('username')
        pswd = request.form.get('password')
        user = User.get_info(uname)
        if (not user):
            return render_template('login.jinja', messages='Username Not exist')
            print('Username Not exist')
        else:
            if (pswd == user.password):
                session['user'] = [user.username, user.fname, user.lname]
                session['cards'] = [user.username]
                return redirect(url_for('profile'))
            else:
                return render_template('login.jinja', messages='Username not match to the password')
                print('Username not match to the password')
    return render_template('login.jinja')
    
@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        i_password = request.form.get('i_password')
        c_password = request.form.get('c_password')
        user = User(username, i_password, fname, lname)
        u_list = user.user_list()
        for each in u_list:
            if(each == ''):
                return render_template('register.jinja', messages = "Please fill in all the information")
        if User.get_info(username):
            return render_template('register.jinja', messages = "Username already exist")
        else:
            if i_password == c_password:
                user.save_user()
                return redirect(url_for('login'))
            else:
                return render_template('register.jinja', messages = "Password not match")
        
    return render_template('register.jinja')



@app.route('/black_jack', methods = ['GET', 'POST'])
def black_jack():
    if not session.get('user'):
        return redirect(url_for('index'))
    if not session.get('cards'):
        session['cards'] = [session.get('user')[0]]
    if request.method == 'POST':
        if request.form.get("get_card"):
            if len(session.get('cards')) == 1:
                check = User.change_money(session.get('user')[0], -100)
                if check == False:
                    return render_template('black_jack.jinja', messages = "you don't have enough money to start a new round", money = User.get_money(session.get('user')[0]))
            cards = session.get('cards')
            Game.deal(cards)
            show = Game.all_cards(cards)
            sum_card = return_sum(cards)
            session['cards'] = cards
            if sum_card > 21:
                User.change_money(session.get('user')[0], Game.stop(sum_card))
                session['cards'] = [session.get('user')[0]]
                return render_template('black_jack.jinja', messages = "you lose", sum_card = sum_card, l_money = Game.stop(sum_card) * (-1), money = User.get_money(session.get('user')[0]), show = show)
            return render_template('black_jack.jinja', sum_card = sum_card, money = User.get_money(session.get('user')[0]), show = show)

        if request.form.get("stop"):
            if len(session.get('cards')) == 1:
                return render_template('black_jack.jinja', money = User.get_money(session.get('user')[0]))
            cards = session.get('cards')
            show = Game.all_cards(cards)
            sum_card = return_sum(cards)
            User.change_money(session.get('user')[0], Game.stop(sum_card))
            session['cards'] = [session.get('user')[0]]
            amount = Game.stop(sum_card)
            if amount > 0:
                message = 'you win'
            else:
                message = 'you lose'
                amount = amount * (-1)
            return render_template('black_jack.jinja', messages = message, sum_card = sum_card, l_money = amount, money = User.get_money(session.get('user')[0]), show = show)

        


    


    
    return render_template('black_jack.jinja', cardn = "3C")

@app.route('/profile')
def profile():
    if (not session.get('user')):
        return redirect(url_for('index'))
    return render_template('profile.jinja')

@app.route('/logout')
def logout():
    if (not session.get('user')):
        return redirect(url_for('index'))
    session['user'] = None
    session['cards'] = None
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()