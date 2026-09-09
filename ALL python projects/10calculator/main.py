print(""" _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")

def add(a1 ,a2):
    return a1 + a2

def subtract(x1 ,x2):
    return x1 - x2

def multiply(a1 ,a2):
    return a1 * a2

def devide(a1 ,a2):
    return a1 / a2

math_dictionary = {
    "+": add,
    "-": subtract, 
    "*": multiply,
    "/": devide 
}




def refresh():
    num1 = float(input("what is your first number? "))
    for key in math_dictionary:
        print(key)

    should_continue = True
    while should_continue:

        chosen_operation = input("pick an operation ")

        num2 = float(input("what is your next number? "))
        calculation = math_dictionary[chosen_operation]
        result = calculation(num1 ,num2) 

        print(f"{num1} {chosen_operation} {num2} = {result}")

        more = input(f"type 'y' to continue calculating with {result} or type 'n' to start a new calculation ")
        if more == "y":
            num1 = result
        elif more == "n":
            should_continue = False
            refresh()


refresh()