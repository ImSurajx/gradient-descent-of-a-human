"""
question-06: take two numbers as input. without using *, calculate and print their product using += in a way that adds the first number to itself the second number of it times. think carefully.
"""
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
sum = 0
for i in range(0,num2):
    sum += num1

print(f"the {num2} times {num1} is: {sum}")