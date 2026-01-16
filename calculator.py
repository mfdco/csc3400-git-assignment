import sys

def main() :

    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    operation = input("What operation would you like : add, subtract, divide, multiply, divide, power, or square root?: ")

    if operation == "add" :
        print(add(x, y))
    elif operation == "subtract" :
        print(sub(x, y))
    elif operation == "divide" :
        print(div(x, y))
    elif operation == "multiply" :
        print(mul(x, y))
    elif operation == "power" :
        print(power(x, y))
    elif operation == "square root" :
        print(square_root(x))
    else:
        print("Invalid operation")

def add(x, y) :
    return x + y

def sub(x, y) : 
    return x - y

def mul(x, y) :
    return x * y 

def div(x, y) :
    if y != 0 :
        return x / y
    else :
        return "undefined"

def power(x, y) :
    return x ** y

def square_root(x) :
    if x < 0 :
        return "imaginary number"
    else :
        return x ** 0.5

if __name__ == "__main__":
    main()
