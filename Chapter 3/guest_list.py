guests = ["Albert Einstein", "Marie Curie", "Leonardo da Vinci"]

# Print an invitation message for each guest
print(f"Dear {guests[0]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[1]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[2]}, I would be honored to invite you to dinner.")

# The guest who can't make it
unable_to_attend = guests[1]
print(f"\nUnfortunately, {unable_to_attend} can't make it to dinner.")

# Replacing the guest who can't attend with a new guest
guests[1] = "Nikola Tesla"

# New invitations
print(f"\nUpdated invitations:")
print(f"Dear {guests[0]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[1]}, I would be honored to invite you to dinner.")
print(f"Dear {guests[2]}, I would be honored to invite you to dinner.")