Repeat = "yes"

print("Welcome to the book title length calculator!")

while Repeat == "yes" or Repeat == "y":

    print(" ")

    NoOfLetters = 0
    Title = input("What is the name of the book? ").title()

    for letter in Title:
        if letter != " ": #I was intending on using .isalpha(), but that didn't work.
            NoOfLetters = NoOfLetters + 1

    print(f'The book {Title} has {NoOfLetters} letters in its title, {len(Title)} with spaces.')
    print(" ")
    Repeat = input("Would you like to find the length of another book title? (Yes/No) ").lower()
print("Ok then, goodbye!")