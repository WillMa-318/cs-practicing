from flask import Flask, render_template, request, redirect, url_for, session
from blackjack import Card, Game, return_sum
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db = SQLAlchemy(app)
app.secret_key = 'AOASndoasinOINoiosaaSFai'

class user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    money = db.Column(db.Integer, nullable=False)
    def __str__(self):
        return 'Username: {}, Password: {}, Firstname: {}, Lastname: {}, Money: {}'.format(self.username, self.password, self.firstname, self.lastname, self.money)
    def __repr__(self):
        return 'Username: {}, Password: {}, Firstname: {}, Lastname: {}, Money: {}'.format(self.username, self.password, self.firstname, self.lastname, self.money)

def user_list(user):
    return [user.username, user.password, user.firstname, user.lastname]

# def get_info(username):
    






# -------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.jinja'), 404

@app.route('/')
def index():
    return render_template('index.jinja')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form.get('sending'):
        uname = request.form.get('username')
        pswd = request.form.get('password')
        user_ = user.query.filter_by(username = uname).first()
        if user_ == None:
            return render_template('login.jinja', messages='Username Not exist')
            print('Username Not exist')
        else:
            if (pswd == user_.password):
                session['user'] = [user_.username, user_.firstname, user_.lastname]
                session['cards'] = [user_.username]
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
        user_ = user(username = username, password = i_password, firstname = fname, lastname = lname, money = 0)
        u_list = user_list(user_)
        for each in u_list:
            if(each == ''):
                return render_template('register.jinja', messages = "Please fill in all the information")
        if not user.query.filter_by(username = username).first() == None:
            return render_template('register.jinja', messages = "Username already exist")
        else:
            if i_password == c_password:
                db.session.add(user_)
                db.session.commit()
                print (user.query.all())
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
    user_ = user.query.filter_by(username = session.get('user')[0]).first()
    if request.method == 'POST':
        if request.form.get("get_card"):
            if len(session.get('cards')) == 1:
                if user_.money < 300:
                    Money = user_.money
                    db.session.commit()
                    return render_template('black_jack.jinja', messages = "you don't have enough money to start a new round", money = Money)
                else:
                    user_.money -= 100
                    db.session.commit()
            cards = session.get('cards')
            Game.deal(cards)
            show = Game.all_cards(cards)
            sum_card = return_sum(cards)
            session['cards'] = cards
            Money = user_.money
            if sum_card > 21:
                user_.money += Game.stop(sum_card)
                Money = user_.money
                session['cards'] = [session.get('user')[0]]
                db.session.commit()
                return render_template('black_jack.jinja', messages = "you lose", sum_card = sum_card, l_money = Game.stop(sum_card) * (-1), money = Money, show = show)
            return render_template('black_jack.jinja', sum_card = sum_card, money = Money, show = show)

        if request.form.get("stop"):
            if len(session.get('cards')) == 1:
                Money = user_.money
                return render_template('black_jack.jinja', money = Money)
            cards = session.get('cards')
            show = Game.all_cards(cards)
            sum_card = return_sum(cards)
            user_.money += Game.stop(sum_card)
            session['cards'] = [session.get('user')[0]]
            amount = Game.stop(sum_card)
            Money = user_.money
            db.session.commit()
            if amount > 0:
                message = 'you win'
            else:
                message = 'you lose'
                amount = amount * (-1)
            return render_template('black_jack.jinja', messages = message, sum_card = sum_card, l_money = amount, money = Money, show = show)
    Money = user_.money
    return render_template('black_jack.jinja', money = Money)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    if (not session.get('user')):
        return redirect(url_for('index'))
    user_ = user.query.filter_by(username = session.get('user')[0]).first()
    Money = user_.money
    if request.method == 'POST':
        if request.form.get("deposit"):
            try:
                change = (int)(request.form.get('amount'))
                if change < 0:
                    Money = user_.money
                    db.session.commit()
                    return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'not a valid amount', money = Money)
                else:
                    user_.money += change
                    Money = user_.money
                    db.session.commit()
                    return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'Succeed', money = Money)
            except:
                Money = user_.money
                db.session.commit()
                return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'not a valid amount', money = Money)

        if request.form.get("withdraw"):
            try:
                change = (int)(request.form.get('amount'))
                if change < 0:
                    Money = user_.money
                    db.session.commit()
                    return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'not a valid amount', money = Money)
                else:
                    if user_.money < change:
                        return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'not a valid amount', money = Money)
                    user_.money -= change
                    Money = user_.money
                    db.session.commit()
                    return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'Succeed', money = Money)
            except:
                Money = user_.money
                db.session.commit()
                return  render_template('profile.jinja', c1 = 'show', b1 = '', c2 = '', b2 = 'collapsed', messages_1 = 'not a valid amount', money = Money)

        if request.form.get("change"):
            o_password = request.form.get('o_password')
            n_password = request.form.get('n_password')
            c_password = request.form.get('c_password')
            if o_password == user_.password:
                if n_password == c_password:
                    user_.password = n_password
                    db.session.commit()
                    return render_template('profile.jinja', c1 = '', b1 = 'collapsed', c2 = 'show', b2 = '', messages_2 = 'Succeed', money = Money)
                    print('a')
                else:
                    return render_template('profile.jinja', c1 = '', b1 = 'collapsed', c2 = 'show', b2 = '', messages_2 = 'Password not match', money = Money)
                    print('b')
            else:
                print('c')
                return render_template('profile.jinja', c1 = '', b1 = 'collapsed', c2 = 'show', b2 = '', messages_2 = 'Current password incorrect', money = Money)
            
                
    Money = user_.money
    print('d')
    db.session.commit()
    return render_template('profile.jinja', c1 = '', b1 = 'collapsed', c2 = '', b2 = 'collapsed', money = Money)

@app.route('/logout')
def logout():
    if (not session.get('user')):
        return redirect(url_for('index'))
    session['user'] = None
    session['cards'] = None
    return redirect(url_for('index'))

if __name__ == "__main__":
    # db.create_all()
    app.run()