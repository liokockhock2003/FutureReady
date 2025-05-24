# We assign the value 85 to the variable 'score'
score = 85

# Check if the score is 90 or above
if score >= 90:
    print("A grade")  # This will not run because 85 is less than 90

# If the first condition is False, check if score is 70 or above
elif score >= 70:
    print("B grade")  # This will run because 85 is greater than 70

# If both previous conditions are False, this block will run
else:
    print("Try harder!")  # This will not run
