from contextlib import redirect_stderr
from flask import Flask, render_template
# importing render_template to return a file 

app = Flask(__name__)
# creating a flask application 
# the __name__ is the current name of the file
# the application is stored in the app variable

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
    # will be using the Jinja template 
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