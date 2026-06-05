import tkinter as tk
from tkinter import messagebox
def calculate_tax():
    try:
        income = float(entry_income.get())
        if income <= 250000:
            tax = 0
        elif income <= 500000:
            tax = (income - 250000) * 0.05
        elif income <= 1000000:
            tax = (250000 * 0.05) + (income - 500000) * 0.2
        else:
            tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3
        result_label.config(text=f"Tax Payable: ₹{tax:.2f}")
    except:
        messagebox.showerror("Error", "Invalid Input")
root = tk.Tk()
root.title("Tax Calculator")
root.geometry("300x200")
tk.Label(root, text="Annual Income").pack()
entry_income = tk.Entry(root)
entry_income.pack()
tk.Button(root, text="Calculate Tax", command=calculate_tax).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
