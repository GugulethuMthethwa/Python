# My Pizzas, Your Pizzas: Work with two separate pizza lists and prove they are independent.

# List of my favorite pizzas
my_pizzas = ["Pepperoni", "Margherita", "BBQ Chicken"]

# Make a copy of the list for my friend's favorite pizzas
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list (my_pizzas)
my_pizzas.append("Hawaiian")

# Add a different pizza to the copied list (friend_pizzas)
friend_pizzas.append("Vegetarian")

# Prove that we have two separate lists by printing the lists
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
