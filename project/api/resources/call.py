from flask_restful import Resource
from flask import jsonify

class Call(Resource):
     def get(self, number):
        from DAL import models
        return jsonify(json_list=[
            i.serialize 
            for i in models.Call.query.filter(models.Call.target_number==number or models.Call.caller_number==number).all()
        ])