"""
## Problem 11 - Calculator

Take:

- First Number
- Operator (+, -, *, /)
- Second Number

Perform the operation and print the result.

Example

```
Input

10
+
5

Output

15
```

---
"""


print("enter equation ")
num1 = int(input())
operator = input()
num2 = int(input())

if operator == "+":
    print(f"sum is: {num1 + num2}")
elif operator == "-":
    print(f"difference is: {num1 - num2}")
elif operator == "*":
    print(f"multiplication is: {num1 * num2}")
elif operator == "/":
    print(f"division is: {num1 / num2}")

# match operator:
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         print(num1 / num2)
#     case _:
#         print("invalid operator")  # Default case
