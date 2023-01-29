

def get_total_bill() -> float:

    while True:
        total_bill_str = input("What was the total bill? ")
        if total_bill_str.isnumeric():
            return float(total_bill_str)


def get_number_of_people() -> int:

    while True:
        num_people_str = input("How many people to split the bill? ")
        if num_people_str.isnumeric():
            return int(num_people_str)


def get_tip() -> int:

    while True:
        tip_str = input("What percentage tip would you like to give? 10, 12, or 15? ")
        if tip_str.isnumeric():
            tip_num = int(tip_str)
            if tip_num in [10, 12, 15]:
                return tip_num


def execute():
    print("Welcome to the tip calculator.")
    total_bill = get_total_bill()
    num_people = get_number_of_people()
    tip = get_tip()
    split = (total_bill * (1 + tip/100)) / num_people
    print(f"Each person should pay: ${split:.2f}")


if __name__ == '__main__':
    execute()
    