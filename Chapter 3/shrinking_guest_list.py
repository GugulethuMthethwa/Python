guests = ["Isaac Newton", "Albert Einstein", "Ada Lovelace", "Marie Curie", "Nikola Tesla"]

# Informing about the smaller guest list
print("Unfortunately, the new dinner table won’t arrive in time, so I can only invite two guests.")

# Remove guests using pop() and notify them
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Let the remaining two guests know they’re still invited
print(f"\n{guests[0]}, you’re still invited to dinner.")
print(f"{guests[1]}, you’re still invited to dinner.")

# Use del to remove the last two guests and make the list empty
del guests[0]
del guests[0]

# Print the empty list
print("\nAfter removing the guests, the guest list is now:", guests)