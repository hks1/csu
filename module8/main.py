from item_to_purchase import ItemToPurchase
from online_shopping_cart import ShoppingCart

'''
Step 7:
'''
# Prompt the user for the customer name and today's date
customer_name = input("Enter customer's name:")
today_date = input("Enter today's date:")

# output the customer name and today's date
print(f"Customer name: {customer_name}")
print(f"Today's date: {today_date}")

# create a shopping cart
shopping_cart = ShoppingCart(customer_name, today_date)