keep_asking = True

while keep_asking == True:
    name = input("Enter your name")
    if name == "Noah" or name == "noah":
        keep_asking = False
    else:
        print("Wrong name")
print("Hi Noah")