# Loop Concepts — Practice Problems (for, while, break, continue)

Rule: No solutions given. Run your code, compare with Expected Output yourself.
Each problem tests a *different* angle of the same 4 concepts — don't skip any, they don't repeat.

---

### 1. For-loop — basic iteration + accumulator
Given a list of numbers, print their sum.

```
Input: [4, 8, 15, 16, 23, 42]
Expected Output: 108
```

---

### 2. For-loop — range() with a step
Print all numbers from 50 down to 0, decreasing by 5 each time.

```
Expected Output: 50 45 40 35 30 25 20 15 10 5 0
```

---

### 3. For-loop — nested (pattern printing)
Print this pattern using nested for-loops (no hardcoded strings):

```
Expected Output:
*
* *
* * *
* * * *
* * * * *
```

---

### 4. While-loop — condition-controlled accumulator
Using a **while loop** (not for), find the smallest power of 2 that is greater than 10,000.

```
Expected Output: 16384
```

---

### 5. While-loop — sentinel-controlled input
Write a while loop that keeps adding numbers to a running total until it reads the number `-1` (the "stop" signal). Print the total when it stops. Don't count `-1` itself.

```
Input sequence fed one by one: 5, 10, 20, -1
Expected Output: 35
```

---

### 6. break — early exit on first match
Given a list of numbers, find and print the **first number divisible by 7**. If none exists, print `"Not found"`. Use `break` — don't just let the loop run to the end.

```
Input: [12, 18, 21, 30, 35]
Expected Output: 21
```

---

### 7. continue — selective skipping
Print all numbers from 1 to 30, but skip any number divisible by 3 **or** 5. Use `continue`.

```
Expected Output: 1 2 4 7 8 11 13 14 16 17 19 22 23 26 28 29
```

---

### 8. break + continue together
Loop through numbers 1 to 50. Skip even numbers using `continue`. Stop the entire loop the moment you find an odd number greater than 40 that is also divisible by 3. Print every number you visited (including the one that triggered the stop).

```
Expected Output: 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45
```
(Reasoning check: 45 is odd, >40, divisible by 3 → triggers break AFTER printing it)

---

### 9. The classic gotcha — break only exits the INNER loop
Given a 3x3 nested loop (outer `i` from 1-3, inner `j` from 1-3), break out of the inner loop the moment `i == j`, but let the outer loop keep running. Print every `(i, j)` pair visited.

```
Expected Output:
(1, 1)
(2, 1)
(2, 2)
(3, 1)
(3, 2)
(3, 3)
```

---

### 10. while True + break (menu-loop simulation, no real input())
Simulate a menu loop using `while True`. You're given a fixed list of "commands" instead of live input: `["add", "add", "show", "exit", "add"]`. Process them one at a time — `"add"` increases a counter by 1, `"show"` prints the current counter, `"exit"` breaks the loop immediately (ignore anything after it, even if the list has more commands).

```
Input: ["add", "add", "show", "exit", "add"]
Expected Output: 2
```

---

**Self-check rule:** agar apna output expected se match nahi karta, code ko dobara mat likho — pehle trace karo (pen-paper pe i, j, counter values likh ke) ki galti kahan hai.