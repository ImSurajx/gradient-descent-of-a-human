"""
Take the user's age.

If the age is 18 or above, print:

```
Eligible to Vote
```
"""
age = int(input("enter user age: "))
if age > 18 :
    print("adult")
else:
    print("minor")