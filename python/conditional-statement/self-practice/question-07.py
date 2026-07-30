"""
## Problem 7 - Adult or Minor

Take age as input.

Print

```
Adult
```

or

```
Minor
```

"""
age = int(input("enter user age: "))
if age > 18 :
    print("adult")
else:
    print("minor")