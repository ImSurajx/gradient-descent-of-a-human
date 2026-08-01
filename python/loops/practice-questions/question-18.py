# question-18: ask a number from the user, print the multiplication table upto 10.
num = int(input("enter a number: "))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1
