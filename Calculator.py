def add(a,b):
    return (a+b)

def substract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    try:
        return (a/b)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

def main():
    while True:
        print("Select Operation")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        operation = input("Enter the operation(1/2/3/4/5) ")

        if operation == '5':
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Input: Please enter a number")
            pass

        if operation == '1':
            print("Result: ", add(num1,num2))

        if operation == '2':
            print("Result: ", substract(num1,num2))

        if operation == '3':
            print("Result: ", multiply(num1,num2))

        if operation == '4':
            print("Result: ", divide(num1,num2))

if __name__ == "__main__":
    main()