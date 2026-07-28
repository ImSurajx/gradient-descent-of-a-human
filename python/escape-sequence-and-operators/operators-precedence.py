"""
when multiple operators are in one expression, python follows a specific order - just like bodmas in math

order (higher to lowest)
    () -> brackets
    ** -> exponention
    *,/,//,% -> multiplication & division
    +,- -> addition & subtraction
"""

# without knowing precedence, this loooks confusing
print(2 + 3 * 4)  # 14 not 20, multiplication first
print(10 - 2**3)  # 2, not 512
print(10 // 2 + 3)  # 8, not 1

# user parenthese to force the order you want
print((2 + 3) * 4)  # 20
print((10 - 2) ** 3)  # 512
