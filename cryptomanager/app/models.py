# Methods to generate password and check password
from werkzeug.security import generate_password_hash, check_password_hash
# Extension for implementing Flask-Login for authentication
from flask_login import UserMixin
from mongoengine import (StringField, EmailField,
                         FloatField, ReferenceField, DateTimeField, CASCADE)
# Imports for database usage and login manager from app
from ..app import db, login_manager
# Import datetime to calculate today's date
import datetime


class User(UserMixin, db.Document):
    """User class

    Attributes:
        :firstname: The firstname of the user
        :email: The email of the user
        :password: The password of the user

    Methods:
        :check_password:
            param: password
        Method to check the password hash
        :set_password:
            param: password
        Method to generate password hash
    """

    firstname = db.StringField(required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True)

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
    """
        :load_user
            param: user_id
        Method to find the user based on user_id
    """
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
    except Exception as e:
        print(e)
        raise


class Assets(db.Document):
    """Assets class

    Attributes:
        :userid: Reference to the user
        :asset_name: The name of the asset
        :amount: The amount of the owned asset
        :costs: The avarage costs of the assets in USD
    Methods:
        :calculate_profits:
            param: list of assets
        Method to calculate the asset profit or loss in percent
        :calculate_current_value:
            param: list of assets
        Method to calculate the current value of the assets
    """

    userid = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    asset_name = db.StringField(required=True)
    amount = db.FloatField(required=True)
    costs = db.FloatField(required=True)

    def __init__(self, userid, asset_name, amount, costs=0, *args, **kwargs):
        super(Assets, self).__init__(*args, **kwargs)
        self.userid = userid
        self.asset_name = asset_name
        self.amount = amount
        self.costs = costs

    @staticmethod
    def calculate_profits(assets):
        for asset in assets:
            asset.p_l = (((asset.prize - asset.costs) / asset.costs) * 100)
        return assets

    @staticmethod
    def calculate_current_value(assets):
        current_value = sum([x.amount * x.prize for x in assets])
        return current_value


class Transactions(db.Document):
    """Transactions class

    Attributes:
        :userid: Reference to the user
        :date: The date of the transaction
        :ordertype: The type of order (deposit, withdrawal, sell or buy)
        :volume: The amount of the order
        :coin_symbol: The coin which is bought or sold
        :vs_currency: The currency which is used for the  transaction
        :price: The price which is payed or obtained with the order,
            depending on the ordertype
        :costs: The costs which is payed or obtained with the order,
            depending on the ordertype
    """

    userid = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    date = db.DateTimeField(required=True)
    ordertype = db.StringField(required=True)
    volume = db.FloatField(required=True)
    coin_symbol = db.StringField()
    vs_currency = db.StringField()
    prize = db.FloatField()
    costs = db.FloatField()
