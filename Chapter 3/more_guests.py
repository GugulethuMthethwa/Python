guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# Initial invitation messages
print(f"Dear {guests[0]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[1]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[2]}, I would be honored to invite you to dinner.")

# Informing about the bigger dinner table
print("\nGood news! I found a bigger dinner table, and there’s more space available!")

# Adding new guests to the list
guests.insert(0, "Isaac Newton")  # Adding a guest at the beginning
guests.insert(2, "Ada Lovelace")  # Adding a guest in the middle
guests.append("Nikola Tesla")     # Adding a guest at the end

# New invitations
print("\nUpdated invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to invite you to dinner.")