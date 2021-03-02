keep_asking = True

while keep_asking == True:
    try:
        first_num = int(input("What is your first number"))
        second_num = int(input("What is your second number"))
        if first_num == second_num:
            print("Enter 2 different numbers")
        else:
            keep_asking = False
    except:
        print("Error enter a intiger")


print("Your 2 numbers are {} and {}. Is this correct?.format(first_num,second_num"))
if first_num > second_num:
    print("{} is larger then {}".format(first_num,second_num))
else:
    print("{} is larger then {}".format(second_num,first_num))

print("{} is the sum of your 2 numbers".format(second_num+first_num))