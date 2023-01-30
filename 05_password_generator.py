import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+', '-', '*', '/', '£', '$', '%', '@', '#', '~']


def execute():
    print("Welcome to the PyPassword Generator!")
    num_letters = int(input("How many letters would you like in your password?\n"))
    num_numbers = int(input("How many numbers would you like?\n"))
    num_symbols = int(input("How many symbols would you like?\n"))

    password = []
    for i in range(num_letters):
        if random.choice([True, False]):
            password.append(letters[random.randint(0, len(letters) - 1)])
        else:
            password.append(letters[random.randint(0, len(letters) - 1)].upper())
    for i in range(num_numbers):
        password.append(numbers[random.randint(0, len(numbers) - 1)])
    for i in range(num_symbols):
        password.append(symbols[random.randint(0, len(symbols) - 1)])

    random.shuffle(password)
    password_str = ''.join(password)
    print(f'Your password is {password_str}')


if __name__ == '__main__':
    execute()
