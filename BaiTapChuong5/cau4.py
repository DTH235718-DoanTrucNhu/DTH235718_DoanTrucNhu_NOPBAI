# Một số hàm quan trọng trong xử lý chuỗi của Python

chuoi = "  Xin Chào Python!  "

# 1. strip() - Xóa khoảng trắng ở đầu và cuối chuỗi
print("strip():", chuoi.strip())

# 2. lower() - Chuyển chuỗi thành chữ thường
print("lower():", chuoi.lower())

# 3. upper() - Chuyển chuỗi thành chữ in hoa
print("upper():", chuoi.upper())

# 4. replace() - Thay thế một chuỗi con bằng chuỗi khác
print("replace():", chuoi.replace("Python", "Thế Giới"))

# 5. split() - Tách chuỗi thành danh sách theo ký tự phân cách
print("split():", chuoi.split())

# 6. join() - Nối các phần tử trong danh sách thành chuỗi
ds = ['Xin', 'chao', 'cac', 'ban']
print("join():", " ".join(ds))

# 7. find() - Tìm vị trí xuất hiện đầu tiên của chuỗi con
print("find():", chuoi.find("Python"))

# 8. count() - Đếm số lần xuất hiện của chuỗi con
print("count():", chuoi.count("o"))

# 9. startswith() và endswith() - Kiểm tra bắt đầu / kết thúc chuỗi
print("startswith('Xin'):", chuoi.strip().startswith("Xin"))
print("endswith('!'):", chuoi.strip().endswith("!"))

# 10. len() - Độ dài chuỗi
print("len():", len(chuoi))
