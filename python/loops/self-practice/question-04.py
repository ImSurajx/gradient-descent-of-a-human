"""
### 4. While-loop — condition-controlled accumulator
Using a **while loop** (not for), find the smallest power of 2 that is greater than 10,000.

```
Expected Output: 16384
```
"""
num = 1

while num <= 10000:
    num = num * 2

print(f"mallest power of 2 that is greater than 10,000 is {num} ")