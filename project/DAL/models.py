from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from DAL.config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.types import TypeDecorator
import datetime 

db = SQLAlchemy()
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)


class Call(db.Model):
    __tablename__ = 'calls'
    id = db.Column(db.Integer, primary_key=True)
    caller_number = db.Column(db.String(50), nullable=False)
    target_number = db.Column(db.String(50), nullable=False)
    call_started_time = db.Column(db.TIMESTAMP(timezone=False), nullable = False)
    call_ended_time = db.Column(db.TIMESTAMP(timezone=False), nullable = False)
    cost = db.Column(db.Numeric, nullable = False)

    def __init__(self, caller_number, target_number, call_started_time, call_ended_time, cost):
        self.caller_number = caller_number
        self.target_number = target_number
        self.call_started_time = call_started_time
        self.call_ended_time = call_ended_time
        self.cost = cost

    
    @classmethod
    def create(cls, **kw):
        from api.app import app
        obj = cls(**kw)
        with app.app_context():
            db.session.add(obj)
            db.session.commit()

class Tariff(db.Model):
    __tablename__ = 'tariffs'
    id = db.Column(db.Integer, primary_key=True)
    connection_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric, nullable=False)


class IntegerTimestamp(TypeDecorator):
    impl = db.Integer

    def __init__(self):
        TypeDecorator.__init__(self, as_decimal=False)

    def process_bind_param(self, value, dialect):
        return value.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000

    def process_result_value(self, value, dialect):
        return datetime.datetime.utcfromtimestamp(value / 1000)