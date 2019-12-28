from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from DAL.models import db
from DAL import config

app = Flask(__name__)
app.config.from_object(config)
app.app_context().push()
db.init_app(app)
