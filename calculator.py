from flask import (Flask, jsonify, request, abort, render_template)
import math
import sqlite3 as sql
import data

app = Flask(__name__)
operators = ['+','-','*','/']


@app.route("/")
def hello():
    return "Sezzle Calculator"

@app.route("/history", methods=['GET'])
def history():
        result=data.select_all_calculations()
        return (jsonify({"Answer" : result}), 200) 
    
@app.route("/calculate", methods=['POST'])
def calculate():
    problem = str(request.form['text'])
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
        return (jsonify({'Answer':result}), 200)        

    except ZeroDivisionError:
        data.insert(problem + " = Infinity")
        return "Infinity"
    except KeyError:
        return "Enter valid numbers"

if __name__ == '__main__':
    data.create_table()
    app.run(debug=True)