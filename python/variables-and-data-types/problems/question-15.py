"""
## Problem 15 - Student Report Card

Take input

- Name
- Maths Marks
- Science Marks
- English Marks

Print

```
Name      : Suraj
Total     : 270
Average   : 90
```
"""
student_name = input("enter name of student: ")
maths_marks = int(input("enter marks of maths: "))
science_marks = int(input("enter marks of science: "))
english_marks = int(input("enter marks of english: "))
print(f"Name       : {student_name}\nTotal      : {maths_marks + science_marks + english_marks }\nAverage    : {int((maths_marks + science_marks + english_marks)/3)}")