"""
## Problem 12 - Month Number

Take a month number (1-12).

Print the corresponding month name.

Example

```
Input

8

Output

August
```
"""
month_number = int(input("enter month number: "))
if month_number == 1:
    print("Jan")
elif month_number == 2:
    print("Feb")
elif month_number == 3:
    print("Mar")
elif month_number == 4:
    print("Apr")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("Aug")
elif month_number == 9:
    print("Sep")
elif month_number == 10:
    print("Oct")
elif month_number == 11:
    print("Nov")
elif month_number == 12:
    print("Dec")
else:
    print("invalid month number.")