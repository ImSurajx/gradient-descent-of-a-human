# logical operator: used to combine condition togehter.
# and, or, not
chemistry = 45
physics = 34

# print true if pass in both subject
print(chemistry > 33 and physics > 33) # both must be true, if first false second one will not check
# print true if pass in any subject
print(chemistry > 33 or physics > 33) # any one condition is true, if first is true not check for second
# print opptosite of coming response
print(not chemistry < 33 and not physics < 33) 
