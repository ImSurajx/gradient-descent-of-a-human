# break-statement: immediately stops the loop and exits it, even if the condtion is still true or there are items left in sequence.
num = 1
while num <= 10:
    if num == 5:
        break   # stops the loop when num reaches 5.
    print(num)
    num += 1

# output: 1 2 3 4

# break in a for loop
for i in range(1,11):
    if i == 6:
        break
    print(i)

# output: 1 2 3 4 5