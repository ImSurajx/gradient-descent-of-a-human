"""
Given two variables

```
a = 10
b = 20
```

Swap their values **without using a third variable.**

Output

```
a = 20
b = 10
```
"""
a = 10
b = 20
print(a,b)
a = a + b
b = a - b
a = a - b
print(a,b)
# also we can do this
a , b = b ,a 
print(a,b)