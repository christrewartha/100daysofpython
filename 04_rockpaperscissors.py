import random
import time

ROCK = 0
PAPER = 1
SCISSORS = 2

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper_art = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
ascii_map = [rock_art, paper_art, scissors_art]


def draw_art(selection):
    print(ascii_map[selection])


def determine_winner(human, computer):
    if human == ROCK:
        if computer == PAPER:
            print("Paper covers Rock. Computer wins!!!")
        elif computer == SCISSORS:
            print("Rock bashes Scissors. Human wins!!!")
        else:
            print("Rock on Rock. It's a tie!")
    elif human == PAPER:
        if computer == ROCK:
            print("Paper covers Rock. Human wins!!!")
        elif computer == SCISSORS:
            print("Scissors cut Paper. Computer wins!!!")
        else:
            print("Paper on Paper. It's a tie!")
    else:  # SCISSORS
        if computer == ROCK:
            print("Rock bashes Scissors. Computer wins!!!")
        elif computer == PAPER:
            print("Scissors cut Paper. Human wins!!!")
        else:
            print("Scissors on Scissors. It's a tie!")


def execute():
    accepted_input = ['0', '1', '2']
    choice = input("What do you choose? Press 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
    if choice not in accepted_input:
        print("You don't know how to play this game!")
        return

    player_choice = int(choice)
    draw_art(player_choice)

    time.sleep(1)

    computer_choice = random.randint(0, 2)
    draw_art(computer_choice)

    time.sleep(0.5)

    determine_winner(player_choice, computer_choice)


if __name__ == '__main__':
    execute()
