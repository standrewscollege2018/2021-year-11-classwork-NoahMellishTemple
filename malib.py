#This is a Madlib, getting the user to enter the details
#Then it prints the story

#Gets their details
subject = input("What subject are you doing")
name = input("what is your name?")
sickness = input("what is your illness?")
body = input("what part of you body is sore?")
days = input("how many days will you be away for?")
year = input("what year are you?")
parent = input("what parent is writing this letter")

print("To whom this may concern,")
print("Please excuse" , name , "from" , year , subject , "today")
print("The muppet hurt his" , body , "playing sport and now has a" , sickness)
print("He will be back in {} days, but untill then , name , will not be able to attend , year , subject")
print("Very amused {}s" parent)

.format(days , parent)