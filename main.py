import re

print("Basic Calculator")
print("Type 'quit' to exit\n")

init = 0
run = True


def perform_math():
    global run
    global init
    equation = input("Enter Equation: ")
    if equation == "quit":
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        init = eval(equation)
        print("You typed", init)


while run:
    perform_math()
