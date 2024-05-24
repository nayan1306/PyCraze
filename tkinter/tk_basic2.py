import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Button Interaction")
window.minsize(width=600,height=300)

# Create a label widget
label = tk.Label(window, text="Click the button", font=("Arial", 25))
label.pack(pady=10)

# Create a button widget
button = tk.Button(window, text="Click Me", command=on_button_click, font=("Arial", 20), bg="light blue", fg="white")
button.pack(pady=10)

# Additional customization: Add a Quit button
quit_button = tk.Button(window, text="Quit", command=window.quit, font=("Arial", 14), bg="red", fg="white")
quit_button.pack(pady=10)

# Start the main event loop
window.mainloop()
