from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "A very long string"

from app import routes