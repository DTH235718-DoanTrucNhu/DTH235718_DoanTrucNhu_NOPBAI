def tinh_toan(a, b, phep_toan):
    if phep_toan == "+":
        return a + b
    elif phep_toan == "-":
        return a - b
    elif phep_toan == "*":
        return a * b
    elif phep_toan == "/":
        # Kiểm tra chia cho 0
        if b != 0:
            return a / b
        else:
            return "Lỗi: Không thể chia cho 0"
    else:
        return "Lỗi: Phép toán không hợp lệ"

# Nhập giá trị a, b và phép toán
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
phep_toan = input("Nhập phép toán (+, -, *, /): ")

# Tính và in kết quả
ket_qua = tinh_toan(a, b, phep_toan)
print(f"Kết quả: {ket_qua}")