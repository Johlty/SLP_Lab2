from Functions.input_handler import get_number_input, get_operator_input
from Functions.operations import add, subtract, multiply, divide, power, square_root, modulo
from Functions.validation import is_valid_operator
from Functions.error_handler import handle_division_error, handle_value_error

class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = ''

    def get_input(self):
        self.num1 = get_number_input("Enter the first number: ")
        self.operator = get_operator_input()
        if self.operator != '√':
            self.num2 = get_number_input("Enter the second number: ")

    def calculate(self):
        try:
            if self.operator == '+':
                result = add(self.num1, self.num2)
            elif self.operator == '-':
                result = subtract(self.num1, self.num2)
            elif self.operator == '*':
                result = multiply(self.num1, self.num2)
            elif self.operator == '/':
                result = divide(self.num1, self.num2)
            elif self.operator == '^':
                result = power(self.num1, self.num2)
            elif self.operator == '√':
                result = square_root(self.num1)
            elif self.operator == '%':
                result = modulo(self.num1, self.num2)
            else:
                result = "Unknown operation!"
            print(f"Result: {result}")
        except ZeroDivisionError:
            handle_division_error()
        except ValueError as ve:
            handle_value_error(str(ve))

    def run(self):
        while True:
            self.get_input()
            if not is_valid_operator(self.operator):
                continue
            self.calculate()
            if input("Do you want to continue (yes/no)? ").lower() != 'yes':
                print("Thank you for using the calculator!")
                break
