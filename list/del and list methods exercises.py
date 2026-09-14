arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]

# Delete using index
del arctic_animals[4]
print(arctic_animals)

# Remove using value
arctic_animals.remove("walrus")
print(arctic_animals)

# Add to the end
arctic_animals.append("arctic fox")
print(arctic_animals)

# Insert at index 3
arctic_animals.insert(3, "snowy owl")
print(arctic_animals)

# Sort alphabetically
arctic_animals.sort()
print(arctic_animals)

# Find the index of reindeer
print(arctic_animals.index("reindeer"))

# Remove and return the last item
arctic_animals.pop()
print(arctic_animals)