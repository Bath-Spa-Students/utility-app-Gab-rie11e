# List of items.
items = {
    'K1': {'name': 'Cheetos', 'price': 10.99, 'category': 'snack'},
    'K2': {'name': 'Snickers', 'price': 4.75, 'category': 'snack'},
    'K3': {'name': 'Lays', 'price': 12.00, 'category': 'snack'},
    'K4': {'name': 'KiKat', 'price': 4.99, 'category': 'snack'},
    'K5': {'name': 'Piatos', 'price': 9.50, 'category': 'snack'},
    'J1': {'name': 'Cola', 'price': 5.50, 'category': 'drink'},
    'J2': {'name': 'Pepsi', 'price': 4.00, 'category': 'drink'},
    'J3': {'name': 'Mountain Dew', 'price': 4.99, 'category': 'drink'},
    'J4': {'name': 'Orange Juice', 'price': 3.00, 'category': 'drink'},
    'J5': {'name': 'Sprite', 'price': 3.50, 'category': 'drink'},
}

# Welcome message.
print("========== Welcome to the vending machine!! ==========")
print("\nHere are our list of items for today:")

# Display selection of items.
print("\nSnacks:")
for code, snack in items.items():
    if snack['category'] == 'snack':
        print(f"\n{code}: {snack['name']} - Price: AED {snack['price']}")

print("\nDrinks:")
for code, drink in items.items():
    if drink['category'] == 'drink':
        print(f"\n{code}: {drink['name']} - Price: AED {drink['price']}")

while True:
    # Selecting user snack.
    pick = input("\nPlease enter the code of the snack you want. (Use capital letter please:D) ")
    if pick in items:
        picked = items[pick]
        print(f"\n{picked['name']}. Good choice! that will be AED {picked['price']}")
        price = picked['price']

        # Managing money and giving change, as well as goodbye message.
        while price > 0:
            try:
                pay = float(input("\nPlease insert money: "))
                if pay >= price:
                    change = pay - price
                    print(f"\nThank you for your purchase! Your change is AED {change:.2f}. Enjoy your {picked['name']} and have a nice day!")
                    break
                else:
                    print("\nInsufficient amount. Please try again.")
            except ValueError:
                print("\nInvalid Payment. Please try again")

    another_purchase = input("\nDo you want to make another purchase? (Enter 'yes' or 'no'): ").lower()
    if another_purchase != 'yes':
        print("\nThank you! come again!")
        break