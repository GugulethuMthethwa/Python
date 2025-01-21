# Buffet: A tuple of five basic foods in a buffet-style restaurant.

# Initial tuple with five foods
buffet_foods = ("Pizza", "Pasta", "Burger", "Salad", "Sushi")

# Print each food item the restaurant offers
print("Original buffet menu:")
for food in buffet_foods:
    print(food)

# Try to modify one of the items (this will raise an error because tuples are immutable)
try:
    buffet_foods[1] = "Steak"  # This will raise an error
except TypeError as e:
    print(f"\nError: {e}")

# The restaurant changes its menu, replacing two of the items with different foods.
# Create a new tuple with the revised menu
buffet_foods = ("Pizza", "Steak", "Tacos", "Soup", "Sushi")

# Print the revised menu
print("\nRevised buffet menu:")
for food in buffet_foods:
    print(food)
