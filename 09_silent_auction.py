import os


def clear_screen():
    os.system('cls')


def get_name_and_bid():
    name = input("What is your name? ")
    bid = input("How much do you bid (in dollars)? ")
    return name, bid


def execute():
    print("Welcome to the secret auction!")
    print("We will clear the screen, pass the computer to the first person to enter a bid")
    bidding = True
    secret_dict = {}

    while bidding:
        clear_screen()
        name, bid = get_name_and_bid()
        secret_dict[name] = bid

        make_another_bid = input("Enter another bid? Y/N: ")
        if make_another_bid != 'Y' and make_another_bid != 'y':
            bidding = False

    clear_screen()

    # get the highest bid
    highest_bid = 0.0
    highest_bidder = ''
    for key in secret_dict:
        bid = float(secret_dict[key])
        if bid > highest_bid:
            highest_bidder = key
            highest_bid = bid

    # this formats the highest bid, should we round it instead?
    print(f"The winner bidder was {highest_bidder} who bid ${highest_bid:.2f}")


if __name__ == '__main__':
    execute()
