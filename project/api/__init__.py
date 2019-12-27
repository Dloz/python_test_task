from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import api.config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(api.config)
app.app_context().push()
db.init_app(app)
