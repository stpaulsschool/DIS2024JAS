Repeat = "yes"  #Needs to be set prior to programs beginning

print("Welcome to the book name fixer!")  #Introduces program

while Repeat == "yes" or Repeat == "y":  #Allows the program to be run repeatedly

    print(" ")
    Name = input("What is the work-in-progress name of your book? ")  #Asking for the book title to be judged

    #Words = 1  #There will always be at least 1 word
    #for Letter in Name:  #Check every character in the word...
    #    if Letter == " ":  #...for if it's a space...
    #        Words = Words + 1  #... and if it is, acknowledge another word

    #alternatively...
    Words = 0  #Start counting at 0
    for Word in Name.split():  #For every words in the title...
        Words = Words + 1  #...acknowledge another word

    print(" ")
    if Words > 2:  #If there are more than 2 words...
        print("That's a long title... May I recommend shortening it to below three words?")  #...recommend less words
    elif Words == 0:  #Otherwise, if there are no words...
        print("Hold on, you didn't even supply a title!")  #...comment on the lack of words
    elif Words <= 2:  #Otherwise, if there are less than, or exactly 2 words...
        print("That's a really good title! You even managed to keep it below three words.")  #...compliment the title

    print(" ")
    Repeat = input("Would you like to try another book title? (Yes/No) ").lower()  #Allow users to do another via while

print("Ok then! Good luck with that book!")  #Program quit note