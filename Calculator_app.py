from enum import Enum
import operator


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
        print("-" * 30)
        return oper.value(a, b)

#Main part of code, this will be where the operations are handled

def run_calculator_app():
    calc_app = Calculator()
    print("Welcome to the calculator app!")
    print("Type 'exit' at anytime to quit")

    while True:
        try:
            num_1_str = input("Enter the first number(or 'exit') " )
            if num_1_str.lower() == "exit":
                break
            num1 = float(num_1_str)  # converts the string into a float... it should.
            oper_string = input("Enter operation (+, -, * , / ):")

            # Where i will assign the input of the string to an operation enum
            selected_operation = None
            if oper_string == "+":
                selected_operation = Operation.ADD
            elif oper_string == "-":
                selected_operation = Operation.SUBTRACT
            elif oper_string == "*":
                selected_operation = Operation.MULTIPLY
            elif oper_string == "/":
                selected_operation = Operation.DIVISION
            else:
                print("Please enter a valid operation such as +, -, *, / ")
                continue  # returns to the start
            # So the operation and the first number have been handled.

            #Handling of the second number (need to add exit here too)
            num2_str = input("Enter second number: ")
            num2 = float(num2_str)  # Convert input to a float

            # 3. Call the calculate method
            result = calc_app.calculate(num1, num2, selected_operation)

            # 4. Display the result
            print(f"Result: {num1} {oper_string} {num2} = {result}")
            print("-" * 30)

        except ValueError:
            print("Invalid number input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:  # Catch any other unexpected errors Need to research Exception
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    run_calculator_app()
#Need to dive into this more to fully grasp how this enabled my code to work,
# I know it's something to do with my unittest ap




