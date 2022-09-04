from market import db
from market import bcrypt


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

    # using the decorator of property 
    @property
    def password(self ): 
        # decorator function 
        # this is a getter function 
        # which will return the password
        return self.password


    @password.setter
    # new decorator function 
    # to set the password
    # this is a setter function, which will set the hashed password
    def password(self , plain_text_password) : 
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
        # using utf-8 decoding
        # generating the password hash using bcrypt from the plain text password
        # and storing it in password_hash

