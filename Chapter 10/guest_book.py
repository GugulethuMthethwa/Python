# Guest Book program to collect names and save them to a file

# Open the file in append mode to add entries without overwriting existing data
with open("guest_book.txt", "a") as file:
    print("Welcome to the Guest Book!")
    print("Enter 'quit' to exit the program.\n")

    while True:
        # Prompt the user for their name
        name = input("Please enter your name: ")
        
        # Check if the user wants to quit
        if name.lower() == 'quit':
            print("Thank you for using the Guest Book. Goodbye!")
            break
        
        # Write the user's name to the file
        file.write(name + "\n")
        print(f"Hello {name}, you've been added to the guest book!\n")