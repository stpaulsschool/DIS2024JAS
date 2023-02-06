inputtotal = 0

print("Welcome to the Permutation and Combination calculator!")
inputs = input("What characters would you like to find the total permutations and combinations for? ")
selections = int(input("How many selections would you like to make? "))

for character in inputs:
    if character != " " and character != ",":
        inputtotal = inputtotal + 1

if selections > inputtotal:
    print(f"There are not enough characters to make {selections} selections")

if inputtotal < 1 or selections < 1:
   print("Please only insert Natural Numbers")
else:

    # Work out n!
    NFactorial = 1
    for x in range(1, inputtotal+1):
        NFactorial = NFactorial * x

    # Work out r!
    RFactorial = 1
    for x in range(1, selections+1):
        RFactorial = RFactorial * x

    # Work out (n-r)!
    NMinusRFactorial = 1
    for x in range(1, inputtotal - selections + 1):
        NMinusRFactorial = NMinusRFactorial * x

    print(f"The number of permutations is {int(NFactorial/NMinusRFactorial)}")
    print(f"and the number of combinations is {int(NFactorial/RFactorial*NMinusRFactorial)}")