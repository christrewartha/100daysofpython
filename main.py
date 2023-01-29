import os

file_list = []


def get_100_days_exercises():

    # list all the files in the folder
    index = 1
    for x in os.listdir():
        if x.endswith(".py") and x[0:1].isnumeric():
            file_list.append(x)
            print(f'{len(file_list)} - {x}')


def execute():

    get_100_days_exercises()
    selection = input(f'Select a file to play, from 1 to {len(file_list)}: ')
    selection = int(selection) - 1

    module_name = file_list[selection]
    # remember to strip the extension
    module = __import__(module_name[0:-3])
    print(f'Playing {module_name[3:-3]}')
    module.execute()


if __name__ == '__main__':
    execute()

