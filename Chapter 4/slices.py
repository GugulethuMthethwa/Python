# Cubes: Create a list of the first 10 cubes (the cube of each integer from 1 to 10) and print each value.

# Generate a list of the first 10 cubes
cubes = [number ** 3 for number in range(1, 11)]

# Print the full list of cubes
print("The full list of cubes:", cubes)

# Print the first three items in the list
print("\nThe first three items in the list are:", cubes[:3])

# Print three items from the middle of the list (items 4, 5, and 6)
middle = len(cubes) // 2  # Find the middle index
print("\nThree items from the middle of the list are:", cubes[middle-1:middle+2])

# Print the last three items in the list
print("\nThe last three items in the list are:", cubes[-3:])
