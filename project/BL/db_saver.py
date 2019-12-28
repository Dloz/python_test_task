import os, sys

#Following lines are for assigning parent directory dynamically.

dir_path = os.path.dirname(os.path.realpath(__file__))

parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)


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
        #Parse call object from file
        file_content = read(file_path)
        call_object = parse(file_content)

        #Calculate cost of the call.
        cost = calculate(
            call_duration=call_object.get_call_duration(), 
            connection_type=call_object.connection_type
            )

        #Add call object to the database.
        Call.create(
            caller_number=call_object.caller_number,
            target_number=call_object.target_number,
            call_started_time=call_object.call_started_time,
            call_ended_time=call_object.call_ended_time,
            cost=cost,
        )


if __name__ == '__main__':
    db_saver = DbSaver(db)
    db_saver.save('..\\test_folder\call1.json')

