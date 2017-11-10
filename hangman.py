# Hangman, Jaden H.

def get_puzzle():
    return "wowsers"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Gimme a letter that might be in the word thank!")
    return letter

def display_board(solved):
    print(solved)

def show_result():
    print("Bruh Gj you're so cool")

def check_strikes():
    if strikes == limit:
        
    else:
def play():
    strikes = 0
    limit = 6
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    while solved != puzzle:
        guesses += get_guess()
        solved = get_solved(puzzle, guesses)
        show_result()
        display_board(solved)

def play_again():
    again = input("Wanna go again bbbboi! (y/n)")
    if again == "y":
        return True
    else:
        return False


y = True
while y == True:
    play()
    y = play_again()
