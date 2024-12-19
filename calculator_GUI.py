import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def perform_operation():
    try:
        # Get the values from the input fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        # Perform the calculation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operator selected.")
            return

        # Display the result
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

def clear_inputs():
    """Clears all inputs and the result."""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    operator_var.set("+")
    result_label.config(text="Result: ")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x500")  # Fixed window size
root.resizable(False, False)

# Apply a theme for better styling
style = ttk.Style()
style.theme_use('vista')

# Create widgets
ttk.Label(root, text="Calculator", font=("Helvetica", 20, "bold"), anchor="center").pack(pady=10)

frame_inputs = ttk.Frame(root)
frame_inputs.pack(pady=20)

ttk.Label(frame_inputs, text="Enter first number:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_num1 = ttk.Entry(frame_inputs, width=15, font=("Helvetica", 12))
entry_num1.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame_inputs, text="Enter second number:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_num2 = ttk.Entry(frame_inputs, width=15, font=("Helvetica", 12))
entry_num2.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(frame_inputs, text="Select operation:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
operator_var = tk.StringVar(value="+")
operator_menu = ttk.OptionMenu(frame_inputs, operator_var, "+", "+", "-", "*", "/")
operator_menu.grid(row=2, column=1, padx=10, pady=10)

frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=20)

calculate_button = ttk.Button(frame_buttons, text="Calculate", command=perform_operation, style="TButton")
calculate_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(frame_buttons, text="Clear", command=clear_inputs, style="TButton")
clear_button.grid(row=0, column=1, padx=10)

result_label = ttk.Label(root, text="Result: ", font=("Helvetica", 14, "bold"), anchor="center")
result_label.pack(pady=20)

# Run the application
root.mainloop()

