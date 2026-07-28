"""
## Problem 17 - Convert Seconds

Take seconds as input.

Convert them into hours.

Example

```
Input

7200

Output

2 hours
```
"""
seconds = int(input("enter seconds: "))
print(f"hours: {int((seconds/60)/60)}")