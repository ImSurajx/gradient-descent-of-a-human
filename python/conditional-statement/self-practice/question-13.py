"""
# Part 4 - Nested if-else

## Problem 13 - Exam Result

Take:

- Theory Marks
- Practical Marks

A student passes only if both marks are at least 40.

If both are passed, then check:

- Total marks are 80 or more → Print

```
Pass with Distinction
```

Otherwise print

```
Pass
```

If either subject is below 40, print

```
Fail
```

---
"""
theory_marks = int(input("enter theory marks: "))
practical_marks = int(input("enter practical marks: "))

if theory_marks >= 40 :
    if practical_marks >= 40:
        print("pass")
    else:
        print("fail")
else:
    print("fail")