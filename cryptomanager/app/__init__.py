# Import Flask
from flask import Flask, render_template
# Import mongoengine to comminucate with database
from flask_mongoengine import MongoEngine
# Extension for implementing Flask-Login for authentication
from flask_login import LoginManager
# Other imports
from .api import API
import os
if os.path.exists("cryptomanager/app/env.py"):
    import cryptomanager.app.env

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY") or "prc9FWjeLYh_KsPGm0vJcg",
    IP=os.environ.get("IP"),
    HOST=os.environ.get("PORT"),
    MONGODB_SETTINGS={
        'db': os.environ.get("MONGO_DBNAME"),
        'host': os.environ.get('MONGODB_URI')
    }
)

db = MongoEngine(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"
login_manager.login_message = ("You need to be logged in to access this page.")
login_manager.login_message_category = "error"

api = API()
api.retrieve_symbols("/coins/list")
api.retrieve_vs_currencies("/simple/supported_vs_currencies")

from .auth.views import auth
app.register_blueprint(auth)

from .general.views import general
app.register_blueprint(general)

from .assets.views import assets
app.register_blueprint(assets)

from .transactions.views import transactions
app.register_blueprint(transactions)

from .leaderboard.views import leaderboard
app.register_blueprint(leaderboard)


@app.template_filter("capitalized")
def capitalize(value):
    return value.capitalize()


@app.template_filter("trim")
def trim(value):
    return '%.2f'%(value)


@app.template_filter("image")
def image(value):
    return "/static/img/symbols/{}.png".format(value.lower())


@app.errorhandler(Exception)
def server_error(err):
    return render_template("error.html")
