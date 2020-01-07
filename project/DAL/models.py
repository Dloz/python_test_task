import os, sys

#Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)

from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from DAL.config import SQLALCHEMY_DATABASE_URI
from DAL.db_saver import db_saver
import datetime 
from api.run import create_app
from DAL import config

db = SQLAlchemy()
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
app = create_app(config)

class Call(db.Model):
    '''
    Represents calls table in a database.
    '''
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

    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'caller_number': self.caller_number,
           'target_number': self.target_number,
           'call_started_time': self.call_started_time.strftime('%Y-%m-%d %H:%M:%S'),
           'call_ended_time': self.call_ended_time.strftime('%Y-%m-%d %H:%M:%S'),
           'cost': self.cost
       }

    
    @classmethod
    def create(cls, **kw):
        '''
        Saves instance of an object to the database.

        Args:
            cls: class on which method would be executed.
            **kw: keyword arguments which represents object to save.
        '''
        #from api.app import app
        obj = cls(**kw)
        with app.app_context():
            db.session.add(obj)
            db.session.commit()


class Tariff(db.Model):
    '''
    Represents tariffs table in a database.
    '''
    __tablename__ = 'tariffs'
    id = db.Column(db.Integer, primary_key=True)
    connection_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
