import tkinter as tk
from tkinter import messagebox

# Hàm chuyển độ F sang độ C
def chuyen():
    try:
        do_f = float(entry.get())
        do_c = (do_f - 32) * 5 / 9
        lbl_kq.config(text=f"{do_c:.2f} °C")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị số hợp lệ!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("400x200")
root.configure(bg="yellow")

# Nhãn và ô nhập
tk.Label(root, text="Nhập độ F", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
entry.grid(row=0, column=1, padx=5, pady=10)

# Nút chuyển
btn = tk.Button(root, text="Chuyển", font=("Arial", 12), command=chuyen, bg="lightblue")
btn.grid(row=0, column=2, padx=10, pady=10)

# Nhãn kết quả
tk.Label(root, text="Độ C", bg="yellow", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
lbl_kq = tk.Label(root, text="Độ C ở đây", bg="yellow", font=("Arial", 12, "bold"), fg="blue")
lbl_kq.grid(row=1, column=1, padx=10, pady=10, sticky="w")

root.mainloop()
