# Define the User class
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    # Method to describe the user's information
    def describe_user(self):
        print(f"User Information: \nName: {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nLocation: {self.location}\n")

    # Method to greet the user
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")

# Create several instances of the User class
user1 = User("John", "Doe", 28, "john.doe@example.com", "New York")
user2 = User("Jane", "Smith", 34, "jane.smith@example.com", "Los Angeles")
user3 = User("Alice", "Johnson", 25, "alice.johnson@example.com", "Chicago")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
