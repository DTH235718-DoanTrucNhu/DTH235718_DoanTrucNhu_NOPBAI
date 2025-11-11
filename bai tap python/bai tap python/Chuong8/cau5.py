import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút OK
def change_password():
    old = entry_old.get()
    new = entry_new.get()
    again = entry_again.get()

    if not old or not new or not again:
        messagebox.showwarning("Warning", "Vui lòng nhập đầy đủ thông tin!")
    elif new != again:
        messagebox.showerror("Error", "Mật khẩu mới không trùng khớp!")
    else:
        messagebox.showinfo("Success", "Đổi mật khẩu thành công!")

# Hàm xử lý khi nhấn Cancel
def cancel():
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Enter New Password")
root.geometry("350x180")
root.resizable(False, False)

# Nhãn và ô nhập
tk.Label(root, text="Old Password:", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_old = tk.Entry(root, show="*", width=25)
entry_old.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="New Password:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_new = tk.Entry(root, show="*", width=25)
entry_new.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter New Password Again:", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_again = tk.Entry(root, show="*", width=25)
entry_again.grid(row=2, column=1, padx=10, pady=5)

# Nút bấm
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=3, column=0, columnspan=2, pady=10)

btn_ok = tk.Button(frame_buttons, text="OK", width=10, command=change_password)
btn_ok.grid(row=0, column=0, padx=5)

btn_cancel = tk.Button(frame_buttons, text="Cancel", width=10, command=cancel)
btn_cancel.grid(row=0, column=1, padx=5)

root.mainloop()
