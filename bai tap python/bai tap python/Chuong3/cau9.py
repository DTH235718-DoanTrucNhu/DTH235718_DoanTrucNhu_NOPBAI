def xac_dinh_quy(thang):
    # Kiểm tra tháng hợp lệ
    if thang < 1 or thang > 12:
        return "Tháng không hợp lệ! Vui lòng nhập từ 1 đến 12."
    
    # Xác định quý tương ứng với tháng
    if thang >= 1 and thang <= 3:
        return "Quý 1"
    elif thang >= 4 and thang <= 6:
        return "Quý 2"
    elif thang >= 7 and thang <= 9:
        return "Quý 3"
    else:
        return "Quý 4"

# Nhập tháng từ người dùng
thang = int(input("Nhập tháng (1-12): "))

# In kết quả
print(f"Tháng {thang} thuộc {xac_dinh_quy(thang)}")