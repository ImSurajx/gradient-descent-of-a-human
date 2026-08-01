# question-19: ask a number from user, and print all the factors.
num = int(input("enter a number: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1