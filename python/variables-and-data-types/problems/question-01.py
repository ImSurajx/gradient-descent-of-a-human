"""
Problem 1 - Personal Introduction

Take the following inputs from the user:

- Name
- Age
- City

Print the output like this:

```
Hello Suraj!
You are 20 years old.
You live in Delhi.
```
"""
name = input("enter your name: ")
age = int(input("enter your age: "))
city = input("enter your city: ")

print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"You live in {city}.")