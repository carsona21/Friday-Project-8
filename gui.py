# gui.py
import tkinter as tk
from tkinter import messagebox
from database import submit_feedback, retrieve_feedback

def submit():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_entry.get("1.0", tk.END)
    
    if name and email and feedback.strip():
        submit_feedback(name, email, feedback)
        messagebox.showinfo("Success", "Feedback submitted successfully!")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        feedback_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

def retrieve_data():
    password = input("Enter password to retrieve data: ")
    if password == "your_password":  # Replace with your desired password
        entries = retrieve_feedback()
        for entry in entries:
            print(f"ID: {entry[0]}, Name: {entry[1]}, Email: {entry[2]}, Feedback: {entry[3]}")
    else:
        print("Access denied: Incorrect password.")

def create_gui():
    global name_entry, email_entry, feedback_entry
    root = tk.Tk()
    root.title("Customer Feedback Application")

    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()

    tk.Label(root, text="Feedback").pack()
    feedback_entry = tk.Text(root, height=5, width=40)
    feedback_entry.pack()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()

    retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_data)
    retrieve_button.pack()

    root.mainloop()
