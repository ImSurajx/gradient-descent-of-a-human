# question14: a shop gives discounts based on purchase amount
# above 5000 -> 20% discount
# above 2000 -> 10% discount
# above 1000 -> 5% discount
# 1000 or below -> no discount

amount = int(input("enter the billing amount: "))

if amount >= 5000:
    discounted_amount = amount - amount * 20 / 100
    print(f"you only have to pay: {discounted_amount}")
elif amount >= 2000:
    discounted_amount = amount - amount * 10 / 100
    print(f"you only have to pay: {discounted_amount}")
elif amount >= 1000:
    discounted_amount = amount - amount * 5 / 100
    print(f"you only have to pay: {discounted_amount}")
elif amount < 1000 and amount >= 0:
    print(f"sorry! no discount.")
else:
    print("invalid amount enter.")

