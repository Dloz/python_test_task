from flask_restful import Resource
from flask import jsonify


class Calls(Resource):
    def get(self):
        from DAL.models import Call
        return jsonify(json_list=[i.serialize for i in Call.query.all()])
    
   