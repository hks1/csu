
class ItemToPurchase:
    item_name = ""
    item_price = 0.0
    item_quantity = 0

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def __init__(self, item_name = "none", item_price = 0.0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_const(self):
        print(f'${self.item_name} ${self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')



print("Item 1")
item1_name = input("Enter the item name:")
item1_price = float(input("Enter the item price:"))
item1_quantity = int(input("Enter the item quantity:"))
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

print("Item 2")
item2_name = input("Enter the item name:")
item2_price = float(input("Enter the item price:"))
item2_quantity = int(input("Enter the item quantity:"))
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

total = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
print("Total: $", total)

print("TOTAL COST")

print(f"{item1.item_name} {item1.item_quantity} @ {item1.item_price} = {item1.item_price * item1.item_quantity}")

print(f"{item2.item_name} {item2.item_quantity} @ {item2.item_price} = {item2.item_price * item2.item_quantity}")

print(f"Total: ${total}")