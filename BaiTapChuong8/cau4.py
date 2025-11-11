import tkinter as tk

# Hàm xử lý khi nhấn nút
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "Clr":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")

# Ô hiển thị
entry = tk.Entry(root, font=("Arial", 16), justify='right', bd=10)
entry.grid(row=0, column=0, columnspan=4)

# Các nút bấm
buttons = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "-", "0", "+",
    "*", "/", "=", "Clr"
]

row_val = 1
col_val = 0

for text in buttons:
    button = tk.Button(root, text=text, font=("Arial", 14), padx=10, pady=10)
    button.grid(row=row_val, column=col_val, sticky="nsew")
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 2 and text not in ["*", "/", "=", "Clr"]:
        col_val = 0
        row_val += 1
    elif text in ["-", "+", "*", "/", "=", "Clr"]:
        if text == "-":
            col_val = 0
            row_val += 1
        elif text in ["+", "*", "/", "=", "Clr"]:
            col_val = (col_val + 1) % 3
            if col_val == 0:
                row_val += 1

# Tùy chỉnh kích thước các cột và hàng
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
