import tkinter as tk

def update_label(event=None):
    label.config(text=entry.get())

# Create the main window
window = tk.Tk()
window.title("Entry Widget")

# Create an entry widget
entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)
entry.bind("<Return>", update_label)

# Create a label widget
label = tk.Label(window, text="Type something and press Enter", font=("Arial", 18))
label.pack(pady=10)

# Additional customization: Add a button to update the label
update_button = tk.Button(window, text="Update Label", command=update_label, font=("Arial", 14), bg="green", fg="white")
update_button.pack(pady=10)

# Start the main event loop
window.mainloop()
