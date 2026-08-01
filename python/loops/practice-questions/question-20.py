# take numbers as input from the usre one by one. skip negative number and keep adding the positive ones. stop when user enter 0 and print the total. use both continues and break.

sum = 0
while True:
    num = int(input("enter a number: "))
    if num == 0:
        print(f"the sum is: {sum}")
        break
    elif num < 0:
        continue
    else:
        sum += num
