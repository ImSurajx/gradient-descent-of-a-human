"""
## Problem 9 - Username Generator

Take

- First Name
- Birth Year

Create a username.

Example

```
Input

First Name : Suraj
Birth Year : 2005

Output

suraj2005
```
"""
first_name = input("enter your first name: ").lower()
birth_year = input("enter your birth year: ")
print(f"your username is: {first_name + birth_year} ")