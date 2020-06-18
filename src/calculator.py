from flask import (Flask, jsonify, request, abort, render_template)
from flask_restful import Resource, Api
import sqlite3 as sql
import re

import data

app = Flask(__name__)
api = Api(app)

class History(Resource):
    def get(self):
        result=data.select_all_calculations()
        return jsonify(result)
 
class Calculate(Resource):
    def post(self):
        problem = str(request.form['data'])
        if problem == "":
            return "Enter value"
        regex = r"^\s*([-+]?)(\d*\.?\d*)(?:\s*([-+*\/])\s*((?:\s[-+])?\d*\.?\d*)\s*)+$"
        matches = re.match(regex, problem)

        if not matches:
            return "Enter a valid text. Format 3*4"
        try:
            result=str(eval(problem))
            data.insert({'operation': problem + " = "+ result})
            return result, 201     

        except ZeroDivisionError:
            data.insert({'operation': problem + " = Infinity"})
            return "Infinity", 201
        except KeyError:
            return "Enter valid numbers"

api.add_resource(History, '/history')
api.add_resource(Calculate, '/calculate')

if __name__ == '__main__':
    data.create_table()
    app.run(host='0.0.0.0',debug=False,port=8080)