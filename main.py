import re

print("Basic Calculator")
print("Type 'quit' to exit\n")

init = 0
run = True


def perform_math():
    global run
    global init
    equation = ""
    if init == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(init))

    if equation == "quit":
        print("Good Bye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if init == 0:
            init = eval(equation)
        else:
            init = eval(str(init) + equation)


while run:
    perform_math()
