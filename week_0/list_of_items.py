#this contains the list of items that are available in the store along with prices
inventory = [
    {"item": "Notebook", "price": 4.50},
    {"item": "Gel Pen", "price": 1.25},
    {"item": "Backpack", "price": 29.99},
    {"item": "Water Bottle", "price": 12.00},
    {"item": "Calculator", "price": 15.00},
    {"item": "Lunch Box", "price": 8.75},
    {"item": "Headphones", "price": 49.99},
    {"item": "Desk Lamp", "price": 22.50},
    {"item": "Sticky Notes", "price": 3.00},
    {"item": "USB Drive", "price": 10.00}
]
def get_items_prices(item_name):
    for item_info in inventory:
        if item_info["item"].lower() == item_name.lower():
            return item_info["price"]
    return None  # Return None if the item is not found

