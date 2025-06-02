from enum import Enum
import operator
from re import match


class Operation(Enum):
    ADD = operator.add
    SUBTRACT = operator.sub
    MULTIPLY = operator.mul
    DIVISION = operator.truediv

class Calculator:

    def calculate(self, a, b, oper: Operation):
        if oper == Operation.DIVISION and b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return oper.value(a, b)

#Main part of code, this will be where the operations are handled
#Note: Come back to this once i have altered the Calculator Class then move to stage 2 of this project
my_calculator = Calculator()