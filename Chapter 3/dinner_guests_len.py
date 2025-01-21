# Dinner Guests: Use len() to print a message indicating the number of people you're inviting to dinner.

guests = ["Isaac Newton", "Albert Einstein", "Ada Lovelace", "Marie Curie", "Nikola Tesla"]

# Print the number of guests
print(f"\nThe number of people I am inviting to dinner is: {len(guests)}")

# Initial invitation messages
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner.")