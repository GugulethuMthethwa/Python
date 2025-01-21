# Every Function: Use different list functions to work with a list of countries.

countries = ["Japan", "Brazil", "Canada", "Australia", "Germany"]

# Print the original list
print(f"Original list: {countries}")

# Use len() to print the number of items in the list
print(f"\nThe number of countries in the list: {len(countries)}")

# Use sorted() to print the list in alphabetical order without changing the original list
print(f"\nList in alphabetical order (using sorted()): {sorted(countries)}")

# Show that the original list is still unchanged
print(f"\nOriginal list after using sorted(): {countries}")

# Use reverse() to reverse the order of the list (this will modify the list)
countries.reverse()
print(f"\nList after using reverse(): {countries}")

# Use reverse() again to restore the original order
countries.reverse()
print(f"\nList after using reverse() again to restore the original order: {countries}")

# Use sort() to sort the list in alphabetical order
countries.sort()
print(f"\nList after using sort() to arrange in alphabetical order: {countries}")

# Use sort() to sort the list in reverse alphabetical order
countries.sort(reverse=True)
print(f"\nList after using sort() to arrange in reverse alphabetical order: {countries}")

# Use append() to add a new country to the list
countries.append("France")
print(f"\nList after using append() to add France: {countries}")

# Use insert() to add a new country at the beginning of the list
countries.insert(0, "Italy")
print(f"\nList after using insert() to add Italy at the beginning: {countries}")

# Use pop() to remove the last item from the list
removed_country = countries.pop()
print(f"\nList after using pop() to remove {removed_country}: {countries}")

# Use remove() to remove a specific country by name
countries.remove("Germany")
print(f"\nList after using remove() to remove Germany: {countries}")

# Use del to delete the list entirely (this will empty the list)
del countries
print("\nAfter using del, the list is deleted.")