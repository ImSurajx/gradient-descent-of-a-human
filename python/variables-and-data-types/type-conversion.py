# implicit: python does it automatically
x = 5 # int
y = 2.0 # float
z = x + y # python converts x to float automatically.
print(z) # 7.0
print(type(z)) # float


# explicit: you do it manually
num1 = "100" # only proper integer conversion allowd
num2 = "200"

float = 500.9
print(int(float)) # choose lower values
print(int(num1) + int(num2)) 