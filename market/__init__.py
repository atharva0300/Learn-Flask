from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# importing Bcrupt from the Flask bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '2a46ac161c157f0d5b899062'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
# creating an instance of the Brcypt app
# passing the app as an argument to the class

from market import routes