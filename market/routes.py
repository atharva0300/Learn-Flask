from market import app,db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm


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
                            password = form.password1.data)
        # create a new user 
        # creating an instance of the User Class 
        # the username, email_address and password1 are the input labels from the form and not from the User class 
        # the password_hash  ,email_address , username on the left side of the '=' are from the User class

        # password is the new hashed password aftr crypting it

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
            # print(f'There was an error with creating a user :  {err_msg}')

            flash(f'There was an error with creating a user :  {err_msg}' , category='danger')
            # flashes the message 
            # get_flashed_message => collects the flashed message


    return render_template('register.html' , form = form)

    # rendering the html form
    # passing the form to the html file