import sys
def add(x, y) :
    return x + y

def sub(x, y) : 
    return x - y

def mul(x, y) :
    return x * y 

def div(x, y) :
    if y != 0 :
        return x // y
    else :
        return "undefined"

def power(x, y) :
    return x ** y

def square_root(x) :
    if x < 0 :
        return "imaginary number"
    else :
        return int(x ** 0.5)

