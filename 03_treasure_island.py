treasure_art = '''******************************************************************************* 
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''

game_description = 'Welcome to Treasure Island.\n Your mission is to find the treasure.'
crossroad_description = 'You are at a cross road. Where do you want to go? Type "left" or "right": '
right_death = 'The right path was the wrong one. You plummet to your death from a cliff. Game over!'
lake_description = 'You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for aboat. Type "swim to swim across: '
swim_death = 'You try to swim across the lake, but are eaten by a shoal of pikes. You are dead. Game over!'
island_description = 'A boat arrives and ferries you across. You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and ne blue. Which colour do you choose? '
red_death = 'You are burned to a crisp by a sudden wildfire. You are dead. Game over!'
blue_death = 'You are frozen to death by an unexpected change in the weather. Game over!'
victory_description = 'The yellow door leads you to untold wealth. You are winning at life!'


def execute():
    print(treasure_art)
    print(game_description)
    command = input(crossroad_description)
    if command == "right":
        print(right_death)
        return

    command = input(lake_description)
    if command == "swim":
        print(swim_death)
        return

    command = input(island_description)
    if command == "red":
        print(red_death)
        return
    if command == "blue":
        print(blue_death)
        return

    print(victory_description)


if __name__ == '__main__':
    execute()
