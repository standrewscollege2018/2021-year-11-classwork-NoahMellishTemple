fizz = int(input("What number do you want fizz to be?"))
buzz = int(input("What number do you want buzz to be?"))

for num in range(1,20):
    if num % fizz ==0 and num % buzz ==0:
        print("Fizz Buzz")
    elif num % buzz ==0:
        print("Buzz")
    elif num % fizz ==0:
        print("Fizz")
    else:
        print(num)




print("All done")