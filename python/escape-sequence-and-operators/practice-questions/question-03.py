"""
question-03: take a users age as input. check and print whether they are eligible to vote (age >= 18) and whether they are a senior citizen (age >= 60)
"""

age = int(input("enter your age: "))
if age >= 60:
    print("eligible to vote and senior citizen.")
elif age <= 60 and age >= 18:
    print("eligible to vote but not a senior citizen.˝")
