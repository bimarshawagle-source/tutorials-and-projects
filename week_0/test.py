cart = [
    {"item": "Notebook", "price": 4.50},
    {"item": "Gel Pen", "price": 1.25},
    {"item": "Backpack", "price": 29.99},
    {"item": "Water Bottle", "price": 12.00}
]

total_price = 0

print("--- Your Shopping Cart ---")

# The for loop iterates through each dictionary in the cart list
for item_info in cart:
    print(f"- {item_info['item']}: ${item_info['price']:.2f}")
    total_price += item_info['price']  # Accumulate the price

print("-" * 26)
print(f"Subtotal: ${total_price:.2f}")

# Apply a 10% discount if the total is over $30
if total_price > 30:
    discount = total_price * 0.10
    total_price -= discount
    print(f"Discount Applied (10%): -${discount:.2f}")

print(f"Final Total: ${total_price:.2f}")