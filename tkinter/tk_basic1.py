import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Basic GUI Program")
window.minsize(width=600, height=400)

# Create a label widget
label = tk.Label(window, text="Crazzyyyy!", font=("Arial", 24))
label.pack(pady=20)  # Add padding for better spacing

# Additional customization: Change the background color
window.config(bg="lightblue")

# Start the main event loop
window.mainloop()
