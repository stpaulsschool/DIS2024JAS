PhraseLength = 0

print("Welcome to the middle letter finder!")
Phrase = input("What would you like to find the middle letter of? ")

for Character in Phrase:
    if Character.isalpha() == True:
        PhraseLength = PhraseLength + 1

if (PhraseLength/2).is_integer() != True:
    print(f"The middle letter is letter number {int(PhraseLength/2+0.5)}, being {Phrase[int(PhraseLength/2+0.5)]}.")
else:
    print("There is no single middle letter")