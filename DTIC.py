#This program calulates grades
#Set up cut scores
mark = int(input("what mark did you get"))
if mark >= 0 and mark <= 100:
    if mark >= 90:
        print("Congrates you got A")
    elif mark >= 70:
        print("Congrates you got B")
    elif mark >= 50:
        print("Congrates you got C")
    else:
        print("Unlucky you failed")
else:
    print("Invalid mark")