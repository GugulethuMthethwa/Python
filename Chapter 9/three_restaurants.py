# Define the Restaurant class (same as Exercise 9-1)
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create three instances of the Restaurant class
restaurant1 = Restaurant("The Gourmet Spot", "Italian")
restaurant2 = Restaurant("Sushi Paradise", "Japanese")
restaurant3 = Restaurant("Taco Haven", "Mexican")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

