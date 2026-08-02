"""
Loop through numbers 1 to 50. Skip even numbers using `continue`. Stop the entire loop the moment you find an odd number greater than 40 that is also divisible by 3. Print every number you visited (including the one that triggered the stop).

```
Expected Output: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45
```
(Reasoning check: 45 is odd, >40, divisible by 3 → triggers break AFTER printing it)

"""
for i in range(1,50+1):
    if i % 2 == 0:
        continue
    elif i > 40 and i % 3 == 0:
        print(i,end=" ")
        break
    else:
        print(i,end=" ")