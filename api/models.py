from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Call(db.Model):
    __tablename__ = 'calls'
    id = db.Column(db.Integer, primary_key=True)
    caller_number = db.Column(db.String(50), nullable=False)
    target_number = db.Column(db.String(50), nullable=False)
    call_started_time = db.Column(db.DateTime, nullable = False)
    call_ended_time = db.Column(db.DateTime, nullable = False)
    cost = db.Column(db.Numeric, nullable = False)

class Tariff(db.Model):
    __tablename__ = 'tariffs'
    id = db.Column(db.Integer, primary_key=True)
    connection_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric, nullable=False)