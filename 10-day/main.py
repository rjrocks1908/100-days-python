from art import logo
import os

#Calculator

#Add
def add(a, b):
    return a + b

#subtract
def subtract(a, b):
    return a - b

#multiply
def multiply(a, b):
    return a * b

#divide
def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    print(logo)
    num1 = float(input("What's the first number? "))
    answer = num1
    
    while True:
        
        for op in operations:
            print(op)
        
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
    
        num1 = answer
        answer = operations[operation_symbol](num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        choice = input(f"Type 'y' to continue calculating with the {answer}. Type 'n' to start new calculator.")
        if choice == "n":
            os.system('cls')
            break
        os.system('cls')