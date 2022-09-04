from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# creating a flask application 
# the __name__ is the current name of the file
# the application is stored in the app variable

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db';
# we add external configuration using config 
# the key of the config is 'SQLALCHEMY_DATABASE_URI'
# and we set the sqllite database
# name of the database => market

app.config['SECRET_KEY'] = '2a46ac161c157f0d5b899062' 

'''
app.run(debug = False)
# setting the debugging to TRUE 
# the page automatically loads after any changes are made
'''

db = SQLAlchemy(app)
# connecting the flask app with the sqllite3 database 


