start_number = int(input("What number do you want your lowest number to be?"))
stop_number = int(input("What number do you want your highest number to be?"))
step = int(input("What do you want the numbers to count up in?"))
for num in range(start_number,stop_number,step):
    print(num)