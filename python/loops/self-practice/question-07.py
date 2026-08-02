"""
### 7. continue — selective skipping
Print all numbers from 1 to 30, but skip any number divisible by 3 **or** 5. Use `continue`.

```
Expected Output: 1 2 4 7 8 11 13 14 16 17 19 22 23 26 28 29
```
"""
for i in range(1,30+1):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i, end=" ")