"""
## Problem 5 - Calculator

Take two numbers from the user.

Print

- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Modulus
- Exponent

Example

```
Addition        : 30
Subtraction     : 10
Multiplication  : 200
Division        : 2.0
Floor Division  : 2
Modulus         : 0
Power           : 100
```
"""
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
print(f"""
Addition        : {num1 + num2}
Subtraction     : {num1 - num2}
Multiplication  : {num1 * num2}
Division        : {num1 / num2}
Floor Division  : {num1 // num2}
Modulus         : {num1 % num2}
Power           : {num1 ** num2}
""")