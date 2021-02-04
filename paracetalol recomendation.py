age = int(input("What is your age?"))


if age <= 11:
    weight = int(input("what is you weight?"))
    print("Recomended dose is", weight * 10, "mg paracetamol")
else:
    print("Recomended dose is 2x 500mg")