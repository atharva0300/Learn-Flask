from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# importing Bcrupt from the Flask bcrypt

# importing login meneger provided by flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '2a46ac161c157f0d5b899062'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
# creating an instance of the Brcypt app
# passing the app as an argument to the class

# creating an instance of the Login manager app
login_manager = LoginManager(app)

login_manager.login_view = "login_page"
# if there is unauthorized access to the market page 
# then redirect it to the login page

login_manager.login_message_category = "info"
# set the category of the message of the login flash as info

from market import routes