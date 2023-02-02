import random

title_image = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
target_word = []
current_attempt = []
used_letters = []
word_list = ['ABRUPTLY',
                'AWKWARD',
                'BAGPIPES',
                'BANDWAGON',
                'BEEKEEPER',
                'BLIZZARD',
                'BOOKWORM',
                'BUCKAROO',
                'BUFFALO',
                'BUFFOON',
                'BUZZARD',
                'BUZZWORDS',
                'COCKINESS',
                'CURACAO',
                'DAIQUIRI',
                'DISAVOW',
                'DIZZYING',
                'EMBEZZLE',
                'ESPIONAGE',
                'FISHHOOK',
                'FIXABLE',
                'FLAPJACK',
                'FLUFFINESS',
                'FOXGLOVE',
                'FRAZZLED',
                'GALVANIZE',
                'GROGGINESS',
                'HAPHAZARD',
                'IATROGENIC',
                'JAUNDICE',
                'JAWBREAKER',
                'JUKEBOX',
                'KILOBYTE',
                'KIWIFRUIT',
                'MEGAHERTZ',
                'MICROWAVE',
                'MNEMONIC',
                'NIGHTCLUB',
                'PEEKABOO',
                'PNEUMONIA',
                'RAZZMATAZZ',
                'STRONGHOLD',
                'THRIFTLESS',
                'THUMBSCREW',
                'TRANSGRESS',
                'VOYEURISM',
                'WELLSPRING',
                'WITCHCRAFT',
                'WRISTWATCH',
                'ZIGZAGGING']

display_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = len(display_stages) - 1

def select_word():
    global target_word, current_attempt
    target_word = random.choice(word_list)
    current_attempt = ['_'] * len(target_word)


def get_guess():
    global used_letters
    while True:
        guess = input("Guess a letter: ").upper()[0]
        if guess not in used_letters:
            used_letters.append(guess)
            return guess
        print("You've already used that one!")


def check_guess(guess):
    global lives, current_attempt
    if guess in target_word:
        print("Well done!")
        for i in range(len(target_word)):
            if target_word[i] == guess:
                current_attempt[i] = guess
    else:
        print(f"Bad luck, {guess} wasn't in the word")
        lives -= 1


def display_status():
    print(f'Lives: {lives}')
    print(display_stages[lives])
    print(' '.join(current_attempt))


def is_success() -> bool:
    if '_' not in current_attempt:
        print(' '.join(current_attempt))
        print("You win!")
        return True
    return False


def is_failure() -> bool:
    if lives == 0:
        display_status()
        print('Game over')
        return True
    return False


def execute():
    print(title_image)
    select_word()

    while True:
        display_status()
        guess = get_guess()
        check_guess(guess)

        if is_success() or is_failure():
            break


if __name__ == '__main__':
    execute()

