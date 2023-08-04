def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def main():
    operation = input("Please select the operation: +, -, *, or /: ")
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))

    if operation == "+":
        print(number_1, "+", number_2, "=", add(number_1, number_2))
    elif operation == "-":
        print(number_1, "-", number_2, "=", subtract(number_1, number_2))
    elif operation == "*":
        print(number_1, "*", number_2, "=", multiply(number_1, number_2))
    elif operation == "/":
        print(number_1, "/", number_2, "=", divide(number_1, number_2))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
