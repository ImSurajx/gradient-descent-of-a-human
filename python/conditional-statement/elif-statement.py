# if-elif-else: when you have more than two possible outcomes, use elif(short for "else if"). python checks each condition from top to bottom and runs the first that is true the rest are skipped entirely.

marks = 82

if marks >= 90:
    print("grade: A")
elif marks >= 75:
    print("grade: B")
elif marks >= 60:
    print("grade: C")
elif marks >= 40:
    print("grade: D")
else:
    print("grade: F")
    