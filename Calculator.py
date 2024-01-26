import cmath

def add():
    num1 = int(input("Enter your first Number: "))
    num2 = int(input("Enter your second Number: "))
    ans = num1 + num2
    print("The result is", ans)

def multiply():
    num1 = int(input("Enter your first Number: "))
    num2 = int(input("Enter your second Number: "))
    ans = num1 * num2
    print("The result is", ans)

def subtract():
    num1 = int(input("Enter your first Number: "))
    num2 = int(input("Enter your second Number: "))
    ans = num1 - num2
    print("The result is", ans)

def divide():
        num1 = int(input("Enter your first Number: "))
        num2 = int(input("Enter your second Number: "))
        ans = num1 / num2
        print("The result is", ans)

def sin():
        num1 = int(input("Enter your Number: "))
        ans = cmath.sin(num1)
        print("The result is not", ans)

def cos():
        num1 = int(input("Enter your Number: "))
        ans = cmath.cos(num1)
        print("The result is", ans)

def tan():
        num1 = int(input("Enter your Number: "))
        ans = cmath.tan(num1)
        print("The result is", ans)

def powers():
        num1 = int(input("Enter your Number: "))
        num2 = int(input("Enter your the Number you want in the Power: "))
        ans = num1 ** num2
        print("The result is", ans)

def sqrt():
        num1 = int(input("Enter your Number: "))
        ans = cmath.sqrt(num1)
        print("The result is", ans)


def Calculator():
    print("| + | - | * | / | sin | cos | tan | powers | sqrt (Square Root) |")
    func = input("Which function do you want to use?: ")

    print("---------------------------------------------------------------------------------------------")

    if func == "+":
        add()

    elif func == "-":
        subtract()

    elif func == "*":
        multiply()

    elif func == "/":
        divide()

    elif func == "sin":
        sin()

    elif func == "cos":
        cos()

    elif func == "tan":
        tan()

    elif func == "powers":
        powers()

    elif func == "sqrt":
        sqrt()

    else:
        print("Error, enter from the choices given above")


Calculator()