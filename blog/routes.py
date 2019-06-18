from flask import request, render_template, url_for, flash, redirect
from blog import app, db, bcrypt
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author':   'Alpha Prechtl',
        'title':    'Blog-Post 1',
        'content':  'First post test content which is longer than the first!',
        'date_posted':  '14. Mai, 2019',
    },
    {
        'author':   'Beta Prechtl',
        'title':    'Blog-Post 2',
        'content':  'Second post test content',
        'date_posted':  '14. Mai, 2019',
    }
]


@app.route("/")
@app.route("/home")
@app.route("/home/<name>")
def home(name=None):
    return render_template('home.html', posts=posts)


@app.route("/about")
def about(name=None):
    return render_template('about.html', title='About')


@app.route("/login", methods=['GET', 'POST'])
def login(name=None):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            ## /next
            next_destination = check(request.args.get('next'))
            return redirect(url_for(next_destination)) if next_destination else redirect(url_for('home'))
            flash(f'Welcome', current_user.username, 'success')
        else:
            flash('Login failed. Please check email and password!', 'danger')  # Bootstrap danger class
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register(name=None):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')


# Temporary Methods that need to be put in seperate Files
def removechar(literal):
        fixed_string = ''.join(literal.split('/', 1))
        return fixed_string
    

def check(literal):
    if literal != None:
        removechar(literal) 


# _____________________________________Testing
