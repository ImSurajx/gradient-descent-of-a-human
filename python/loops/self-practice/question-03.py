"""
### 3. For-loop — nested (pattern printing)
Print this pattern using nested for-loops (no hardcoded strings):

```
Expected Output:
*
* *
* * *
* * * *
* * * * *
```
"""
for i in range(0,6,1):
    for j in range(0,i,1):
        print("*", end=" ")
    print("\n", end="")