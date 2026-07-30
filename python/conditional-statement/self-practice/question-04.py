"""
## Problem 4 - Divisible by 5

Take a number.

If it is divisible by 5, print:

```
Divisible by 5
```
"""
num = int(input("enter a number: "))
if num % 5 == 0:
    print("divisible by 5.")
else:
    print("not divisible by 5.")