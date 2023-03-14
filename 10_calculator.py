

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    operand_a = int(input("What's the first number? "))
    while True:

        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")
        operand_b = int(input("What's the second number? "))

        calculation = operations[operation]

        answer = calculation(operand_a, operand_b)

        print(f"{operand_a} {operation} {operand_b} = {answer}")

        decision = input(f"Type 'y' to continue calulating with {answer}, type 'n' to start new, type x to exit ")
        if decision == 'y':
            operand_a = answer
        elif decision == 'n':
            operand_a = int(input("What's the first number? "))
        elif decision == 'x':
            return


def execute():
    print("Welcome to calculator!!!")

    calculator()


if __name__ == '__main__':
    execute()
