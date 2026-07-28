"""
## Problem 18 - Profile Card

Take

- Name
- Age
- Height
- Weight

Print a beautiful profile card.

Example

```
=========================
        PROFILE
=========================

Name   : Suraj
Age    : 20
Height : 170 cm
Weight : 65 kg

=========================
```
"""
name = input("enter name: ")
age = int(input("enter age: "))
height = int(input("enter height: "))
weight = int(input("enter weight: "))

print(f"=========================\n        PROFILE\n\nName   : {name}\nAge    : {age}\nHeight : {height} cm\nWeight : {weight} kg\n\n=========================")