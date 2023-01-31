while True:
    NoOfLetters = 0
    Title = input("What is the name of the book? ")
#print("The book " + Title + " has " + str(len(Title)) + " characters in its title.")

#Ok then, but actually...
    for letter in Title:
        if letter != " ":
            NoOfLetters = NoOfLetters + 1
    print('The book "' + Title + '" has ' + str(NoOfLetters) + " characters in its title.")