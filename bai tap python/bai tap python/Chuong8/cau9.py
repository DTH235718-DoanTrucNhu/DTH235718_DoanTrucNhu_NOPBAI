import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút "Tính BMI"
def tinh_bmi():
    try:
        # Lấy giá trị Chiều cao và Cân nặng
        chieu_cao = float(entry_chieu_cao.get())
        can_nang = float(entry_can_nang.get())

        # Kiểm tra giá trị hợp lệ
        if chieu_cao <= 0 or can_nang <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và Cân nặng phải lớn hơn 0.")
            return

        # 1. Tính BMI: BMI = Cân nặng (kg) / (Chiều cao (m) * Chiều cao (m))
        # Cân nặng được nhập là 172 (có thể là gram hoặc kg, nhưng 172kg là rất lớn).
        # Giả sử người dùng nhập Cân nặng là **kilogram** (ví dụ: 72, 85, v.v.)
        # Nếu theo hình ảnh ví dụ, 172 có thể là cân nặng **tính bằng pound** hoặc **một lỗi nhập liệu**.
        # Tuy nhiên, theo công thức quốc tế, Cân nặng phải là **kilogram**.
        
        # Để tuân thủ công thức chuẩn:
        bmi = can_nang / (chieu_cao ** 2)
        
        # Làm tròn BMI đến 2 chữ số thập phân
        bmi = round(bmi, 2)

        # Cập nhật BMI trên giao diện
        lbl_bmi_ket_qua.config(text=str(bmi))

        # 2. Đánh giá Tình trạng và Nguy cơ phát triển bệnh
        tinh_trang = ""
        nguy_co = ""

        # Tiêu chuẩn Tình trạng cân nặng
        if bmi < 18.5:
            tinh_trang = "Gầy"
            nguy_co = "Thấp"
        elif 18.5 <= bmi <= 24.9:
            tinh_trang = "Bình thường"
            nguy_co = "Trung bình"
        elif 25 <= bmi <= 29.9:
            tinh_trang = "Mập" # Trong hình ví dụ là "Hơi Béo"
            nguy_co = "Hơi cao" # Trong hình ví dụ là "Hơi hơi cao"
        elif bmi >= 30:
            tinh_trang = "Béo phì"
            nguy_co = "Cao"

        # Cập nhật Tình trạng và Nguy cơ
        # Điều chỉnh để khớp với hình ảnh ví dụ nếu BMI rơi vào khoảng 25-29.9
        if tinh_trang == "Mập":
             entry_tinh_trang.delete(0, tk.END)
             entry_tinh_trang.insert(0, "Hơi Béo") # Dùng như hình minh họa
        else:
             entry_tinh_trang.delete(0, tk.END)
             entry_tinh_trang.insert(0, tinh_trang)

        if nguy_co == "Hơi cao":
             entry_nguy_co.delete(0, tk.END)
             entry_nguy_co.insert(0, "Hơi hơi cao") # Dùng như hình minh họa
        else:
             entry_nguy_co.delete(0, tk.END)
             entry_nguy_co.insert(0, nguy_co)


    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho Chiều cao và Cân nặng.")

# Hàm xử lý khi nhấn nút "Thoát"
def thoat_chuong_trinh():
    window.quit()

# --- Thiết lập cửa sổ chính (GUI) ---
window = tk.Tk()
window.title("Tính Chỉ Số BMI")

# Khung chứa màu vàng
frame = tk.Frame(window, bg='yellow', padx=20, pady=20)
frame.pack(padx=10, pady=10)

# --- Các thành phần giao diện ---

# 1. Chiều cao
tk.Label(frame, text="Nhập chiều cao:", bg='yellow').grid(row=0, column=0, sticky='w', pady=5)
entry_chieu_cao = tk.Entry(frame)
entry_chieu_cao.grid(row=0, column=1, pady=5)
entry_chieu_cao.insert(0, "1.8") # Giá trị mặc định như hình

# 2. Cân nặng
tk.Label(frame, text="Nhập cân nặng:", bg='yellow').grid(row=1, column=0, sticky='w', pady=5)
entry_can_nang = tk.Entry(frame)
entry_can_nang.grid(row=1, column=1, pady=5)
entry_can_nang.insert(0, "72") # Giá trị mặc định hợp lý hơn (ví dụ 72 kg)
# Nếu bạn muốn thử với 172 (như trong hình ví dụ):
# entry_can_nang.insert(0, "172")

# 3. Nút Tính BMI
btn_tinh_bmi = tk.Button(frame, text="Tính BMI", command=tinh_bmi)
btn_tinh_bmi.grid(row=2, column=1, pady=10)

# 4. Kết quả BMI
tk.Label(frame, text="BMI của bạn:", bg='yellow').grid(row=3, column=0, sticky='w', pady=5)
lbl_bmi_ket_qua = tk.Label(frame, text="x", bg='white', relief='sunken', width=10)
lbl_bmi_ket_qua.grid(row=3, column=1, pady=5)

# 5. Tình trạng của bạn
tk.Label(frame, text="Tình trạng của bạn:", bg='yellow').grid(row=4, column=0, sticky='w', pady=5)
entry_tinh_trang = tk.Entry(frame, justify='center')
entry_tinh_trang.grid(row=4, column=1, pady=5)
entry_tinh_trang.insert(0, "Hơi Béo") # Giá trị mặc định như hình

# 6. Nguy cơ phát triển bệnh
tk.Label(frame, text="Nguy cơ\nphát triển bệnh:", bg='yellow').grid(row=5, column=0, sticky='w', pady=5)
entry_nguy_co = tk.Entry(frame, justify='center')
entry_nguy_co.grid(row=5, column=1, pady=5)
entry_nguy_co.insert(0, "Hơi hơi cao") # Giá trị mặc định như hình

# 7. Nút Thoát
btn_thoat = tk.Button(frame, text="Thoát", command=thoat_chuong_trinh)
btn_thoat.grid(row=6, column=1, pady=10)

# Chạy vòng lặp chính của GUI
window.mainloop()