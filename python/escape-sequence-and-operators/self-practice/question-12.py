"""
## Problem 12 - Marks Comparison

Take marks of two students.

Print

```
Did Student A score more than Student B?

True / False
"""
student_a = int(input("enter marks of first student: "))
student_b = int(input("enter mars of second student: "))

print(f"student a score more than student b? {student_a > student_b}")
print(f"student b score more than student a? {student_a < student_b}")