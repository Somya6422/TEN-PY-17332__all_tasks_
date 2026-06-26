import tkinter as tk
from tkinter import messagebox
def calculate_emi():
    try:
        P = float(entry_p.get())
        r = float(entry_r.get()) / (12 * 100)
        n = int(entry_n.get())

        emi = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
        result_label.config(text=f"Monthly EMI: ₹{emi:.2f}")
    except:
        messagebox.showerror("Error", "Invalid Input")
root = tk.Tk()
root.title("EMI Calculator")
root.geometry("300x300")
tk.Label(root, text="Loan Amount").pack()
entry_p = tk.Entry(root)
entry_p.pack()
tk.Label(root, text="Interest Rate (%)").pack()
entry_r = tk.Entry(root)
entry_r.pack()
tk.Label(root, text="Tenure (months)").pack()
entry_n = tk.Entry(root)
entry_n.pack()
tk.Button(root, text="Calculate EMI", command=calculate_emi).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
