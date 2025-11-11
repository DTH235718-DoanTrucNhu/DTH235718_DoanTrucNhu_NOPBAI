import json
import os
from datetime import datetime

# Tên file để lưu trữ dữ liệu JSON
FILE_NAME = 'student_management.json'

# Cấu trúc dữ liệu toàn cục trong bộ nhớ:
# university_data = {
#     "MaLop": {
#         "TenLop": "Ten Lop",
#         "SinhVien": [
#             {"MaSV": "SV001", "TenSV": "Nguyen A", "NamSinh": 2003},
#             ...
#         ]
#     },
#     ...
# }
university_data = {}

# --- HÀM XỬ LÝ FILE JSON ---

def load_data():
    """Đọc dữ liệu từ file JSON vào bộ nhớ."""
    global university_data
    
    if not os.path.exists(FILE_NAME):
        print(f"File '{FILE_NAME}' không tồn tại. Bắt đầu với dữ liệu trống.")
        university_data = {}
        return
    
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            university_data = json.load(file)
        print("Đã tải dữ liệu quản lý sinh viên thành công.")
    except json.JSONDecodeError:
        print("Lỗi giải mã file JSON. Bắt đầu với dữ liệu trống.")
        university_data = {}
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}. Bắt đầu với dữ liệu trống.")
        university_data = {}

def save_data():
    """Lưu dữ liệu từ bộ nhớ vào file JSON."""
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            # indent=4 giúp file JSON dễ đọc hơn
            json.dump(university_data, file, ensure_ascii=False, indent=4)
        print(f"Đã lưu dữ liệu vào file '{FILE_NAME}' thành công.")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

# --- HÀM HỖ TRỢ TRUY XUẤT ---

def get_student_by_id(ma_sv):
    """Tìm sinh viên theo mã SV trong tất cả các lớp."""
    for ma_lop, class_info in university_data.items():
        for sv in class_info['SinhVien']:
            if sv['MaSV'] == ma_sv:
                return ma_lop, sv
    return None, None # Trả về Mã Lớp và Sinh Viên

def get_class_by_id(ma_lop):
    """Tìm thông tin lớp theo mã lớp."""
    return university_data.get(ma_lop)

# --- CÁC HÀM XỬ LÝ NGHIỆP VỤ (CRUD) ---

def create_new():
    """Thêm mới Lớp và Sinh viên."""
    print("\n--- THÊM MỚI SINH VIÊN ---")
    
    # 1. Chọn/Tạo Lớp
    while True:
        ma_lop = input("Nhập Mã Lớp (hoặc 'new' để tạo lớp mới): ").strip().upper()
        class_info = get_class_by_id(ma_lop)
        
        if class_info:
            print(f"Lớp '{class_info['TenLop']}' đã được chọn.")
            break
        elif ma_lop == 'NEW' or ma_lop not in university_data:
            # Tạo Lớp mới
            if ma_lop == 'NEW':
                ma_lop = input("Nhập Mã Lớp MỚI: ").strip().upper()
            if get_class_by_id(ma_lop):
                print("Mã lớp đã tồn tại. Vui lòng nhập mã khác.")
                continue

            ten_lop = input(f"Nhập Tên Lớp cho '{ma_lop}': ").strip()
            if not ten_lop:
                print("Tên lớp không được trống.")
                continue
                
            university_data[ma_lop] = {'TenLop': ten_lop, 'SinhVien': []}
            print(f"Lớp '{ten_lop}' đã được tạo.")
            class_info = university_data[ma_lop]
            break
        else:
            print("Mã lớp không hợp lệ.")

    # 2. Nhập Sinh viên
    while True:
        ma_sv = input("Nhập Mã Sinh viên: ").strip().upper()
        if get_student_by_id(ma_sv)[1]:
            print("Mã sinh viên đã tồn tại trong hệ thống. Vui lòng nhập mã khác.")
            continue
            
        ten_sv = input("Nhập Tên Sinh viên: ").strip()
        try:
            nam_sinh = int(input("Nhập Năm sinh (YYYY): "))
            if nam_sinh < 1900 or nam_sinh > datetime.now().year:
                print("Năm sinh không hợp lệ.")
                continue
        except ValueError:
            print("Năm sinh không hợp lệ.")
            continue
        
        new_student = {
            'MaSV': ma_sv,
            'TenSV': ten_sv,
            'NamSinh': nam_sinh
        }
        class_info['SinhVien'].append(new_student)
        print(f"Sinh viên '{ten_sv}' đã được thêm vào lớp {class_info['TenLop']}.")
        break

