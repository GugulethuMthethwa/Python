# Define the Restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance of the Restaurant class
restaurant = Restaurant("The Gourmet Spot", "Italian")

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
