def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operator_input():
    return input("Enter operator (+, -, *, /, ^, √, %): ")
