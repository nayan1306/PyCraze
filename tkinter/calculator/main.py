import tkinter as tk
from calculator import Calculator

def main():
    root = tk.Tk()
    root.title("Cool Calculator")
    root.geometry("400x500")
    root.resizable(False, False)
    
    calculator = Calculator(root)
    calculator.pack(expand=True, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()
