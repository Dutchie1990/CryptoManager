# Import Flask
from flask import Flask, render_template
# Import mongoengine to comminucate with database
from flask_mongoengine import MongoEngine
# Extension for implementing Flask-Login for authentication
from flask_login import LoginManager
# Other imports
import os
if os.path.exists("cryptomanager/app/env.py"):
    import cryptomanager.app.env

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY") or "prc9FWjeLYh_KsPGm0vJcg",
    IP=os.environ.get("IP"),
    HOST=os.environ.get("PORT"),
    MONGODB_SETTINGS = {
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

from .api import API
cached_symbols = API.retrieve_data("/coins/list")

from .auth.views import auth
app.register_blueprint(auth)

from .general.views import general
app.register_blueprint(general)

from .assets.views import assets
app.register_blueprint(assets)

@app.template_filter("capitalized")
def capitalize(value):
    return value.capitalize()
