#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return parameter


@app.route("/count/<int:number>")
def count(number):
    list_items = [f'{num}\n' for num in range(0, number)]

    return f'{"".join(list_items)}'


@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f'{num1 + num2}'
    elif operation == "-":
        return f'{num1 - num2}'
    elif operation == "*":
        return f'{num1 * num2}'
    elif operation == "div":
        return f'{num1 / num2}'
    elif operation == "%":
        return f'{num1 % num2}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
