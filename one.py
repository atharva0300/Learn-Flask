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
