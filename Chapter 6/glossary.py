# Creating a glossary with programming terms and their meanings
glossary = {
    'Variable': 'A variable is a container for storing data values.',
    'Function': 'A function is a block of code that only runs when it is called.',
    'Loop': 'A loop is used to repeat a block of code as long as a condition is true.',
    'Array': 'An array is a collection of elements, all of the same type, stored in a single variable.',
    'Class': 'A class is a blueprint for creating objects, providing initial values for state and implementations of behavior.'
}

# Printing each word and its meaning
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
