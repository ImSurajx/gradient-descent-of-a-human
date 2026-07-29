"""
question-04: a student marks in 3 subjects. take all three as input, calculate the total and average and print both using f-string.
"""

sub1 = int(input("enter marks of first subject: "))
sub2 = int(input("enter marks of second subject: "))
sub3 = int(input("enter marks of third subject: "))
print(
    f"the total of all subject is {sub1 + sub2 + sub3} and the average is {(sub1 + sub2 + sub3)/3:.2f}."
)
