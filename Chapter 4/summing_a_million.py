# Summing a Million: Use min(), max(), and sum() to check a list of numbers from 1 to 1 million.

# Generate a list of numbers from 1 to 1 million
numbers = range(1, 1000001)

# Use min() to check the first number
print(f"The smallest number is: {min(numbers)}")

# Use max() to check the last number
print(f"The largest number is: {max(numbers)}")

# Use sum() to calculate the sum of all numbers
total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")
