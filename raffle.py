import random

keep_asking = True
names = []
print("Welcome to my raffle in which the winner will be choosen randomly")
prize = input("What is the prize for this raffle")
value = int(input("How much is {} worth in NZ dollars".format(prize)))

while keep_asking == True:
        name = input("Enter a name")

        if name.lower() == "end":
            keep_asking = False
        else:
            names.append(name)
print(names)
print("The prize is {} and is worth {} dollars".format(prize, value))
winner = random.randint(0,len(names)-1)

print(len(names))

print("The winner is")
print(names[winner])