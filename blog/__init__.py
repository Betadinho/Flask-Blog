from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b3249d14ac73126a8c40d751f6865a1a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category = 'info'

from blog import routes
