import tkinter as tk

# Declare expression global variable to hold the math expression



# Function to update expression when a button is pressed
def press(key):
    # Declare expression global variable inside this function
    global ______
    expression += str(key)
    displayExpression.set(expression)  # show updated expression

# Function to calculate the expression once "=" button is clicked
def calculate():
    # Declare expression global variable inside this function
    global ______
    # Build the logical math operation by using Python Fundamentals
    #------------------------------------------------------------------------------------------------------------------------------------------------
    # Use if/elif/else to determine whether which operators (+ or - or * or /) exist in the expression and
    # calculate the number (float) accordingly
    
    #------------------------------------------------------------------------------------------------------------------------------------------------



# Function to clear the screen
def clear():
    global expression
    expression = ""
    displayExpression.set("")


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# StringVar to update text entry automatically
displayExpression = tk.StringVar()

# Entry box to displayExpression expressions
entry = tk.Entry(window, textvariable=displayExpression, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)


# Build the Numbers and Operators layout of the Calculator
#------------------------------------------------------------------------------------------------------------------------------------------------
# Declare "Buttons" lists that stores the Numbers and Operators




# Declare row = 1 and col = 0 and use for loop to access each element in "Buttons" list



# Use For Loop to iterate through the "Buttons" list and assign each button their respective function





#  sample code to assign the action(function) to each button and style it accordingly
#  tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=action).grid(row=row, column=col)
#------------------------------------------------------------------------------------------------------------------------------------------------

# Clear button
tk.Button(window, text='Clear', padx=85, pady=20, font=('Arial', 14),
          command=clear).grid(row=row, column=0, columnspan=4)

# Run the app
window.mainloop()

