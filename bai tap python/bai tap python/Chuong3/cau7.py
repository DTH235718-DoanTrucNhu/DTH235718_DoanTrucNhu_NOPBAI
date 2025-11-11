from datetime import datetime, timedelta

def ngay_ke_sau(ngay, thang, nam):
    # Tạo đối tượng ngày từ thông tin ngày, tháng, năm nhập vào
    ngay_nhap = datetime(nam, thang, ngay)
    
    # Tính ngày kế tiếp (cộng thêm 1 ngày)
    ngay_ke = ngay_nhap + timedelta(days=1)
    
    # Trả về ngày kế tiếp theo định dạng dd/mm/yyyy
    return ngay_ke.strftime("%d/%m/%Y")

# Nhập ngày, tháng, năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# In kết quả
print(f"Ngày kế tiếp là: {ngay_ke_sau(ngay, thang, nam)}")