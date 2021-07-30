from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)
app.secret_key = 'AOASndoasinOINoiosaaSFai'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    restaurants = db.relationship('Restaurant', backref='user')
    def __str__(self):
        return 'Username: {}, Password: {}, Firstname: {}, Lastname: {}'.format(self.username, self.password, self.firstname, self.lastname)
    def __repr__(self):
        return 'Username: {}, Password: {}, Firstname: {}, Lastname: {}'.format(self.username, self.password, self.firstname, self.lastname)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    menu = db.relationship('Menu', backref='restaurant')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    isdish = db.Column(db.Boolean, nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)





def user_list(user):
    return [user.username, user.password, user.firstname, user.lastname]

    






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
        user = User.query.filter_by(username = uname).first()
        if user == None:
            return render_template('login.jinja', messages='Username Not exist')
            print('Username Not exist')
        else:
            if (pswd == user.password):
                session['user'] = [user.username, user.firstname, user.lastname]
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
        user = User(username = username, password = i_password, firstname = fname, lastname = lname)
        u_list = user_list(user)
        for each in u_list:
            if(each == ''):
                return render_template('register.jinja', messages = "Please fill in all the information")
        if not User.query.filter_by(username = username).first() == None:
            return render_template('register.jinja', messages = "Username already exist")
        else:
            if i_password == c_password:
                db.session.add(user)
                db.session.commit()
                print (User.query.all())
                return redirect(url_for('login'))
            else:
                return render_template('register.jinja', messages = "Password not match")
        
    return render_template('register.jinja')

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    if (not session.get('user')):
        return redirect(url_for('index'))
    user = User.query.filter_by(username = session.get('user')[0]).first()
    if (request.method == 'POST'):
        id_ = request.form.get('name')
        for each in user.restaurants:
            if each.id == id_:
                restaurant_id = each.id
        if id_ == 'create_new_res':
            return redirect(url_for('create_r'))
        else:
            print(restaurant_id)
            return redirect(url_for('edit'), id = restaurant_id)
    return render_template('profile.jinja', user = user)


@app.route('/profile/create_new', methods = ['GET', 'POST'])
def create_r():
    if (not session.get('user')):
        return redirect(url_for('index'))
    user = User.query.filter_by(username = session.get('user')[0]).first()
    return render_template('create_r.jinja')

@app.route('/profile/<id>', methods = ['GET', 'POST'])
def edit(id):
    if (not session.get('user')):
        return redirect(url_for('index'))
    user = User.query.filter_by(username = session.get('user')[0]).first()
    return render_template('edit.jinja')
    
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
    # new_user = User(username = 'malin11', password = 'malin123', firstname = 'Lin', lastname = 'Ma')
    # db.session.add(new_user)
    # db.session.commit()

    # user = User.query.filter_by(username = 'malin11').first()
    # new_r = Restaurant(name = 'third', phone = '120938109', address = 'akjsdnaskjd', category = 'aaa', description = 'ansdjaksndkajsndkajsndkajsnd')
    # user.restaurants.append(new_r)
    # db.session.commit()
    # print (user.restaurants)


