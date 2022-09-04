from flask import Flask, render_template, redirect , url_for
from flask_sqlalchemy import SQLAlchemy
# importing render_template to return a file 
from forms import RegisterForm

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

db = SQLAlchemy(app)

# creating a table from the class
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

    # creating a new column to set the owner of the item
    # this will be used for backref 
    owner = db.Column(db.Integer() , db.ForeignKey('user.id'))
    # maps with the id attribute of the user table 

    def __repr__(self) : 
        # the __repr__ method is an inbuilt private function 
        # we are overriding the method
        # This method is executed when we use the Item.query.all() method
        # # so, we are overriding it to return the below string 
        return f'Item {self.name}'


# creating another table from the class
class User(db.Model): 
    id = db.Column(db.Integer() , primary_key = True)
    username = db.Column(db.String(length = 30) , nullable = False , unique = True)   

    # new column for email address
    email_address = db.Column(db.String(length = 50) , nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 60) , nullable = False , unique = False)
    # totally fine is 2 users have the same password
    budget = db.Column(db.Integer() , nullable = False , default = 1000)
    # default => sets the default value to the column

    # creating a relationship with another table
    items = db.relationship('Item' , backref = 'owned_user' ,lazy =True)
    # backref => allows us to see the owner of the item 
    # lazy => setting the lazy to true will return the items in one shot 



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


@app.route('/register' , methods = ["GET" , "POST"]) 
# allowing the GET and POST request to access this url
# ommiting the methods will give an error
# important to mention the methods
def register_page() : 
    form = RegisterForm()

    # checking validation of the form
    if form.validate_on_submit() : 
        print("Form on vaildation : " , form.validate_on_submit)

        user_to_create = User(username = form.username.data , 
                            email_address = form.email_address.data,
                            password_hash = form.password1.data)
        # create a new user 
        # creating an instance of the User Class 
        # the username, email_address and password1 are the input labels from the form and not from the User class 
        # the password_hash  ,email_address , username on the left side of the '=' are from the User class


        db.session.add(user_to_create)
        # add the user to the database 
        db.session.commit()
        # save the changes to the database

        return redirect(url_for('market_page'))
        # redirecting the url
        # we are not hardcode encoding the url 
        # the url is dynamic 
        # redirects to the market_page 
        # insert the function name in the url_for() method 


    if form.errors!={} : 
        # if there are no errors from the validations 
        for err_msg in form.errors.values() : 
            print(f'There was an error with creating a user :  {err_msg}')

    return render_template('register.html' , form = form)

    # rendering the html form
    # passing the form to the html file