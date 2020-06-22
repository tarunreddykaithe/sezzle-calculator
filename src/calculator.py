from flask import (Flask, jsonify, request, abort, render_template)
from flask_restful import Resource, Api
import sqlite3 as sql
import logging, re

from model import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('index.html')

class History(Resource):
    """
    GET method to retrieve last 10 operations
    """
    def get(self):
        result=list_operations()
        return result, 200
 
class Calculate(Resource):

    """
    POST method to calculate the operation, store in the database and return the result
    """
    def post(self):
        try:
            if request.is_json:
                problem = request.get_json().get('operation')
            else:
                problem=request.form['operation']
            if problem == "":
                return "Enter value",422   
            #regular expression to validate given input is correct or not
            regex = r"^\s*([-+]?)(\(?\d*\.?\d*\)?)(?:\s*([-+*\/%])\s*((?:\s[-+])?\(?\d*\.?\d*\)?)\s*)*$"
            matches = re.match(regex, problem)

            if not matches:
                return "Enter a valid text. Format 3*4",422

            #calculates the operation and formats the result
            result = ('%.4f' % eval(problem)).rstrip('0').rstrip('.')
            
            store_operation({'operation': problem + " = "+ str(result)})
            return result, 201     

        except ZeroDivisionError:
            store_operation({'operation': problem + " = Infinity"})            
            return "Infinity", 201
            
        except (SyntaxError, TypeError, KeyError) as e:
            logger.error("Error is :"+str(e))
            return "Enter valid data",422

api.add_resource(History, '/history')
api.add_resource(Calculate, '/calculate')

if __name__ == '__main__':
    # drops previous data(not shared sessions data) and creates new table. We can skip the drop command if needed.
    create_calculations_table()
    app.run(host='0.0.0.0',debug=False,port=8080)