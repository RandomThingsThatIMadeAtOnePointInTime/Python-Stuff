import random

maxNumber = 100
correctNumber = random.randint(1, maxNumber)
hasGuessedCorrectly = False
guesses = 0
maxGuesses = int(maxNumber / 15)

def isnumber(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

while not hasGuessedCorrectly and guesses < maxGuesses:
    guess = input("What's the number? ")

    if not isnumber(guess):
        print("That's not a number, nerd")
        continue

    if int(guess) < correctNumber:
        print("Too low")
    if int(guess) > correctNumber:
        print("Too high")
    if int(guess) is correctNumber:
        hasGuessedCorrectly = True
    else:
        guesses += 1

if guesses is not maxGuesses:
    print("Correct! The number was " + str(correctNumber))
else:
    print("You're not very smart. The number was " + str(correctNumber) + ". Better luck next time, loser.")
