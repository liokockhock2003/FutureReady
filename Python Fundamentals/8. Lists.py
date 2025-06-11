# Create a lists of fruits
fruits = ["apple", "banana", "orange", "grape"]

# Print the whole list
print("All fruits:", fruits)

# Accessing individual elements (index starts at 0)
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Adding a new fruit (append())
fruits.append("mango")
print("After adding mango:", fruits)

# Removing a fruit (remove("----"))
fruits.remove("banana")
print("After removing banana:", fruits)

# Looping through the array
for fruit in fruits:
    print("I like", fruit)
