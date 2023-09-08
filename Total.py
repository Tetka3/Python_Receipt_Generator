
cart = []  
total_cost = 0.0


product_catalog = {
    'apple': 1.0,
    'banana': 0.5,
    'bread': 2.0,
    'milk': 1.5,
    'cheese': 3.0
}


print("Welcome to the Supermarket!")


while True:
    
    print("\nProduct Catalog:")
    for item, price in product_catalog.items():
        print(f"{item.capitalize()}: ${price:.2f}")

   
    item_choice = input("\nEnter the item you want to purchase (or 'checkout' to finish): ").lower()

    
    if item_choice == 'checkout':
        break

   
    if item_choice in product_catalog:
        
        cart.append(item_choice)
        total_cost += product_catalog[item_choice]
        print(f"{item_choice.capitalize()} added to your cart.")
    else:
        print("Item not found in the catalog. Please choose a valid item.")


print("\nReceipt:")
for item in cart:
    print(f"{item.capitalize()}: ${product_catalog[item]:.2f}")
print(f"Total Cost: ${total_cost:.2f}")


print("\nThank you for shopping with us! Have a great day!")
