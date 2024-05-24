import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Using Frames")

# Create a top frame and add widgets
top_frame = tk.Frame(window, bg="lightblue", pady=20)
top_frame.pack(fill="x")

label = tk.Label(top_frame, text="Top Frame", font=("Arial", 18), bg="lightblue")
label.pack()

button1 = tk.Button(top_frame, text="Button 1", font=("Arial", 14), bg="green", fg="white")
button1.pack(side="left", padx=10)

button2 = tk.Button(top_frame, text="Button 2", font=("Arial", 14), bg="green", fg="white")
button2.pack(side="right", padx=10)

# Create a bottom frame and add widgets
bottom_frame = tk.Frame(window, bg="lightgray", pady=20)
bottom_frame.pack(fill="x")

entry = tk.Entry(bottom_frame, font=("Arial", 14))
entry.pack(pady=10)

button3 = tk.Button(bottom_frame, text="Button 3", font=("Arial", 14), bg="blue", fg="white")
button3.pack(pady=10)

# Additional customization: Add an exit button
exit_button = tk.Button(bottom_frame, text="Exit", command=window.quit, font=("Arial", 14), bg="red", fg="white")
exit_button.pack(pady=10)

# Start the main event loop
window.mainloop()
