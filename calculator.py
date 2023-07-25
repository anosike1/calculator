# import the calc_art module - the one I created
from calc_art import *

#define a calculator function to call the logo (which was stored in the calc_art file)
def calculator():
    print (logo)

# define the add, subtract, multiply, and divide functions
def add (x,y):
    return x+y
def subtract (x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide (x,y):
    return x/y

# create a dictionary with symbols as keys and the function names as the values
operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide
}

# call the calculator function
# this prints the logo or art on our screen
calculator()

# create an input for the first number and assign the value to a variable
# I converted the data to a float type to enable me work with decimals
num1 = float(input("What's the first number?: "))

# loop through the operations dictionary to get EACH key
for symbol in operations:
    print (symbol)

# create a variable and assign it to the TRUE boolean
# this acts like an ON switch
cont = True

# Create a while loop that runs as long as long as cont is TRUE 
# this will request for an operation
# request for the next number
# and call the function depending on the symbol selected
while cont:
    op_symbol = input ("Select an operation: ")
    num2 = float (input ("What's the next number?: "))
    calc_function = operations[op_symbol]
    answer = calc_function (num1,num2)

# the answer will also be printed out
    print (f"{num1}{op_symbol}{num2} = {answer}")

# you can proceed with further calculations or start a new one
    if input (f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calcualtion: ") == 'y':
        num1 = answer
    else:
        cont = False
        calculator()