from enum import Enum
import operator
from re import match

#This is where I keep the operations that will be called in the calculator app.
class Operation(Enum):
    ADD = operator.add
    SUBTRACT = operator.sub
    MULTIPLY = operator.mul
    DIVISION = operator.truediv

#This is where the function of the calculator will be handled and the maths operation will be called.
class Calculator:

    def calculate(self, a, b, oper: Operation):
        if oper == Operation.DIVISION and b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return oper.value(a, b)

#Main part of code, this will be where the operations are handled

def run_calculator_app():
    calculator_app_home = Calculator()
    print("Welcome to the calculator app!")
    print("Type exit at anytime to quit")

while True:
    try:
        num_1_str = input("Enter the first number(or 'exit')")
        if num_1_str.lower() == "exit":
            break
        num1 = float(num_1_str) #converts the string into a float... it should.
        oper_string = input("Enter operation (+, -, * , / ):")

        #Where i will assign the input of the string to an operation enum
        if oper_string ==





