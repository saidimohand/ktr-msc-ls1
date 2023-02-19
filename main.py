import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("User Profile")

# Create the form labels
name_label = tk.Label(root, text="Name*:")
company_label = tk.Label(root, text="Company:")
email_label = tk.Label(root, text="Email:")
phone_label = tk.Label(root, text="Telephone:")

# Create the form fields
name_field = tk.Entry(root)
company_field = tk.Entry(root)
email_field = tk.Entry(root)
phone_field = tk.Entry(root)

# Define the form layout using the grid geometry manager
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
name_field.grid(row=0, column=1, padx=5, pady=5, sticky="W")
company_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")
company_field.grid(row=1, column=1, padx=5, pady=5, sticky="W")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")
email_field.grid(row=2, column=1, padx=5, pady=5, sticky="W")
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="E")
phone_field.grid(row=3, column=1, padx=5, pady=5, sticky="W")

# Create the save and cancel buttons
save_button = tk.Button(root, text="Save")
cancel_button = tk.Button(root, text="Cancel")

# Define the button layout
save_button.grid(row=4, column=0, padx=5, pady=10, sticky="E")
cancel_button.grid(row=4, column=1, padx=5, pady=10, sticky="W")

# Start the main loop
root.mainloop()

# Define the password to access the profile
PASSWORD = "1234"

def check_password():
    """Check if the entered password is correct."""
    password = password_field.get()
    if password == PASSWORD:
        # Password is correct, allow access to the profile
        root.deiconify()
        password_window.withdraw()
    else:
        # Password is incorrect, show an error message
        error_label.config(text="Incorrect password!")

# Create the password window
password_window = tk.Tk()
password_window.title("Enter Password")

# Create the password label and field
password_label = tk.Label(password_window, text="Password:")
password_field = tk.Entry(password_window, show="*")

# Create the submit button and error label
submit_button = tk.Button(password_window, text="Submit", command=check_password)
error_label = tk.Label(password_window, text="", fg="red")

# Define the layout of the password window
password_label.pack(padx=5, pady=5)
password_field.pack(padx=5, pady=5)
submit_button.pack(padx=5, pady=5)
error_label.pack(padx=5, pady=5)

# Hide the main window until the correct password is entered
root = tk.Tk()
root.withdraw()

# Define the main window and form elements
def show_profile():
    """Show the user profile."""
    root.deiconify()

name_label = tk.Label(root, text="Name*:")
company_label = tk.Label(root, text="Company:")
email_label = tk.Label(root, text="Email:")
phone_label = tk.Label(root, text="Telephone:")

name_field = tk.Entry(root)
company_field = tk.Entry(root)
email_field = tk.Entry(root)
phone_field = tk.Entry(root)

save_button = tk.Button(root, text="Save")
cancel_button = tk.Button(root, text="Cancel", command=show_profile)

# Define the layout of the user profile form
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
name_field.grid(row=0, column=1, padx=5, pady=5, sticky="W")
company_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")
company_field.grid(row=1, column=1, padx=5, pady=5, sticky="W")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")
email_field.grid(row=2, column=1, padx=5, pady=5, sticky="W")
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="E")
phone_field.grid(row=3, column=1, padx=5, pady=5, sticky="W")
save_button.grid(row=4, column=0, padx=5, pady=10, sticky="E")
cancel_button.grid(row=4, column=1, padx=5, pady=10, sticky="W")

# Start the main loop
password_window.mainloop()

