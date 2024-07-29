import tkinter as tk

# Function to update expression in the entry box
def press(key):
    current_text = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(0, current_text + str(key))

# Function to evaluate the expression and update the entry box with the result
def equal_press():
    try:
        result = str(eval(expression_entry.get()))
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, result)
    except:
        expression_entry.delete(0, tk.END)
        expression_entry.insert(0, "Error")

# Function to clear the entry box
def clear():
    expression_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for expression
expression_entry = tk.Entry(root, width=40, borderwidth=5)
expression_entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        btn = tk.Button(root, text=button, padx=30, pady=20, command=equal_press)
    else:
        btn = tk.Button(root, text=button, padx=30, pady=20, command=lambda key=button: press(key))
    
    btn.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_button = tk.Button(root, text='C', padx=30, pady=20, command=clear)
clear_button.grid(row=row_val, column=0, columnspan=4)

# Run the application
root.mainloop()