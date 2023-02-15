import random

Repeat = "y"
NameValid = False

print("Welcome to the number guessing game!")

while NameValid != True:
    Invalid = False
    Name = input("What is you name? ")

    for Character in Name:
        if Invalid == False:
            if Character.isalpha() != True:
                print("Please only use regular characters.")
                Invalid = True

    if Invalid == False:
        NameValid = True

while Repeat == "yes" or Repeat == "y":

    EasyLB = open("leaderboard_easy", "r").read().splitlines()
    MediumLB = open("leaderboard_medium", "r").read().splitlines()
    HardLB = open("leaderboard_hard", "r").read().splitlines()
    ImpossibleLB = open("leaderboard_impossible", "r").read().splitlines()

    Leaderboard = []
    Guessed = False
    Lost = False
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
            for Highscore in EasyLB:
                Leaderboard.append(Highscore)
        elif Difficulty == "medium":
            Guesses = 7
            for Highscore in MediumLB:
                Leaderboard.append(Highscore)
        elif Difficulty == "hard":
            Guesses = 5
            for Highscore in HardLB:
                Leaderboard.append(Highscore)
        elif Difficulty == "impossible":
            Guesses = 1
            for Highscore in ImpossibleLB:
                Leaderboard.append(Highscore)
        else:
            print("That is not a valid difficulty.")

    print("Selecting a number between 1 and 100!")
    Number = random.randint(1, 1)

    while Guessed == False and Lost == False:
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
            Guessed = True

        if Guessed != True and NoGuesses == Guesses:
            print(f"You lost. The number was {Number}.")
            Lost = True

    if Guessed == True and Difficulty != ImpossibleLB:
        for Items in Leaderboard:
            User = Items.split(",")[0]
            Score = Items.split(",")[1]
            if User == Name:
                if NoGuesses < int(Score):
                    Leaderboard[Name] = NoGuesses

    print(Leaderboard)

    print(" ")
    Repeat = input("Would you like to play again? (Yes/No) ").lower()