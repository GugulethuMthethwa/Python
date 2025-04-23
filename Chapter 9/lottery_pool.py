import random

# Create a list containing 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 numbers or letters from the list
winning_ticket = random.sample(lottery_pool, 4)

# Print the winning ticket message
print("Winning Ticket:")
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")