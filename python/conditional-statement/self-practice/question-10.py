"""
## Problem 10 - Largest of Three Numbers

Take three numbers.

Print the largest number.

"""
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter thrid number: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is greatest.")
    else:
        print(f"{num3} is greatest.")
else:
    if num2 > num3:
        print(f"{num2} is greatest.")
    else:  
        print(f"{num3} is greatest.")
