# Intentional Error: Create an index error by accessing an invalid index in the list.

guests = ["Isaac Newton", "Albert Einstein", "Ada Lovelace", "Marie Curie", "Nikola Tesla"]

# Attempting to access an invalid index (index 5) which is out of range, will raise an IndexError
print(guests[5])  # This will cause an IndexError

# Correcting the error by accessing a valid index (index 4)
print(guests[4])  # This will work correctly, printing the last element in the list