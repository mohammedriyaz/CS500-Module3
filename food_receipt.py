
def place_purchase_order(order_list):
    """
    The function will keep prompting the user to enter the items until the user
    enters 'done'. The function returns the updated order list.
    This function takes prior order list as an argument and returns the updated order list.
    """    
    done_ordering = False
    while not done_ordering:
        item = input("Please enter the food item you would like to order. (Enter 'done' to finish ordering): ")
        if item.lower() == "done":
            done_ordering = True            
        else:
            item = item.capitalize()
            if (item not in order_list):
                price = float(input("Enter the price of the {}: ".format(item)))
                quantity = int(input("Enter the quantity of the {}: ".format(item)))
                order_list.append({
                    "food": item,
                    "price": price,
                    "quantity": quantity
                })
    return order_list

def print_receipt(order_list):
    """
    The function will print the receipt of the order. It will calculate the total
    cost of the order including the gratuity and tax.
    """
    print("-" * 50)
    print("Thank you for your order! Here is your receipt:".center(50))
    item_template = "{quantity} {food} @ ${price:.2f} = ${sub_total:.2f}"
    total = 0
    
    for i in range(len(order_list)):
        # unpack the dictionary into the format method to print the item
        sub_total = order_list[i]["price"] * order_list[i]["quantity"]
        print(item_template.format(**order_list[i], sub_total=sub_total).rjust(50))
        total += sub_total
    gratuity = total * 0.15
    tax = total * 0.07
    total += gratuity + tax
    print("Gratuity: ${:.2f}".format(gratuity).rjust(50))
    print("Tax: ${:.2f}".format(tax).rjust(50))
    print(("-" * 15).rjust(50))
    print("Total: ${:.2f}".format(total).rjust(50))
    print("-" * 50)
   
# Main program
print("Welcome to the food ordering system!")
# get all the items details in the order
order_items = place_purchase_order([])

finished_order = False
# Provides the option to update the order or finish the order
while not finished_order:
    finished_order = input("Would you like to place another order? (yes/no): ").lower() == "no"
    if not finished_order:
        order_items = place_purchase_order(order_items)

if len(order_items) > 0:
    print_receipt(order_items)
else:
    # if there are no items in the order, print the message
    print("No items in the order. See you next!")
