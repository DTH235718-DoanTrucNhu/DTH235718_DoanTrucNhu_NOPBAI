def ToiUuChuoiDanhTu(chuoi):
    # Xóa khoảng trắng dư thừa ở đầu và cuối, tách các từ theo khoảng trắng
    tu = chuoi.strip().split()
    
    # Viết hoa chữ cái đầu và viết thường các ký tự còn lại
    tu_toi_uu = [t.capitalize() for t in tu]
    
    # Ghép lại thành chuỗi, mỗi từ cách nhau 1 khoảng trắng
    ket_qua = " ".join(tu_toi_uu)
    return ket_qua

# --- Chương trình chính ---
chuoi = input("Nhập chuỗi danh từ: ")
print("Chuỗi sau khi tối ưu là:", ToiUuChuoiDanhTu(chuoi))
