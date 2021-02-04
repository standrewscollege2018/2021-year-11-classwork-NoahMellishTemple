
age = int(input("Enter you age"))
weight = int(input("Enter your weight"))
MINIMUM_AGE = 16
MINIMUM_WEIGHT = 50

if age >= MINIMUM_AGE and weight >= MINIMUM_WEIGHT:
    print("You are eligible to donate blood")
    print("You are a hero")
else:
    print("You are not elegible to donate blood")
    print("Thank you for trying though")