def display_all_students(list_data=None):
    """Hiển thị tất cả sinh viên theo lớp, hoặc danh sách đã lọc."""
    
    if not university_data:
        print("Hệ thống chưa có dữ liệu lớp học nào.")
        return

    print("\n==================================")
    print("      DANH SÁCH SINH VIÊN HỆ THỐNG")
    print("==================================")
    
    # Chuẩn bị dữ liệu hiển thị (từ list_data nếu có, hoặc từ data gốc)
    if list_data:
        data_to_display = list_data
    else:
        # Chuyển đổi data gốc thành flat list để dễ in
        data_to_display = []
        for ma_lop, class_info in university_data.items():
            for sv in class_info['SinhVien']:
                data_to_display.append({
                    **sv, 
                    'MaLop': ma_lop, 
                    'TenLop': class_info['TenLop']
                })
                
    if not data_to_display:
        print("Danh sách sinh viên trống.")
        return

    print(f"{'Mã SV':<8} {'Tên Sinh viên':<25} {'Năm Sinh':<10} {'Mã Lớp':<8} {'Tên Lớp'}")
    print("-" * 70)
    for sv in data_to_display:
        print(f"{sv['MaSV']:<8} {sv['TenSV']:<25} {sv['NamSinh']:<10} {sv['MaLop']:<8} {sv['TenLop']}")
    print("-" * 70)


def update_student():
    """Sửa thông tin Sinh viên."""
    display_all_students()
    ma_sv = input("Nhập Mã Sinh viên CẦN SỬA: ").strip().upper()
    
    ma_lop, student = get_student_by_id(ma_sv)
    
    if not student:
        print("Không tìm thấy sinh viên này.")
        return

    print(f"\n--- SỬA SINH VIÊN: {student['TenSV']} ({ma_sv}) ---")
    print("Bỏ qua (Enter) để giữ nguyên giá trị cũ.")
    
    # Sửa Tên
    new_ten = input(f"Nhập Tên mới (hiện tại: {student['TenSV']}): ").strip()
    if new_ten:
        student['TenSV'] = new_ten
        
    # Sửa Năm sinh
    while True:
        new_nam = input(f"Nhập Năm sinh mới (hiện tại: {student['NamSinh']}): ").strip()
        if not new_nam:
            break
        try:
            new_nam = int(new_nam)
            if 1900 < new_nam <= datetime.now().year:
                student['NamSinh'] = new_nam
                break
            else:
                print("Năm sinh không hợp lệ.")
        except ValueError:
            print("Năm sinh không hợp lệ (phải là số nguyên).")
            
    print("Cập nhật sinh viên thành công.")


def delete_student():
    """Xóa Sinh viên."""
    display_all_students()
    ma_sv = input("Nhập Mã Sinh viên CẦN XÓA: ").strip().upper()
    
    ma_lop, student_to_delete = get_student_by_id(ma_sv)
    
    if not student_to_delete:
        print(" Không tìm thấy sinh viên này.")
        return
        
    class_info = university_data[ma_lop]
    
    confirm = input(f"Bạn có chắc muốn xóa sinh viên '{student_to_delete['TenSV']}' (Y/N)? ").strip().upper()
    if confirm == 'Y':
        class_info['SinhVien'].remove(student_to_delete)
        # Kiểm tra nếu lớp không còn sinh viên nào, có thể xóa lớp (tùy chọn)
        # if not class_info['SinhVien']:
        #     del university_data[ma_lop]
        #     print(f"Lớp {ma_lop} đã bị xóa do không còn sinh viên.")
            
        print("Đã xóa sinh viên thành công.")
    else:
        print("Hủy thao tác xóa.")


