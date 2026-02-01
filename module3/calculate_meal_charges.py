# take food charges as input
food_charges = float(input("Enter food charges:"))
# salestax and tip rate
sales_tax_rate = 7
tip_rate = 18

# calculate sales tax and tip
sales_tax = food_charges * sales_tax_rate / 100
tip = food_charges * tip_rate / 100
total = food_charges + sales_tax + tip

# print food charges, sales tax, tip, and total
print('food charges: {:.2f}'.format(food_charges))
print('sales tax: {:.2f}'.format(sales_tax))
print('tip: {:.2f}'.format(tip))
print('total: {:.2f}'.format(total))



