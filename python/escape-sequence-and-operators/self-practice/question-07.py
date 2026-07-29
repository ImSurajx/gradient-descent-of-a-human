"""
## Problem 7 - Rectangle Calculator

Take

- Length
- Breadth

Print

- Area
- Perimeter
"""
length = int(input("enter length of rectangle: "))
breadth = int(input("enter breadth of rectangle: "))
print(f"area of rectangle is: {length * breadth}")
print(f"perimeter of rectangle is: {2*(length + breadth)}")