from flask import (Flask, jsonify, request, abort, render_template)
from flask_restful import Resource, Api
import sqlite3 as sql

import data

app = Flask(__name__)
api = Api(app)

operators = ['+','-','*','/']

class History(Resource):
    def get(self):
        result=data.select_all_calculations()
        return result,200
 
class Calculate(Resource):
    def post(self):
        problem = str(request.form['data'])
        print(len(problem.split()))
        result=''
        if len(problem.split()) !=3 or problem.split()[1] not in operators:
            return "Enter a valid text. Format 3 * 4"

        operator = problem.split()[1]
        operand1 = problem.split()[0]
        operand2 = problem.split()[2]
        if (not operand1.lstrip('-').replace('.','',1).isdigit()) or (not operand2.lstrip('-').replace('.','',1).isdigit()):
            return "Enter valid number."

        if '.' in operand1 or '.' in operand2:
            operand1 = float(operand1)
            operand2 = float(operand2)
        else:
            operand1 = int(operand1)
            operand2 = int(operand2)
        try:
            if operator == '*':
                result=str(operand1 * operand2)
            elif operator == '+':
                result= str(operand1 + operand2)
            elif operator == '-':
                result=str(operand1 - operand2)
            elif operator == '/':
                result=str(operand1 / operand2)
            data.insert(problem + " = "+ result)
            return result, 201     

        except ZeroDivisionError:
            data.insert(problem + " = Infinity")
            return "Infinity", 201
        except KeyError:
            return "Enter valid numbers"

api.add_resource(History, '/history')
api.add_resource(Calculate, '/calculate')

if __name__ == '__main__':
    data.create_table()
    app.run(host='0.0.0.0',debug=True,port=8080)