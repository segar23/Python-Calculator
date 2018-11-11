import re

print("Basic Calculator")
print("Type 'quit' to exit\n")

init = 0
run = True


def perform_math():
    global run
    equation = input("Enter Equation: ")
    if equation == "quit":
        run = False
    else:
        print("You typed", equation)


while run:
    perform_math()
