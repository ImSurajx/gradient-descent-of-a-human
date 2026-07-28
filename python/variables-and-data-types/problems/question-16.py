"""
Take input

- Customer Name
- Item Name
- Quantity
- Price per Item

Print

```
------------------------
SHOP RECEIPT
------------------------

Customer : Suraj
Item     : Apple
Quantity : 5
Price    : ₹20

Total    : ₹100

------------------------
"""
customer_name = input("enter customer name: ")
item_name = input("enter item name: ")
quantity = int(input("enter quantity: "))
price_per_item = int(input("enter price per item: "))
print(f"------------------------\nSHOP RECEIPT\n------------------------\n\nCustomer : {customer_name}\nItem     : {item_name}\nQuantity : {quantity}\nPrice    : ₹{price_per_item}\n\nTotal    : ₹{quantity * price_per_item}\n\n------------------------")