# import Flask
from flask import Flask
# import mongoengine to comminucate with database
from flask_mongoengine import MongoEngine
# other imports
import os
if os.path.exists("env.py"):
    import env

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