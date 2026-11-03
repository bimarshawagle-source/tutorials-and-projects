customers = ("Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah")
orders = [
    {"name": "Alice", "particulars": {"Notebook": 2, "Gel Pen": 5}},
    {"name": "Bob", "particulars": {"Backpack": 1, "Water Bottle": 1}},
    {"name": "Charlie", "particulars": {"Calculator": 1, "Lunch Box": 2}},
    {"name": "Diana", "particulars": {"Headphones": 1, "Desk Lamp": 1}},
    {"name": "Eve", "particulars": {"Sticky Notes": 3, "USB Drive": 1}},
    {"name": "Frank", "particulars": {"Notebook": 1, "Gel Pen": 2, "Backpack": 1}},
    {"name": "Grace", "particulars": {"Water Bottle": 3, "Calculator": 2, "Lunch Box": 3, "Headphones": 1}},
    {"name": "Hannah", "particulars": {"Lunch Box": 1, "Headphones": 1}}
    ]
def get_order_details(name_placeholder):
    for order in orders:
        if order["name"].lower() == name_placeholder.lower():
            return order["particulars"]
    return "NIR"  # Return not in records if the name is not found