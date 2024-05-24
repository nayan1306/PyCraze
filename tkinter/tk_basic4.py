import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Grid Layout")

# Create and place widgets using grid layout
label1 = tk.Label(window, text="Label 1", font=("Arial", 14), bg="lightgray")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(window, text="Label 2", font=("Arial", 14), bg="lightgray")
label2.grid(row=0, column=1, padx=10, pady=10)

entry1 = tk.Entry(window, font=("Arial", 14))
entry1.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(window, font=("Arial", 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

# Add a submit button that prints entries to the console
def submit():
    print(f"Entry 1: {entry1.get()}")
    print(f"Entry 2: {entry2.get()}")

button = tk.Button(window, text="Submit", command=submit, font=("Arial", 14), bg="blue", fg="white")
button.grid(row=2, column=0, columnspan=2, pady=20)

# Additional customization: Add a clear button
def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

clear_button = tk.Button(window, text="Clear", command=clear, font=("Arial", 14), bg="orange", fg="white")
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main event loop
window.mainloop()
