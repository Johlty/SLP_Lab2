def is_valid_operator(operator):
    valid_operators = ['+', '-', '*', '/', '^', '√', '%']
    if operator not in valid_operators:
        print("Invalid operator! Please enter a valid operator.")
        return False
    return True
