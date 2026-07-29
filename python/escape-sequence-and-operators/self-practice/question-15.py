"""
## Problem 15 - Number Range

Take a number.

Print

```
Is the number between 10 and 100?

True / False
```

"""
num = int(input("enter a number: "))

print(f"Is the number between 10 and 100? {num > 10 and num < 100}")