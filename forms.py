from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField

from wtforms.validators import Length, EqualTo, Email, DataRequired
# importing the validators for validating the input fields


# creating the regstration form
# this class is the form
class RegisterForm(FlaskForm) : 
    username = StringField(label = "User Name" , validators = [Length(min=2 ,max=30) , DataRequired() ])
    # setting the min and max characters to 2 and 30
    # DataRequired => makes the input field mandatory to fill
    # labelling the input 
    email_address = StringField(label = "Email" , validators=[Email() , DataRequired()])
    # checking the email's @ sign

    password1 = PasswordField(label = "Password" , validators= [Length(min=6) , DataRequired()])
    # setting the min characters to 6 
    password2 = PasswordField(label= "Confirm Password" , validators=[EqualTo('password1') , DataRequired()])
    # EqualTo(password1) validates to the password1 field 
    submit = SubmitField(label = "Create Account")

     


