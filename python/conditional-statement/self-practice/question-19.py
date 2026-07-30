"""

## Problem 19 - ATM Eligibility

Take:

- Age
- Account Balance

Rules:

- Age must be at least 18.
- Balance must be at least ₹1000.

Print one of the following:

```
Transaction Allowed
```

```
Insufficient Balance
```

```
Age Restriction
```

---
"""
age = int(input("enter your age: "))
account_balance = int(input("enter your account balance: "))

if age >= 18:
    if account_balance > 1000:
        print("transection allowed.")
    else:
        print("insufficient balance.")
else:
    print("age restriction.")