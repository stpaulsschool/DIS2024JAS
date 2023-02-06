import random

NoGuesses = 0
GuessedOrLost = False

print("Welcome to the number guessing game!")
print(" ")
print("What difficulty do you want?")
print("Easy: Unlimited Guesses")
print("Medium: 7 Guesses")
print("Hard: 5 Guesses")
print("Impossible: 1 Guess")
print(" ")
Difficulty = input("Difficulty: ").lower()

if Difficulty == "easy":
    Guesses = -1
elif Difficulty == "medium":
    Guesses = 7
elif Difficulty == "hard":
    Guesses = 5
elif Difficulty == "impossible":
    Guesses = 1

Number = random.randint(1, 100)

while GuessedOrLost != True:
    Guess = int(input("What will your guess be? "))

    if Guess > Number:
        NoGuesses = NoGuesses + 1
        print("You're guess was too high")
    elif Guess < Number:
        NoGuesses = NoGuesses + 1
        print("You're guess was too low")
    elif Guess == Number:
        NoGuesses = NoGuesses + 1
        print(f"Congrats! You got it in {NoGuesses} guesses!")
        GuessedOrLost = True

    if GuessedOrLost != True and NoGuesses == Guesses:
        print(f"You lost. The number was {Number}.")
        GuessedOrLost = True