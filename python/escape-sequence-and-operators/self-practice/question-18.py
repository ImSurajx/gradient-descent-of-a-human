"""
## Problem 18 - Pass Eligibility

Take the marks of a student in **Maths** and **Science** as input.

A student is considered **eligible to pass** only if they score **40 or more marks in both subjects**.

Print the result of the eligibility check.

### Example 1

**Input**

```
Maths Marks   : 75
Science Marks : 82
```

**Output**

```
Eligible to Pass : True
```

### Example 2

**Input**

```
Maths Marks   : 75
Science Marks : 35
```

**Output**

```
Eligible to Pass : False
```

**Hint:** Use the `>=` comparison operator along with the `and` logical operator.
"""
maths = int(input("enter marks of maths: "))
science = int(input("enter marks of science: "))
print(f"eligible to pass: {maths >= 40 and science >= 40}")
