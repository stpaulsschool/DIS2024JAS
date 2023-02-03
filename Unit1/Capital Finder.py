Repeat = "yes"

print(" ")
print("Welcome to the capital letter finder!")

while Repeat == "yes" or Repeat == "y":

    NonLetters = 0
    CapitalFound = False

    Phrase = input("What phrase would you like to find the capital letters in? ")

    print(" ")
    print(50 * "=")

    for Index, Character in enumerate(Phrase):
        Index = Index + 1 - NonLetters
        if Character.isalpha() == False:
            NonLetters = NonLetters + 1
        elif Character.isupper() == True:
            print(f"The capital letter {Character} was found as letter number {Index}")
            CapitalFound = True

    if CapitalFound == False:
        print("No capital letters were found.")

    print(50 * "=")
    print(" ")

    Repeat = input("Would you like to use this program again? (Yes/No) ").lower()
print("Ok then, goodbye!")