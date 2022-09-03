from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField


# creating the regstration form
# this class is the form
class RegisterForm(FlaskForm) : 
    username = StringField(label = "User Name")
    # labelling the input 
    email_address = StringField(label = "Email")
    password1 = PasswordField(label = "Password")
    password2 = PasswordField(label= "Confirm Password")
    submit = SubmitField(label = "Create Account")

     


