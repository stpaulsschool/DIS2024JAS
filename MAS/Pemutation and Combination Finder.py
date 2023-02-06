inputtotal = 0

print("Welcome to the Permutation and Combination calculator!")
inputs = input("What characters would you like to find the total permutations and combinations for? ")
selections = input("How many selections would you like to make? ")

for character in input:
    if character != " " and character != ",":
        inputtotal = inputtotal + 1

if selections < inputtotal:
    print(f"There are not enough characters to make {selections} selections")

if inputtotal < 1 or inputtotal.is_integer() == False or selections < 1 or selections.is_integer() == False:
   print("Please only insert Natural Numbers")
else:
