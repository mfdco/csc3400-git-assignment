import calculator

def main() :

    total = 0

    while True:

        operation = input("What operation would you like : add, subtract, divide, multiply, divide, power, or square root? (quit to exit): ")

        if operation == "quit" :
            break

        if operation == "square root" :
            if total < 0 :
                print(calculator.square_root(total))
            else :
                total = calculator.square_root(total)

            continue

        num = int(input("Enter the number: "))

        if operation == "add" :
            total = calculator.add(total, num)

        elif operation == "subtract" :
            total = calculator.sub(total, num)

        elif operation == "divide" :
            if num != 0 :
                total = calculator.div(total, num)
            else :
                print(calculator.div(total, num))

        elif operation == "multiply" :
            total = calculator.mul(total, num)

        elif operation == "power" :
            total = calculator.power(total, num)

        else:
            print("Invalid operation")


    print(total)

if __name__ == "__main__" :
    main()