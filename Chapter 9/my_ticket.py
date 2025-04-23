import random

# Create a list containing 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [1, 'A', 3, 'C']

# Counter for the number of draws
draw_count = 0

while True:
    # Randomly select 4 numbers or letters from the list
    winning_ticket = random.sample(lottery_pool, 4)
    draw_count += 1

    # Check if the winning ticket matches your ticket
    if set(winning_ticket) == set(my_ticket):
        break

# Print the results
print(f"Your ticket {my_ticket} won after {draw_count} draws!")
