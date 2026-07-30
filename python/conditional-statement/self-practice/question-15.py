"""
## Problem 15 - Scholarship Eligibility

Take:

- Percentage
- Annual Family Income

Rules:

- Percentage must be at least 75.
- If eligible, then check income.
- Income less than ₹500000

Print

```
Scholarship Approved
```

Otherwise

```
Scholarship Not Approved
```

---
"""
percentage = int(input("enter your percentage: "))
gross_income = int(input("enter your famliy income: "))

if percentage >= 75 and percentage <= 100:
    if gross_income < 500000:
        print("scholarship approved.")
    else:
        print("scholarship not approved.")
else:
    print("not eligible for scholarship.")