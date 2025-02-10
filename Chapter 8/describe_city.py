# Function definition with a default country
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Calling the function with different cities
describe_city("Reykjavik")  # Default country (Iceland)
describe_city("Paris", "France")  # Custom country (France)
describe_city("Tokyo", "Japan")  # Custom country (Japan)
