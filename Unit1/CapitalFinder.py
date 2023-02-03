Repeat = "yes"

print(" ")
print("Welcome to the capital letter finder!")

while Repeat == "yes" or Repeat == "y":

    NonLetters = 0
    CapitalFound = False

    Phrase = input("What phrase would you like to find the capital letters in? ")

    print(" ")
    print(50 * "=")  #Creates a nice break

    for Index, Character in enumerate(Phrase):  #Checks every letter in the phrase, and their index number
        Index = Index + 1 - NonLetters  #The index will be one behind how a human counts, so 1 is added. Aditionally,
                                        #some characters are ignored and removed from the total
        if Character.isalpha() == False:  #Checks for non-letters
            NonLetters = NonLetters + 1  #Adds to a total that will remove non-letters from the total
        elif Character.isupper() == True:  #Checks for capitals
            print(f"The capital letter {Character} was found as letter number {Index}")  #If the letter is capital, it
                                                                                         #will point out that it is,
                                                                                         #as well as its location in
                                                                                         #the phrase

            CapitalFound = True  #Acknowledges that a capital has been found so an error message isn't used

    if CapitalFound == False:  #If no capitals are found...
        print("No capital letters were found.")  #...print an error message

    print(50 * "=") #Creates a nice break
    print(" ")

    Repeat = input("Would you like to use this program again? (Yes/No) ").lower()

print("Ok then, goodbye!")