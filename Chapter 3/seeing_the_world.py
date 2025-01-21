# Seeing the World: Store five places you'd like to visit in a list and demonstrate various list manipulations.

places = ["Tokyo", "Paris", "New York", "Sydney", "Cape Town"]

# Print the list in its original order
print("Original list:")
print(places)

# Print the list in alphabetical order without modifying the original list
print("\nList in alphabetical order (using sorted()):")
print(sorted(places))

# Show that the list is still in its original order
print("\nOriginal list after sorted() was used:")
print(places)

# Print the list in reverse alphabetical order without modifying the original list
print("\nList in reverse alphabetical order (using sorted()):")
print(sorted(places, reverse=True))

# Show that the list is still in its original order
print("\nOriginal list after reverse sorted() was used:")
print(places)

# Use reverse() to change the order of the list and print it
places.reverse()
print("\nList after using reverse():")
print(places)

# Use reverse() again to change the order back to the original
places.reverse()
print("\nList after using reverse() again to restore original order:")
print(places)

# Use sort() to permanently change the list to alphabetical order
places.sort()
print("\nList after using sort() to arrange in alphabetical order:")
print(places)

# Use sort() to permanently change the list to reverse alphabetical order
places.sort(reverse=True)
print("\nList after using sort() to arrange in reverse alphabetical order:")
print(places)