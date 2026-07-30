# question-07: take a number. print whether it is positive, negative or zero.
number = int(input("enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is a nor positive/negative number.")

