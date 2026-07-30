"""

## Problem 16 - Even or Odd

Using only the ternary operator, print

```
Even
```

or

```
Odd
```

"""
num = int(input("enter a number: "))

print("even") if num % 2 == 0 else print("odd")