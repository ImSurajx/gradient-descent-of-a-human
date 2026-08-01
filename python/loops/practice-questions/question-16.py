# question-16: sum of all numbers from 1 to 100
start = int(input("enter start number: "))
end = int(input("enter end number: "))
i = start
sum = 0
while i <= end:
    sum += i
    i += 1
print(f"the sum of all numbers form {start} to {end} is: {sum}")