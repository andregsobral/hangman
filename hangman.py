
from random import choice

GAME_LAYOUT = [
    ["=", "=", "=",  "=", "="],
    ["=", " ",  " ", " ", " "],
    ["=", " ",  " ", " ", " "],
    ["=", " ",  " ", " ", " "],
    ["=", " ",  " ", " ", " "],
    ["=", " ",  " ", " ", " "]        
]

GAME_ACTIONS = [ 
    ["=", " ", "(", ")", " "], ["=", " ", "-", "-", "-"], ["=", " ", " ", "|", " "],
    ["=", " ", " ", "-",  " "], ["=", " ", "/", " ", " "], ["=", " ", "/", " ", "\\"]
]

def select_word():
    f = open("words.txt", "r")
    words = f.readlines()
    return choice(words).strip()

def print_secret_word(secret_word, correct_guesses):
    visible_len = correct_guesses+1
    output = []
    # --- Hide invisible characters
    for wi in range(len(secret_word)):
        word = secret_word[wi] if wi < visible_len else '-'
        output.append(word)
    secret_display = ''.join(output)
    print("Your word is: " + secret_display)

def validate_guess(secret_word, correct_guesses, player_guess):
    letter_guess_index = 1+correct_guesses
    letter = secret_word[letter_guess_index]
    return letter == player_guess

def get_layout():
    return GAME_LAYOUT

def get_actions():
    return GAME_ACTIONS

def print_hangman_state(maximum_guesses):
    # --- update layout based on action taken
    layout  = get_layout()
    actions = get_actions()
    layout_index = 1
    for i in range(len(actions)-maximum_guesses):
        layout[layout_index] = actions[i]
        # --- if the end of the is reached, don't increment
        if(layout_index != len(actions)-1):
            layout_index += 1

    # --- print layout
    for l in layout:
        print(''.join(l))


def the_game():
    secret_word = select_word()
    correct_guesses = 0
    maximum_guesses = 6
    while True:
        # --- Display secret word
        print_secret_word(secret_word, correct_guesses)
        # --- Get the players guess in lowercase
        player_guess = input("Guess a letter: ").lower()
        if validate_guess(secret_word, correct_guesses, player_guess):
            correct_guesses += 1
            print("Correct!")
            if(correct_guesses+1 == len(secret_word)):
                print("Yes! You did it!")
                return
        else:
            print("Sorry that is not correct...")
            maximum_guesses -= 1
            print_hangman_state(maximum_guesses)
            if(maximum_guesses == 0):
                print("Sorry you've been done in...")
                return

the_game()