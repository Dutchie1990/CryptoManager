# import Flask
from flask import Flask
# other imports
import os
if os.path.exists("env.py"):
    import env

app = Flask(__name__)