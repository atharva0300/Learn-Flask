from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, ValidationError
from market.models import User 


from wtforms.validators import Length, EqualTo, Email, DataRequired
# importing the validators for validating the input fields


# creating the regstration form
# this class is the form
class RegisterForm(FlaskForm) : 

    def validate_username(self , username_to_check) : 
        # checking if the username already exists or not 
        user = User.query.filter_by(username = username_to_check.data).first()
        # checking all the user's from the User table which has that username

        if user :
            # if the user already exists, then
            raise ValidationError('Username already exists! Please try a different username')
    
    # validating email_address 
    def validate_email_address(self , email_address_to_check) : 
        user = User.query.filter_by(email_address = email_address_to_check.data).first()


        if user : 
            raise ValidationError('Email address already exists! Please try a different username')



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



# creating Login form 
class LoginForm(FlaskForm) : 
    username = StringField(label = 'User Name:' , validators=[DataRequired()])
    password = StringField(label = 'Password:' , validators=[DataRequired()])
    submit = SubmitField(label = "Sign in")

     


