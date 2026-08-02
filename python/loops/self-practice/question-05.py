"""
### 5. While-loop — sentinel-controlled input
Write a while loop that keeps adding numbers to a running total until it reads the number 
`-1` (the "stop" signal). Print the total when it stops. Don't count `-1` itself.

```
Input sequence fed one by one: 5, 10, 20, -1
Expected Output: 35
```
"""

sum = 0
while True:
    num = int(input("enter a number: "))
    if num == -1:
        break
    else:
        sum += num
print(f"the sum of inputs are: {sum}")