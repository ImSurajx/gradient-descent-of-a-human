"""
### 1. For-loop — basic iteration + accumulator
Given a list of numbers, print their sum.

```
Input: [4, 8, 15, 16, 23, 42]
Expected Output: 108
```
"""
input = [4, 8, 15, 16, 23, 42]
sum = 0

for i in range(0, len(input)):
    sum += input[i]

print(f"the sum of list is: {sum}")