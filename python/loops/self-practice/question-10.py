"""
### 10. while True + break (menu-loop simulation, no real input())
Simulate a menu loop using `while True`. You're given a fixed list of "commands" instead of live input: `["add", "add", "show", "exit", "add"]`. Process them one at a time — `"add"` increases a counter by 1, `"show"` prints the current counter, `"exit"` breaks the loop immediately (ignore anything after it, even if the list has more commands).

```
Input: ["add", "add", "show", "exit", "add"]
Expected Output: 2
```
"""
list = ["add", "add", "show", "add","add", "add", "show", "add","show","exit","add"]
counter = 0
i = 0
while True:
    if list[i] == "add":
        counter += 1
    elif list[i] == "show":
        print(f"the counter value is: {counter}")
    elif list[i] == "exit":
        break
    if i == len(list)-1:
        break
    else:
        i += 1
    

