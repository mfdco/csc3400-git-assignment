import sys

def add(x, y) :
    if isinstance(x, str) or isinstance(y, str) :
        print('Can\'t input a string, must be a number\t')
    return x + y

def sub(x, y) :
    if isinstance(x, str) or isinstance(y, str) :
        print('Can\'t input a string, must be a number\t')
    return x - y

def mul(x, y) :
    if isinstance(x, str) or isinstance(y, str) :
        print('Can\'t input a string, must be a number\t')
    return x * y 

def div(x, y) :
    if isinstance(x, str) or isinstance(y, str) :
        print('Can\'t input a string, must be a number\t')
    if y != 0 :
        return x / y
    else :
<<<<<<< HEAD
        return "undefined, becuase you cannot divide by 0"
=======
        return "Undefined, can't divide by zero"
>>>>>>> feature/error-handling

def power(x, y) :
    if isinstance(x, str) or isinstance(y, str) :
        print('Can\'t input a string, must be a number\t')
    return x ** y

def square_root(x) :
    if isinstance(x, str):
        print('Can\'t input a string, must be a number\t')
    if x < 0 :
<<<<<<< HEAD
        return "imaginary number, you cannot find square root of negative number  "
=======
        return "Imaginary number, can't take root of negative numbers"
>>>>>>> feature/error-handling
    else :
        return int(x ** 0.5)

