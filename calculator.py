import sys


def main() :

    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    operation = input("what operation would you like : add, subtract, divide, multiply, or divide?: ")

    if operation == "add":
        print(add(x, y))
    elif operation == "subtract":
        print(sub(x, y))
    elif operation == "divide":
        print(div(x, y))
    elif operation == "multiply":
        print(mul(x, y))
    else:
        print("Invalid operation")

def add(x, y) :
    return x + y

def sub(x, y) : 
    return x - y

def mul(x, y) :
    return x * y 

def div(x, y) :
    return x / y

if __name__ == "__main__":
    main()

