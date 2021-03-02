import random
high_score = 1000
keep_playing = True
check_number = True
while keep_playing == True:
    number = random.randint(1,100)
    keep_asking = True
    counter = 0

    while keep_asking == True:
        counter += 1
    while check_number = True:
        try:
            guess = int(input("Guess a number:"))
            check_number = False
        except:
            print("Please enter a integer")
        guess = int(input("Guess a number between 1-100"))
        if guess == number:
            keep_asking = False
        else:
            print("Wrong number")
            if guess > number:
                print("Too high")
            elif guess < number:
                print("Too low")
    if counter <= high_score:
        print("Congrates you got a high score")
        high_score = counter
    print("Thats right")
    print("You took {} guesses".format(counter))
    print("The current best score is {}".format(high_score))
    y_n = input("Do you want to play again y/n")
    if y_n == "y":
        keep_playing = True
    else:
        keep_playing = False