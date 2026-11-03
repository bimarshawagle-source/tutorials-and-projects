from list_of_items import get_items_prices
from buyers_list import get_order_details
from discount_eligibility import eligible_for_fnf, eligible_for_bulk_discount

name = input("Enter your name: ")
order_details = get_order_details(name)
if order_details == "NIR":
    print("Name not in records.")
else:
    total_amount = 0
    print(f"Order details for {name}:")
    for item, quantity in order_details.items():
        price = get_items_prices(item)
        if price is not None:
            item_total = price * quantity
            total_amount += item_total
            print(f"{item}: {quantity} x ${price:.2f} = ${item_total:.2f}")
    fnf_discount = eligible_for_fnf(name)
    final_amount = total_amount * (1 - fnf_discount)  # Apply friends and family discount if applicable
    bulk_discount = eligible_for_bulk_discount(final_amount)
    final_amount *= (1 - bulk_discount)  # Apply bulk discount if applicable
    discount_amount = total_amount - final_amount

    print(f"Total amount: ${total_amount:.2f}")
    print(f"Total discount: ${discount_amount:.2f}")
    print(f"Final amount to pay: ${final_amount:.2f}")