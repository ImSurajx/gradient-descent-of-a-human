"""
## Problem 6 - Positive or Negative

Take a number.

Print

```
Positive
```

or

```
Negative
```
"""
num = int(input("enter a number: "))

if num > 0:
    print("positive")
elif num < 0:
    print("negative")