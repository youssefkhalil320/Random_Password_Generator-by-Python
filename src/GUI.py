import tkinter as tk
from tkinter import ttk, messagebox
from main import generate_password

# Constants global variables
WINDOW_SIZE = "400x200"

def on_generate_password():
    # Retrieve the number from the entry widget and convert it to an integer
    number_str = entry.get()
    try:
        number = int(number_str)
        # Generate a password with the provided number
        password = generate_password(number)
        # Update the result_label with the generated password
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        # Handle the case where the conversion fails
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Abo-Leeh Password Generator")
root.configure(bg='#F5F5F5')  # Set background color

# Set a fixed window size
root.geometry(WINDOW_SIZE)
root.resizable(False, False)  # Disable resizing

# Creating the widgets with styles
welcome_label = ttk.Label(root, text="Welcome to Abo-Leeh password generator", style='TLabel')
instruction_label = ttk.Label(root, text="Please enter a number greater than or equal to 6", style='TLabel')
entry = ttk.Entry(root)
generate_button = ttk.Button(root, text="Generate Password", command=on_generate_password, style='TButton')
result_label = ttk.Label(root, text="Generated Password: ", style='TLabel')

# Placing the widgets in the window with padding
welcome_label.pack(pady=10)
instruction_label.pack(pady=5)
entry.pack(pady=5)
generate_button.pack(pady=10)
result_label.pack(pady=10)

# Apply a theme
style = ttk.Style()
style.theme_use('clam')  # or 'alt', 'default', 'classic', 'vista', 'xpnative'

# Customize button and label styles
style.configure('TButton', font=('Arial', 10), background='#E1E1E1')
style.configure('TLabel', font=('Arial', 10), background='#F5F5F5', foreground='#333333')

# Running the main loop
root.mainloop()