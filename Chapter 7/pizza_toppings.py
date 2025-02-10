# Loop to ask for pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    # Check if the user wants to quit
    if topping.lower() == 'quit':
        print("Finished adding toppings to your pizza!")
        break
    
    # Otherwise, print the topping being added
    print(f"Adding {topping} to your pizza.")
