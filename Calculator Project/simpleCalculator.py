import tkinter as tk

# This variable will hold the math expression
expression = ""

# Function to update expression when a button is pressed
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)  # show updated expression

def calculate():
    global expression
    try:
        # Cover selection, Basic math, Data Type, Comparison
        # Build the logical math operation by using Basic math operators,
        # If/Else and Comparison Operators.
        # Make sure the datatype of the num1, num2 is cast to Float.
        
        # A problem: In this example we have to use float casting, but
        #            we didn't teach them in the fundamentals
        
#------------------------------------------------------------------------------------------------------------------------------------------------
        # Detect operator and split the expression
        if '+' in expression:
            num1, num2 = expression.split('+')
            result = float(num1) + float(num2)
        elif '-' in expression:
            num1, num2 = expression.split('-')
            result = float(num1) - float(num2)
        elif '*' in expression:
            num1, num2 = expression.split('*')
            result = float(num1) * float(num2)
        elif '/' in expression:
            num1, num2 = expression.split('/')
            if float(num2) == 0:
                raise ZeroDivisionError
            result = float(num1) / float(num2)
        else:
            result = "Error"

        equation.set(str(result))
        expression = str(result)  # allow chaining
#------------------------------------------------------------------------------------------------------------------------------------------------
    except:
        equation.set("Error")
        expression = ""


# Function to clear the screen
def clear():
    global expression
    expression = ""
    equation.set("")


# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# StringVar to update text entry automatically
equation = tk.StringVar()

# Entry box to display expressions
entry = tk.Entry(window, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)


# Build the numbers and operators of the caculator
# by using "Buttons" Array that stores the numbers and operators
# declare row = 1 and col = 0 and use for loop to access each element in "Buttons" array
#------------------------------------------------------------------------------------------------------------------------------------------------
# Button text layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons using loop
row = 1
col = 0

# Cover For loop, Array, Comparison and Basic Math
for button in buttons:
    if button == '=':
        action = calculate
    else:
        action = lambda x=button: press(x)
        
    tk.Button(window, text=button, padx=20, pady=20, font=('Arial', 14), command=action).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1
#------------------------------------------------------------------------------------------------------------------------------------------------

# Clear button
tk.Button(window, text='Clear', padx=85, pady=20, font=('Arial', 14),
          command=clear).grid(row=row, column=0, columnspan=4)

# Run the app
window.mainloop()

