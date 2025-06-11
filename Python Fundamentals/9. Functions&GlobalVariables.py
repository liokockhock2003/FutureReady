# This is a global variable
count = 0

# This is a function that updates the global variable
def increment():
    global count  # Tell Python we want to use the global 'count'
    count = count + 1
    print("Count is now:", count)

# This is another function
def reset():
    global count
    count = 0
    print("Count has been reset to:", count)

# Calling the functions
increment()  # Output: Count is now: 1
increment()  # Output: Count is now: 2
reset()      # Output: Count has been reset to: 0