def search_students():
    """Tìm kiếm Sinh viên theo Tên hoặc Mã SV."""
    keyword = input("Nhập từ khóa tìm kiếm (Tên/Mã SV): ").strip().lower()
    
    found_students = []
    
    for ma_lop, class_info in university_data.items():
        for sv in class_info['SinhVien']:
            if keyword in sv['TenSV'].lower() or keyword in sv['MaSV'].lower():
                found_students.append({
                    **sv, 
                    'MaLop': ma_lop, 
                    'TenLop': class_info['TenLop']
                })

    if found_students:
        print(f"\n--- KẾT QUẢ TÌM KIẾM cho '{keyword}' ({len(found_students)} sinh viên) ---")
        display_all_students(found_students)
    else:
        print(f"Không tìm thấy sinh viên nào với từ khóa '{keyword}'.")


def sort_students():
    """Sắp xếp tất cả Sinh viên theo Năm sinh."""
    
    # 1. Chuyển đổi dữ liệu sang list phẳng để dễ sắp xếp
    all_students_flat = []
    for ma_lop, class_info in university_data.items():
        for sv in class_info['SinhVien']:
            all_students_flat.append({
                **sv, 
                'MaLop': ma_lop, 
                'TenLop': class_info['TenLop']
            })

    if not all_students_flat:
        print("Danh sách sinh viên trống, không thể sắp xếp.")
        return
        
    print("\n--- SẮP XẾP SINH VIÊN ---")
    
    while True:
        choice = input("Sắp xếp theo (1) Năm sinh tăng dần (SV cũ nhất lên đầu) hoặc (2) Năm sinh giảm dần (SV trẻ nhất lên đầu)? (1/2): ").strip()
        
        if choice == '1':
            all_students_flat.sort(key=lambda sv: sv['NamSinh'], reverse=False)
            print(" Đã sắp xếp theo Năm sinh Tăng dần (từ cũ nhất).")
            break
        elif choice == '2':
            all_students_flat.sort(key=lambda sv: sv['NamSinh'], reverse=True)
            print("Đã sắp xếp theo Năm sinh Giảm dần (từ trẻ nhất).")
            break
        else:
            print("Lựa chọn không hợp lệ.")
            
    # 2. Hiển thị danh sách đã sắp xếp
    display_all_students(all_students_flat)


# --- CHƯƠNG TRÌNH CHÍNH (MENU) ---

def main_menu():
    """Hiển thị menu chính và xử lý lựa chọn."""
    
    load_data() # Tải dữ liệu khi chương trình khởi động
    
    while True:
        print("\n==================================")
        print("      PHẦN MỀM QUẢN LÝ SINH VIÊN")
        print("      Sử dụng JSON File")
        print("==================================")
        print("1. Thêm mới Lớp/Sinh viên")
        print("2. Xem danh sách Sinh viên")
        print("3. Sửa thông tin Sinh viên")
        print("4. Xóa Sinh viên")
        print("5. Tìm kiếm Sinh viên")
        print("6. Sắp xếp Sinh viên (theo Năm sinh)")
        print("7. Lưu dữ liệu và Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
        
        if choice == '1':
            create_new()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_students()
        elif choice == '6':
            sort_students()
        elif choice == '7':
            save_data()
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print(" Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 7.")

# Khởi chạy chương trình
# Bỏ comment dòng dưới để chạy chương trình
main_menu() 
print("\n--- ĐỂ CHẠY CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN, VUI LÒNG BỎ COMMENT DÒNG 'main_menu()' TRONG CODE ---")