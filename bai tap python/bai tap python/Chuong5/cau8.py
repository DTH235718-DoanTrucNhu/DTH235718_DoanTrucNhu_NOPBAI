import os

# Hàm 1: Lấy tên file kèm phần mở rộng (.mp3)
def LayTenFile(dayduongdan):
    return os.path.basename(dayduongdan)

# Hàm 2: Lấy tên file không có phần mở rộng
def LayTenBaiHat(dayduongdan):
    tenfile = os.path.basename(dayduongdan)   # Lấy "muabui.mp3"
    ten, _ = os.path.splitext(tenfile)        # Tách "muabui" và ".mp3"
    return ten

# --- Chương trình chính ---
duongdan = input("Nhập đường dẫn bài hát: ")

print("Tên file (có đuôi mở rộng):", LayTenFile(duongdan))
print("Tên bài hát (không có đuôi):", LayTenBaiHat(duongdan))
