keep_asking = True

people = [["Dr Evil", 45], ["Gru", 34], ["Emperor" , 200]]

while keep_asking == True:
    person = []
    name = input("Enter a name")
    age = int(input("Enter a age"))
    if name == "end":
        keep_asking = False
    else keep_asking = True





person.append(name)
person.append(age)
people.append(person)





for i in range(len(people)):
    print("{} is {} years old".format(people[i][0], people[i][1]))



