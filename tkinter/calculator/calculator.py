import tkinter as tk
from tkinter import ttk

class Calculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.total_expression = ""
        self.current_expression = ""
        
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def create_display_frame(self):
        frame = tk.Frame(self, height=221, bg="lightgray")
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="lightgray", fg="black", padx=24, font=("Arial", 18))
        total_label.pack(expand=True, fill="both")
        
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="lightgray", fg="black", padx=24, font=("Arial", 48, "bold"))
        label.pack(expand=True, fill="both")
        
        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = ttk.Button(self.buttons_frame, text=str(digit), command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = ttk.Button(self.buttons_frame, text=symbol, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_special_buttons(self):
        clear_button = ttk.Button(self.buttons_frame, text="C", command=self.clear)
        clear_button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)
        
        equal_button = ttk.Button(self.buttons_frame, text="=", command=self.evaluate)
        equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def bind_keys(self):
        self.bind("<Return>", lambda event: self.evaluate())
        self.bind("<BackSpace>", lambda event: self.clear())
        for key in self.digits:
            self.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.bind(key, lambda event, operator=key: self.append_operator(operator))
