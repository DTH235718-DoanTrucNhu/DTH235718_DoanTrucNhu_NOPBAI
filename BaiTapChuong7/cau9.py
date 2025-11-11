import csv
import os
from collections import defaultdict

# Tên file để lưu trữ dữ liệu
FILE_NAME = 'product_management.csv'
# Cấu trúc file: Mã Danh mục, Tên Danh mục, Mã Sản phẩm, Tên Sản phẩm, Đơn giá

# Cấu trúc dữ liệu trong bộ nhớ (sẽ được tải từ file)
# categories = { 'MA_DM': 'Ten Danh Muc' }
# products = [ { 'MaSP': 'P001', 'TenSP': 'Ao Thun', 'DonGia': 150000, 'MaDM': 'DM01' }, ... ]
categories = {}
products = []

# --- CÁC HÀM XỬ LÝ TEXT FILE (I/O) ---

def load_data():
    """Đọc dữ liệu từ file CSV vào bộ nhớ (dictionaries và lists)."""
    global categories, products
    categories = {}
    products = []
    
    if not os.path.exists(FILE_NAME):
        print(f"File '{FILE_NAME}' không tồn tại. Bắt đầu với dữ liệu trống.")
        return

    with open(FILE_NAME, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # 1. Tải Danh mục
            ma_dm = row['MaDanhMuc']
            ten_dm = row['TenDanhMuc']
            if ma_dm and ma_dm not in categories:
                categories[ma_dm] = ten_dm
                
            # 2. Tải Sản phẩm
            if row['MaSP']:
                product = {
                    'MaSP': row['MaSP'],
                    'TenSP': row['TenSP'],
                    'DonGia': float(row['DonGia']),
                    'MaDM': row['MaDanhMuc']
                }
                products.append(product)
    print(" Đã tải dữ liệu thành công.")

def save_data():
    """Lưu toàn bộ dữ liệu (categories và products) vào file CSV."""
    
    # Chuẩn bị dữ liệu để ghi (Gộp Danh mục và Sản phẩm)
    data_to_save = []
    
    # 1. Thêm các sản phẩm, kèm thông tin danh mục tương ứng
    for p in products:
        ma_dm = p['MaDM']
        data_to_save.append({
            'MaDanhMuc': ma_dm,
            'TenDanhMuc': categories.get(ma_dm, 'N/A'), # Lấy tên DM từ dict categories
            'MaSP': p['MaSP'],
            'TenSP': p['TenSP'],
            'DonGia': p['DonGia']
        })
    
    # 2. Thêm các danh mục KHÔNG CÓ sản phẩm (nếu có, để đảm bảo lưu đủ danh mục)
    saved_dm_codes = {p['MaDM'] for p in products}
    for ma_dm, ten_dm in categories.items():
        if ma_dm not in saved_dm_codes:
            data_to_save.append({
                'MaDanhMuc': ma_dm,
                'TenDanhMuc': ten_dm,
                'MaSP': '', # Trống nếu là danh mục không có SP
                'TenSP': '',
                'DonGia': ''
            })

    # Ghi vào file
    fieldnames = ['MaDanhMuc', 'TenDanhMuc', 'MaSP', 'TenSP', 'DonGia']
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_to_save)
        
    print(f" Đã lưu dữ liệu vào file '{FILE_NAME}' thành công.")

# --- CÁC HÀM XỬ LÝ NGHIỆP VỤ ---

def get_product_by_id(ma_sp):
    """Tìm sản phẩm theo mã."""
    for p in products:
        if p['MaSP'] == ma_sp:
            return p
    return None

def display_product_list(list_to_display=None):
    """Hiển thị danh sách sản phẩm (hoặc danh sách đã lọc)."""
    if list_to_display is None:
        list_to_display = products
        
    if not list_to_display:
        print("Danh sách sản phẩm trống.")
        return

    print("\n--- DANH SÁCH SẢN PHẨM ---")
    print(f"{'Mã SP':<8} {'Tên Sản phẩm':<30} {'Đơn giá':<10} {'Mã DM':<8} {'Tên Danh mục'}")
    print("-" * 70)
    for p in list_to_display:
        ma_dm = p['MaDM']
        ten_dm = categories.get(ma_dm, 'N/A')
        print(f"{p['MaSP']:<8} {p['TenSP']:<30} {p['DonGia']:,<10.0f} {ma_dm:<8} {ten_dm}")
    print("-" * 70)

