# Loop to ask for user's age and tell them the ticket price
while True:
    age = int(input("Enter your age (or type 'quit' to exit): "))
    
    # Check the ticket price based on age
    if age < 3:
        print("Your movie ticket is free!")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    elif age > 12:
        print("Your movie ticket costs $15.")
    
    # Option to exit the loop
    continue_prompt = input("Would you like to check another ticket? (yes/no): ")
    if continue_prompt.lower() != 'yes':
        print("Goodbye!")
        break
