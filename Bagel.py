# MODS
import random

# GLOBAL VARIABLE
secretNum = ""
guess = ""
clue = []
GUESS_NUM = 1
game_running = True

# Global VARIABLE SETTINGS
MAX_GUESSES = 10
NUM_DIGITS = 3


# FUNCTIONS
# Gets the secret number
def getSecretNum():
    global secretNum

    number = list("0123456789")
    random.shuffle(number)
    secretNum = number[:3]
    secretNum = "".join(secretNum)


# Gets a valid guess from the user
def getGuess():
    global guess, GUESS_NUM

    while len(guess) != NUM_DIGITS:
        guess = input(f"Guess #{GUESS_NUM}:\n")


# this function helps reset the clue after every loop
def resetClue():
    global clue

    clue = []


# MAIN
print('''---------------------------------------------------------------------
Bagels, a deductive logic game.

I am thinking of a 3-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
    Pico    One digit is correct but in the wrong position.
    Fermi   One digit is correct and in the right position.
    Bagels  No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
---------------------------------------------------------------------''')
while game_running:
    print("I have thought up a number.")
    print(f'You have {MAX_GUESSES} guesses to get it right (Type "000" to quit).')
    getSecretNum()
    # print(secretNum)  #un-comment for testing purposes
    while GUESS_NUM < (MAX_GUESSES + 1):
        getGuess()
        if guess == "000":  # If the user enters "000" program ends
            break
        else:
            if guess == secretNum:
                print("You got it correct!")
                print(f"The secret number was [{secretNum}]")
                break
            elif guess != secretNum:
                for i in range(NUM_DIGITS):
                    if guess[i] == secretNum[i]:  # check for matching spot
                        clue.append("Fermi")
                    elif guess[i] in secretNum:  # check to see if number is in secretNum
                        clue.append("Pico")
                if len(clue) != 0:  # Sort the clues in order to not give away the answer
                    clue.sort()
                    clue = " ".join(clue)
                    print(clue)
                if len(clue) == 0:
                    print("Bagel")
            # RESET
            resetClue()
            guess = ""
            GUESS_NUM += 1
    if guess == "000":
        # Goodbye prompt when quitting the game
        print(f"The secret number was [{secretNum}]. \n\t\t\t\t\tGoodbye =]")
        break
    else:
        # Ask the user if they want to continue playing the game if they win or lose
        print(f">>>You ran out of guesses. The secret number was [{secretNum}].")
        response = input(">>>Do you want to play again? (YES/NO): ").upper()
        if response == "YES":
            # MASTER RESET
            print()
            guess = ""
            secretNum = ""
            GUESS_NUM = 1
            game_running = True
        else:
            # End the game
            game_running = False
print("exiting...")
