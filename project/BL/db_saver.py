from BL.file_reader import read
from BL.json_parser import parse
from BL.models import Call
from flask_sqlalchemy import SQLAlchemy
from BL.cost_calculator import calculate
from DAL.models import Call

db = SQLAlchemy()

class DbSaver:
    def __init__(self, db):
        self.db = db
    
    def save(self, file_path):
        file_content = read(file_path)
        call_object = parse(file_content)
        cost = calculate(
            call_duration=call_object.get_call_duration(), 
            connection_type=call_object.connection_type
            )
        call_db_model = Call(
            caller_number=call_object.caller_number,
            target_number=call_object.target_number,
            call_started_time=call_object.call_started_time,
            call_ended_time=call_object.call_ended_time,
            cost=cost,
            )

