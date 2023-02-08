import random

Repeat = "y"
#EasyLB = open('leaderboard.txt','w')
with open('leaderboard.txt', 'r') as file:
    print(file.read())

print("Welcome to the number guessing game!")

while Repeat == "yes" or Repeat == "y":

    GuessedOrLost = False
    NoGuesses = 0
    Guesses = 0

    while Guesses == 0:
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
        else:
            print("That is not a valid difficulty.")

    print("Selecting a number between 1 and 100!")
    Number = random.randint(1, 100)

    while GuessedOrLost == False:
        if Difficulty != "easy":
            Guess = input(f"You have {Guesses-NoGuesses} guesses left! What will your guess be? ")
        else:
            Guess = input("What will your guess be? ")
        try:
            Testing = float(Guess)
        except ValueError:
            Guess = -1
        Guess = float(Guess)
        if Guess > 100 or Guess < 0 or Guess.is_integer() == False:
            print("Please only guess a whole number between 1 and 100.")
        elif Guess > Number:
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



    print(" ")
    Repeat = input("Would you like to play again? (Yes/No) ").lower()