def create_new():
    """Thêm mới Danh mục và Sản phẩm."""
    print("\n--- THÊM MỚI SẢN PHẨM ---")
    
    # 1. Nhập Danh mục
    while True:
        ma_dm = input("Nhập Mã Danh mục (hoặc 'new' để tạo mới): ").strip().upper()
        if ma_dm in categories:
            print(f"Danh mục '{categories[ma_dm]}' đã được chọn.")
            break
        elif ma_dm == 'NEW' or ma_dm not in categories:
            # Tạo Danh mục mới
            if ma_dm == 'NEW':
                ma_dm = input("Nhập Mã Danh mục MỚI: ").strip().upper()
            if ma_dm in categories:
                print("Mã danh mục đã tồn tại. Vui lòng nhập lại.")
                continue

            ten_dm = input(f"Nhập Tên Danh mục cho '{ma_dm}': ").strip()
            if not ten_dm:
                print("Tên danh mục không được trống.")
                continue
            categories[ma_dm] = ten_dm
            print(f"Danh mục '{ten_dm}' đã được tạo.")
            break
        else:
            print("Mã danh mục không hợp lệ.")

    # 2. Nhập Sản phẩm
    while True:
        ma_sp = input("Nhập Mã Sản phẩm: ").strip().upper()
        if get_product_by_id(ma_sp):
            print("Mã sản phẩm đã tồn tại. Vui lòng nhập mã khác.")
            continue
        ten_sp = input("Nhập Tên Sản phẩm: ").strip()
        try:
            don_gia = float(input("Nhập Đơn giá: "))
            if don_gia < 0:
                print("Đơn giá không được âm.")
                continue
        except ValueError:
            print("Đơn giá không hợp lệ.")
            continue
        
        new_product = {
            'MaSP': ma_sp,
            'TenSP': ten_sp,
            'DonGia': don_gia,
            'MaDM': ma_dm
        }
        products.append(new_product)
        print(" Sản phẩm '{ten_sp}' đã được thêm.")
        break

def update_item():
    """Sửa thông tin Sản phẩm."""
    display_product_list()
    ma_sp = input("Nhập Mã Sản phẩm CẦN SỬA: ").strip().upper()
    product = get_product_by_id(ma_sp)
    
    if not product:
        print("Không tìm thấy sản phẩm này.")
        return

    print(f"\n--- SỬA SẢN PHẨM: {product['TenSP']} ---")
    print("Bỏ qua để giữ nguyên giá trị cũ.")
    
    # Sửa Tên
    new_ten = input(f"Nhập Tên mới (hiện tại: {product['TenSP']}): ").strip()
    if new_ten:
        product['TenSP'] = new_ten
        
    # Sửa Đơn giá
    while True:
        new_gia = input(f"Nhập Đơn giá mới (hiện tại: {product['DonGia']:,<.0f}): ").strip()
        if not new_gia:
            break
        try:
            new_gia = float(new_gia)
            if new_gia >= 0:
                product['DonGia'] = new_gia
                break
            else:
                print("Đơn giá không được âm.")
        except ValueError:
            print("Đơn giá không hợp lệ.")
            
    print("Cập nhật sản phẩm thành công.")

def delete_item():
    """Xóa Sản phẩm."""
    display_product_list()
    ma_sp = input("Nhập Mã Sản phẩm CẦN XÓA: ").strip().upper()
    product = get_product_by_id(ma_sp)
    
    if not product:
        print("Không tìm thấy sản phẩm này.")
        return
        
    confirm = input(f"Bạn có chắc muốn xóa sản phẩm '{product['TenSP']}' (Y/N)? ").strip().upper()
    if confirm == 'Y':
        products.remove(product)
        print("Đã xóa sản phẩm thành công.")
    else:
        print("Hủy thao tác xóa.")

def search_items():
    """Tìm kiếm Sản phẩm theo Tên hoặc Mã."""
    keyword = input("Nhập từ khóa tìm kiếm (Tên/Mã SP): ").strip().lower()
    
    found_products = [
        p for p in products 
        if keyword in p['TenSP'].lower() or keyword in p['MaSP'].lower()
    ]
    
    if found_products:
        print(f"\n--- KẾT QUẢ TÌM KIẾM cho '{keyword}' ---")
        display_product_list(found_products)
    else:
        print(f"Không tìm thấy sản phẩm nào với từ khóa '{keyword}'.")

def sort_items():
    """Sắp xếp Sản phẩm theo Đơn giá."""
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    
    while True:
        choice = input("Sắp xếp theo (1) Tăng dần Đơn giá hoặc (2) Giảm dần Đơn giá? (1/2): ").strip()
        if choice == '1':
            products.sort(key=lambda p: p['DonGia'], reverse=False)
            print("Đã sắp xếp theo Đơn giá Tăng dần.")
            break
        elif choice == '2':
            products.sort(key=lambda p: p['DonGia'], reverse=True)
            print("Đã sắp xếp theo Đơn giá Giảm dần.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
            
    display_product_list()

# --- CHƯƠNG TRÌNH CHÍNH (MENU) ---

def main_menu():
    """Hiển thị menu và xử lý lựa chọn."""
    
    load_data() # Tải dữ liệu khi chương trình khởi động
    
    while True:
        print("\n==================================")
        print("      PHẦN MỀM QUẢN LÝ SẢN PHẨM")
        print("==================================")
        print("1. Thêm mới Sản phẩm/Danh mục")
        print("2. Xem danh sách Sản phẩm")
        print("3. Sửa thông tin Sản phẩm")
        print("4. Xóa Sản phẩm")
        print("5. Tìm kiếm Sản phẩm")
        print("6. Sắp xếp Sản phẩm (theo Đơn giá)")
        print("7. Lưu dữ liệu và Thoát")
        
        choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
        
        if choice == '1':
            create_new()
        elif choice == '2':
            display_product_list()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            search_items()
        elif choice == '6':
            sort_items()
        elif choice == '7':
            save_data()
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print(" Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 7.")

# Khởi chạy chương trình
main_menu();
# Bỏ comment dòng trên để chạy chương trình quản lý sản phẩm
