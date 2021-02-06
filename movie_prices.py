age = int(input("How old are you?"))
student = int(input("If you are a student type 1 if not type 2"))

if age >=14 and student <=1 :
    print("Ticket is $8")
elif age >= 18 and student >= 2:
    print("Ticket is $12")
elif age >= 13 and student >= 2:
    print("Ticket is $9")
elif age >= 5 and student >= 2:
    print("Ticket is $7")
else:
    print("Ticket is free")