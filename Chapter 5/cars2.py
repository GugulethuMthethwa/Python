# Test for equality and inequality with strings
name = 'alice'
print("Is name == 'alice'? I predict True.")
print(name == 'alice')  # True because name is 'alice'

print("\nIs name != 'bob'? I predict True.")
print(name != 'bob')  # True because name is not 'bob'

# Tests using the lower() method
greeting = 'HELLO'
print("\nIs greeting.lower() == 'hello'? I predict True.")
print(greeting.lower() == 'hello')  # True because 'HELLO'.lower() is 'hello'

print("\nIs greeting.lower() == 'HELLO'? I predict False.")
print(greeting.lower() == 'HELLO')  # False because 'HELLO'.lower() is 'hello', not 'HELLO'

# Numerical tests involving equality and inequality
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)  # True because age is 25

print("\nIs age != 30? I predict True.")
print(age != 30)  # True because age is not 30

# Greater than and less than comparisons
print("\nIs age > 20? I predict True.")
print(age > 20)  # True because 25 is greater than 20

print("\nIs age < 20? I predict False.")
print(age < 20)  # False because 25 is not less than 20

# Greater than or equal to, less than or equal to
print("\nIs age >= 25? I predict True.")
print(age >= 25)  # True because age is 25, and 25 is greater than or equal to 25

print("\nIs age <= 20? I predict False.")
print(age <= 20)  # False because age is 25, and 25 is not less than or equal to 20

# Tests using the and keyword
has_sunroof = True
has_air_conditioning = False
print("\nIs the car equipped with both a sunroof and air conditioning? I predict False.")
print(has_sunroof and has_air_conditioning)  # False because both conditions are not true

# Tests using the or keyword
print("\nDoes the car have either a sunroof or air conditioning? I predict True.")
print(has_sunroof or has_air_conditioning)  # True because at least one condition is true

# Test whether an item is in a list
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'apple' in the fruits list? I predict True.")
print('apple' in fruits)  # True because 'apple' is in the list

print("\nIs 'orange' in the fruits list? I predict False.")
print('orange' in fruits)  # False because 'orange' is not in the list

# Test whether an item is not in a list
print("\nIs 'grape' not in the fruits list? I predict True.")
print('grape' not in fruits)  # True because 'grape' is not in the list

print("\nIs 'banana' not in the fruits list? I predict False.")
print('banana' not in fruits)  # False because 'banana' is in the list
