import tkinter as tk
from tkinter import messagebox
def calculate_attendance():
    try:
        attended = int(entry_attended.get())
        total = int(entry_total.get())
        percentage = (attended / total) * 100
        if percentage >= 75:
            msg = "Eligible ✅"
        else:
            needed = int((0.75 * total) - attended)
            msg = f"Not Eligible ❌\nAttend {needed} more classes"
        result_label.config(text=f"Attendance: {percentage:.2f}%\n{msg}")
    except:
        messagebox.showerror("Error", "Invalid Input")
root = tk.Tk()
root.title("Attendance Calculator")
root.geometry("300x250")
tk.Label(root, text="Classes Attended").pack()
entry_attended = tk.Entry(root)
entry_attended.pack()
tk.Label(root, text="Total Classes").pack()
entry_total = tk.Entry(root)
entry_total.pack()
tk.Button(root, text="Calculate Attendance", command=calculate_attendance).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
