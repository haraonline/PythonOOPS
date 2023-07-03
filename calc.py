PI = 3.14

def addtion(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero!")
    return a / b



if __name__ == "__main__":
    print("this part of code is executed only if the calc.py module is run as main program and not when called from other python files")


print(__file__) # prints the path of the file

