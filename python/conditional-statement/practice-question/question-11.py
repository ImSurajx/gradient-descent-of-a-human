# question-11: take a person's age and whether they have a valid ID (true/false) as input. they can enter a venue only if they are 18 or older and have a valid id. print the appropriate message.

age = int(input("enter your age: "))
validID = True

if age >= 18 and validID:
    print("you are eligible to enter in the venue.")
elif age >= 18 and not validID:
    print("you have a valid age but not valid id card so your are not eligible.")
else:
    print("you are not eligible.")