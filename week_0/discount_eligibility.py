# checks if the buyer is eligible for a discount based on their order details, their name or total bill amount.
friends_and_family = ("Alice", "Bob", "Diana")
def eligible_for_fnf(name):
    if name.lower() in [friend.lower() for friend in friends_and_family]:
        print("Congratulations! You are eligible for a friends and family discount.")
        return 0.10  # 10% discount for friends and family
    
    return 0.0  # No discount for others

def eligible_for_bulk_discount(total_amount):
    if total_amount > 100:
        print("Congratulations! You are eligible for a bulk purchase discount.")
        return 0.05  # 5% discount for bulk purchases
    return 0.0  # No discount for others
