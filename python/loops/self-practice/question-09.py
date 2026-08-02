"""
### 9. The classic gotcha — break only exits the INNER loop
Given a 3x3 nested loop (outer `i` from 1-3, inner `j` from 1-3), break out of the inner loop the moment 
`i == j`, but let the outer loop keep running. Print every `(i, j)` pair visited.

```
Expected Output:
(1, 1)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
(3, 3)
```
"""
for i in range(1,3+1):
    for j in range(1,3+1):
        print(f"({i},{j})")
        if i == j:
            break