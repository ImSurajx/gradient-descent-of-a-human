# ternary-operator: python let you write a simple if-else in singgle line. this is called the ternary operator. it is useful when you want to assign a vaue based on a condition.

# normal-way
age = 19
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(status)

# sorthand way (same result, one line)
status ="Adult" if age >= 18 else "Minor"
print(status)
