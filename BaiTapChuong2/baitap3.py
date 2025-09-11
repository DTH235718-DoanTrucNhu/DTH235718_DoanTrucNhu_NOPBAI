print("Nhập điểm Toán, Lý, Hóa")
toan = float(input("Nhập điểm toán: "))
ly = float(input("Nhập điểm lý: "))
hoa = float(input("Nhập điểm hóa: "))
dtb = (toan + ly + hoa)/3
print("Điểm trung bình: ", dtb)
print("Điểm làm tròn: ", round(dtb,2))