"""
## Problem 10 - Compare Two Numbers

Take two numbers.

Print the result of

```
>
<
>=
<=
==
!=
```
"""
num_one = int(input("enter first number: "))
num_two = int(input("enter second number: "))

print(f"""
>       : {num_one > num_two}
<       : {num_one < num_two}
>=      : {num_one >= num_two}
<=      : {num_one <= num_two}
==      : {num_one == num_two}
!=      : {num_one != num_two}
""")    