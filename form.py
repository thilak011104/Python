import tkinter as tk
from tkinter import messagebox


def submit_form():
    name = name_var.get()
    email = email_var.get()
    gender = gender_var.get()

    if not name or not email or not gender:
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Submitted", f"Name: {name}\nEmail: {email}\nGender: {gender}")


# Create the main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x200")

# Variables to store form data
name_var = tk.StringVar()
email_var = tk.StringVar()
dob_var = tk.StringVar()
phone_var = tk.StringVar()
gender_var = tk.StringVar()


# Labels and Entry widgets
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=email_var).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Dob").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=dob_var).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Phone").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=phone_var).grid(row=3, column=1, padx=10, pady=10)

# Radio buttons for gender selection
tk.Label(root, text="Gender").grid(row=3, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, padx=10, pady=10, sticky='w')
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=1, padx=10, pady=10,sticky='e')

# Submit button
tk.Button(root, text="Submit", command=submit_form).grid(row=5, column=1, padx=10, pady=20)

# Run the main event loop
root.mainloop()