import os
import shutil

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

    if selection < len(file_list):
        module_name = file_list[selection]
        # remember to strip the extension
        module = __import__(module_name[0:-3])
        print(f'Playing {module_name[3:-3]}')
        module.execute()
    else:
        choice = input("Do you want to create a new file? ").upper()
        if choice == 'Y' or choice == "YES":
            module_name = input("What module are you creating? ").lower().replace(' ', '_')
            num_files = len(file_list)
            new_file_index = str(num_files + 1).zfill(2)
            new_file_name = f'{new_file_index}_{module_name}.py'
            print(f'Creating new file: {new_file_name}')
            src = '__template__.py'
            print(shutil.copyfile(src, new_file_name))


if __name__ == '__main__':
    execute()

