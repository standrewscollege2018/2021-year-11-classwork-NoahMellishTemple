import random
number = random.randint(1,10)
keep_asking = True
counter = 0
while keep_asking == True:
    counter += 1
    guess = int(input("Guess a number between 1-10"))
    if guess == number:
        keep_asking = False
    else:
        print("Wrong number")
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
print("Thats right")
print("You took {} guesses".format(counter))