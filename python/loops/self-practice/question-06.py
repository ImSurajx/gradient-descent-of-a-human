"""
### 6. break — early exit on first match
Given a list of numbers, find and print the **first number divisible by 7**. If none exists, print `"Not found"`. Use `break` — don't just let the loop run to the end.

```
Input: [12, 18, 21, 30, 35]
Expected Output: 21
```
"""
list = [12, 18, 21, 30, 35]

for i in range(0,len(list)):
    if list[i] % 7 == 0:
        print(f"the first number, which is divisible by 7 is: {list[i]}")
        break
    