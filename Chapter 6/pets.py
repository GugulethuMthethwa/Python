# Creating dictionaries for different pets
pet_1 = {
    'animal': 'Dog',
    'owner': 'Alice'
}

pet_2 = {
    'animal': 'Cat',
    'owner': 'Bob'
}

pet_3 = {
    'animal': 'Rabbit',
    'owner': 'Charlie'
}

pet_4 = {
    'animal': 'Parrot',
    'owner': 'Diana'
}

# Storing all pet dictionaries in a list called 'pets'
pets = [pet_1, pet_2, pet_3, pet_4]

# Looping through the list of pets and printing information about each pet
for pet in pets:
    print(f"\nInformation about the {pet['animal']}:")
    print(f"  Animal: {pet['animal']}")
    print(f"  Owner: {pet['owner']}")
