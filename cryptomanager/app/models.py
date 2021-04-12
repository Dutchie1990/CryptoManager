# Methods to generate password and check password
from werkzeug.security import generate_password_hash, check_password_hash
# Extension for implementing Flask-Login for authentication
from flask_login import UserMixin
from mongoengine import StringField, EmailField, FloatField, ReferenceField
# Imports for database usage and login manager from app
from ..app import db, login_manager

class User(UserMixin, db.Document):
    firstname = db.StringField(required=True)
    email = db.StringField(required=True)
    password =  db.StringField(required=True)
    
    def __init__(self, firstname="", email="", password="", *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.firstname = firstname
        self.email = email
        self.password = password
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

@login_manager.user_loader
def load_user(user_id):
    try: 
        return User.objects.get(id=user_id) 
    except Exception as e: 
        print(e)
        raise

class Assets(db.Document):
    userid = db.ReferenceField(User, reverse_delete_rule="CASCADE")
    asset_name = db.StringField(required=True)
    amount = db.FloatField(required=True)
    prize = db.FloatField()
    p_l = db.FloatField()

    def __init__(self, userid, asset_name, amount, prize=0.0, p_l=0.0, *args, **kwargs):
        super(Assets, self).__init__(*args, **kwargs)
        self.userid = userid
        self.asset_name = asset_name
        self.amount = amount
        self.prize = prize
        self.p_l = p_l