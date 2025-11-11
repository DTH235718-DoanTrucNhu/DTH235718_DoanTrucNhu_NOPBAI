import tkinter as tk

root = tk.Tk()
root.title("frame 2")

# Tạo danh sách các kiểu relief (style)
reliefs = ['raised', 'sunken', 'flat', 'ridge', 'groove', 'solid']

# Tạo các hàng với độ dày viền khác nhau
for i in range(5):
    border = i  # borderwidth = i
    tk.Label(root, text=f"borderwidth = {border}", width=15, anchor='w').grid(row=i, column=0, padx=5, pady=5)
    
    # Tạo các nút với kiểu relief khác nhau
    for j, style in enumerate(reliefs):
        btn = tk.Button(root, text=style, relief=style, borderwidth=border, width=8)
        btn.grid(row=i, column=j+1, padx=5, pady=5)

root.mainloop()
