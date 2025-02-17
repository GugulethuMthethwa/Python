# Creating dictionaries representing different people
person_1 = {
    'first_name': 'Themba',
    'last_name': 'Maetane',
    'age': 28,
    'city': 'Joburg'
}

person_2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Chicago'
}

# Storing all three dictionaries in a list called 'people'
people = [person_1, person_2, person_3]

# Looping through the list of people and printing information about each person
for person in people:
    print(f"\nInformation about {person['first_name']} {person['last_name']}:")
    print(f"  First name: {person['first_name']}")
    print(f"  Last name: {person['last_name']}")
    print(f"  Age: {person['age']}")
    print(f"  City: {person['city']}")