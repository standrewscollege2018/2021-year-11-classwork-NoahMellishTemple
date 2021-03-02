keep_asking = True
while keep_asking == True:
    try:
        number = int(input("Enter integer"))
        print("You choose" , number)
        keep_asking = False
    except:
        print("Thats not an integar")
print("**** All Done ****")