# input number of books purchased
num_books_purchased = int(input("Enter number of books purchased:"))

# calculate points
points = 0
if num_books_purchased == 0:
    points = 0
elif 2 <= num_books_purchased < 4:
    points = 5
elif 4 <= num_books_purchased < 6:
    points = 15
elif 6 <= num_books_purchased < 8   :
    points = 30
else: # number of books purchased >= 8
    points = 60
# print points awarded
print(f"Points awarded: {points}")