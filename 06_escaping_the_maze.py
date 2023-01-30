example_solution = '''
# Example Solution

def turn_right():
    for _ in range(3):
        turn_left()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
        else:
            turn_left()
            move()
'''


def execute():
    print("This module uses an online code playground")
    print("Go to: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json"
          "&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json")
    print(example_solution)

if __name__ == '__main__':
    execute()
