"""

## Problem 20 - Admission Eligibility

Take:

- Maths Marks
- Science Marks
- English Marks

Rules:

- Every subject must have at least 40 marks.
- Average must be at least 60.

Print

```
Admission Granted
```

Otherwise

```
Admission Denied
```

---
"""
math_marks = int(input("enter math marks: "))
science_marks = int(input("enter science marks: "))
english_marks = int(input("enter english marks: "))

if math_marks >= 40 and science_marks >= 40 and english_marks >= 40:
    if (math_marks + science_marks + english_marks)/3 >= 60:
        print("Admission Granted")
    else:
        print("Admission Denied")
else:
    print("Not! Eligible for Admission.")
    