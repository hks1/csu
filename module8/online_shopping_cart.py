from turtle import width
from item_to_purchase import ItemToPurchase

'''
shopping cart class
'''
class ShoppingCart:
    # parameterized constructor - customer name and date as parameters
    def __init__(self, customer_name, date):
        self.customer_name = customer_name
        self.current_date = date

    # customer name
    customer_name = 'none'
    # current date
    current_date = 'January 1, 2020'
    # initialize cart items
    cart_items = []

    '''
    Step 8:
    '''
    # Add items of type ItemToPurchase
    def add_items(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    '''
    Step 9:
    '''
    # remove item by item name
    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                print(f'removed item: {item.item_name}')
                item_found = True
        
        if not item_found:
            print('Item not found in cart. Nothing removed.')

    # modify item (quantity)
    def modify_item(self, item_to_modify):
        is_modified = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_to_modify.item_name:
                self.cart_items[i].item_quantity = item_to_modify.item_quantity
                is_modified = True
        if not is_modified:
            print('Item not found in cart. Nothing modified.')

    # get number of items in the cart
    def get_num_items_in_cart(self):
        # calculate total number of items in the cart
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        # return total number of items in the cart    
        return total_quantity

    # get cost of cart
    def get_cost_of_cart(self):
        total_cart_cost = 0
        for item in self.cart_items:
            total_cart_cost += item.item_price * item.item_quantity
        return total_cart_cost

    # total - output total of objects in the cart
    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            width = 60
            # output total of the objects in the cart
            print(f'OUTPUT SHOPPING CART'.center(width))
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(width))
            print(f'Number of Items: {self.get_num_items_in_cart()}'.center(width))
            for item in self.cart_items:
                print(f'{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}'.center(width))
            print(f'Total: ${self.get_cost_of_cart()}'.center(width))

    # print descriptions
    def print_descriptions(self):
        width = 60
        # outputs each item's description
        print(f"OUTPUT ITEMS' DESCRIPTIONS".center(width))
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}".center(width))
        print(f'Item Descriptions'.center(width))
        # print Item Descriptions
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}'.center(width))
        

def print_menu(online_shopping_cart):
    while True:
        # print menu
        user_input = input('''MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    Choose an option:''')
        if user_input == 'q':
            break
        if user_input == 'a':
            # Add item to the cart
            print('ADD ITEM TO CART')
            # input item details to add
            name = input("Enter the item name:")
            price = float(input("Enter the item price:"))
            quantity = int(input("Enter the item quantity:"))
            descr = input("Enter item descripiton:")
            item = ItemToPurchase(name, price, quantity, descr)
            cart.add_items(item)
        elif user_input == 'r':
            # Remove item from the cart
            print('REMOVE ITEM FROM CART')
            # input item name to remove
            name = input("Enter item name to remove:")
            cart.remove_item(name)
        elif user_input == 'c':
            print('CHANGE ITEM QUANTITY')
            # change item's quantity
            name = input("Enter item name to change quantity:")
            quantity = int(input("Input item qunatity:"))
            item = ItemToPurchase(item_name=name, item_quantity=quantity)
            cart.modify_item(item)
        elif user_input == 'i':
            # output items' descripitons
            cart.print_descriptions()
        elif user_input == 'o':
            # output shopping cart
            cart.print_total()
        else:
            print('Invalid choice.')
        input('Input any key to continue:')

if __name__ == '__main__':

    # create cart
    cart = ShoppingCart('John Doe', 'February 1, 2020')
    # create items
    nikes = ItemToPurchase('Nike Romaleos', 189.0, 2, 'Volt color, Weightlifting shoes')
    choco_chips = ItemToPurchase('Chocolate Chips', 3, 5, 'Semi-sweet')
    headphones = ItemToPurchase('Powerbeats 2 Headphones', 128, 1, 'Bluetooth headphones')
    # add items to cart
    cart.add_items(nikes)
    cart.add_items(choco_chips)
    cart.add_items(headphones)

    # print menu option to manipulate/display cart and item descriptions
    print_menu(cart)







