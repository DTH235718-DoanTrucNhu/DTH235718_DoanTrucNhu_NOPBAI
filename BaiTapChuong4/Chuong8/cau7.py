import tkinter as tk
from tkinter import messagebox

# Danh sách 10 Thiên Can và 12 Địa Chi
can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Hàm chuyển đổi năm
def chuyen():
    try:
        nam = int(entry.get())
        can_index = (nam + 6) % 10
        chi_index = (nam + 8) % 12
        nam_am = can[can_index] + " " + chi[chi_index]
        lbl_kq.config(text=nam_am)
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm hợp lệ!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển năm Dương Lịch sang Âm Lịch")
root.geometry("400x200")
root.configure(bg="yellow")

# Nhãn và ô nhập
tk.Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
entry.grid(row=0, column=1, padx=5, pady=10)

# Nút chuyển
btn = tk.Button(root, text="Chuyển", font=("Arial", 12), command=chuyen, bg="lightblue")
btn.grid(row=0, column=2, padx=10, pady=10)

# Hiển thị kết quả
tk.Label(root, text="Năm âm:", bg="yellow", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
lbl_kq = tk.Label(root, text="", bg="yellow", font=("Arial", 12, "bold"), fg="blue")
lbl_kq.grid(row=1, column=1, padx=10, pady=10, sticky="w")

root.mainloop()
