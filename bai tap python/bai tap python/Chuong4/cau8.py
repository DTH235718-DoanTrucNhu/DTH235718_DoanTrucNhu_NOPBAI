import math

# Nhập giá trị a và x
a = float(input("Nhập cơ số a (>0, ≠1): "))
x = float(input("Nhập số x (>0): "))

# Kiểm tra điều kiện hợp lệ
if a <= 0 or a == 1 or x <= 0:
    print("Giá trị không hợp lệ! Cần có a > 0, a ≠ 1 và x > 0.")
else:
    # Tính log_a(x) theo công thức loga(x) = ln(x)/ln(a)
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x}")
