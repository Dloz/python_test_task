from flask_restful import Resource
from DAL.models import Call
from flask import jsonify


class Calls(Resource):
    def get(self):
        return jsonify(json_list=[i.serialize for i in Call.query.all()])
    
   