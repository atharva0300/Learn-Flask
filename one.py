from contextlib import redirect_stderr
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# importing render_template to return a file 

app = Flask(__name__)
# creating a flask application 
# the __name__ is the current name of the file
# the application is stored in the app variable

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db';
# we add external configuration using config 
# the key of the config is 'SQLALCHEMY_DATABASE_URI'
# and we set the sqllite database
# name of the database => market


db = SQLAlchemy(app)
# connecting the flask app with the sqllite3 database 

class Item(db.Model): 
    # creating a class named Item 
    # and inheriting the db.Model class 
    # Model is a class in the db 

    # creating the primary key ( the identiier )
    id = db.Column(db.Integer() , primary_key = True)

    name = db.Column(db.String(length = 30) , nullable = False , unique = True)
    # stating the maximum length of the characters to 30
    # creating a column named as 'name'
    # This field wont have NULL values, so we set the nullable as False
    # making the column data unique, we set the unique as True

    # creating a new column
    price = db.Column(db.Integer() , nullable = False)
    barcode = db.Column(db.String(length =12) , nullable = False , unique = True)
    description = db.Column(db.String(length = 1024) , nullable = False , unique = True)

    def __repr__(self) : 
        # the __repr__ method is an inbuilt private function 
        # we are overriding the method
        # This method is executed when we use the Item.query.all() method
        # # so, we are overriding it to return the below string 
        return f'Item {self.name}'



@app.route('/')
# adding the homepage location 
@app.route('/home')
# routing to the homepage ( / )
# decorator function 
def home_page() : 
    return render_template('home.html')
    # returning the html file


# another decorator 
@app.route('/about/<username>')
# the username will be put in the url by the user 
# and the specific request to the username will be received
# this below function will be executed when the url goes to about location
def about_page(username) : 
    # taking the username argument
    return f'<h1>About Page of {username} </h1>'


# creating another route 
@app.route('/market')
def market_page(): 
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    
    return render_template('market.html' , item_name = items)
    # item_name is the key name 
    # items is the value of the key
    # will be using the Jinja tem   plate 
    # we can then use the item_name directly in the market.html file 


@app.route('/base')
def base_page() : 
    return render_template('base.html')

@app.route('/base2')
def base_page2() : 
    return render_template('base2.html')

@app.route('/table')
def table_page() : 
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('table.html' , item_name = items)

@app.route('/market2')
def market_page2() : 
    items = Item.query.all() 
    # getting all the items 
    return render_template('market.html' , item_name = items)