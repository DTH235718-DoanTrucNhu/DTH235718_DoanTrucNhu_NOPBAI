import random
import os

# Tên file mặc định
FILE_NAME = 'random_numbers.csv'
# Số dòng và số cột theo yêu cầu
NUM_ROWS = 10
NUM_COLS = 10

def create_csv_file(filename=FILE_NAME, rows=NUM_ROWS, cols=NUM_COLS):
    """
    Tạo tập tin CSV, 10 dòng, mỗi dòng 10 số ngẫu nhiên (1-99), 
    phân cách bằng dấu chấm phẩy (;).
    """
    
    data = []
    # Tạo dữ liệu: 10 dòng, mỗi dòng 10 số ngẫu nhiên
    for _ in range(rows):
        # Tạo 10 số ngẫu nhiên từ 1 đến 99
        row = [random.randint(1, 99) for _ in range(cols)]
        data.append(row)
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for row in data:
                # Nối các số thành chuỗi, phân cách bằng dấu chấm phẩy (';')
                file.write(';'.join(map(str, row)) + '\n')
        print(f"✅ Đã tạo file '{filename}' với {rows} dòng thành công.")
    except Exception as e:
        print(f"❌ Lỗi khi tạo file: {e}")

def read_and_sum_csv(filename=FILE_NAME):
    """
    Đọc tập tin CSV, xuất ra tổng giá trị của các phần tử trên mỗi dòng.
    """
    
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' không tồn tại. Vui lòng tạo file trước.")
        return

    print(f"\n--- TÍNH TỔNG CÁC PHẦN TỬ TRÊN MỖI DÒNG CỦA FILE '{filename}' ---")
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                # Loại bỏ ký tự xuống dòng và tách chuỗi bằng dấu chấm phẩy (';')
                parts = line.strip().split(';')
                
                current_sum = 0
                
                # Tính tổng các phần tử
                for part in parts:
                    try:
                        # Chuyển phần tử về số nguyên để tính tổng
                        number = int(part.strip())
                        current_sum += number
                    except ValueError:
                        # Bỏ qua các phần tử không phải là số
                        continue
                
                print(f"Dòng {line_number} có Tổng: {current_sum}")
                
    except Exception as e:
        print(f"❌ Lỗi khi đọc file: {e}")

# --- THỰC THI CHƯƠNG TRÌNH CHÍNH CHO CÂU 12 ---
def run_csv_program_c12():
    print("\n==================================")
    print("  CHƯƠNG TRÌNH XỬ LÝ CSV (CÂU 12)")
    print("==================================")
    
    # Bước 1: Tạo file
    create_csv_file()
    
    # Bước 2: Đọc và tính tổng
    read_and_sum_csv()

# Khởi chạy chương trình
run_csv_program_c12()