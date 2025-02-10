# Modified function definition with default values
def make_shirt(size="L", message="I love Python"):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'.")

# Calling the function with the default size and message (large shirt)
make_shirt()

# Calling the function with the default message but a medium shirt size
make_shirt(size="M")

# Calling the function with a custom message and shirt size
make_shirt(size="S", message="Code More, Worry Less")
