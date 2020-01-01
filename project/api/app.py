from flask import Blueprint
from flask_restful import Api
from api.resources.calls import Calls
from api.resources.call import Call
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

with app.app_context():
    db.create_all()


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Calls, '/calls')
api.add_resource(Call, '/calls/<string:number>')